# Copyright 2022-2026 Louis Héraut <louis.heraut@inrae.fr>*1
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

"""delta : changement d'une variable entre deux périodes (ex R get_deltaX)."""

import numpy as np
import pandas as pd

from .aggregation import _to_float_array
from .baseflow import BFI
from .return_period import return_level


def _nanmean_or_nan(x):
    if len(x) == 0 or np.all(np.isnan(x)):
        return np.nan
    return np.nanmean(x)


def _one_date(v):
    """Une date depuis un scalaire (str/Timestamp) ou une colonne constante
    par série (Series/ndarray, cas des paramètres d'horizon en entrée)."""
    if isinstance(v, (pd.Series, np.ndarray)):
        s = pd.Series(v).dropna()
        v = s.iloc[0] if len(s) else np.nan
    return pd.Timestamp(v)


def delta(X, dates, ref_start, ref_end, horizon_start, horizon_end, relative,
          return_period=None, water_type="low", Q_for_BFI=None):
    """Change in X between a reference period and a horizon period.

    Parameters
    ----------
    X : array-like
        The values to aggregate over each period.
    dates : array-like, optional
        Column of dates, aligned on X.
    ref_start, ref_end : optional
        Bounds of the reference period.
    horizon_start, horizon_end : optional
        Bounds of the horizon period.
    relative : bool, default False
        Return the relative change in per cent rather than the difference.
    return_period : float, optional
        Aggregate with a return level of that period instead of a mean.
    water_type : {"low", "high"}, default "low"
        Which tail the return level is fitted on.
    Q_for_BFI : array-like, optional
        Aggregate with a base flow index instead of a mean.

    Returns
    -------
    float
        Horizon minus reference, or the relative change in per cent when
        `relative` is set.

    Notes
    -----
    The four bounds are dates, scalars or columns constant per series
    (horizon parameters supplied as input, from which the constant value is
    taken).
    """
    x = _to_float_array(X)
    d = pd.to_datetime(pd.Series(dates) if not isinstance(dates, pd.Series)
                       else dates)

    p0, p1 = _one_date(ref_start), _one_date(ref_end)
    f0, f1 = _one_date(horizon_start), _one_date(horizon_end)
    ok_past = ((p0 <= d) & (d <= p1)).to_numpy()
    ok_future = ((f0 <= d) & (d <= f1)).to_numpy()
    x_past = x[ok_past]
    x_future = x[ok_future]

    if return_period is not None:
        agg_past = return_level(x_past, return_period=return_period,
                                water_type=water_type)
        agg_future = return_level(x_future, return_period=return_period,
                                  water_type=water_type)
    elif Q_for_BFI is not None:
        q = _to_float_array(Q_for_BFI)
        agg_past = BFI(q[ok_past], x_past)
        agg_future = BFI(q[ok_future], x_future)
    else:
        agg_past = _nanmean_or_nan(x_past)
        agg_future = _nanmean_or_nan(x_future)

    if relative:
        return (agg_future - agg_past) / agg_past * 100
    return agg_future - agg_past
