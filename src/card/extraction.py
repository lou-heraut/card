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
import re
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import yaml
from stase import Adaptive, process_extraction

from . import functions
from . import suffix as _sfx
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


_MMDD_RE = re.compile(r"^\d{2}-\d{2}$")


def _override_sampling(sp, override, preferred, card_id):
    """Applique le paramètre sampling_period= d'extract à un process.

    Seules les fenêtres ANNUELLES sont écrasées (adaptatives ou fixes
    'MM-DD') : une fenêtre partielle [début, fin] restreint les données
    à une sous-période et fait partie de la définition de la variable,
    elle n'est jamais touchée. Un process sans sampling_period reste
    sans fenêtre.
    """
    if override is None or sp is None or isinstance(sp, list):
        return sp
    if override == "preferred":
        if preferred:
            return preferred
        if isinstance(sp, dict):        # adaptatif sans repli déclaré
            raise ValueError(
                f"sampling_period='preferred' : la fiche {card_id} a une "
                "fenêtre adaptative mais ne déclare pas de "
                "meta.global.preferred_sampling_period."
            )
        return sp                       # fenêtre fixe = déjà 'preferred'
    return override


def _run_process(data, proc, period_default=None, cancel_lim=False,
                 sampling_override=None, preferred=None, card_id="",
                 suffix_keys=None, suffix_delimiter="_", param_cols=None,
                 verbose=False):
    period = proc["period"] if proc["period"] is not None else period_default
    sp = _override_sampling(proc["sampling_period"], sampling_override,
                            preferred, card_id)
    return process_extraction(
        data,
        func={e["name"]: _funct_tuple(e) for e in proc["func"]},
        time_step=proc["time_step"],
        sampling_period=_sampling_period(sp),
        period=period,
        max_na_pct=None if cancel_lim else proc["max_na_pct"],
        max_na_years=None if cancel_lim else proc["max_na_years"],
        seasons=proc["seasons"],
        keep=proc["keep"],
        compress=proc["compress"],
        expand=proc["expand"],
        suffix=suffix_keys or None,
        suffix_delimiter=suffix_delimiter,
        param_cols=param_cols or None,
        verbose=verbose,
    )


# ---------------------------------------------------------------------------
# meta
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


def _corpus_path(path):
    """Chemin de la fiche relatif à la racine du corpus (`flow/series/
    QA.yaml`), ou son nom si elle vit ailleurs (fiche personnelle)."""
    p = Path(path)
    try:
        return p.relative_to(_DEFAULT_CARD_DIR).as_posix()
    except ValueError:
        return p.name


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

    def cfield(d, key):
        """Facette de classification -> valeur par variable (str, plot-ready).
        Une liste de longueur n est par-variable ; toute autre liste
        (ex. domain multiple) est jointe en une chaîne."""
        v = d.get("classification", {}).get(key)
        if isinstance(v, list) and (n == 1 or len(v) != n):
            v = ", ".join(str(x) for x in v)
        return _as_list(v if v is not None else "", n)

    _OPERATORS = [("delta-", "delta"), ("median-", "median"), ("mean-", "mean"),
                  ("alpha-", "trend slope"), ("hyp-", "trend test"), ("n-", "count")]

    def operator(var):
        for prefix, op in _OPERATORS:
            if str(var).startswith(prefix):
                return op
        return ""

    return pd.DataFrame({
        "variable_en": _as_list(variable_en, n),
        "unit_en": field(en, "unit"),
        "name_en": field(en, "name"),
        "description_en": field(en, "description"),
        "method_en": field(en, "method"),
        "sampling_period_en": _as_list(_join_sp(en.get("sampling_period")), n),
        "domain_en": cfield(en, "domain"),
        "phenomenon_en": cfield(en, "phenomenon"),
        "aspect_en": cfield(en, "aspect"),
        "season_en": cfield(en, "season"),
        "output_en": cfield(en, "output"),
        "purpose_en": cfield(en, "purpose"),
        "variable_fr": _as_list(fr.get("variable"), n),
        "unit_fr": field(fr, "unit"),
        "name_fr": field(fr, "name"),
        "description_fr": field(fr, "description"),
        "method_fr": field(fr, "method"),
        "sampling_period_fr": _as_list(_join_sp(fr.get("sampling_period")), n),
        "domain_fr": cfield(fr, "domain"),
        "phenomenon_fr": cfield(fr, "phenomenon"),
        "aspect_fr": cfield(fr, "aspect"),
        "season_fr": cfield(fr, "season"),
        "output_fr": cfield(fr, "output"),
        "purpose_fr": cfield(fr, "purpose"),
        "operator": [operator(v) for v in _as_list(variable_en, n)],
        "functions": [", ".join(dict.fromkeys(
            e["fn_name"] for p in card["processes"] for e in p["func"]))] * n,
        "is_experimental": _as_list(gl.get("is_experimental"), n),
        "input_vars": _as_list(gl.get("input_vars"), n),
        "source": _as_list(gl.get("source"), n),
        "preferred_sampling_period": _as_list(gl.get("preferred_sampling_period"), n),
        "is_date": _as_list(gl.get("is_date"), n),
        "relative": _as_list(gl.get("relative"), n),
        "palette": _as_list(palette, n),
        "version": [card.get("version")] * n,
        # Identifiant pérenne du fichier de fiche, et son chemin DANS le
        # corpus (pas sur la machine : un chemin absolu de serveur
        # n'apprend rien à personne et expose son arborescence).
        "swhid": [card.get("swhid")] * n,
        "script_path": [_corpus_path(card["path"])] * n,
    })


def _meta_frame(card, out_cols=None, keys=(), records=None, delim="_"):
    """Lignes de méta, une par variable RÉELLEMENT sortie.

    Un suffixe change le nom d'une variable, donc c'est une autre
    variable, donc une autre ligne. On lit les colonnes sorties plutôt
    que de raisonner sur la fiche : la règle de stase est conditionnelle
    (une fonction dont aucune référence n'a de variante suffixée sort une
    seule fois, sans suffixe), donc dans un même appel une fiche peut
    donner deux lignes et sa voisine une seule. Lire la sortie est exact
    par construction et ne peut pas diverger de stase.

    out_cols None (metadata_only) : forme par défaut de la fiche, celle
    que produit aussi une extraction sans suffixe.
    """
    records = records or {}
    en, fr, gl = card["meta"]["en"], card["meta"]["fr"], card["meta"]["global"]
    card_id = card.get("id") or card.get("path")

    def frame_for(key):
        meta = {"global": gl}
        for lang, meta_lang in (("en", en), ("fr", fr)):
            rec = (_sfx.default_record(meta_lang) if key is None
                   else _sfx.record(key, lang, meta_lang, records))
            meta[lang] = {**meta_lang,
                          **_sfx.apply(meta_lang, rec, card_id=card_id,
                                       lang=lang, key=key)}
        df = _meta_rows({**card, "meta": meta})
        if key is not None:
            for col in ("variable_en", "variable_fr"):
                df[col] = [f"{v}{delim}{key}" if isinstance(v, str) else v
                           for v in df[col]]
        df["suffix"] = key or ""
        return df

    if out_cols is None:
        return frame_for(None)

    base_vars = list(_meta_rows(card)["variable_en"])
    parts, kept = [], set()

    idx = [i for i, v in enumerate(base_vars) if v in out_cols]
    if idx:
        parts.append(frame_for(None).iloc[idx])
        kept.update(idx)
    for key in keys:
        idx = [i for i, v in enumerate(base_vars)
               if f"{v}{delim}{key}" in out_cols]
        if idx:
            parts.append(frame_for(key).iloc[idx])
            kept.update(idx)

    # Variable déclarée mais absente de la sortie : la méta décrit la
    # fiche, on la garde sous sa forme par défaut.
    idx = [i for i in range(len(base_vars)) if i not in kept]
    if idx:
        parts.append(frame_for(None).iloc[idx])

    if not parts:
        return frame_for(None)
    return pd.concat(parts).sort_index(kind="stable").reset_index(drop=True)


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


_INPUTS_PATH = Path(__file__).resolve().parent / "inputs.yaml"
_INPUTS_CACHE = None


def _input_registry():
    """Registre des variables d'entrée (inputs.yaml). Chargé une fois.

    Copie locale volontaire : schema.py importe extraction, donc importer
    schema ici créerait un cycle. La source de vérité reste inputs.yaml."""
    global _INPUTS_CACHE
    if _INPUTS_CACHE is None:
        _INPUTS_CACHE = yaml.safe_load(_INPUTS_PATH.read_text(encoding="utf-8"))
    return _INPUTS_CACHE


def _date_param_cols(card, data_cols, suffix_keys, delim) -> list[str]:
    """Colonnes de paramètre présentes dans les données : les input_vars de
    type date (inputs.yaml), sous leur nom bare ou suffixé. Ce sont les
    colonnes que stase met de côté (param_cols) : ni axe, ni mesure,
    conservées à travers les process."""
    reg = _input_registry()
    date_vars = [v for v in _required_vars(card)
                 if reg.get(v, {}).get("type") == "date"]
    data_cols = set(data_cols)
    cols: list[str] = []
    for v in date_vars:
        for cand in [v] + [f"{v}{delim}{s}" for s in (suffix_keys or [])]:
            if cand in data_cols and cand not in cols:
                cols.append(cand)
    return cols


def _check_input_vars(data: pd.DataFrame, loaded: dict,
                      suffix_keys=(), delim="_") -> dict:
    """Vérifie que les colonnes requises par les fiches sont présentes.

    Une exigence 'Q_lim' est satisfaite par la colonne 'Q_lim' ou par
    n'importe quelle variante suffixée 'Q_lim_DOE'.

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

    def _present(var):
        return var in data.columns or any(
            f"{var}{delim}{s}" in data.columns for s in suffix_keys)

    for name, card in loaded.items():
        required = _required_vars(card)
        missing = [v for v in required if not _present(v)]
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
            sampling_period=None,
            simplify=False, metadata_only=False,
            rename=None, suffix=None, suffix_delimiter="_",
            verbose=False, CARD_name=None):
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
    sampling_period : écrase la fenêtre annuelle des fiches.
           "preferred" : chaque fiche prend SON
           meta.global.preferred_sampling_period (protocole MAKAHO,
           reproductible : la fenêtre adaptative dépend des données).
           "MM-DD" (ex. "09-01") : fenêtre imposée. Ne touche ni les
           fenêtres partielles [début, fin] (définition de la
           variable), ni les process sans fenêtre.
    simplify : fusionne les DataFrames de sortie en un seul.
    metadata_only : ne calcule rien, retourne seulement les métadonnées.
    rename : dict {nom_colonne_data: nom_variable_fiche} pour faire
           correspondre vos colonnes aux noms attendus, ex.
           rename={"Qm3s": "Q"}. Si les données n'ont qu'une seule
           colonne numérique et la fiche une seule variable requise, la
           correspondance est automatique (signalée par un warning).
    suffix : applique les fiches à plusieurs variantes d'une entrée en
           un appel (plusieurs seuils, obs/sim...). Liste de clés,
           suffix=["DOE", "DCR"] : les colonnes 'Q_lim_DOE' et
           'Q_lim_DCR' donnent les sorties 'rp-VCN10_DOE' et
           'rp-VCN10_DCR', et les colonnes partagées (la chronique 'Q')
           ne sont lues qu'une fois. Une fonction dont aucune référence
           n'a de variante suffixée n'est calculée qu'une fois et sort
           sans suffixe. Ou un dict pour nommer les variantes dans les
           métadonnées, suffix={"DOE": {"fr": {"name": "débit objectif
           d'étiage"}}} : chaque sortie a alors sa propre ligne de méta,
           avec son nom, et la colonne 'suffix' rappelle la clé.
    suffix_delimiter : délimiteur variable/suffixe (défaut "_").
    CARD_name : alias hérité du R pour `cards` (prioritaire si fourni).

    Retourne {"data": {id_fiche: DataFrame}, "meta": DataFrame}, où la
    sortie est de la donnée comme une autre : elle peut repartir en
    entrée d'une nouvelle extraction ou de stase.trend.
    """
    if CARD_name is not None:
        cards = CARD_name
    CARD_path = path
    period_default = default_period
    cancel_lim = ignore_na_limits
    extract_only_metadata = metadata_only

    if sampling_period is not None and not (
            sampling_period == "preferred"
            or (isinstance(sampling_period, str)
                and _MMDD_RE.match(sampling_period))):
        raise ValueError(
            f"sampling_period invalide : {sampling_period!r}. Valeurs "
            "acceptées : 'preferred' (fenêtre fixe déclarée par chaque "
            "fiche) ou 'MM-DD' (ex. '09-01')."
        )
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

    suffix_keys, suffix_records = _sfx.normalize(suffix)

    auto_map = ({} if extract_only_metadata
                else _check_input_vars(data, loaded, suffix_keys,
                                       suffix_delimiter))

    meta_parts, out_data = [], {}
    for name, card in loaded.items():
        if extract_only_metadata:
            meta_parts.append(_meta_frame(card))
            continue
        if verbose:
            print(f"Computes {name}")
        result = (data.rename(columns=auto_map[name])
                  if name in auto_map else data)
        preferred = card["meta"]["global"].get("preferred_sampling_period")
        # colonnes de paramètre (dates d'horizon...) : mises de côté par stase,
        # conservées à travers les process, puis retirées de la sortie finale.
        param_cols = _date_param_cols(card, result.columns, suffix_keys,
                                      suffix_delimiter)
        for proc in card["processes"]:
            result = _run_process(result, proc,
                                  period_default=period_default,
                                  cancel_lim=cancel_lim,
                                  sampling_override=sampling_period,
                                  preferred=preferred,
                                  card_id=name,
                                  suffix_keys=suffix_keys,
                                  suffix_delimiter=suffix_delimiter,
                                  param_cols=param_cols,
                                  verbose=verbose)
        if param_cols:
            result = result.drop(columns=[c for c in param_cols
                                          if c in result.columns])
        out_data[name] = result
        # Après le run : seule la sortie dit quelles variables sont
        # suffixées (cf. _meta_frame).
        meta_parts.append(_meta_frame(card, set(result.columns), suffix_keys,
                                      suffix_records, suffix_delimiter))

    out_meta = pd.concat(meta_parts, ignore_index=True) if meta_parts \
        else pd.DataFrame()

    if extract_only_metadata:
        return {"meta": out_meta}

    if simplify and out_data:
        dfs = list(out_data.values())
        merged = dfs[0]
        for df in dfs[1:]:
            by = [c for c in merged.columns
                  if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])]
            merged = merged.merge(df, on=by, how="outer")
        return {"data": merged, "meta": out_meta}

    return {"data": out_data, "meta": out_meta}


# Alias hérité du package R CARD
CARD_extraction = extract
