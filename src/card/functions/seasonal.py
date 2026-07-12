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

"""delta — changement d'une variable entre deux périodes (ex R get_deltaX)."""

import numpy as np
import pandas as pd

from .aggregation import _to_float_array
from .baseflow import BFI
from .return_period import return_level


def _nanmean_or_nan(x):
    if len(x) == 0 or np.all(np.isnan(x)):
        return np.nan
    return np.nanmean(x)


def delta(X, dates, past, future, relative,
          return_period=None, water_type="low", Q_for_BFI=None):
    """Différence de X entre deux périodes.

    X est agrégé sur `past` puis sur `future` (moyenne par défaut ; niveau
    de retour si `return_period` est donné ; BFI si `Q_for_BFI` est donné),
    et la fonction retourne future − past (`relative=False`) ou le
    changement relatif en % (`relative=True`).
    """
    x = _to_float_array(X)
    d = pd.to_datetime(pd.Series(dates) if not isinstance(dates, pd.Series)
                       else dates)

    p0, p1 = pd.Timestamp(past[0]), pd.Timestamp(past[1])
    f0, f1 = pd.Timestamp(future[0]), pd.Timestamp(future[1])
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
