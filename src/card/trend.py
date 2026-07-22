# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
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

"""card.trend : diagnostic de stationnarité des sorties de card.extract.

Enveloppe fiche-consciente de stase.trend : contrôle de la facette
output (la tendance n'a de sens que sur les fiches `series`) et passage
de la table meta (pentes relatives pilotées par la colonne `relative`
des fiches). Toute la statistique est dans stase.
"""

from pathlib import Path

import pandas as pd
from stase import process_trend


def _outputs_by_card(meta: pd.DataFrame) -> dict:
    """{id de fiche: {facettes output de ses variables}}."""
    out: dict = {}
    for path, output in zip(meta["script_path"], meta["output_en"]):
        out.setdefault(Path(path).stem, set()).add(str(output))
    return out


def _relative_by_variable(meta: pd.DataFrame) -> dict:
    """{variable: relative} d'après les fiches, pour stase.trend.

    Les clés sont les noms de variables tels que l'extraction les a
    produits, suffixe compris : depuis que la méta est par suffixe,
    QA_obs et QA_sim ont chacun leur ligne, donc leur propre valeur.
    """
    return {str(v): bool(r)
            for v, r in zip(meta["variable_en"], meta["relative"])}


def _suffixes_used(meta: pd.DataFrame) -> list:
    """Suffixes réellement présents dans l'extraction (colonne suffix)."""
    if "suffix" not in meta.columns:
        return []
    return sorted({str(s) for s in meta["suffix"] if str(s)})


def trend(extraction, level=0.1, dependency="AR1", period=None,
          extremes_pool_suffixes=False, seed=None, verbose=False):
    """Tendance Mann-Kendall + pente de Sen sur un résultat de card.extract.

    extraction : le retour de card.extract, {"data": ..., "meta": ...},
        data est un dict {id_fiche: DataFrame} (défaut) ou un DataFrame
        unique (simplify=True).
    level : niveau de signification du test (défaut 0.1).
    dependency : 'AR1' (défaut, robuste à l'autocorrélation d'ordre 1,
        fréquente sur les séries hydro annuelles ; Hamed & Rao 1998),
        'INDE' (test standard) ou 'LTP' (mémoire longue, Hamed 2008).
    extremes_pool_suffixes : sur une extraction suffixée (obs/sim,
        plusieurs seuils), met les bornes de quantiles en commun entre
        les variantes d'une même variable de base, ce qui les rend
        comparables entre elles. Défaut False : chaque variante a ses
        propres bornes.
    period, seed, verbose : passés à stase.trend.

    Seules les fiches de facette `output: series` sont acceptées : la
    tendance d'un scalaire ou d'une courbe n'a pas de sens, ValueError
    explicite sinon.

    Le caractère relatif de chaque variable vient des fiches
    (meta.global.relative) et pilote a_relative et change_relative dans
    la sortie. Rien à saisir : card le traduit pour stase, qui reste
    agnostique du format des fiches.

    Retourne {"data": {id_fiche: DataFrame} | DataFrame, "meta": meta}, où
    même forme de data que l'entrée.
    """
    if not (isinstance(extraction, dict)
            and "data" in extraction and "meta" in extraction):
        raise TypeError(
            "trend attend le retour de card.extract : un dict avec les "
            "clés 'data' et 'meta'. Pour un DataFrame seul (sans "
            "métadonnées de fiches), utilisez stase.trend directement."
        )
    data, meta = extraction["data"], extraction["meta"]

    outputs = _outputs_by_card(meta)
    names = data.keys() if isinstance(data, dict) else outputs.keys()
    bad = {n: sorted(outputs.get(n, set()) - {"series"})
           for n in names if outputs.get(n, set()) - {"series"}}
    if bad:
        detail = " ; ".join(f"{n} ({', '.join(v)})" for n, v in sorted(bad.items()))
        raise ValueError(
            f"La tendance ne s'applique qu'aux fiches de facette "
            f"output 'series'. Fiches refusées : {detail}. "
            "Filtrez avec card.list_cards(output='series')."
        )

    suffixes = _suffixes_used(meta)
    kw = dict(level=level, dependency=dependency, period=period,
              seed=seed, verbose=verbose,
              relative=_relative_by_variable(meta),
              suffix=suffixes or None,
              extremes_pool_suffixes=extremes_pool_suffixes)
    if isinstance(data, dict):
        return {"data": {name: process_trend(df, **kw)
                         for name, df in data.items()},
                "meta": meta}
    return {"data": process_trend(data, **kw), "meta": meta}
