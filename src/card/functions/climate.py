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

"""Élasticité climatique et coefficient de ruissellement
(ex R elasticity.R et seasonal_dynamic.R)."""

import numpy as np

from .aggregation import _to_float_array


def elasticity(Q, X):
    """Élasticité bivariée de Sankarasubramanian et al. (2001) :
    médiane de ((Q-Qmean)/(X-Xmean)) * Xmean/Qmean."""
    q = _to_float_array(Q)
    x = _to_float_array(X)
    q_mean = np.nanmean(q)
    x_mean = np.nanmean(x)
    with np.errstate(divide="ignore", invalid="ignore"):
        eps = (q - q_mean) / (x - x_mean) * x_mean / q_mean
    return np.nanmedian(eps)


def runoff_coefficient(Q, R):
    """Coefficient de ruissellement : somme(Q) / somme(R)."""
    q = _to_float_array(Q)
    r = _to_float_array(R)
    if len(q) != len(r):
        import warnings
        warnings.warn("'Q' et 'R' n'ont pas la même longueur !")
    return np.nansum(q) / np.nansum(r)
