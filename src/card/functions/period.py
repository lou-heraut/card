# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package (Python port of the
# CARD R package).
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Restriction d'un calcul à une sous-période.

Une fiche ne doit pas figer de dates : la période se fournit en colonnes
d'entrée, constantes par série, ce qui permet un horizon différent d'une
station à l'autre (par exemple défini par un degré de réchauffement).

La restriction se fait DANS la fonction d'agrégation, jamais en masquant
la série en amont. Mesuré le 2026-07-22 : des valeurs mises à NaN hors
fenêtre sont comptées comme des lacunes, et une agrégation mensuelle avec
`max_na_pct=3` sur une série masquée à 20 ans sur 51 ne rend plus aucun
mois. Restreindre à l'intérieur de la fonction laisse le comptage des
lacunes porter sur ce qui est réellement calculé.

`_const_date` et `_subset_period` vivent ici pour les trois fonctions qui
en ont besoin (`return_level`, `apply_threshold`, `over_period`).
"""

import re

import numpy as np
import pandas as pd


_IDENTIFIANT = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _const_date(v):
    """Date depuis un scalaire ou une colonne constante par série (Series
    ou ndarray, cas des bornes de période fournies en colonnes).

    Une entrée FACULTATIVE absente des données arrive telle quelle, sous
    la forme du nom de colonne non résolu : le moteur passe en littéral
    une référence qu'il n'a pas trouvée. Un identifiant est donc traité
    comme une borne absente. Une chaîne qui ressemble à une date sans en
    être une reste une erreur : sans cette distinction, `2020-13-45`
    passerait pour « pas de borne » et fausserait le résultat en silence.
    """
    if isinstance(v, (pd.Series, np.ndarray)):
        s = pd.Series(v).dropna()
        v = s.iloc[0] if len(s) else np.nan
    if isinstance(v, str) and _IDENTIFIANT.match(v):
        return pd.NaT
    return pd.Timestamp(v)


def _period_bounds(period=None, period_start=None, period_end=None):
    """Paire de bornes depuis l'une ou l'autre des deux écritures."""
    if period_start is not None or period_end is not None:
        return [_const_date(period_start), _const_date(period_end)]
    return period


def _subset_period(x, dates, period):
    """Sous-ensemble de x dont les dates tombent dans period.

    Une borne absente (None ou NaT) laisse ce côté ouvert : donner
    seulement une date de début restreint à « depuis », et ne donner
    aucune borne calcule sur toute la chronique. Sans quoi une colonne
    d'horizon laissée vide viderait le calcul en silence.
    """
    if dates is None or period is None:
        return x
    p0, p1 = pd.Timestamp(period[0]), pd.Timestamp(period[1])
    if pd.isna(p0) and pd.isna(p1):
        return x
    d = pd.to_datetime(pd.Series(dates) if not isinstance(dates, pd.Series)
                       else dates)
    garde = pd.Series(True, index=d.index)
    if not pd.isna(p0):
        garde &= p0 <= d
    if not pd.isna(p1):
        garde &= d <= p1
    return x[garde.to_numpy()]


def over_period(X, func=None, dates=None, period=None,
                period_start=None, period_end=None, **kwargs):
    """Applique `func` aux seules valeurs de X situées dans la période.

    Enveloppe générique, pour les agrégations qui ne peuvent pas recevoir
    elles-mêmes des bornes : `nanmean` et `nanmedian` sont des fonctions
    numpy, on ne leur ajoute pas de paramètres.

    func   : nom de la fonction à appliquer (résolu comme dans une fiche,
             card.functions puis numpy), ou callable.
    dates  : colonne de dates, alignée sur X.
    period_start / period_end : bornes, généralement des colonnes
             constantes par série ; `period` accepte aussi la paire.
    kwargs : transmis tels quels à `func`. Les noms de cette enveloppe
             (func, dates, period, period_start, period_end) lui sont
             réservés et ne peuvent donc pas être transmis.

    Une borne absente laisse son côté ouvert, et deux bornes absentes
    reviennent à calculer sur toute la chronique : une fiche dont
    l'appelant ne renseigne pas l'horizon rend un résultat plutôt qu'une
    colonne de NaN.
    """
    if func is None:
        raise ValueError("over_period : le nom de la fonction à appliquer "
                         "est requis, ex. {func: nanmean}.")
    if callable(func):
        fn = func
    else:
        from ..extraction import resolve      # tardif : évite un cycle
        fn = resolve(str(func))

    bounds = _period_bounds(period, period_start, period_end)
    x = np.asarray(X, dtype=np.float64)
    return fn(_subset_period(x, dates, bounds), **kwargs)
