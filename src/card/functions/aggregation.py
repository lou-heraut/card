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

"""Port Python de R/global.R (fonctions d'agrégation et de transformation).

Convention d'index : les fonctions positionnelles (which.*NA, apply_threshold
first/last) retournent des index 0-based, attendus par le pipeline is_date
d'EXstat_py (np.argmax). La chaîne complète (fonction 0-based + conversion
_apply_is_date) reproduit exactement les valeurs du pipeline R (validé
empiriquement sur tQJXA et delta-endLF_H).
"""

import os

import numpy as np
import pandas as pd


def _to_float_array(X) -> np.ndarray:
    if isinstance(X, pd.Series):
        return X.astype("float64").to_numpy()
    return np.asarray(X, dtype=np.float64)


# ── 0. BASIC ────────────────────────────────────────────────────────────────

def _rle_most_frequent(x: np.ndarray):
    """Valeur du run le plus long (équivalent R rle + which.max des longueurs)."""
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return np.nan
    change = np.concatenate([[True], x[1:] != x[:-1]])
    starts = np.flatnonzero(change)
    lengths = np.diff(np.concatenate([starts, [len(x)]]))
    return x[starts[np.argmax(lengths)]]


def _squeeze_scalar(x):
    """Résultat élémentaire de taille 1 → scalaire (en R un vecteur de
    longueur 1 est un scalaire ; les agrégations attendent un scalaire)."""
    x = np.asarray(x)
    if x.size == 1:
        return float(x.reshape(-1)[0])
    return x


# Ces quatre fonctions arithmétiques gardent la longueur de leur entrée :
# une valeur d'entrée, une valeur de sortie. Leurs jumelles `*_longest_run`,
# plus bas, réduisent au contraire à UNE valeur. Une fonction ne peut avoir
# qu'une de ces deux natures, sans quoi `is_transform` ne veut rien dire et
# la figure ne peut pas annoncer ce que produit une étape : c'est pourquoi
# le drapeau `first` a été scindé le 2026-07-31 (cf. RENAMING.md).

def difference(a, b):
    """Difference between two series, term by term.

    Parameters
    ----------
    a, b : array-like
        The two series.

    Returns
    -------
    numpy.ndarray or float
        ``a - b``, NaN if either side is all NaN. A result of length 1 is
        returned as a number, for convenience of type: it is still one value
        per time step.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _squeeze_scalar(a - b)


def ratio(a, b):
    """Ratio of two series, term by term.

    Parameters
    ----------
    a, b : array-like
        The two series.

    Returns
    -------
    numpy.ndarray or float
        ``a / b``, under the same conventions as :func:`difference`.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _squeeze_scalar(a / b)


def ratio_longest_run(a, b):
    """Ratio of the longest-run values of two series: ONE value.

    For columns that are constant over the group, a threshold broadcast by
    an upstream ``keep: all`` for instance, whose value is wanted once.

    Parameters
    ----------
    a, b : array-like
        The two columns.

    Returns
    -------
    float
        The ratio of the two longest-run values, NaN if either side is all
        NaN.

    Notes
    -----
    The longest run is taken after dropping the gaps, so a hole in the
    column does not contaminate the result, where a term-by-term division
    would return NaN on that day.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _rle_most_frequent(a) / _rle_most_frequent(b)


# ── 1. SOMME STRICTE ────────────────────────────────────────────────────────
# minNA/maxNA/which.*NA ont été remplacés par np.nanmin/nanmax/nanargmin/
# nanargmax directement dans les fiches YAML (comportements identiques,
# div= jamais utilisé dans les fiches). Seul nansum_strict subsiste :
# np.nansum(tout-NaN) vaut 0.0 alors que la sémantique voulue est NaN
# (année sans aucune donnée ≠ cumul nul). NB : le `sum` R avec na.rm=TRUE
# vaut aussi 0 ; les fiches qui utilisaient `sum` sont passées à nansum,
# celles qui utilisaient nansum_strict gardent la version stricte.

def nansum_strict(X, div=1):
    """Sum ignoring the gaps, but NaN when everything is a gap.

    Parameters
    ----------
    X : array-like
        The values to sum.
    div : float, default 1
        The result is divided by this.

    Returns
    -------
    float
        The sum, or NaN when no value is available. A period without any
        data is not a zero total, whereas ``np.nansum`` answers 0.0.
    """
    x = _to_float_array(X)
    if np.all(np.isnan(x)):
        return np.nan
    return np.nansum(x) / div


# ── 3. ROLLING (transforms : sortie vectorielle, même longueur) ────────────

def _roll_center(x: np.ndarray, k: int, stat: str) -> np.ndarray:
    """Rolling centré, convention pandas (center=True), na.rm=FALSE : toute
    fenêtre contenant un NaN donne NaN.

    Divergence assumée avec R (RcppRoll) pour k pair : pandas place le jour
    excédentaire à gauche de la fenêtre ([i-5, i+4] pour k=10) là où RcppRoll
    le place à droite ([i-4, i+5]). La série Python est donc décalée de +1
    position par rapport au R pour k pair ; identique pour k impair. Choix
    délibéré : rester sur l'outil pandas standard plutôt que répliquer un
    détail d'implémentation R (décision utilisateur, 2026-07-11).

    Pour la validation croisée, CARD_ROLL_COMPAT=rcpp bascule sur
    l'alignement RcppRoll exact.
    """
    s = pd.Series(x)
    if os.environ.get("CARD_ROLL_COMPAT") == "rcpp":
        r = getattr(s.rolling(k, min_periods=k), stat)()
        return r.shift(-int(np.ceil((k - 1) / 2))).to_numpy()
    return getattr(s.rolling(k, center=True, min_periods=k), stat)().to_numpy()


def _roll_cyclical(x: np.ndarray, k: int, stat: str) -> np.ndarray:
    n = len(x)
    padded = np.concatenate([x[n - k:], x, x[: k + 1]])
    rolled = _roll_center(padded, k, stat)
    return rolled[k: len(rolled) - (k + 1)]


def rollmean_center(X, k, cyclical=False):
    """Centred rolling mean: smooths the series without shifting it in time.

    Parameters
    ----------
    X : array-like
        The series to smooth.
    k : int
        Width of the window.
    cyclical : bool, default False
        Treat the series as circular, for inter-annual regimes.

    Returns
    -------
    numpy.ndarray
        Same length as X (transform). The window is aligned on its centre
        and gaps propagate strictly: a window containing a NaN is NaN.
    """
    x = _to_float_array(X)
    if cyclical:
        return _roll_cyclical(x, k, "mean")
    return _roll_center(x, k, "mean")


def rollsum_center(X, k, cyclical=False):
    """Centred rolling sum: running total over k time steps, without shift.

    Parameters
    ----------
    X : array-like
        The series to accumulate.
    k : int
        Width of the window.
    cyclical : bool, default False
        Treat the series as circular, for inter-annual regimes.

    Returns
    -------
    numpy.ndarray
        Same length as X (transform), under the same conventions as
        :func:`rollmean_center`.
    """
    x = _to_float_array(X)
    if cyclical:
        return _roll_cyclical(x, k, "sum")
    return _roll_center(x, k, "sum")


# ── 4. CIRCULAR STAT ────────────────────────────────────────────────────────

def _circular_tweak(X, Y, periodicity):
    """Décale de +periodicity le plus petit des deux éléments quand l'écart
    dépasse une demi-période (équivalent circularTWEAK R)."""
    X = _to_float_array(X).copy()
    Y = _to_float_array(Y).copy()
    with np.errstate(invalid="ignore"):
        to_add = np.abs(X - Y) > (periodicity / 2)
        xy_min = np.fmin(X, Y)
        x_is_min = X == xy_min
        y_is_min = Y == xy_min
    to_add = np.where(np.isnan(to_add.astype(float)), False, to_add)
    x_is_min = np.where(np.isnan(x_is_min.astype(float)), False, x_is_min)
    y_is_min = np.where(np.isnan(y_is_min.astype(float)), False, y_is_min)
    X[to_add & x_is_min] += periodicity
    Y[to_add & y_is_min] += periodicity
    return X, Y


def circular_difference(X, Y, periodicity):
    """Difference between two series on a circular axis.

    Parameters
    ----------
    X, Y : array-like
        The two series, on a cyclic axis.
    periodicity : float
        Length of one period, 365.25 for days of the year for instance.

    Returns
    -------
    numpy.ndarray
        ``X - Y``, the smaller term being shifted by one period when the gap
        exceeds half a period.
    """
    X, Y = _circular_tweak(X, Y, periodicity)
    return _squeeze_scalar(X - Y)


def circular_ratio(X, Y, periodicity):
    """Ratio of two series after circular realignment of both terms.

    Parameters
    ----------
    X, Y : array-like
        The two series, on a cyclic axis.
    periodicity : float
        Length of one period.

    Returns
    -------
    numpy.ndarray
        ``X / Y``, realigned as in :func:`circular_difference`.
    """
    X, Y = _circular_tweak(X, Y, periodicity)
    return _squeeze_scalar(X / Y)


def circular_median(X, periodicity):
    """Median of a cyclic quantity, a date within the year for instance.

    Parameters
    ----------
    X : array-like
        The values, on a cyclic axis.
    periodicity : float
        Length of one period.

    Returns
    -------
    float
        The arctangent of the medians of the sine and the cosine. A plain
        mean would place on 1 July the median of two dates straddling
        1 January.
    """
    x = _to_float_array(X)
    scaling = 2 * np.pi / periodicity
    radians = x * scaling
    med = np.arctan2(np.nanmedian(np.sin(radians)),
                     np.nanmedian(np.cos(radians))) / scaling
    if np.isnan(med):
        return np.nan
    return med if med >= 0 else med + periodicity


# ── PROPRIÉTÉS DÉCLARÉES ────────────────────────────────────────────────────
# Rassemblées en fin de fichier, après toutes les définitions, pour qu'on
# lise d'un coup d'œil la nature de chacune.

# TRANSFORME : une valeur d'entrée, une valeur de sortie. C'est le cas RARE
# et délibéré, donc celui qui se déclare ; l'absence vaut « réduit ».
# `render.decoupe` s'en sert pour dire ce que produit une étape
# `time_step: none` / `keep: all`, et un test le MESURE (voir
# tests/test_nature_fonctions.py) : une déclaration fausse rougit.
rollmean_center.is_transform = True
rollsum_center.is_transform = True
difference.is_transform = True
ratio.is_transform = True
circular_difference.is_transform = True
circular_ratio.is_transform = True
# Rien pour ratio_longest_run : elle réduit.
