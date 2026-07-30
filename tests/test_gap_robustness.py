"""Robustesse aux chroniques trouées : depuis stase 0.2, la grille
temporelle est matérialisée par le moteur (pas manquants = NaN). Une
chronique à lignes absentes doit donner exactement le même résultat que
la même chronique densifiée à la main, y compris pour les fiches à
positions (dates d'extremum) et à fenêtres glissantes (VCN10) et pour
les chaînes multi-processus (QMNA)."""

import warnings

import numpy as np
import pandas as pd

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import extract

CARDS = ["QA", "QJXA", "tQJXA", "VCN10", "QMNA"]


def _chronicle():
    dates = pd.date_range("1985-01-01", "2014-12-31", freq="D")
    rng = np.random.default_rng(11)
    q = 5 + 20 * rng.gamma(2.0, 1.0, len(dates))
    return pd.DataFrame({"date": dates, "Q": q, "id": "S1"})


def test_row_gaps_equal_nan_dense_on_corpus_sample():
    full = _chronicle()
    rng = np.random.default_rng(4)
    holes = rng.random(len(full)) < 0.02                 # 2 % épars
    holes |= ((full["date"] >= "1999-04-01")             # + un bloc de 2 mois
              & (full["date"] <= "1999-05-31")).to_numpy()

    gapped = full[~holes]
    nan_dense = full.copy()
    nan_dense.loc[holes, "Q"] = np.nan

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        res_g = extract(gapped, cards=CARDS, verbose=False)
        res_d = extract(nan_dense, cards=CARDS, verbose=False)

    for name in CARDS:
        pd.testing.assert_frame_equal(res_g["data"][name],
                                      res_d["data"][name],
                                      obj=f"fiche {name}")


def test_exceedance_frequency_ne_compte_que_le_temps_observe():
    """Un jour manquant n'est pas un jour de non-dépassement.

    Le dénominateur comptait TOUS les pas de temps, lacunes comprises,
    alors que le numérateur les écartait : la fréquence rendue valait la
    vraie fréquence multipliée par la part de données présentes. La
    complétude des chroniques s'améliorant avec les années, ce biais se
    lisait comme une tendance à la hausse. Rupture de parité R du
    2026-07-30 (ORIGINE_R.md).
    """
    from card.functions.fdc import exceedance_frequency

    q = np.arange(1.0, 101.0)                     # 100 jours, seuil à 90
    assert exceedance_frequency(q, 90.0) == 0.10

    # Mêmes observations, un cinquième de la chronique effacé : la
    # fréquence des jours OBSERVÉS ne bouge pas.
    troue = q.copy()
    troue[:20] = np.nan                           # aucun ne dépassait 90
    assert exceedance_frequency(troue, 90.0) == 10 / 80

    # L'ancien calcul rendait la vraie fréquence multipliée par la part
    # de données présentes, ni plus ni moins : 0,125 devenait 0,10.
    ancien = 10 / len(troue)
    assert ancien == (10 / 80) * (80 / 100)

    # Une série entièrement absente ne vaut plus 0, qui se lisait comme
    # « aucun dépassement observé » au lieu de « rien d'observé ».
    assert np.isnan(exceedance_frequency(np.full(50, np.nan), 90.0))


def test_exceedance_frequency_compte_comme_exceedance_quantile():
    """Les deux moitiés d'une fiche fQ doivent compter pareil.

    fQ01A tire son seuil de exceedance_quantile, qui écarte les lacunes,
    puis sa fréquence de exceedance_frequency. Tant que l'une écartait et
    l'autre comptait, la fiche se contredisait au milieu.
    """
    from card.functions.fdc import exceedance_frequency, exceedance_quantile

    rng = np.random.default_rng(3)
    q = rng.gamma(2.0, 10.0, 4000)
    troue = q.copy()
    troue[rng.choice(4000, 400, replace=False)] = np.nan

    seuil = exceedance_quantile(troue, 0.10)
    obtenu = exceedance_frequency(troue, seuil)
    assert abs(obtenu - 0.10) < 0.005, obtenu
