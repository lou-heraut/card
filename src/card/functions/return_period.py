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

"""return_level — valeur associée à une période de retour
(ex R return_period.R : lois de Gumbel et log-normale)."""

from statistics import NormalDist

import numpy as np
import pandas as pd

from .aggregation import _to_float_array

_EULER = 0.5772


def _gumbel_params(X):
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


def _lognormal_level(X, return_period):
    if return_period <= 1:
        raise ValueError("return_period doit être supérieur à 1")
    x = _to_float_array(X)
    x = x[~np.isnan(x)]
    n = len(x)
    if n == 0:
        return np.nan
    freq = 1 / return_period
    n_null = int(np.sum(x == 0))
    if (n_null / n) <= freq:
        freq = freq - (n_null / n)
        pos = np.log(x[x > 0])
        return np.exp(NormalDist().inv_cdf(freq) * np.std(pos, ddof=1)
                      + np.mean(pos))
    return 0.0


def return_level(X, return_period, water_type="low", dates=None, period=None):
    """Valeur de période de retour `return_period` (années) :
    loi de Gumbel pour les hautes eaux (`water_type="high"`, maxima),
    loi log-normale pour les basses eaux (`water_type="low"`, minima).
    `dates`/`period` permettent de restreindre à une sous-période."""
    x = _to_float_array(X)
    if dates is not None and period is not None:
        d = pd.to_datetime(pd.Series(dates) if not isinstance(dates, pd.Series)
                           else dates)
        p0, p1 = pd.Timestamp(period[0]), pd.Timestamp(period[1])
        ok = ((p0 <= d) & (d <= p1)).to_numpy()
        x = x[ok]

    if water_type == "high":
        a, b = _gumbel_params(x)
        return _gumbel_level(a, b, return_period)
    if water_type == "low":
        return _lognormal_level(x, return_period)
    raise ValueError(f"water_type invalide : {water_type!r}")
