"""Tests unitaires des fonctions hydro — valeurs golden figées lors de la
validation croisée R↔Python (2026-07-12)."""

import numpy as np
import pytest

from card.functions import (
    KGE,
    NSE,
    RAT,
    apply_threshold,
    baseflow,
    bias,
    circular_median,
    deficit_volume,
    delta,
    elasticity,
    exceedance_frequency,
    exceedance_quantile,
    fdc_probabilities,
    fdc_quantiles,
    mannkendall_slope,
    nansum_strict,
    ratio,
    return_level,
    return_period,
    rollmean_center,
    runoff_coefficient,
    snowmelt_timing,
    snowmelt_volume,
    std_ratio,
)


@pytest.fixture(scope="module")
def series():
    rng = np.random.default_rng(7)
    Q = 10 + 5 * np.sin(2 * np.pi * np.arange(400) / 365.25) \
        + rng.normal(0, 1, 400)
    obs = Q[:100]
    sim = obs * 1.05 + rng.normal(0, 0.5, 100)
    return Q, obs, sim


# ── analytiques ─────────────────────────────────────────────────────────────

def test_exceedance_quantile_analytic():
    # quantile type 7 : P(dépassement)=0.9 → quantile(0.1) de 1..10 = 1.9
    assert exceedance_quantile(np.arange(1.0, 11), 0.9) == pytest.approx(1.9)


def test_exceedance_frequency_counts_all_rows():
    q = np.array([1.0, 2, 3, np.nan, 5])
    # 3 valeurs > 1.5, N = 5 (NaN compté au dénominateur, comme en R)
    assert exceedance_frequency(q, 1.5) == pytest.approx(3 / 5)


def test_apply_threshold_longest_length():
    x = np.array([5.0, 1, 1, 4, 1, 1, 1, 5])
    assert apply_threshold(x, 2, where="<=", what="length",
                           select="longest") == 3.0


def test_apply_threshold_first_last_zero_based():
    x = np.array([5.0, 1, 1, 4, 1, 1, 1, 5])
    assert apply_threshold(x, 2, "<=", "first", "longest") == 4.0
    assert apply_threshold(x, 2, "<=", "last", "longest") == 6.0


def test_apply_threshold_no_event_is_nan():
    assert np.isnan(apply_threshold(np.array([5.0, 6, 7]), 2,
                                    where="<=", what="length",
                                    select="longest"))


def test_delta_absolute_and_relative():
    x = np.array([10.0] * 5 + [15.0] * 5)
    d = np.array(["2000-06-01"] * 5 + ["2050-06-01"] * 5, dtype="datetime64[D]")
    past, future = ("2000-01-01", "2000-12-31"), ("2050-01-01", "2050-12-31")
    assert delta(x, d, past, future, relative=False) == pytest.approx(5.0)
    assert delta(x, d, past, future, relative=True) == pytest.approx(50.0)


def test_nansum_strict_all_nan_is_nan():
    assert np.isnan(nansum_strict(np.array([np.nan, np.nan])))
    assert nansum_strict(np.array([1.0, np.nan, 2.0])) == pytest.approx(3.0)


def test_ratio_first_mode_uses_dominant_value():
    a = np.array([4.0, 4, 4, 8])
    b = np.array([2.0, 2, 2, 1])
    assert ratio(a, b, first=True) == pytest.approx(2.0)


def test_rollmean_center_pandas_convention():
    # k=10 pair : fenêtre pandas [i-5, i+4] → position 5 = mean(1..10)
    r = rollmean_center(np.arange(1.0, 13), k=10)
    assert r[5] == pytest.approx(5.5)
    assert np.isnan(r[4])


def test_runoff_coefficient():
    assert runoff_coefficient([2.0, 4], [4.0, 4]) == pytest.approx(0.75)


def test_fdc_shapes():
    p = fdc_probabilities(n=100, norm_spacing=True)
    q = fdc_quantiles(np.arange(1.0, 101), n=100, norm_spacing=True)
    assert len(p) == len(q) == 100
    assert np.all(np.diff(p) > 0)
    assert np.all(np.diff(q) <= 0)   # dépassement : quantiles décroissants


# ── golden values (figées le 2026-07-12, parité R validée) ─────────────────

def test_baseflow_golden(series):
    Q, _, _ = series
    assert baseflow(Q, method="LH")[50] == pytest.approx(11.734592812070815)
    assert baseflow(Q, method="Wal")[50] == pytest.approx(12.529596465941022)


def test_return_level_golden():
    high = np.array([20.0, 25, 22, 30, 28, 24, 26, 31, 23, 27])
    low = np.array([2.0, 1.5, 1.8, 1.2, 2.2, 1.9, 1.4, 2.1, 1.7, 1.6])
    assert return_level(high, 10, "high") == pytest.approx(30.169076292728434)
    assert return_level(low, 5, "low") == pytest.approx(1.4570309500573475)


def test_return_period_roundtrip():
    # return_period est l'inverse exacte de return_level, quelle que
    # soit la convention p0 de la loi mixte (invariant du binôme)
    high = np.array([20.0, 25, 22, 30, 28, 24, 26, 31, 23, 27])
    low = np.array([2.0, 1.5, 1.8, 1.2, 2.2, 1.9, 1.4, 2.1, 1.7, 1.6])
    for T in (2, 5, 10, 50):
        assert return_period(low, return_level(low, T, "low"),
                             "low") == pytest.approx(T)
        assert return_period(high, return_level(high, T, "high"),
                             "high") == pytest.approx(T)
    # seuil en colonne constante (chemin kwarg des fiches)
    lim = np.full(10, return_level(low, 5, "low"))
    assert return_period(low, lim, "low") == pytest.approx(5)
    # seuil nul sur série intermittente : T = 1/p0 dans toute convention
    inter = np.array([0.0, 0, 1.2, 1.5, 0.9, 1.1, 1.8, 1.3, 0.7, 1.6])
    assert return_period(inter, 0.0, "low") == pytest.approx(5)
    # seuil nul sans année nulle : indéfini sous la loi
    assert np.isnan(return_period(low, 0.0, "low"))


def test_performance_golden(series):
    _, obs, sim = series
    assert bias(obs, sim) == pytest.approx(0.04167875625429763)
    assert NSE(obs, sim) == pytest.approx(0.851623563220732)
    assert KGE(obs, sim) == pytest.approx(0.9319062585373101)
    assert std_ratio(obs, sim) == pytest.approx(1.0443666878024322)


def test_elasticity_golden(series):
    _, obs, sim = series
    assert elasticity(obs, sim) == pytest.approx(0.9645736834027886)


def test_circular_median_golden():
    x = np.array([350.0, 10, 5, 355, 15])
    assert circular_median(x, 365.25) == pytest.approx(5.059670349108231)


def test_snowmelt_golden(series):
    Q, _, _ = series
    assert snowmelt_volume(Q[:100]) == pytest.approx(103.0667829535919)
    assert snowmelt_timing(Q[:100], 0.5) == pytest.approx(54.0)


def test_deficit_volume_golden():
    q = np.array([5.0, 4, 3, 2, 3, 6, 7, 3, 2, 4])
    assert deficit_volume(q, 4.0) == pytest.approx(1.0368)


def test_mannkendall_slope_golden():
    rng = np.random.default_rng(7)
    rng.normal(0, 1, 400)                # même position de flux que series
    rng.normal(0, 0.5, 100)
    x = np.arange(30) + rng.normal(0, 2, 30)
    assert mannkendall_slope(x) == pytest.approx(1.006389413828005)


def test_rat_detects_correlation():
    rng = np.random.default_rng(3)
    x = np.arange(30.0)
    correlated = x + rng.normal(0, 1, 30)
    assert RAT(correlated, x) is True
    assert RAT(rng.normal(0, 1, 30), x) is False
