# Copyright 2020      Ivan Horner <ivan.horner@irstea.fr>*3
#           2021      Léonard Santos <leonard.santos@inrae.fr>*1
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

"""Port Python de R/performance.R et R/rat.R (critères de performance
obs/sim : biais, NSE, KGE, STD, RAT)."""

import numpy as np
from scipy import stats

from .aggregation import _to_float_array


def _clean_pair(obs, sim, skipna=True):
    obs = _to_float_array(obs)
    sim = _to_float_array(sim)
    if len(obs) != len(sim):
        raise ValueError("obs et sim doivent avoir la même longueur")
    if skipna:
        ok = ~(np.isnan(obs) | np.isnan(sim))
        obs, sim = obs[ok], sim[ok]
    return obs, sim


def bias(obs, sim, sim_minus_obs=True):
    """Biais relatif Σ(sim-obs)/Σobs (ou obs-sim si
    sim_minus_obs=False). Paires contenant un NaN écartées.
    """
    obs, sim = _clean_pair(obs, sim)
    if sim_minus_obs:
        return np.sum(sim - obs) / np.sum(obs)
    return np.sum(obs - sim) / np.sum(obs)


def NSE(obs, sim):
    """Efficience de Nash-Sutcliffe (1 = parfait, < 0 = pire que la
    moyenne des observations). Paires contenant un NaN écartées.
    """
    obs, sim = _clean_pair(obs, sim)
    return 1 - np.sum((sim - obs) ** 2) / np.sum((obs - np.mean(obs)) ** 2)


def _hsa_log(x, method="inf.na"):
    x = _to_float_array(x).copy()
    if method == "Pushpalatha2012":
        x = x + np.nanmean(x) / 100
    elif isinstance(method, (int, float)):
        x = x + method
    with np.errstate(divide="ignore", invalid="ignore"):
        y = np.log(x)
    if method == "inf.na":
        y[~np.isfinite(y)] = np.nan
    return y


def NSE_log(obs, sim, log_method="inf.na"):
    """NSE sur les logarithmes (sensible aux basses valeurs).
    log_method : 'inf.na' (log(0) → NaN), 'Pushpalatha2012'
    (décalage +mean/100) ou une constante à ajouter avant le log.
    """
    obs = _to_float_array(obs)
    sim = _to_float_array(sim)
    if np.nansum(obs != 0) > 0 and np.nansum(sim != 0) > 0:
        return NSE(_hsa_log(obs, method=log_method),
                           _hsa_log(sim, method=log_method))
    return 0.0


def NSE_inverse(obs, sim):
    """NSE sur les inverses 1/X (très sensible aux étiages).
    """
    obs = _to_float_array(obs)
    sim = _to_float_array(sim)
    if np.nansum(obs != 0) > 0 and np.nansum(sim != 0) > 0:
        with np.errstate(divide="ignore"):
            return NSE(1 / obs, 1 / sim)
    return np.nan


def NSE_sqrt(obs, sim):
    """NSE sur les racines carrées (compromis hautes/basses valeurs).
    """
    return NSE(np.sqrt(_to_float_array(obs)),
                       np.sqrt(_to_float_array(sim)))


def _kge_short(R, AG, BETA):
    return 1 - np.sqrt((R - 1) ** 2 + (AG - 1) ** 2 + (BETA - 1) ** 2)


def KGE(obs, sim, method=1):
    """Efficience de Kling-Gupta (1 = parfait) : corrélation, rapport
    de variabilité et biais. method=1 : α = sd(sim)/sd(obs)
    (Gupta 2009) ; method=2 : γ = CV(sim)/CV(obs) (Kling 2012).
    """
    obs, sim = _clean_pair(obs, sim)
    mobs, msim = np.mean(obs), np.mean(sim)
    sobs, ssim = np.std(obs, ddof=1), np.std(sim, ddof=1)
    rso = np.corrcoef(sim, obs)[0, 1]
    beta = msim / mobs
    if method == 2:
        gamma = (ssim / msim) / (sobs / mobs)
        return _kge_short(rso, gamma, beta)
    return _kge_short(rso, ssim / sobs, beta)


def KGE_sqrt(obs, sim):
    """KGE sur les racines carrées des débits.
    """
    return KGE(np.sqrt(_to_float_array(obs)),
                       np.sqrt(_to_float_array(sim)))


def std_ratio(obs, sim):
    """Rapport des écarts-types sd(sim)/sd(obs)."""
    obs = _to_float_array(obs)
    sim = _to_float_array(sim)
    sd_obs = np.std(obs[~np.isnan(obs)], ddof=1)
    sd_sim = np.std(sim[~np.isnan(sim)], ddof=1)
    return sd_sim / sd_obs


def RAT(Bias, X, thresh=0.05):
    """RAT (Nicolle et al. 2020) : corrélation de Spearman significative entre
    un critère de performance et une variable explicative → manque de
    robustesse. p-value asymptotique (equiv. R cor.test exact=FALSE)."""
    b = _to_float_array(Bias)
    x = _to_float_array(X)
    ok = ~(np.isnan(b) | np.isnan(x))
    if ok.sum() <= 2:
        return np.nan
    p = stats.spearmanr(b[ok], x[ok]).pvalue
    return bool(p < thresh)
