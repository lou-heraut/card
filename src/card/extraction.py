# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#           2025      David Dorchies <david.dorchies@inrae.fr>*2
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

"""CARD_extraction — exécution des fiches CARD YAML via le moteur exstat.

card ne gère que les fiches et leurs métadonnées : chaque processus P1..Pn
est traduit en un appel à exstat.process_extraction, qui porte toute la
mécanique de données (sampling adaptatif, sorties vectorielles, kwargs
référencant des colonnes, colonnes creuses, NA...).
"""

import os
from pathlib import Path

import numpy as np
import pandas as pd
from exstat import Adaptive, process_extraction

from . import functions
from .loader import load_card

_DEFAULT_CARD_DIR = Path(__file__).resolve().parent / "cards"


def resolve(name: str):
    """Nom de fonction d'une fiche YAML → callable Python.

    Le nom EST le nom Python réel : d'abord le namespace card.functions
    (fonctions hydro), puis numpy en repli (nanmean, nanargmax...).
    Aucune table de traduction.
    """
    fn = getattr(functions, name, None)
    if fn is None:
        fn = getattr(np, name, None)
    if not callable(fn):
        raise KeyError(
            f"Fonction inconnue dans les fiches CARD : '{name}' "
            "(ni dans card.functions, ni dans numpy)."
        )
    return fn


def _funct_tuple(entry: dict):
    """FunctEntry (loader) → tuple (fn, *args, kwargs?, is_date?) exstat.

    L'ordre positionnel d'origine (colonnes et littéraux mélangés) est
    préservé : le moteur parse les littéraux nativement.
    """
    t = [resolve(entry["fn_name"])]
    t += [v for _, v in entry["pos_args"]]
    if entry["kwargs"]:
        t.append(dict(entry["kwargs"]))
    if entry["is_date"]:
        t.append(True)
    return tuple(t)


def _sampling_period(sp):
    if isinstance(sp, dict):        # {type: adaptive, funct: entry}
        entry = sp["funct"]
        return Adaptive(funct=resolve(entry["fn_name"]),
                        col=entry["cols"][0])
    return sp                       # None, "MM-DD" ou ["MM-DD", "MM-DD"]


def _run_process(data, proc, period_default=None, cancel_lim=False,
                 verbose=False):
    period = proc["period"] if proc["period"] is not None else period_default
    return process_extraction(
        data,
        funct={e["name"]: _funct_tuple(e) for e in proc["funct"]},
        time_step=proc["time_step"],
        sampling_period=_sampling_period(proc["sampling_period"]),
        period=period,
        NApct_lim=None if cancel_lim else proc["NApct_lim"],
        NAyear_lim=None if cancel_lim else proc["NAyear_lim"],
        Seasons=proc["Seasons"],
        keep=proc["keep"],
        compress=proc["compress"],
        expand=proc["expand"],
        verbose=verbose,
    )


# ---------------------------------------------------------------------------
# metaEX
# ---------------------------------------------------------------------------

def _as_list(x, n):
    if isinstance(x, list):
        if len(x) != n:
            return (x + [x[-1]] * (n - len(x)))[:n]
        return x
    return [x] * n


def _join_sp(sp):
    if isinstance(sp, list):
        if sp and isinstance(sp[0], list):
            return [", ".join(s) for s in sp]
        return ", ".join(sp)
    return sp


def _meta_rows(card) -> pd.DataFrame:
    en, fr, gl = card["meta"]["en"], card["meta"]["fr"], card["meta"]["global"]

    variable_en = en.get("variable")
    n = len(variable_en) if isinstance(variable_en, list) else 1

    def field(d, key):
        return _as_list(d.get(key, ""), n)

    palette = gl.get("palette")
    if isinstance(palette, list) and palette and isinstance(palette[0], list):
        palette = [" ".join(p) for p in palette]
    elif isinstance(palette, list):
        palette = " ".join(palette)

    return pd.DataFrame({
        "variable_en": _as_list(variable_en, n),
        "unit_en": field(en, "unit"),
        "name_en": field(en, "name"),
        "description_en": field(en, "description"),
        "method_en": field(en, "method"),
        "sampling_period_en": _as_list(_join_sp(en.get("sampling_period")), n),
        "topic_en": field(en, "topic"),
        "variable_fr": _as_list(fr.get("variable"), n),
        "unit_fr": field(fr, "unit"),
        "name_fr": field(fr, "name"),
        "description_fr": field(fr, "description"),
        "method_fr": field(fr, "method"),
        "sampling_period_fr": _as_list(_join_sp(fr.get("sampling_period")), n),
        "topic_fr": field(fr, "topic"),
        "is_experimental": _as_list(gl.get("is_experimental"), n),
        "input_vars": _as_list(gl.get("input_vars"), n),
        "source": _as_list(gl.get("source"), n),
        "preferred_sampling_period": _as_list(gl.get("preferred_sampling_period"), n),
        "is_date": _as_list(gl.get("is_date"), n),
        "to_normalise": _as_list(gl.get("to_normalise"), n),
        "palette": _as_list(palette, n),
        "script_path": [card["path"]] * n,
    })


# ---------------------------------------------------------------------------
# API principale
# ---------------------------------------------------------------------------

def _find_cards(CARD_path, CARD_name):
    root = Path(CARD_path)
    found = {}
    for p in sorted(root.rglob("*.yaml")):
        stem = p.stem
        # préfixe numérique optionnel '001_' posé par CARD_management
        if "_" in stem and stem.split("_", 1)[0].isdigit():
            stem = stem.split("_", 1)[1]
        found.setdefault(stem, p)
    if CARD_name is None:
        return found
    missing = [n for n in CARD_name if n not in found]
    if missing:
        raise FileNotFoundError(f"CARD introuvables sous {root} : {missing}")
    return {n: found[n] for n in CARD_name}


def CARD_extraction(data, CARD_name=("QA", "QJXA"), CARD_path=None,
                    period_default=None, cancel_lim=False,
                    simplify=False, extract_only_metadata=False,
                    verbose=False):
    """Extrait des variables hydroclimatiques selon des fiches CARD YAML.

    data : DataFrame avec une colonne datetime, une colonne str (id) et
           les colonnes numériques d'entrée requises par les fiches.
    Retourne {"metaEX": DataFrame, "dataEX": {card_id: DataFrame}}.
    """
    if CARD_path is None:
        CARD_path = os.environ.get("CARD_YML_PATH", _DEFAULT_CARD_DIR)

    cards = _find_cards(CARD_path, list(CARD_name) if CARD_name else None)

    metaEX_parts, dataEX = [], {}
    for name, path in cards.items():
        card = load_card(path)
        metaEX_parts.append(_meta_rows(card))
        if extract_only_metadata:
            continue
        if verbose:
            print(f"Computes {name}")
        result = data
        for proc in card["processes"]:
            result = _run_process(result, proc,
                                  period_default=period_default,
                                  cancel_lim=cancel_lim,
                                  verbose=verbose)
        dataEX[name] = result

    metaEX = pd.concat(metaEX_parts, ignore_index=True) if metaEX_parts \
        else pd.DataFrame()

    if extract_only_metadata:
        return {"metaEX": metaEX}

    if simplify and dataEX:
        dfs = list(dataEX.values())
        merged = dfs[0]
        for df in dfs[1:]:
            by = [c for c in merged.columns
                  if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])]
            merged = merged.merge(df, on=by, how="outer")
        return {"metaEX": metaEX, "dataEX": merged}

    return {"metaEX": metaEX, "dataEX": dataEX}
