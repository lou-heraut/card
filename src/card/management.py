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

from .extraction import (_DEFAULT_CARD_DIR, _corpus_path, _find_cards,
                         _meta_frame)
from . import method as _method
from . import suffix as _sfx
from .loader import load_card
from .schema import _vocab, input_registry


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
               domain=None, phenomenon=None, aspect=None, statistic=None,
               season=None, output=None, purpose=None,
               function=None, variable=None, search=None,
               family=None, family_of=None) -> pd.DataFrame:
    """List the available CARD cards with their metadata.

    One row per VARIABLE. The ``card`` column gives the card that
    produces it, and that is what :func:`card.extract` expects: the two
    names differ as soon as one card yields several columns
    (``mean-TMA_jan`` comes from ``mean-TMA_month``). Chaining the two
    functions therefore goes through ``card``, deduplicated.

    Unlike the R package, which reads a pre-generated CSV, the metadata
    is read straight from the ``meta`` blocks of the YAML cards, so it
    cannot fall out of step with them.

    Parameters
    ----------
    path : str or pathlib.Path, optional
        Directory of YAML cards. Defaults to the cards shipped with the
        package.
    include_experimental : bool, default False
        Also list the cards flagged as experimental.
    domain : str, optional
        Measured quantity: ``"flow"``, ``"precipitation"``,
        ``"temperature"``, ``"evapotranspiration"``.
    phenomenon : str, optional
        Hydrological phenomenon: ``"low flows"``, ``"baseflow"``,
        ``"snow"``...
    aspect : str, optional
        IHA dimension: ``"magnitude"``, ``"timing"``, ``"duration"``...
    statistic : str, optional
        Statistical operation the variable comes from: ``"mean"``,
        ``"minimum"``, ``"quantile"``, ``"trend"``... Orthogonal to
        ``aspect``: ``VCN10`` and ``tVCN10`` are both a ``"minimum"``,
        one being its value and the other its date.
    season : str, optional
        Sampling window: ``"annual"``, ``"summer"``, ``"by month"``...
    output : str, optional
        Shape of the result: ``"series"``, ``"scalar"``, ``"curve"``.
    purpose : str, optional
        ``"model performance"`` or ``"climate sensitivity"``.
    function : str, optional
        Substring of a function name used by the process, such as
        ``"baseflow"``, ``"rollmean"``, ``"delta"``.
    variable : str, optional
        Substring of a variable name, such as ``"VCN"``.
    search : str, optional
        Substring looked up in names, descriptions and variable names.
    family : str, optional
        Family identifier, as the ``family`` column holds it.
    family_of : str, optional
        Name of a variable: returns the variables sharing its family,
        that is the ones that differ from it only by a parameter.
        ``family_of="VCN10"`` gives ``QNA``, ``VCN3``, ``VCN10``,
        ``VCN30``, the same concept at four durations. Not to be confused
        with ``variable="VCN"``, a substring search that also returns
        ``delta-VCN10`` and misses ``QNA``.

    Returns
    -------
    pandas.DataFrame
        One row per variable, with its unit, names, classification,
        method, input columns and provenance.

    Notes
    -----
    Filters are case-insensitive. For the classification facets, the
    vocabulary slug and both labels are equivalent:
    ``phenomenon="low-flows"``, ``"low flows"`` and ``"basses eaux"``
    return the same rows. :func:`card.vocabulary` gives the closed list
    of values each facet accepts.

    Examples
    --------
    >>> low = card.list_cards(phenomenon="low flows", output="series")
    >>> res = card.extract(data, cards=low["card"].unique())
    """
    if path is None:
        path = _DEFAULT_CARD_DIR
    cards = _find_cards(path, None)
    # `_meta_frame` et non `_meta_rows` : il résout les placeholders de
    # suffixe avec le défaut de la fiche, comme le font `info()` et le
    # catalogue. Sans lui, la fonction de découverte du corpus affichait
    # « between the {suffix.name} horizon » sur les 83 fiches delta-,
    # c'est-à-dire un gabarit brut là où on cherche une variable.
    rows = [_meta_frame(load_card(p)) for p in cards.values()]
    metaEX = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    # `suffix` n'a pas de sens dans un listing : aucune variante n'est
    # demandée ici, la colonne serait vide sur toutes les lignes.
    metaEX = metaEX.drop(columns=["suffix"], errors="ignore")
    if not include_experimental and "is_experimental" in metaEX.columns:
        metaEX = metaEX[~metaEX["is_experimental"].astype(bool)]

    def _contains(cols, needle):
        mask = pd.Series(False, index=metaEX.index)
        for c in cols:
            if c in metaEX.columns:
                mask |= (metaEX[c].astype(str)
                         .str.contains(needle, case=False, regex=False))
        return mask

    def _needles(facette, needle):
        """Un filtre accepte le SLUG du vocabulaire autant que les
        libellés : `card.vocabulary()` (et /v1/vocabulary) annoncent les
        slugs, il serait piégeux qu'ils ne filtrent pas. 'low-flows'
        cherche donc aussi 'low flows' et 'basses eaux'."""
        entry = _vocab().get(facette, {}).get(needle) if facette else None
        if entry:
            return [v for k, v in entry.items() if k in ("en", "fr")]
        return [needle]

    for needle, cols, facette in [
        (domain, ["domain_fr", "domain_en"], "domain"),
        (phenomenon, ["phenomenon_fr", "phenomenon_en"], "phenomenon"),
        (aspect, ["aspect_fr", "aspect_en"], "aspect"),
        (statistic, ["statistic_fr", "statistic_en"], "statistic"),
        (season, ["season_fr", "season_en"], "season"),
        (output, ["output_fr", "output_en"], "output"),
        (purpose, ["purpose_fr", "purpose_en"], "purpose"),
        (function, ["functions"], None),
    ]:
        if needle is not None:
            mask = pd.Series(False, index=metaEX.index)
            for n in _needles(facette, needle):
                mask |= _contains(cols, n)
            metaEX = metaEX[mask]
    if family_of is not None:
        # Résolu AVANT tout filtrage de facette : sinon la variable citée
        # pourrait avoir déjà été écartée, et la famille serait vide sans
        # que rien ne le dise.
        cible = metaEX[metaEX["variable_en"].astype(str) == str(family_of)]
        if cible.empty:
            cible = metaEX[metaEX["variable_fr"].astype(str) == str(family_of)]
        if cible.empty:
            raise ValueError(
                f"family_of='{family_of}' : aucune variable de ce nom. "
                "Voir la colonne 'variable_en' de card.list_cards().")
        metaEX = metaEX[metaEX["family"] == cible.iloc[0]["family"]]
    if family is not None:
        metaEX = metaEX[metaEX["family"].astype(str) == str(family)]
    if variable is not None:
        metaEX = metaEX[_contains(["variable_fr", "variable_en"], variable)]
    if search is not None:
        metaEX = metaEX[_contains(
            ["variable_fr", "variable_en", "name_fr", "name_en",
             "description_fr", "description_en"], search)]
    return metaEX.reset_index(drop=True)


def info(name, path=None, lang="fr", quiet=False) -> dict:
    """Draw one CARD card and return its metadata as a dict.

    Parameters
    ----------
    name : str
        Name of the card, such as ``"QA"``, ``"VCN10"``, ``"dtLF"``.
    path : str or pathlib.Path, optional
        Directory of YAML cards. Defaults to the cards shipped with the
        package.
    lang : {"fr", "en"}, default "fr"
        Language the figure and the metadata are drawn in.
    quiet : bool, default False
        Print nothing and return the dict alone. Meant for programmatic
        calls: a web service has no terminal, so the figure would be
        computed for nothing and land in the logs at every request. To
        get the figure as a STRING, use :func:`card.figure`.

    Returns
    -------
    dict
        The card metadata, with its placeholders resolved.

    See Also
    --------
    card.figure : the same drawing, returned as a string.
    card.list_cards : find the card to name here.
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
        # `method` est une table indexée par process (cf. card/method.py) :
        # ce qui se lit ici est sa forme publiée, la même que celle des
        # métadonnées de sortie, et non la structure brute.
        "method": _fmt(_method.published(
            {**card, "meta": {**card["meta"], lang: meta_l}}, lang)),
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
    if not quiet:
        from .render import figure
        try:
            print(figure(name, path=path, lang=lang))
        except Exception:                   # une fiche hors norme reste lisible
            width = max(len(k) for k in info)
            for k, v in info.items():
                if v not in (None, ""):
                    print(f"{k.ljust(width)}  {v}")
    return info


def copy_cards(cards=("QA", "QJXA"), dest="./WIP",
               source=None, numbered=False, overwrite=False,
               verbose=False):
    """Copy YAML cards into a working directory, to adapt or extend them.

    Parameters
    ----------
    cards : sequence of str or dict, default ``("QA", "QJXA")``
        Card names, or a nested dict ``{subfolder: [names, ...]}`` to
        organise the copy into numbered subfolders.
    dest : str or pathlib.Path, default ``"./WIP"``
        Destination directory.
    source : str or pathlib.Path, optional
        Directory to copy from. Defaults to the cards shipped with the
        package.
    numbered : bool, default False
        Prefix the copied files (``001_``, ``002_``...). Left False,
        because the linter requires the identifier of a card to also be
        its file name, and a prefix would make it fail. It is only worth
        turning on to order a working directory.
    overwrite : bool, default False
        Replace the destination directory if it already exists.
    verbose : bool, default False
        Print each file as it is copied.

    Returns
    -------
    None
        The cards are written under ``dest``. Point
        ``card.extract(path=dest)`` at them to run your own versions.
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
