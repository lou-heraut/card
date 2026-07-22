# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#           2025      David Dorchies <david.dorchies@inrae.fr>*2
#           2023      Éric Sauquet <eric.sauquet@inrae.fr>*1
#                     Jean-Philippe Vidal <jean-philippe.vidal@inrae.fr>*1
#                     Nathan Pellerin
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

"""Gestion des fiches CARD YAML : catalogue, détail, copie locale."""

import shutil
from pathlib import Path

import pandas as pd

from .extraction import _DEFAULT_CARD_DIR, _corpus_path, _find_cards, _meta_rows
from . import suffix as _sfx
from .loader import load_card
from .schema import input_registry


def _describe_inputs(raw, lang="fr"):
    """'Q, R' -> 'Q [m^{3}.s^{-1}] (débit journalier moyen), R [mm] (...)'."""
    if not raw:
        return raw
    reg = input_registry()
    parts = []
    for var in str(raw).split(","):
        var = var.strip()
        opt = var.endswith("?")                 # entrée facultative
        var = var.rstrip("?").strip()
        entry = reg.get(var)
        suite = (", facultatif" if lang == "fr" else ", optional") if opt else ""
        if entry:
            label = entry.get("unit") or entry.get("type") or ""
            parts.append(f"{var} [{label}] ({entry[lang]}{suite})")
        else:
            parts.append(var)
    return ", ".join(parts)


def list_cards(path=None, include_experimental=False,
               domain=None, phenomenon=None, aspect=None, season=None,
               output=None, purpose=None, operator=None, function=None,
               variable=None, search=None) -> pd.DataFrame:
    """Liste toutes les fiches CARD disponibles avec leurs métadonnées.

    Contrairement au package R (qui lit un CSV pré-généré), les métadonnées
    sont lues directement depuis les blocs meta des YAML.

    Filtres optionnels (insensibles à la casse, fr et en confondus pour
    les facettes de classification, cf. docs/dev/TOPICS.md) :
    domain     : grandeur ('débit', 'flow', 'precipitation'...).
    phenomenon : phénomène ('basses eaux', 'baseflow', 'snow'...).
    aspect     : dimension IHA ('intensité', 'timing', 'duration'...).
    season     : fenêtre d'échantillonnage ('estivale', 'annual'...).
    output     : forme du résultat ('série', 'scalar', 'curve').
    purpose    : finalité ('performance', 'sensitivity').
    operator   : opérateur dérivé du préfixe de l'id ('delta', 'median',
                 'mean', 'trend slope', 'trend test', 'count').
    function   : sous-chaîne d'un nom de fonction du process
                 (ex. 'baseflow', 'rollmean', 'delta').
    variable   : sous-chaîne du nom de variable (ex. 'VCN').
    search     : sous-chaîne cherchée dans nom, description et variable.
    """
    if path is None:
        path = _DEFAULT_CARD_DIR
    cards = _find_cards(path, None)
    rows = [_meta_rows(load_card(p)) for p in cards.values()]
    metaEX = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    if not include_experimental and "is_experimental" in metaEX.columns:
        metaEX = metaEX[~metaEX["is_experimental"].astype(bool)]

    def _contains(cols, needle):
        mask = pd.Series(False, index=metaEX.index)
        for c in cols:
            if c in metaEX.columns:
                mask |= (metaEX[c].astype(str)
                         .str.contains(needle, case=False, regex=False))
        return mask

    for needle, cols in [
        (domain, ["domain_fr", "domain_en"]),
        (phenomenon, ["phenomenon_fr", "phenomenon_en"]),
        (aspect, ["aspect_fr", "aspect_en"]),
        (season, ["season_fr", "season_en"]),
        (output, ["output_fr", "output_en"]),
        (purpose, ["purpose_fr", "purpose_en"]),
        (operator, ["operator"]),
        (function, ["functions"]),
    ]:
        if needle is not None:
            metaEX = metaEX[_contains(cols, needle)]
    if variable is not None:
        metaEX = metaEX[_contains(["variable_fr", "variable_en"], variable)]
    if search is not None:
        metaEX = metaEX[_contains(
            ["variable_fr", "variable_en", "name_fr", "name_en",
             "description_fr", "description_en"], search)]
    return metaEX.reset_index(drop=True)


def info(name, path=None, lang="fr") -> dict:
    """Affiche la description complète d'une fiche CARD et retourne ses
    métadonnées sous forme de dict.

    name : nom de la fiche (ex. 'QA', 'VCN10', 'dtLF').
    lang : 'fr' (défaut) ou 'en'.
    """
    if path is None:
        path = _DEFAULT_CARD_DIR
    if lang not in ("fr", "en"):
        raise ValueError(f"lang='{lang}' invalide : 'fr' ou 'en'.")
    found = _find_cards(path, [name])
    card = load_card(found[name])
    meta_g = card["meta"]["global"]
    # Forme par défaut d'une fiche à placeholders, jamais l'accolade :
    # info() est une lecture humaine, comme le catalogue.
    meta_l = {**card["meta"][lang],
              **_sfx.apply(card["meta"][lang],
                           _sfx.default_record(card["meta"][lang]),
                           card_id=card.get("id"), lang=lang, key=None)}

    def _fmt(v):
        return ", ".join(str(x) for x in v) if isinstance(v, list) else v

    info = {
        "id": card.get("id", name),
        "variable": _fmt(meta_l.get("variable")),
        "name": _fmt(meta_l.get("name")),
        "unit": _fmt(meta_l.get("unit")),
        "description": _fmt(meta_l.get("description")) or "",
        "method": _fmt(meta_l.get("method")),
        "sampling_period": _fmt(meta_l.get("sampling_period")),
        **{k: _fmt(v) for k, v in (meta_l.get("classification") or {}).items()},
        "input_vars": _describe_inputs(meta_g.get("input_vars"), lang),
        "is_experimental": bool(meta_g.get("is_experimental", False)),
        # chemin DANS le corpus, et identifiant pérenne du fichier :
        # un chemin absolu de machine n'apprend rien et expose son
        # arborescence (cf. _corpus_path dans extraction.py)
        "path": _corpus_path(found[name]),
        "version": card.get("version"),
        "swhid": card.get("swhid"),
    }
    # Ce qui s'imprime est une FIGURE, pas une liste de champs : elle
    # montre la chaîne de calcul, ses paramètres et sa fenêtre. Les
    # champs bruts restent dans le dict retourné, c'est son rôle.
    from .render import figure
    try:
        print(figure(name, path=path, lang=lang))
    except Exception:                       # une fiche hors norme reste lisible
        width = max(len(k) for k in info)
        for k, v in info.items():
            if v not in (None, ""):
                print(f"{k.ljust(width)}  {v}")
    return info


def copy_cards(cards=("QA", "QJXA"), dest="./WIP",
               source=None, numbered=False, overwrite=False,
               verbose=False):
    """Copie des fiches YAML dans un dossier de travail pour personnalisation.

    cards    : liste de noms, ou dict imbriqué {sous_dossier: [noms, ...]}
               pour organiser en sous-dossiers numérotés.
    dest     : dossier de destination.
    source   : dossier source des fiches (défaut : fiches embarquées).
    numbered : préfixe les fichiers copiés (001_, 002_, ...). Faux par
               défaut : le linter exige que l'identifiant d'une fiche soit
               aussi son nom de fichier, et un préfixe le ferait échouer.
               N'a d'intérêt que pour ordonner un dossier de travail.
    """
    if source is None:
        source = _DEFAULT_CARD_DIR
    dest = Path(dest)

    if dest.exists():
        if overwrite:
            shutil.rmtree(dest)
        else:
            raise FileExistsError(
                f"Le dossier {dest} existe déjà, utilisez overwrite=True "
                "pour l'écraser."
            )
    dest.mkdir(parents=True)

    available = _find_cards(source, None)

    def _copy_names(names, target: Path):
        for j, name in enumerate(names, start=1):
            if name not in available:
                raise FileNotFoundError(f"CARD introuvable : {name}")
            fname = f"{j:03d}_{name}.yaml" if numbered else f"{name}.yaml"
            shutil.copy(available[name], target / fname)
            if verbose:
                print(f"  {available[name]} -> {target / fname}")

    if isinstance(cards, dict):
        for i, (sub, names) in enumerate(cards.items(), start=1):
            sub_dir = dest / (f"{i:03d}_{sub}" if numbered else sub)
            sub_dir.mkdir(parents=True)
            _copy_names(names, sub_dir)
    else:
        _copy_names(list(cards), dest)


# Alias hérités du package R CARD
CARD_list_all = list_cards
CARD_info = info
CARD_management = copy_cards
