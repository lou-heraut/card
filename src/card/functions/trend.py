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

"""Tendances Mann-Kendall : délègue au GeneralMannKendall de stase."""

from stase import GeneralMannKendall

from .aggregation import _to_float_array


def mannkendall_slope(X, level=0.1, time_dependency_option="AR1"):
    """
    en: Sen-Theil slope (trend) of the generalised Mann-Kendall test.

    fr: Pente de Sen-Theil (tendance) du test de Mann-Kendall généralisé.
    """
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["a"]


def mannkendall_test(X, level=0.1, time_dependency_option="AR1"):
    """
    en: Test outcome, true when the trend is significant at level `level`.

    fr: Résultat du test, vrai si la tendance est significative au niveau
        `level`.
    """
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["h"]


def mannkendall_pvalue(X, level=0.1, time_dependency_option="AR1"):
    """p-value du test de Mann-Kendall généralisé."""
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["p"]
