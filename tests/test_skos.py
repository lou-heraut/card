# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""`docs/card.ttl` : généré, donc à garder frais et valide.

Même doctrine que `test_catalogue.py` : un artefact généré qui n'est pas
gardé périme en silence, et un fichier RDF périmé est pire qu'un
catalogue périmé, parce que personne ne le relit.

Ce qui est vérifié n'est pas la beauté du fichier mais ce qui casserait
un consommateur : il se relit, il ne contient aucune référence pendante,
ses littéraux portent une langue, aucun concept n'a deux `prefLabel` dans
la même langue (contrainte SKOS), et rien n'y annonce une adresse
publiable tant que les identifiants ne sont pas tranchés.
"""

import collections
import pathlib
import subprocess
import sys

import pytest

rdflib = pytest.importorskip("rdflib")
from rdflib import Graph, Namespace  # noqa: E402
from rdflib.namespace import RDF, SKOS  # noqa: E402

RACINE = pathlib.Path(__file__).resolve().parent.parent
TTL = RACINE / "docs" / "card.ttl"
BASE = "https://example.invalid/card/"
CARD = Namespace(BASE)
RELANCE = "relancer : python scripts/generate_skos.py"


@pytest.fixture(scope="module")
def graphe():
    assert TTL.exists(), f"{TTL} manque : {RELANCE}"
    g = Graph()
    g.parse(TTL, format="turtle")
    return g


def test_the_file_is_up_to_date_with_the_corpus():
    """Un `.ttl` en retard sur les fiches est un vocabulaire qui ment."""
    avant = TTL.read_text(encoding="utf-8")
    subprocess.run([sys.executable, "scripts/generate_skos.py"],
                   cwd=RACINE, check=True, capture_output=True)
    apres = TTL.read_text(encoding="utf-8")
    if avant != apres:
        TTL.write_text(apres, encoding="utf-8")
    # `dcterms:modified` porte la date du jour : la ligne change chaque
    # jour sans que le corpus bouge, et la comparer n'apprendrait rien.
    def sans_date(texte):
        return "\n".join(ligne for ligne in texte.splitlines()
                         if "dcterms:modified" not in ligne)
    assert sans_date(avant) == sans_date(apres), (
        f"{TTL} n'est plus à jour : {RELANCE}")


def test_no_dangling_reference(graphe):
    """Une URI citée mais jamais décrite est un lien mort dans le graphe.

    Elle ne casse pas la lecture du fichier, mais un navigateur de
    thésaurus affiche un concept vide, et personne ne comprend pourquoi.
    Les URIs EXTERNES sont exclues : elles sont décrites chez leur
    propriétaire, c'est tout l'intérêt d'un alignement.
    """
    decrits = {s for s in graphe.subjects() if str(s).startswith(BASE)}
    cites = {o for o in graphe.objects()
             if hasattr(o, "startswith") and str(o).startswith(BASE)}
    pendantes = cites - decrits
    assert not pendantes, f"références pendantes : {sorted(pendantes)[:5]}"


def test_every_label_carries_a_language(graphe):
    """Un littéral sans étiquette de langue est un troisième objet.

    `"minimum"` et `"minimum"@en` ne sont pas le même terme pour un
    outil SKOS, et le mélange casse les recherches par langue.
    """
    sans = [(s, o) for s, _, o in graphe.triples((None, SKOS.prefLabel, None))
            if not o.language]
    assert not sans, f"prefLabel sans langue : {sans[:5]}"


def test_one_preflabel_per_language_and_concept(graphe):
    """Contrainte SKOS, et elle se viole sans qu'on le voie.

    Une fiche multi-sorties dont les métadonnées sont des listes
    produirait deux libellés pour un même concept si on concaténait au
    lieu d'éclater.
    """
    compte = collections.Counter()
    for s, _, o in graphe.triples((None, SKOS.prefLabel, None)):
        compte[(s, o.language)] += 1
    doubles = {k: v for k, v in compte.items() if v > 1}
    assert not doubles, f"deux prefLabel pour une langue : {list(doubles)[:5]}"


def test_nothing_announces_a_publishable_address(graphe):
    """Tant que les identifiants ne sont pas tranchés, rien ne se cite.

    La base est un domaine que la RFC 2606 réserve : il ne résoudra
    jamais, donc personne ne peut prendre une URI de ce fichier pour un
    identifiant pérenne. Ce test est là pour que le jour où la vraie base
    arrive, ce soit une DÉCISION et non un oubli.
    """
    interne = {str(s) for s in graphe.subjects()
               if str(s).startswith("https://") and "w3id.org" not in str(s)
               and "purl.org" not in str(s) and "w3.org" not in str(s)
               and "etalab" not in str(s)}
    hors_base = {u for u in interne if not u.startswith(BASE)}
    assert not hors_base, (
        f"URIs hors de la base provisoire : {sorted(hors_base)[:5]}")


def test_the_expected_shape_of_one_variable(graphe):
    """Un cas complet, éprouvé de bout en bout.

    `VCN10` porte tout ce que le plan annonce : sa notation, ses deux
    libellés, son parent de famille, ses composants I-ADOPT dont deux
    pointent chez Theia, sa contrainte de durée et sa fiche.
    """
    v = CARD["variable/VCN10"]
    iop = Namespace("https://w3id.org/iadopt/ont/")
    assert (v, RDF.type, SKOS.Concept) in graphe
    assert str(next(graphe.objects(v, SKOS.notation))) == "VCN10"
    assert len(set(graphe.objects(v, SKOS.prefLabel))) == 2
    assert next(graphe.objects(v, SKOS.broader), None) is not None
    for propriete in (iop.hasProperty, iop.hasObjectOfInterest,
                      iop.hasStatisticalModifier, iop.hasConstraint):
        assert next(graphe.objects(v, propriete), None) is not None, (
            f"VCN10 sans {propriete}")
    externes = [o for o in graphe.objects(v, iop.hasProperty)
                if "ozcar-theia" in str(o)]
    assert externes, "VCN10 n'est aligné sur aucune propriété externe"
