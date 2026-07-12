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
    """Quantile de probabilité de dépassement p : quantile(Q, 1-p),
    interpolation linéaire (type 7 R = défaut numpy)."""
    q = _to_float_array(Q)
    q = q[~np.isnan(q)]
    p = np.asarray(p, dtype=float)
    res = np.quantile(q, 1 - p)
    return res if res.ndim else float(res)


def exceedance_frequency(Q, threshold):
    """Fréquence de dépassement du seuil : n(Q > threshold) / N
    (N inclut les NaN, comme en R)."""
    q = _to_float_array(Q)
    lim_arr = _to_float_array(threshold) if np.ndim(threshold) > 0 else \
        np.asarray([threshold], dtype=float)
    lim = _rle_most_frequent(lim_arr[~np.isnan(lim_arr)])
    n = np.sum(q[~np.isnan(q)] > lim)
    return float(n) / len(q)


def fdc_slope(Q, p=(0.33, 0.66)):
    """Pente du segment médian de la courbe des débits classés."""
    p = np.asarray(p, dtype=float)
    qp = exceedance_quantile(Q, p)
    return -(np.log10(qp[0]) - np.log10(qp[1])) / (p[1] - p[0])


def _fdc_p(n, norm_spacing):
    if norm_spacing:
        nd = NormalDist()
        return np.array([nd.cdf(v) for v in np.linspace(-3, 3, n)])
    return np.linspace(0, 1, n)


def fdc_probabilities(n=1000, norm_spacing=False):
    """Probabilités de la courbe des débits classés : n points uniformes,
    ou espacés selon une loi normale centrée réduite (norm_spacing)."""
    return _fdc_p(n, norm_spacing)


def fdc_quantiles(Q, n=1000, norm_spacing=False):
    """Quantiles de la courbe des débits classés (mêmes probabilités que
    fdc_probabilities)."""
    return exceedance_quantile(Q, _fdc_p(n, norm_spacing))
