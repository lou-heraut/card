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

from .extraction import _DEFAULT_CARD_DIR, _find_cards, _meta_rows
from .loader import load_card


def list_cards(path=None, include_experimental=False,
               topic=None, variable=None, search=None) -> pd.DataFrame:
    """Liste toutes les fiches CARD disponibles avec leurs métadonnées.

    Contrairement au package R (qui lit un CSV pré-généré), les métadonnées
    sont lues directement depuis les blocs meta des YAML.

    Filtres optionnels (insensibles à la casse) :
    topic    : sous-chaîne du thème (ex. 'Étiages', 'Low Flows').
    variable : sous-chaîne du nom de variable (ex. 'VCN').
    search   : sous-chaîne cherchée dans nom, description et variable
               (fr et en confondus).
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

    if topic is not None:
        metaEX = metaEX[_contains(["topic_fr", "topic_en"], topic)]
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
    meta_l = card["meta"][lang]
    meta_g = card["meta"]["global"]

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
        "topic": _fmt(meta_l.get("topic")),
        "input_vars": meta_g.get("input_vars"),
        "is_experimental": bool(meta_g.get("is_experimental", False)),
        "path": str(found[name]),
    }
    width = max(len(k) for k in info)
    for k, v in info.items():
        if v not in (None, ""):
            print(f"{k.ljust(width)}  {v}")
    return info


def copy_cards(cards=("QA", "QJXA"), dest="./WIP",
               source=None, numbered=True, overwrite=False,
               verbose=False):
    """Copie des fiches YAML dans un dossier de travail pour personnalisation.

    cards    : liste de noms, ou dict imbriqué {sous_dossier: [noms, ...]}
               pour organiser en sous-dossiers numérotés.
    dest     : dossier de destination.
    source   : dossier source des fiches (défaut : fiches embarquées).
    numbered : préfixe les fichiers copiés (001_, 002_, ...).
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
