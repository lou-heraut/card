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
    """Sen-Theil slope of the generalised Mann-Kendall test.

    Parameters
    ----------
    X : array-like
        The series to test, in chronological order.
    level : float, default 0.1
        Significance level of the test.
    time_dependency_option : {"AR1", "INDE", "LTP"}, default "AR1"
        Dependency model assumed for the series.

    Returns
    -------
    float
        The trend, in the unit of X per time step.
    """
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["a"]


def mannkendall_test(X, level=0.1, time_dependency_option="AR1"):
    """Outcome of the generalised Mann-Kendall test.

    Parameters
    ----------
    X : array-like
        The series to test, in chronological order.
    level : float, default 0.1
        Significance level of the test.
    time_dependency_option : {"AR1", "INDE", "LTP"}, default "AR1"
        Dependency model assumed for the series.

    Returns
    -------
    bool
        True when the trend is significant at `level`.
    """
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["h"]


def mannkendall_pvalue(X, level=0.1, time_dependency_option="AR1"):
    """p-value of the generalised Mann-Kendall test.

    Parameters
    ----------
    X : array-like
        The series to test, in chronological order.
    level : float, default 0.1
        Significance level of the test.
    time_dependency_option : {"AR1", "INDE", "LTP"}, default "AR1"
        Dependency model assumed for the series.

    Returns
    -------
    float
        The p-value of the test.
    """
    res = GeneralMannKendall(_to_float_array(X), level=level,
                             time_dependency_option=time_dependency_option,
                             do_detrending=True)
    return res["p"]
