"""Tests de card.trend : enveloppe fiche-consciente de stase.trend
(contrôle de la facette output, passage de meta, formes d'entrée)."""

import numpy as np
import pandas as pd
import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import extract, trend


def _daily():
    dates = pd.date_range("1980-01-01", "2019-12-31", freq="D")
    years = dates.year.to_numpy()
    rng = np.random.default_rng(7)
    q = 10 + 0.05 * (years - 1980) + rng.gamma(2.0, 2.0, len(dates))
    return pd.DataFrame({"date": dates, "Q": q, "id": "S1"})


def test_trend_on_series_card():
    res = extract(_daily(), cards=["QA"], verbose=False)
    tr = trend(res, dependency="INDE")
    assert set(tr) == {"data", "meta"}
    df = tr["data"]["QA"]
    assert set(df["variable"]) == {"QA"}
    assert df["H"].iloc[0]                       # tendance imposée détectée
    assert df["a"].iloc[0] == pytest.approx(0.05, rel=0.3)


def test_trend_uses_meta_relative():
    res = extract(_daily(), cards=["QA"], verbose=False)
    df = trend(res, dependency="INDE")["data"]["QA"]
    # QA est relative (défaut fiche) : a_relative en % de la moyenne
    a, a_rel = df["a"].iloc[0], df["a_relative"].iloc[0]
    mean = res["data"]["QA"]["QA"].mean()
    assert a_rel == pytest.approx(a / mean * 100.0, rel=1e-6)


def test_trend_refuses_non_series_card():
    res = extract(_daily(), cards=["QA", "BFI-LH"], verbose=False)
    with pytest.raises(ValueError, match="BFI-LH"):
        trend(res)


def test_trend_simplify_dataframe():
    res = extract(_daily(), cards=["QA"], simplify=True, verbose=False)
    tr = trend(res, dependency="INDE")
    assert isinstance(tr["data"], pd.DataFrame)
    assert set(tr["data"]["variable"]) == {"QA"}


def test_trend_requires_extract_result():
    with pytest.raises(TypeError, match="card.extract"):
        trend(pd.DataFrame({"x": [1.0]}))
