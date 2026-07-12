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

"""Port Python de R/baseflow.R — séparation de débit de base
(Wallingford et Lyne & Hollick) et indicateurs dérivés."""

import numpy as np

from .aggregation import _to_float_array


def approx_extrap(x, y, xout):
    """Interpolation linéaire avec extrapolation linéaire au-delà des bornes
    (équivalent approxExtrap R : pente des 2 premiers / 2 derniers points)."""
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    ok = ~(np.isnan(x) | np.isnan(y))
    x, y = x[ok], y[ok]
    _, idx = np.unique(x, return_index=True)
    x, y = x[idx], y[idx]

    xout = np.asarray(xout, dtype=float)
    w = np.interp(xout, x, y)
    below = xout < x[0]
    if below.any():
        w[below] = (y[1] - y[0]) / (x[1] - x[0]) * (xout[below] - x[0]) + y[0]
    above = xout > x[-1]
    if above.any():
        w[above] = ((y[-1] - y[-2]) / (x[-1] - x[-2])
                    * (xout[above] - x[-2]) + y[-2])
    return w


def _bfs_wallingford(Q, d=5, w=0.9):
    N = len(Q)
    if np.all(np.isnan(Q)):
        return np.full(N, np.nan)

    # minimum par tranche de d jours (indices globaux 0-based)
    id_min = []
    for start in range(0, N, d):
        s = Q[start:start + d]
        if np.all(np.isnan(s)):
            id_min.append(np.nan)
        else:
            id_min.append(start + int(np.nanargmin(s)))
    id_min = np.asarray(id_min, dtype=float)
    q_min = np.array([Q[int(i)] if not np.isnan(i) else np.nan
                      for i in id_min])

    if len(q_min) == 1:
        return np.full(N, np.nan)

    # points pivots : w*Qmin_k < min(Qmin_k-1, Qmin_k+1) (NA -> False)
    prev_ = np.concatenate([[np.nan], q_min[:-1]])
    next_ = np.concatenate([q_min[1:], [np.nan]])
    with np.errstate(invalid="ignore"):
        test = w * q_min < np.minimum(prev_, next_)
    test = np.where(np.isnan(w * q_min) | np.isnan(np.minimum(prev_, next_)),
                    False, test)

    id_pivots = id_min[test]
    pivots = q_min[test]
    ok = ~(np.isnan(id_pivots) | np.isnan(pivots))
    if ok.sum() >= 2:
        BF = approx_extrap(id_pivots[ok], pivots[ok], np.arange(N))
        BF[np.isnan(Q)] = np.nan
        BF[BF < 0] = 0
        with np.errstate(invalid="ignore"):
            over = BF > Q
        BF[np.where(np.isnan(over), False, over)] = \
            Q[np.where(np.isnan(over), False, over)]
        return BF
    return np.full(N, np.nan)


def _bfs_lyne_hollick(Q, a=0.925, passes=3):
    n = len(Q)
    q_tmp = Q.copy()
    for p in range(1, passes + 1):
        if p % 2 == 0:
            q_tmp = q_tmp[::-1]
        SF = np.zeros(n)
        for i in range(1, n):
            if not np.isnan(q_tmp[i]) and not np.isnan(q_tmp[i - 1]):
                SF[i] = a * SF[i - 1] + (1 + a) / 2 * (q_tmp[i] - q_tmp[i - 1])
            else:
                SF[i] = 0.0
        # comme en R : clamp négatif APRÈS la récursion complète
        SF[SF < 0] = 0
        q_tmp = q_tmp - SF
        if p % 2 == 0:
            q_tmp = q_tmp[::-1]
    return q_tmp


def baseflow(Q, d=5, w=0.9, a=0.925, passes=3, method="Wal"):
    """Débit de base par séparation d'hydrogramme. method='Wal'
    (Wallingford / smoothed minima : blocs de d jours, points
    pivots au facteur w) ou 'LH' (filtre de Lyne & Hollick,
    paramètre a, nombre de passes). Sortie de même longueur que Q
    (transform).
    """
    q = _to_float_array(Q)
    if method == "Wal":
        return _bfs_wallingford(q, d=d, w=w)
    if method == "LH":
        return _bfs_lyne_hollick(q, a=a, passes=passes)
    raise ValueError(f"méthode baseflow invalide : {method!r}")


def quickflow(Q, d=5, w=0.9, a=0.925, passes=3, method="Wal"):
    """Écoulement rapide : Q - baseflow(Q) (mêmes paramètres).
    Sortie de même longueur que Q (transform).
    """
    q = _to_float_array(Q)
    return q - baseflow(q, d=d, w=w, a=a, passes=passes, method=method)


baseflow.is_transform = True
quickflow.is_transform = True


def BFI(Q, BF):
    """Base Flow Index : somme du débit de base / somme du débit
    total (NaN ignorés).
    """
    q = _to_float_array(Q)
    bf = _to_float_array(BF)
    if len(q) != len(bf):
        import warnings
        warnings.warn("'Q' et 'BF' n'ont pas la même longueur !")
    return np.nansum(bf) / np.nansum(q)


def BFM(BFA):
    """Base Flow Magnitude : (max - min) / max des débits de base
    agrégés (ex. régime mensuel interannuel).
    """
    x = _to_float_array(BFA)
    bfa_max = np.nanmax(x)
    bfa_min = np.nanmin(x)
    return (bfa_max - bfa_min) / bfa_max


def snowmelt_volume(Q, d=5, w=0.9, a=0.925, passes=3, method="Wal"):
    """Volume de fonte (hm³) : somme du débit de base (m³/s) convertie
    en volume journalier (× 86 400 s / 10⁶).
    """
    BF = baseflow(Q, d=d, w=w, a=a, passes=passes, method=method)
    return np.nansum(BF) * 24 * 3600 / 1e6


def snowmelt_timing(Q, fraction, d=5, w=0.9, a=0.925, passes=3, method="Wal"):
    """Index (0-based, convention du pipeline is_date) où la fraction p du
    volume total de fonte est atteinte."""
    BF = baseflow(Q, d=d, w=w, a=a, passes=passes, method=method)
    vol = np.cumsum(BF)
    if np.all(np.isnan(vol)):
        return np.nan
    pvol = vol / np.nanmax(vol)
    diff = np.abs(pvol - fraction)
    if np.all(np.isnan(diff)):
        return np.nan
    return float(np.nanargmin(diff))


def snowmelt_duration(Q, fraction1, fraction2, d=5, w=0.9, a=0.925, passes=3, method="Wal"):
    """Durée (en pas de temps, bornes incluses) entre les atteintes des
    fractions fraction1 puis fraction2 du volume de fonte cumulé.
    """
    BF = baseflow(Q, d=d, w=w, a=a, passes=passes, method=method)
    vol = np.cumsum(BF)
    if np.all(np.isnan(vol)):
        return np.nan
    pvol = vol / np.nanmax(vol)
    d1 = np.abs(pvol - fraction1)
    d2 = np.abs(pvol - fraction2)
    if np.all(np.isnan(d1)) or np.all(np.isnan(d2)):
        return np.nan
    return float(np.nanargmin(d2) - np.nanargmin(d1) + 1)
