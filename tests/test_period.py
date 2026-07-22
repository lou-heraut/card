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
    ("QM_H", "QM", 12),
    ("median-QJ_H", "median-QJ", 365),
    ("FDC_H", "FDC_Q", 1000),
])
def test_fiche_horizon_suit_les_bornes_fournies(fiche, variable, lignes):
    """Deux horizons différents doivent donner deux résultats différents,
    et la sortie garder sa forme."""
    d = _serie()
    a = extract(d.assign(horizon_start="2001-01-01", horizon_end="2020-12-31"),
                cards=[fiche])["data"][fiche]
    b = extract(d.assign(horizon_start="2041-01-01", horizon_end="2060-12-31"),
                cards=[fiche])["data"][fiche]
    assert len(a) == len(b) == lignes
    assert not np.allclose(a[variable].to_numpy(), b[variable].to_numpy(),
                           equal_nan=True)


def test_fiche_horizon_se_decline_par_suffixe():
    d = _serie().assign(
        horizon_start_H1="2001-01-01", horizon_end_H1="2020-12-31",
        horizon_start_H3="2041-01-01", horizon_end_H3="2060-12-31")
    res = extract(d, cards=["QM_H"], suffix=["H1", "H3"])
    assert set(res["data"]["QM_H"].columns) >= {"QM_H1", "QM_H3"}
    assert set(res["meta"]["variable_en"]) == {"QM_H1", "QM_H3"}


def test_sans_bornes_la_fiche_calcule_sur_tout():
    """L'appelant qui ne fournit pas d'horizon obtient la chronique
    entière plutôt qu'un refus."""
    d = _serie()
    entier = extract(d.assign(horizon_start=None, horizon_end=None),
                     cards=["QM_H"])["data"]["QM_H"]
    assert entier["QM"].notna().all()


def test_une_borne_absente_laisse_son_cote_ouvert():
    d = pd.Series(pd.date_range("2000-01-01", periods=10, freq="D"))
    x = np.arange(10.0)
    vide = pd.Series([None] * 10)
    depuis = pd.Series(["2000-01-06"] * 10)
    assert over_period(x, func="nanmean", dates=d,
                       period_start=depuis, period_end=vide) == 7.0
    assert over_period(x, func="nanmean", dates=d,
                       period_start=vide, period_end=depuis) == 2.5
