# Copyright 2020      Ivan Horner <ivan.horner@irstea.fr>*3
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

"""Quantiles de dépassement et courbe des débits classés
(ex R flow_duration_curve.R)."""

from statistics import NormalDist

import numpy as np

from .aggregation import _rle_most_frequent, _to_float_array


def exceedance_quantile(Q, p):
    """Discharge exceeded a fraction of the time, read off the flow duration curve.

    Parameters
    ----------
    Q : array-like
        Discharge series.
    p : float
        Fraction of the time the value is exceeded, between 0 and 1.

    Returns
    -------
    float
        ``quantile(Q, 1 - p)``, by linear interpolation (R type 7, the numpy
        default). Gaps are dropped before the computation.
    """
    q = _to_float_array(Q)
    q = q[~np.isnan(q)]
    p = np.asarray(p, dtype=float)
    res = np.quantile(q, 1 - p)
    return res if res.ndim else float(res)


def exceedance_frequency(Q, threshold):
    """Share of the OBSERVED time when Q is strictly above a threshold.

    Parameters
    ----------
    Q : array-like
        Discharge series.
    threshold : float or array-like
        The threshold to exceed.

    Returns
    -------
    float
        ``n(Q > threshold) / N``, where N counts only the recorded time
        steps, like the numerator.

    Notes
    -----
    A missing day is a day nothing is known about, not a day without
    exceedance. A fully missing series therefore gives NaN, not 0.
    """
    q = _to_float_array(Q)
    lim_arr = _to_float_array(threshold) if np.ndim(threshold) > 0 else \
        np.asarray([threshold], dtype=float)
    lim = _rle_most_frequent(lim_arr[~np.isnan(lim_arr)])
    observes = ~np.isnan(q)
    if not observes.any():
        return np.nan
    return float(np.sum(q[observes] > lim)) / int(observes.sum())


def fdc_slope(Q, p=(0.33, 0.66)):
    """Slope of the middle segment of the flow duration curve.

    Parameters
    ----------
    Q : array-like
        Discharge series.
    p : tuple of float, default (0.33, 0.66)
        The two exceedance probabilities bounding the segment.

    Returns
    -------
    float
        The slope of the curve between the two probabilities.
    """
    p = np.asarray(p, dtype=float)
    qp = exceedance_quantile(Q, p)
    return -(np.log10(qp[0]) - np.log10(qp[1])) / (p[1] - p[0])


def _fdc_p(n, norm_spacing):
    if norm_spacing:
        nd = NormalDist()
        return np.array([nd.cdf(v) for v in np.linspace(-3, 3, n)])
    return np.linspace(0, 1, n)


def fdc_probabilities(X=None, n=1000, norm_spacing=False):
    """Probability axis of the flow duration curve.

    Parameters
    ----------
    X : array-like, optional
        Kept for signature compatibility with the curve it accompanies.
    n : int, default 1000
        Number of points.
    norm_spacing : bool, default False
        Space the points along a standard normal law rather than evenly.

    Returns
    -------
    numpy.ndarray
        The probability axis, of length ``n``.
    """
    return _fdc_p(n, norm_spacing)


def fdc_quantiles(Q, n=1000, norm_spacing=False):
    """Quantiles of the flow duration curve.

    Parameters
    ----------
    Q : array-like
        Discharge series.
    n : int, default 1000
        Number of points, over the same probabilities as
        :func:`fdc_probabilities`.
    norm_spacing : bool, default False
        Space the points along a standard normal law rather than evenly.

    Returns
    -------
    numpy.ndarray
        The discharges of the curve, of length ``n``.
    """
    return exceedance_quantile(Q, _fdc_p(n, norm_spacing))
