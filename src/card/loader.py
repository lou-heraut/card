# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
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

"""Lecture des fiches CARD YAML : remplace sourceProcess() du package R.

Une fiche chargée est un dict :
    {
      "id": str,
      "meta": {"en": {...}, "fr": {...}, "global": {...}},   # défauts appliqués
      "processes": [                                          # P1..Pn ordonnés
          {
            "name": "P1",
            "func": [FunctEntry, ...],
            "time_step": str, "sampling_period": ..., "period": ...,
            "max_na_pct": ..., "max_na_years": ..., "seasons": [...],
            "keep": ..., "compress": bool, "expand": bool,
          },
      ],
    }

FunctEntry (dict) : {name, fn_name, fn, cols, kwargs, is_date}
Les symboles $H0..$Hn sont substitués par les dates de meta.global.horizons.
Le sampling_period adaptatif {type: adaptive, func: [...]} est parsé de la
même façon qu'un tuple func.
"""

import hashlib
from pathlib import Path

import yaml

_GLOBAL_DEFAULTS = {
    "is_experimental": False,
    "input_vars": "X",
    "source": None,
    "preferred_sampling_period": None,
    "is_date": False,
    "relative": True,
    "palette": None,
}

_PROCESS_DEFAULTS = {
    "time_step": "year",
    "sampling_period": None,
    "period": None,
    "max_na_pct": None,
    "max_na_years": None,
    "seasons": ["DJF", "MAM", "JJA", "SON"],
    "keep": None,
    "compress": False,
    "expand": False,
}

def _parse_funct_tuple(name, raw):
    """Parse [fn_name, *cols, kwargs?, is_date?] en FunctEntry."""
    if not isinstance(raw, list) or not raw or not isinstance(raw[0], str):
        raise ValueError(f"Tuple func invalide pour '{name}' : {raw!r}")
    fn_name = raw[0]
    rest = list(raw[1:])

    is_date = False
    if rest and isinstance(rest[-1], bool):
        is_date = rest.pop()

    kwargs = {}
    if rest and isinstance(rest[-1], dict):
        kwargs = rest.pop()

    # arguments positionnels : str = nom de colonne, numérique = littéral
    # (ex. [divided, "dQXA", 2, {first: true}], cf. delta-dtFlood_H)
    pos_args = []
    for item in rest:
        if isinstance(item, str):
            pos_args.append(("col", item))
        elif isinstance(item, (int, float)):
            pos_args.append(("lit", item))
        else:
            raise ValueError(
                f"Élément inattendu dans le tuple func de '{name}' : {item!r}"
            )

    # la résolution fn_name -> callable est paresseuse (extraction.resolve
    # à l'exécution) : le chargement des métadonnées n'exige pas que la
    # fonction soit disponible
    return {
        "name": name,
        "fn_name": fn_name,
        "pos_args": pos_args,
        "cols": [v for t, v in pos_args if t == "col"],
        "kwargs": kwargs,
        "is_date": is_date,
    }


def _parse_sampling_period(raw):
    if raw is None:
        return None
    if isinstance(raw, dict):
        if raw.get("type") != "adaptive":
            raise ValueError(f"sampling_period dict invalide : {raw!r}")
        entry = _parse_funct_tuple("_sampling", raw["func"])
        return {"type": "adaptive", "func": entry}
    return raw  # "MM-DD" ou ["MM-DD", "MM-DD"]


def load_card(path):
    """Charge une fiche CARD YAML et la normalise : méta fr/en/global
    complétées par les défauts, processus P1..Pn ordonnés avec leurs
    tuples func prêts pour stase.
    Retourne un dict {id, path, meta, processes}.
    """
    octets = Path(path).read_bytes()
    raw = yaml.safe_load(octets.decode("utf-8"))
    # SWHID de contenu du FICHIER de fiche. Software Heritage identifie un
    # contenu par son hash git de blob : on le calcule donc localement,
    # sans réseau ni dépôt git. Il désigne la DÉFINITION exacte employée,
    # indépendamment du dépôt et de la révision d'où elle vient, et reste
    # le même tant que le fichier ne change pas.
    swhid = "swh:1:cnt:" + hashlib.sha1(
        b"blob %d\0" % len(octets) + octets).hexdigest()

    meta = raw.get("meta", {})
    meta_global = {**_GLOBAL_DEFAULTS, **meta.get("global", {})}

    processes = []
    process_raw = raw.get("process", {})
    names = sorted(process_raw, key=lambda p: int(p.lstrip("P")))
    for i, pname in enumerate(names, start=1):
        if pname != f"P{i}":
            raise ValueError(
                f"{path} : processus non consécutifs ({names}), attendu P1..Pn."
            )
        p_raw = process_raw[pname]
        proc = {**_PROCESS_DEFAULTS,
                **{k: v for k, v in p_raw.items() if k != "func"}}
        proc["name"] = pname
        proc["func"] = [
            _parse_funct_tuple(var, t)
            for var, t in p_raw["func"].items()
        ]
        proc["sampling_period"] = _parse_sampling_period(
            proc["sampling_period"]
        )
        processes.append(proc)

    if not processes:
        raise ValueError(f"{path} : aucun processus défini.")

    return {
        "id": raw.get("id"),
        # La version de la fiche voyage avec elle : c'est ce qui permet à un
        # résultat de dire avec quelle définition il a été calculé.
        "version": raw.get("version"),
        "swhid": swhid,
        "meta": {
            "en": meta.get("en", {}),
            "fr": meta.get("fr", {}),
            "global": meta_global,
        },
        "processes": processes,
        "path": str(path),
    }
