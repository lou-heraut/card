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


# ── Suffixes : le cas obs/sim de bout en bout ────────────────────────────────

def _obs_sim():
    dates = pd.date_range("1980-01-01", "2009-12-31", freq="D")
    rng = np.random.default_rng(12)
    n = len(dates)
    return pd.DataFrame({
        "date": dates, "id": "S1",
        "Q_obs": 5 + 20 * rng.gamma(2.0, 1.0, n) + 0.001 * np.arange(n),
        "Q_sim": 5 + 20 * rng.gamma(2.0, 1.0, n) + 0.002 * np.arange(n),
    })


def test_trend_follows_the_suffixes_of_the_extraction():
    """card.trend n'a rien à redemander : la colonne suffix de meta suffit."""
    res = extract(_obs_sim(), cards=["QA"], suffix=["obs", "sim"],
                  verbose=False)
    df = trend(res, dependency="INDE")["data"]["QA"]

    assert set(df["variable"]) == {"QA_obs", "QA_sim"}
    # suffix= a bien été transmis : le nom de base est retrouvé
    assert set(df["variable_no_suffix"]) == {"QA"}
    # QA est relative (défaut des fiches) : la méta suffixée est lue
    assert df["a_relative"].notna().all()


def test_trend_can_pool_the_extreme_bounds_across_suffixes():
    res = extract(_obs_sim(), cards=["QA"], suffix=["obs", "sim"],
                  verbose=False)
    apart = trend(res, dependency="INDE")["data"]["QA"]
    pooled = trend(res, dependency="INDE",
                   extremes_pool_suffixes=True)["data"]["QA"]

    assert apart.groupby("variable")["a_relative_min"].first().nunique() == 2
    assert pooled.groupby("variable")["a_relative_min"].first().nunique() == 1
