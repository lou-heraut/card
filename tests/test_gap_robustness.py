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
