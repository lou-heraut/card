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
    """Différence a - b, terme à terme.

    Tout-NaN d'un côté → NaN. Un résultat de longueur 1 est rendu comme
    un nombre, par commodité de type : c'est toujours une valeur par pas
    de temps.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _squeeze_scalar(a - b)


def ratio(a, b):
    """Rapport a / b, terme à terme.

    Mêmes conventions que difference.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _squeeze_scalar(a / b)


def difference_longest_run(a, b):
    """Différence des valeurs du plus long palier de a et de b : UNE valeur.

    Sert quand a et b sont des colonnes constantes sur le groupe (un seuil
    rediffusé par un `keep: all` en amont) et qu'on en veut la valeur, une
    seule fois. Le plus long palier est retenu après avoir écarté les
    lacunes, si bien qu'un trou dans la colonne ne contamine pas le
    résultat, là où la soustraction terme à terme rendrait NaN ce jour-là.
    Tout-NaN d'un côté → NaN.
    """
    a = _to_float_array(a)
    b = _to_float_array(b)
    if np.all(np.isnan(a)) or np.all(np.isnan(b)):
        return np.nan
    return _rle_most_frequent(a) - _rle_most_frequent(b)


def ratio_longest_run(a, b):
    """Rapport des valeurs du plus long palier de a et de b : UNE valeur.

    Mêmes conventions que difference_longest_run.
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
    """Somme ignorant les NaN, mais NaN si TOUT est NaN (≠ np.nansum
    qui vaut 0.0) : une année sans aucune donnée n'est pas un cumul
    nul. Résultat divisé par div.
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
    """Moyenne mobile centrée de fenêtre k : lisse la série sans la
    décaler dans le temps.

    Fenêtre alignée sur son centre (pandas center=True), lacunes
    propagées strictement : une fenêtre contenant un NaN vaut NaN.
    cyclical=True : la série est considérée circulaire (régimes
    interannuels). Sortie de même longueur que X (transform).
    """
    x = _to_float_array(X)
    if cyclical:
        return _roll_cyclical(x, k, "mean")
    return _roll_center(x, k, "mean")


def rollsum_center(X, k, cyclical=False):
    """Somme mobile centrée de fenêtre k : cumul glissant sur k pas de
    temps, sans décalage.

    Mêmes conventions que rollmean_center. Sortie de même longueur que X
    (transform).
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
    """Différence X - Y sur un axe circulaire de période donnée (ex.
    jours de l'année, periodicity=365.25) : quand l'écart dépasse une
    demi-période, le plus petit terme est décalé d'une période.
    """
    X, Y = _circular_tweak(X, Y, periodicity)
    return _squeeze_scalar(X - Y)


def circular_ratio(X, Y, periodicity):
    """Rapport X / Y après recalage circulaire des deux termes
    (cf. circular_difference).
    """
    X, Y = _circular_tweak(X, Y, periodicity)
    return _squeeze_scalar(X / Y)


def circular_median(X, periodicity):
    """Médiane circulaire de X sur une période donnée (arctangente des
    médianes de sin/cos), ex. date médiane d'un événement annuel.
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
# Rien pour difference_longest_run ni ratio_longest_run : elles réduisent.

# GLOSE MUETTE : choix éditorial, pas propriété du calcul. Pour
# `ratio(a, b)`, l'appel affiché dans la figure dit déjà tout et la glose
# ne ferait que le répéter. Déclaré ici plutôt que listé dans render.py :
# un renommage emporte la déclaration avec lui. Les jumelles
# `*_longest_run` ont, elles, quelque chose à expliquer, et le font.
ratio.glose_inutile = True
difference.glose_inutile = True
