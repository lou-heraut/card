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

"""card.extract : exécution des fiches CARD YAML via le moteur stase.

card ne gère que les fiches et leurs métadonnées : chaque processus P1..Pn
est traduit en un appel à stase.extract, qui porte toute la mécanique de
données (sampling adaptatif, sorties vectorielles, kwargs référençant des
colonnes, colonnes creuses, NA...).
"""

import os
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
from stase import Adaptive, process_extraction

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
    """FunctEntry (loader) → tuple (fn, *args, kwargs?, is_date?) stase.

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
        entry = sp["func"]
        return Adaptive(func=resolve(entry["fn_name"]),
                        col=entry["cols"][0])
    return sp                       # None, "MM-DD" ou ["MM-DD", "MM-DD"]


def _run_process(data, proc, period_default=None, cancel_lim=False,
                 verbose=False):
    period = proc["period"] if proc["period"] is not None else period_default
    return process_extraction(
        data,
        func={e["name"]: _funct_tuple(e) for e in proc["func"]},
        time_step=proc["time_step"],
        sampling_period=_sampling_period(proc["sampling_period"]),
        period=period,
        max_na_pct=None if cancel_lim else proc["max_na_pct"],
        max_na_years=None if cancel_lim else proc["max_na_years"],
        seasons=proc["seasons"],
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
        "relative": _as_list(gl.get("relative"), n),
        "palette": _as_list(palette, n),
        "script_path": [card["path"]] * n,
    })


# ---------------------------------------------------------------------------
# Vérification amont des variables d'entrée
# ---------------------------------------------------------------------------

def _required_vars(card) -> list[str]:
    """Variables d'entrée requises par une fiche (meta global input_vars)."""
    raw = card["meta"]["global"].get("input_vars")
    if not raw:
        return []
    if isinstance(raw, str):
        return [v.strip() for v in raw.split(",") if v.strip()]
    return [str(v).strip() for v in raw]


def _check_input_vars(data: pd.DataFrame, loaded: dict) -> dict:
    """Vérifie que les colonnes requises par les fiches sont présentes.

    Retourne {card_name: {col_data: var_fiche}} pour les affectations
    automatiques non ambiguës : une fiche ne requiert qu'UNE variable
    absente ET les données n'ont qu'UNE colonne numérique → cette
    colonne est utilisée (signalé par un UserWarning). Tout autre
    manque lève une ValueError listant fiche par fiche les colonnes
    requises vs disponibles, avec le paramètre rename= en solution.
    """
    numeric_cols = [c for c in data.columns
                    if pd.api.types.is_numeric_dtype(data[c])]
    auto: dict = {}
    problems: list[str] = []
    auto_msgs: set = set()

    for name, card in loaded.items():
        required = _required_vars(card)
        missing = [v for v in required if v not in data.columns]
        if not missing:
            continue
        if len(required) == 1 and len(numeric_cols) == 1:
            col = numeric_cols[0]
            auto[name] = {col: required[0]}
            auto_msgs.add(
                f"colonne '{col}' utilisée comme '{required[0]}'"
            )
        else:
            problems.append(
                f"  - {name} : requiert {required}, manquant {missing}"
            )

    if problems:
        raise ValueError(
            "Colonnes d'entrée manquantes pour certaines fiches CARD "
            "(les fiches référencent les colonnes par leur nom) :\n"
            + "\n".join(problems)
            + f"\nColonnes numériques disponibles : {numeric_cols}.\n"
            "Renommez vos colonnes ou passez rename= à CARD_extraction, "
            "ex. CARD_extraction(data, rename={'Qm3s': 'Q'})."
        )

    if auto_msgs:
        warnings.warn(
            "Affectation automatique (une seule colonne numérique, une "
            "seule variable requise) : " + " ; ".join(sorted(auto_msgs))
            + ". Passez rename= pour rendre la correspondance explicite.",
            UserWarning, stacklevel=3,
        )
    return auto


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


def extract(data, cards=("QA", "QJXA"), path=None,
            default_period=None, ignore_na_limits=False,
            simplify=False, metadata_only=False,
            rename=None, verbose=False, CARD_name=None):
    """Extrait des variables hydroclimatiques selon des fiches CARD YAML.

    data : DataFrame avec une colonne datetime, une colonne texte
           (identifiant de série) et les colonnes numériques d'entrée
           requises par les fiches (référencées par leur nom, ex. 'Q' :
           cf. input_vars des fiches, via card.list_cards() ou
           card.info()).
    cards : noms des fiches à exécuter (cf. card.list_cards()).
    path : dossier des fiches YAML (défaut : fiches embarquées, ou la
           variable d'environnement CARD_YML_PATH).
    default_period : [début, fin] appliqué aux fiches sans période propre.
    ignore_na_limits : désactive les seuils de lacunes des fiches
           (max_na_pct, max_na_years).
    simplify : fusionne les DataFrames de sortie en un seul.
    metadata_only : ne calcule rien, retourne seulement les métadonnées.
    rename : dict {nom_colonne_data: nom_variable_fiche} pour faire
           correspondre vos colonnes aux noms attendus, ex.
           rename={"Qm3s": "Q"}. Si les données n'ont qu'une seule
           colonne numérique et la fiche une seule variable requise, la
           correspondance est automatique (signalée par un warning).
    CARD_name : alias hérité du R pour `cards` (prioritaire si fourni).

    Retourne {"data": {id_fiche: DataFrame}, "meta": DataFrame}. Les
    clés héritées "dataEX" et "metaEX" pointent vers les mêmes objets.
    """
    if CARD_name is not None:
        cards = CARD_name
    CARD_path = path
    period_default = default_period
    cancel_lim = ignore_na_limits
    extract_only_metadata = metadata_only
    if CARD_path is None:
        CARD_path = os.environ.get("CARD_YML_PATH", _DEFAULT_CARD_DIR)

    if rename:
        absent = [c for c in rename if c not in data.columns]
        if absent:
            raise ValueError(
                f"rename : colonnes introuvables dans data : {absent}. "
                f"Colonnes disponibles : {list(data.columns)}."
            )
        data = data.rename(columns=rename)

    found = _find_cards(CARD_path, list(cards) if cards else None)
    loaded = {name: load_card(path) for name, path in found.items()}

    auto_map = ({} if extract_only_metadata
                else _check_input_vars(data, loaded))

    metaEX_parts, dataEX = [], {}
    for name, card in loaded.items():
        metaEX_parts.append(_meta_rows(card))
        if extract_only_metadata:
            continue
        if verbose:
            print(f"Computes {name}")
        result = (data.rename(columns=auto_map[name])
                  if name in auto_map else data)
        for proc in card["processes"]:
            result = _run_process(result, proc,
                                  period_default=period_default,
                                  cancel_lim=cancel_lim,
                                  verbose=verbose)
        dataEX[name] = result

    metaEX = pd.concat(metaEX_parts, ignore_index=True) if metaEX_parts \
        else pd.DataFrame()

    if extract_only_metadata:
        return {"meta": metaEX, "metaEX": metaEX}

    if simplify and dataEX:
        dfs = list(dataEX.values())
        merged = dfs[0]
        for df in dfs[1:]:
            by = [c for c in merged.columns
                  if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])]
            merged = merged.merge(df, on=by, how="outer")
        return {"data": merged, "meta": metaEX,
                "dataEX": merged, "metaEX": metaEX}

    return {"data": dataEX, "meta": metaEX,
            "dataEX": dataEX, "metaEX": metaEX}


# Alias hérité du package R CARD
CARD_extraction = extract
