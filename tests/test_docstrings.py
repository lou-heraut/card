# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""La docstring d'une fonction PUBLIQUE est de la documentation.

Deux règles, et elles ne valent que pour `card.__all__`, c'est-à-dire ce
qu'un utilisateur appelle. La machinerie interne écrit dans la langue
qu'elle veut et comme elle veut : elle s'adresse à qui ouvre le fichier.

**Anglais.** C'est la langue de la publication scientifique, celle du
README, celle du site. Une API française sous une vitrine anglaise oblige
le lecteur à changer de langue au moment précis où il passe de la
promesse à l'usage.

**Sections NumPy.** `Parameters`, `Returns`, et les autres au besoin.
C'est la norme du Python scientifique, c'est déjà celle de stase, et
c'est ce qu'un générateur de documentation sait rendre en tableaux
plutôt qu'en pavé. Écrire un paragraphe libre n'est pas plus rapide, ça
déplace juste le travail sur le lecteur.

Ce fichier MESURE ces deux règles au lieu de compter sur la mémoire.
Elles ont été appliquées le 2026-08-11, sur les treize noms exportés.
"""

import ast
import re
from pathlib import Path

import pytest

import card

# Mots français sans équivalent anglais, donc sans faux positif possible
# sur une docstring correcte : « information » ou « format » seraient
# ambigus, ceux-ci ne le sont pas.
FRANCAIS = re.compile(
    r"\b(fiche|fiches|une|des|qui|dans|pour|avec|chaque|selon|sont|"
    r"est|les|la|du|aux|leur|cette|ce|par|sans|plus|donc)\b"
)
SECTION = re.compile(r"^\s*(Parameters|Returns|Yields)\s*\n\s*-{3,}", re.M)


def _publiques():
    """Les noms exportés qui sont des fonctions, alias R compris."""
    return [(n, getattr(card, n)) for n in card.__all__
            if callable(getattr(card, n))]


def test_the_public_api_is_documented_in_english():
    """Une docstring publique qui parle français renvoie le lecteur à sa
    langue au moment où il cherche à s'en servir.

    Le seuil est à deux mots : un accident de citation (« la fiche QA »
    dans un exemple) ne doit pas faire échouer, une phrase française
    doit.
    """
    fautifs = {}
    for nom, fonction in _publiques():
        trouves = set(FRANCAIS.findall((fonction.__doc__ or "").lower()))
        if len(trouves) >= 2:
            fautifs[nom] = sorted(trouves)
    assert not fautifs, (
        f"docstrings publiques encore en français : {fautifs}")


@pytest.mark.parametrize("nom", [n for n, _ in _publiques()])
def test_the_public_api_uses_numpy_sections(nom):
    """Sans sections, un générateur de documentation rend un pavé, et un
    lecteur cherche le sens de `sampling_period` dans un paragraphe."""
    doc = getattr(card, nom).__doc__ or ""
    assert doc.strip(), f"{nom} n'a aucune docstring"
    assert SECTION.search(doc), (
        f"{nom} : docstring sans section NumPy `Parameters` ou `Returns`")


def test_every_exported_name_is_covered():
    """La garde doit suivre le paquet, pas une liste écrite ici.

    Si un nom entre dans `__all__` sans docstring conforme, les deux
    tests au-dessus le voient. Celui-ci vérifie seulement qu'ils ont
    quelque chose à regarder, c'est-à-dire que `__all__` n'est pas vide
    et que tout ce qu'il annonce existe vraiment.
    """
    assert card.__all__, "__all__ vide : les deux gardes ne testent rien"
    for nom in card.__all__:
        assert hasattr(card, nom), f"__all__ annonce {nom}, absent du paquet"


# ── Le balisage : du Markdown, pas du reStructuredText ──────────────────
#
# Le style NumPy est né pour Sphinx, et sa syntaxe en ligne est donc du
# reST : doubles accents graves pour du code, rôles `:func:` pour un
# renvoi. Le site, lui, découpe les SECTIONS NumPy puis rend le CORPS en
# Markdown, qui ne connaît ni l'un ni l'autre.
#
# Ce que ça coûtait, mesuré le 2026-08-13 : trente-huit `:func:` en clair
# au milieu des phrases des deux pages de fonctions, et des paires
# d'accents graves visibles dans les valeurs par défaut. Les doubles
# accents graves, eux, passaient par chance, le Markdown les acceptant
# comme délimiteurs de code.
#
# La règle retenue est donc : sections NumPy, corps en Markdown. Un
# accent grave simple pour du code, aucun rôle. Un renvoi vers une autre
# fonction s'écrit `card.list_cards`, sans lien : la syntaxe de lien de
# mkdocstrings laisserait ses crochets dans `help()`, et le terminal est
# le premier lecteur d'une docstring.

REST = re.compile(r":(?:func|meth|class|mod|attr|data|obj|ref):`")
DOUBLE = re.compile(r"``")


def _docstrings_du_paquet():
    """(fichier, docstring) pour tout le paquet, publiques ou non.

    La règle porte sur le BALISAGE, pas sur la langue : elle vaut donc
    aussi pour la machinerie interne, dont les docstrings finissent sous
    les yeux de qui ouvre le fichier.
    """
    racine = Path(card.__file__).parent
    for chemin in sorted(racine.rglob("*.py")):
        arbre = ast.parse(chemin.read_text(encoding="utf-8"))
        for noeud in ast.walk(arbre):
            if isinstance(noeud, (ast.Module, ast.ClassDef, ast.FunctionDef,
                                  ast.AsyncFunctionDef)):
                texte = ast.get_docstring(noeud)
                if texte:
                    yield chemin.relative_to(racine), texte


def test_les_docstrings_sont_ecrites_en_markdown():
    fautes = []
    for chemin, texte in _docstrings_du_paquet():
        if REST.search(texte):
            fautes.append(f"{chemin} : rôle reST (`:func:` et compagnie)")
        if DOUBLE.search(texte):
            fautes.append(f"{chemin} : doubles accents graves")
    assert not fautes, (
        "le corps d'une docstring s'écrit en Markdown : un accent grave "
        "simple pour du code, aucun rôle.\n  " + "\n  ".join(sorted(set(fautes)))
    )
