# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Les deux pages de documentation des fonctions désignent des FONCTIONS.

Une page du site appelle une fonction par un chemin pointé
(`::: card.functions.baseflow`), et mkdocstrings le résout dans
l'arborescence des modules, où **un sous-module l'emporte sur un
attribut de même nom**. Python, lui, fait l'inverse quand le paquet
réexporte la fonction : `card.functions.baseflow` est la fonction pour
un `import`, et le module `baseflow.py` pour le générateur.

Ce qu'un chemin ambigu produit n'est pas une erreur mais une page :
le module entier s'affiche, avec tous ses membres, y compris ceux qu'on
ne documente pas, et les fonctions déjà appelées ailleurs sur la page
apparaissent une seconde fois, un rang plus bas. Constaté le 2026-08-13
sur quatre chemins, `baseflow`, `return_period`, `trend` et
`provenance` : la section « Extreme values » se mordait la queue, et
rien dans la construction ne rougissait.

La garde ne relit donc pas le rendu, elle refuse l'AMBIGUÏTÉ à la
source. Elle est aussi ce qui prévient d'une fonction déplacée d'un
fichier à l'autre, puisque le chemin cesserait alors de résoudre.
"""

import importlib
import importlib.util
import re
from pathlib import Path

import pytest

DOCS = Path(__file__).resolve().parent.parent / "docs"
PAGES = (DOCS / "toolbox.md", DOCS / "functions.md")
DIRECTIVE = re.compile(r"^::: +([\w.]+)\s*$", re.M)


def _chemins():
    trouves = []
    for page in PAGES:
        for chemin in DIRECTIVE.findall(page.read_text(encoding="utf-8")):
            trouves.append((page.name, chemin))
    return trouves


def test_les_pages_appellent_bien_des_fonctions():
    assert _chemins(), "aucune directive `::: ` : les gardes ne testent rien"


@pytest.mark.parametrize("page,chemin", _chemins())
def test_le_chemin_designe_une_fonction_et_pas_un_module(page, chemin):
    module, _, nom = chemin.rpartition(".")
    objet = getattr(importlib.import_module(module), nom, None)
    assert callable(objet), (
        f"{page} appelle `{chemin}`, qui n'est pas une fonction de card"
    )


@pytest.mark.parametrize("page,chemin", _chemins())
def test_le_chemin_ne_designe_pas_aussi_un_module(page, chemin):
    """Un chemin qui nomme un module rend le MODULE, pas la fonction."""
    try:
        spec = importlib.util.find_spec(chemin)
    except ModuleNotFoundError:
        # Un parent qui n'est pas un paquet : le chemin ne peut donc pas
        # désigner un module, ce qui est exactement ce qu'on veut.
        return
    assert spec is None, (
        f"{page} appelle `{chemin}`, qui est AUSSI un module : la page "
        f"rendra tout le module. Viser la fonction dans son fichier, "
        f"par exemple `{chemin}.{chemin.rsplit('.', 1)[-1]}`"
    )
