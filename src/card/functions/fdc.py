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
    """Débit dépassé une fraction p du temps, lu sur la courbe des débits
    classés.

    EN: Discharge exceeded a fraction p of the time, read off the flow
    duration curve.

    Vaut quantile(Q, 1-p), interpolation linéaire (type 7 R = défaut
    numpy). Les lacunes sont écartées avant le calcul.
    """
    q = _to_float_array(Q)
    q = q[~np.isnan(q)]
    p = np.asarray(p, dtype=float)
    res = np.quantile(q, 1 - p)
    return res if res.ndim else float(res)


def exceedance_frequency(Q, threshold):
    """Fréquence de dépassement du seuil : part du temps OBSERVÉ où Q est
    strictement supérieur à threshold.

    EN: Exceedance frequency of the threshold: share of the OBSERVED time
    when Q is strictly above threshold.

    Vaut n(Q > threshold) / N, où N ne compte que les pas de temps
    renseignés, comme le numérateur. Un jour manquant est un jour dont on
    ne sait rien, pas un jour de non-dépassement : le compter au
    dénominateur abaissait la fréquence exactement de la part de lacunes
    de la chronique, et cette part diminuant avec les années, le biais se
    lisait comme une tendance à la hausse. Rupture de parité R assumée le
    2026-07-30, cf. docs/dev/ORIGINE_R.md. Série entièrement manquante :
    NaN, et non plus 0.
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
    """Pente du segment médian de la courbe des débits classés.

    EN: Slope of the middle segment of the flow duration curve.
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
    """Axe des probabilités de la courbe des débits classés, en n points.

    EN: Probability axis of the flow duration curve, over n points.

    Points uniformément répartis, ou espacés selon une loi normale
    centrée réduite si norm_spacing.

    `X` est accepté et ignoré : cette fonction ne dépend d'aucune donnée,
    elle produit l'axe des abscisses de la courbe. Mais le moteur affecte
    d'office la première colonne numérique à une fonction qui ne déclare
    aucune colonne, et cette valeur doit bien atterrir quelque part. Sans
    ce paramètre, elle se liait à `n` et faisait échouer l'appel : les
    cinq fiches FDC plantaient depuis l'origine du portage, trois d'entre
    elles le masquant par une période sans données (corrigé 2026-07-22).
    """
    return _fdc_p(n, norm_spacing)


def fdc_quantiles(Q, n=1000, norm_spacing=False):
    """Quantiles de la courbe des débits classés (mêmes probabilités que
    fdc_probabilities)."""
    return exceedance_quantile(Q, _fdc_p(n, norm_spacing))
