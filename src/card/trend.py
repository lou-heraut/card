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


def trend(extraction, level=0.1, dependency="AR1", period=None,
          seed=None, verbose=False):
    """Tendance Mann-Kendall + pente de Sen sur un résultat de card.extract.

    extraction : le retour de card.extract, {"data": ..., "meta": ...} —
        data est un dict {id_fiche: DataFrame} (défaut) ou un DataFrame
        unique (simplify=True).
    level : niveau de signification du test (défaut 0.1).
    dependency : 'AR1' (défaut — robuste à l'autocorrélation d'ordre 1,
        fréquente sur les séries hydro annuelles ; Hamed & Rao 1998),
        'INDE' (test standard) ou 'LTP' (mémoire longue, Hamed 2008).
    period, seed, verbose : passés à stase.trend.

    Seules les fiches de facette `output: series` sont acceptées : la
    tendance d'un scalaire ou d'une courbe n'a pas de sens, ValueError
    explicite sinon. La colonne `relative` de la table meta pilote le
    calcul de a_relative (pente en % de la moyenne).

    Retourne {"data": {id_fiche: DataFrame} | DataFrame, "meta": meta} —
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
            f"output 'series' — fiches refusées : {detail}. "
            "Filtrez avec card.list_cards(output='series')."
        )

    kw = dict(level=level, dependency=dependency, period=period,
              seed=seed, verbose=verbose, meta=meta)
    if isinstance(data, dict):
        return {"data": {name: process_trend(df, **kw)
                         for name, df in data.items()},
                "meta": meta}
    return {"data": process_trend(data, **kw), "meta": meta}
