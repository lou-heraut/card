# Copyright 2022      David Dorchies <david.dorchies@inrae.fr>*2
#           2022-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
# *2 INRAE, UMR G-Eau, Montpellier, France
# *3 IRSTEA, France
#
# This file is part of the card Python package (Python port of the
# CARD R package).
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.
#
# card is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.

"""Lois de période de retour (ex R return_period.R).

Conventions :
- basses eaux (`water_type="low"`) : loi log-normale mixte, fraction
  p0 d'années nulles + log-normale sur les valeurs strictement
  positives ; T = 1/P(X <= x) (non-dépassement) ;
- hautes eaux (`water_type="high"`) : loi de Gumbel ;
  T = 1/P(X > x) (dépassement).

`return_level` : T (années) -> valeur ; `return_period` : seuil ->
T (années). Les deux sont inverses exactes l'une de l'autre sur la
même série.
"""

from statistics import NormalDist

from .period import _const_date, _subset_period

import numpy as np
import pandas as pd

from .aggregation import _rle_most_frequent, _to_float_array

_EULER = 0.5772


# ── Gumbel (hautes eaux, maxima) ───────────────────────────────────────────

def _gumbel_params(X):
    """Ajustement par la méthode des moments : (a, b) tels que
    F(x) = exp(-exp(-(x - a)/b))."""
    x = _to_float_array(X)
    b = np.sqrt(6) / np.pi * np.std(x[~np.isnan(x)], ddof=1)
    a = np.nanmean(x) - b * _EULER
    return a, b


def _gumbel_level(a, b, return_period):
    if return_period <= 1:
        raise ValueError("return_period doit être supérieur à 1")
    F_x = 1 - (1 / return_period)
    u = -np.log(-np.log(F_x))
    return b * u + a


def _gumbel_period(a, b, threshold):
    """T = 1/P(X > threshold) sous la loi ajustée. Seuil sous le corps
    de la loi -> T tend vers 1 (dépassé presque chaque année)."""
    F_x = np.exp(-np.exp(-(threshold - a) / b))
    if F_x >= 1.0:
        return np.inf
    return max(1.0 / (1.0 - F_x), 1.0)


# ── Log-normale mixte (basses eaux, minima) ────────────────────────────────

def _lognormal_params(X):
    """Ajuste la loi mixte : (p0, mu, sigma, n) avec p0 la fraction
    d'années nulles et (mu, sigma) moyenne/écart-type (ddof=1) du log
    des valeurs strictement positives. n = 0 si aucune donnée ;
    mu/sigma NaN si aucune valeur positive."""
    x = _to_float_array(X)
    x = x[~np.isnan(x)]
    n = len(x)
    if n == 0:
        return np.nan, np.nan, np.nan, 0
    p0 = float(np.sum(x == 0)) / n
    pos = np.log(x[x > 0])
    if len(pos) == 0:
        return p0, np.nan, np.nan, n
    return p0, float(np.mean(pos)), float(np.std(pos, ddof=1)), n


# NOTE p0 : approche des probabilités conditionnelles (Jennings &
# Benson 1969) : F(x) = p0 + (1 - p0) * F_pos(x). Le R historique
# omettait la division par (1 - p0) (quantiles biaisés bas jusqu'à
# -13 % sur stations intermittentes, parité volontairement rompue le
# 2026-07-18, cf. RENAMING.md). Identique quand p0 = 0. Les DEUX
# helpers ci-dessous portent la convention : les modifier ensemble
# garde level/period inverses exactes.

def _lognormal_quantile(p0, mu, sigma, freq):
    """Quantile de non-dépassement freq sous la loi mixte.
    freq == p0 exactement : 0.0 (borne du bloc d'années nulles)."""
    if p0 < freq:
        freq_pos = (freq - p0) / (1.0 - p0)
        return float(np.exp(NormalDist().inv_cdf(freq_pos) * sigma + mu))
    return 0.0


def _lognormal_cdf(p0, mu, sigma, x):
    """P(X <= x) sous la loi mixte (inverse exacte du quantile).
    Bornée par 1 par construction."""
    if x == 0:
        return p0
    return p0 + (1.0 - p0) * NormalDist().cdf((np.log(x) - mu) / sigma)


def _lognormal_level(X, return_period):
    if return_period <= 1:
        raise ValueError("return_period doit être supérieur à 1")
    p0, mu, sigma, n = _lognormal_params(X)
    if n == 0:
        return np.nan
    if np.isnan(mu):        # aucune valeur positive : tout est nul
        return 0.0
    return _lognormal_quantile(p0, mu, sigma, 1.0 / return_period)


def _lognormal_period(X, threshold):
    p0, mu, sigma, n = _lognormal_params(X)
    if n == 0 or threshold < 0:
        return np.nan
    if threshold == 0:
        # P(X <= 0) = p0 ; jamais nul sous la loi si p0 = 0
        return 1.0 / p0 if p0 > 0 else np.nan
    if np.isnan(mu):        # aucune valeur positive : seuil toujours franchi
        return 1.0
    F_x = _lognormal_cdf(p0, mu, sigma, threshold)
    if F_x <= 0.0:
        return np.nan      # seuil hors du support (sous-flux numérique)
    return max(1.0 / F_x, 1.0)


# ── API fiches ─────────────────────────────────────────────────────────────

def return_level(X, return_period, water_type="low", dates=None, period=None,
                 period_start=None, period_end=None):
    """Value reached on average once every `return_period` years.

    Parameters
    ----------
    X : array-like
        The series to fit, usually annual minima or maxima.
    return_period : float
        Return period, in years.
    water_type : {"low", "high"}, default "low"
        `"low"` fits a log-normal law on minima, `"high"` a Gumbel law
        on maxima.
    dates : array-like, optional
        Column of dates, aligned on X.
    period : list, optional
        Pair of bounds restricting the fit.
    period_start, period_end : optional
        The same bounds given separately, often columns constant per series.

    Returns
    -------
    float
        The value of X reached on average once every `return_period`
        years.
    """
    if period_start is not None:
        period = [_const_date(period_start), _const_date(period_end)]
    x = _subset_period(_to_float_array(X), dates, period)
    if water_type == "high":
        a, b = _gumbel_params(x)
        return _gumbel_level(a, b, return_period)
    if water_type == "low":
        return _lognormal_level(x, return_period)
    raise ValueError(f"water_type invalide : {water_type!r}")


def return_period(X, threshold, water_type="low", dates=None, period=None):
    """Return period, in years, of a threshold: the inverse of a return level.

    Parameters
    ----------
    X : array-like
        The series to fit, annual minima or maxima.
    threshold : float or array-like
        The threshold whose return period is wanted. A scalar, or a column
        constant per series, in which case the most frequent value is kept
        and NaN is returned when all are missing.
    water_type : {"low", "high"}, default "low"
        `"low"` gives `T = 1 / P(X <= threshold)` under a mixed
        log-normal law, `"high"` gives `T = 1 / P(X > threshold)` under
        a Gumbel law.
    dates : array-like, optional
        Column of dates, aligned on X.
    period : list, optional
        Pair of bounds restricting the fit.

    Returns
    -------
    float
        A value greater than or equal to 1. A threshold far from the body of
        the law gives an extrapolated period, returned as is.
    """
    lim_arr = _to_float_array(threshold) \
        if np.ndim(threshold) > 0 or isinstance(threshold, pd.Series) \
        else np.asarray([threshold], dtype=np.float64)
    if np.all(np.isnan(lim_arr)):
        return np.nan
    lim_val = _rle_most_frequent(lim_arr)

    x = _subset_period(_to_float_array(X), dates, period)
    if water_type == "high":
        a, b = _gumbel_params(x)
        return _gumbel_period(a, b, lim_val)
    if water_type == "low":
        return _lognormal_period(x, lim_val)
    raise ValueError(f"water_type invalide : {water_type!r}")
