"""Restriction d'un calcul à une sous-période fournie en colonnes.

Une fiche ne fige pas de dates : l'appelant donne les bornes, ce qui
permet un horizon différent par série. La restriction se fait DANS la
fonction d'agrégation, jamais en masquant la série en amont, sans quoi
les valeurs écartées seraient comptées comme des lacunes.
"""

import numpy as np
import pandas as pd
import pytest

from card.extraction import extract
from card.functions import fdc_probabilities, over_period


def _serie(debut="1990-01-01", fin="2060-12-31"):
    dates = pd.date_range(debut, fin, freq="D")
    return pd.DataFrame({
        "date": dates, "id": "S",
        "Q": np.random.default_rng(0).gamma(2, 5, len(dates))})


def test_over_period_restreint_puis_delegue():
    d = pd.Series(pd.date_range("2000-01-01", periods=10, freq="D"))
    x = np.arange(10.0)
    assert over_period(x, func="nanmean", dates=d) == 4.5
    borne = pd.Series(["2000-01-06"] * 10), pd.Series(["2000-01-10"] * 10)
    assert over_period(x, func="nanmean", dates=d,
                       period_start=borne[0], period_end=borne[1]) == 7.0


def test_over_period_exige_une_fonction():
    with pytest.raises(ValueError, match="fonction"):
        over_period(np.arange(3.0))


def test_fdc_probabilities_accepte_la_colonne_imposee():
    """Le moteur affecte d'office la première colonne numérique à une
    fonction qui n'en déclare aucune. Sans un paramètre pour l'accueillir,
    elle se liait à `n` : les cinq fiches FDC ont planté depuis l'origine
    du portage jusqu'au 2026-07-22, trois d'entre elles masquant le défaut
    par une période sans données."""
    assert len(fdc_probabilities(np.arange(50.0), n=10)) == 10
    assert np.array_equal(fdc_probabilities(n=10), fdc_probabilities(None, n=10))


@pytest.mark.parametrize("fiche,variable,lignes", [
    ("QM", "QM", 12),
    ("QJD", "QJD", 365),
    ("FDC", "FDC_Q", 1000),
])
def test_fiche_horizon_suit_les_bornes_fournies(fiche, variable, lignes):
    """Deux horizons différents doivent donner deux résultats différents,
    et la sortie garder sa forme."""
    d = _serie()
    a = extract(d.assign(period_start="2001-01-01", period_end="2020-12-31"),
                cards=[fiche])["data"][fiche]
    b = extract(d.assign(period_start="2041-01-01", period_end="2060-12-31"),
                cards=[fiche])["data"][fiche]
    assert len(a) == len(b) == lignes
    assert not np.allclose(a[variable].to_numpy(), b[variable].to_numpy(),
                           equal_nan=True)


def test_fiche_horizon_se_decline_par_suffixe():
    d = _serie().assign(
        period_start_H1="2001-01-01", period_end_H1="2020-12-31",
        period_start_H3="2041-01-01", period_end_H3="2060-12-31")
    res = extract(d, cards=["QM"], suffix=["H1", "H3"])
    assert set(res["data"]["QM"].columns) >= {"QM_H1", "QM_H3"}
    assert set(res["meta"]["variable_en"]) == {"QM_H1", "QM_H3"}


def test_les_bornes_sont_facultatives():
    """La période est une entrée facultative : absente, la fiche calcule
    sur toute la chronique. C'est ce qui permet à une seule fiche de
    remplacer la version libre et la version restreinte."""
    d = _serie()
    entier = extract(d, cards=["QM"])["data"]["QM"]          # colonnes absentes
    vides = extract(d.assign(period_start=None, period_end=None),
                    cards=["QM"])["data"]["QM"]              # colonnes vides
    restreint = extract(d.assign(period_start="2001-01-01",
                                 period_end="2020-12-31"),
                        cards=["QM"])["data"]["QM"]
    assert entier["QM"].notna().all()
    assert np.allclose(entier["QM"], vides["QM"])
    assert not np.allclose(entier["QM"], restreint["QM"])


def test_une_date_invalide_reste_une_erreur():
    """Une borne absente arrive sous la forme du nom de colonne non
    résolu. La tolérer ne doit pas faire passer une date fautive pour
    une absence de borne."""
    from card.functions.period import _const_date
    assert pd.isna(_const_date("period_start"))       # colonne absente
    with pytest.raises(Exception):
        _const_date("2020-13-45")                     # date impossible


def test_une_borne_absente_laisse_son_cote_ouvert():
    d = pd.Series(pd.date_range("2000-01-01", periods=10, freq="D"))
    x = np.arange(10.0)
    vide = pd.Series([None] * 10)
    depuis = pd.Series(["2000-01-06"] * 10)
    assert over_period(x, func="nanmean", dates=d,
                       period_start=depuis, period_end=vide) == 7.0
    assert over_period(x, func="nanmean", dates=d,
                       period_start=vide, period_end=depuis) == 2.5


def test_fdc_horizon_couvre_ses_deux_coordonnees():
    """Une courbe a deux coordonnées : l'axe des probabilités, partagé par
    tous les horizons donc émis une seule fois, et les quantiles, un jeu
    par horizon. Chaque colonne de données doit avoir sa ligne de méta,
    avec son unité propre."""
    d = _serie().assign(
        period_start_H1="2001-01-01", period_end_H1="2020-12-31",
        period_start_H3="2041-01-01", period_end_H3="2060-12-31")
    res = extract(d, cards=["FDC"], suffix=["H1", "H3"])

    colonnes = {c for c in res["data"]["FDC"].columns if c != "id"}
    assert colonnes == {"FDC_p", "FDC_Q_H1", "FDC_Q_H3"}
    assert set(res["meta"]["variable_en"]) == colonnes

    unites = dict(zip(res["meta"]["variable_en"], res["meta"]["unit_en"]))
    assert unites["FDC_p"] == "without unit"
    assert unites["FDC_Q_H1"] == "m^{3}.s^{-1}"


def test_info_montre_la_forme_generique_pas_l_accolade():
    """`card.info` est une lecture humaine : elle doit rendre la fiche
    telle qu'elle se lit par défaut, comme le catalogue, et non exposer
    le placeholder brut. Défaut préexistant, corrigé le 2026-07-22."""
    from card.management import info
    for nom in ("QM", "delta-QA_H"):
        for lang in ("fr", "en"):
            i = info(nom, lang=lang)
            assert "{suffix" not in i["name"], (nom, lang, i["name"])
            assert "{suffix" not in str(i["method"]), (nom, lang)


def test_info_signale_une_entree_facultative():
    from card.management import info
    assert "facultatif" in info("QM", lang="fr")["input_vars"]
    assert "optional" in info("QM", lang="en")["input_vars"]
