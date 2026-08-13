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
from rdflib import Graph, Namespace, URIRef  # noqa: E402
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS  # noqa: E402

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
    # Seules les RÉFÉRENCES comptent. Le schéma déclare aussi son propre
    # espace de noms en toutes lettres (`vann:preferredNamespaceUri`),
    # qui est une chaîne et non un renvoi vers une ressource.
    cites = {o for o in graphe.objects()
             if isinstance(o, URIRef) and str(o).startswith(BASE)}
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


def test_no_orphan_concept(graphe):
    """Un concept sans parent ni statut de tête n'a aucun point d'entrée.

    `skosify`, l'outil de qualité SKOS écrit par l'équipe de Skosmos, en
    signalait 188 avant le découpage en un schéma par facette : autant de
    concepts qu'un navigateur ne sait pas où ranger. Ce test garde
    l'acquis sans imposer la dépendance, la règle tenant en une ligne.
    """
    orphelins = []
    for concept in set(graphe.subjects(RDF.type, SKOS.Concept)):
        if next(graphe.objects(concept, SKOS.broader), None) is not None:
            continue
        if next(graphe.objects(concept, SKOS.topConceptOf), None) is not None:
            continue
        orphelins.append(concept)
    assert not orphelins, (
        f"{len(orphelins)} concepts sans parent ni statut de tête : "
        f"{sorted(orphelins)[:3]}")


def test_every_scheme_has_a_label(graphe):
    """Un schéma sans libellé s'affiche sans nom, et `skosify` le dit."""
    from rdflib.namespace import RDFS
    muets = [s for s in graphe.subjects(RDF.type, SKOS.ConceptScheme)
             if next(graphe.objects(s, RDFS.label), None) is None]
    assert not muets, f"schémas sans rdfs:label : {muets}"


def test_every_variable_says_what_its_numbers_are(graphe):
    """Un thésaurus de variables sans unité renvoie au catalogue.

    Zéro unité sur 10 809 triplets avant le 2026-08-13 : c'était le plus
    gros manque de l'export. Chaque variable dit désormais soit son
    unité (`qudt:hasUnit`), soit ce que ses nombres SONT quand ce n'est
    pas une mesure (`card:valueType`, un jour de l'année ou un booléen).
    """
    qudt = Namespace("http://qudt.org/schema/qudt/")
    muettes = []
    for v in graphe.subjects(RDF.type,
                             URIRef("https://w3id.org/iadopt/ont/Variable")):
        if "/variable/" not in str(v):
            continue
        if (next(graphe.objects(v, qudt.hasUnit), None) is None
                and next(graphe.objects(v, CARD["valueType"]), None) is None):
            muettes.append(str(v).rsplit("/", 1)[-1])
    assert not muettes, (
        f"{len(muettes)} variable(s) sans unité ni type de valeur : "
        f"{sorted(muettes)[:5]}")


def test_the_units_card_defines_itself_are_complete(graphe):
    """Trois unités n'existent pas chez QUDT : card définit les siennes.

    Elles doivent alors porter ce qui les rend utilisables, c'est-à-dire
    leur code UCUM, sans quoi on aurait remplacé une URI absente par une
    URI vide. Et elles ne sont PAS des concepts du vocabulaire : une
    unité n'est pas une notion de card, c'est une ressource citée.
    """
    qudt = Namespace("http://qudt.org/schema/qudt/")
    notres = list(graphe.subjects(RDF.type, qudt.Unit))
    assert notres, "aucune unité propre : la table a-t-elle changé ?"
    for u in notres:
        assert next(graphe.objects(u, qudt.ucumCode), None) is not None, (
            f"{u} : unité définie sans code UCUM")
        assert (u, RDF.type, SKOS.Concept) not in graphe, (
            f"{u} : une unité n'est pas un concept du vocabulaire")


def test_a_card_can_be_cited_and_opened(graphe):
    """Une ressource qui ne mène nulle part n'est pas une ressource.

    Le chemin relatif publié avant (`flow/low-flows/…`) ne s'ouvrait pour
    personne, et le `swh:1:cnt:…` est exact mais muet. La fiche porte
    donc son auteur, sa date, l'adresse de son fichier et celle où son
    identifiant se résout.
    """
    fiche = CARD["card/VCN10"]
    for propriete in (DCTERMS.creator, DCTERMS.created, DCTERMS.source,
                      DCTERMS.identifier, RDFS.seeAlso):
        assert next(graphe.objects(fiche, propriete), None) is not None, (
            f"la fiche VCN10 ne dit pas {propriete}")
    for propriete in (DCTERMS.source, RDFS.seeAlso):
        assert str(next(graphe.objects(fiche, propriete))).startswith("http"), (
            f"{propriete} doit être une adresse, pas une chaîne")


def test_the_scheme_says_how_to_name_it(graphe):
    """Sans `vann:`, un outil tiers affiche une URI nue au lieu de `card:`."""
    vann = Namespace("http://purl.org/vocab/vann/")
    for propriete in (vann.preferredNamespacePrefix, vann.preferredNamespaceUri,
                      DCTERMS.publisher, DCTERMS.language):
        assert next(graphe.objects(CARD[""], propriete), None) is not None, (
            f"le schéma ne déclare pas {propriete}")


def test_a_window_is_a_beginning_and_a_duration(graphe):
    """Une fenêtre n'est pas « une année ou pas ».

    `_summer` court de mai à novembre, `_winter` de novembre à avril :
    opposer l'année au reste n'avait pas de sens. OWL-Time décrit les
    six fenêtres du corpus d'une seule forme, un début en mois-jour et
    une durée, et son `DateTimeDescription` accepte un mois sans année,
    ce qui est exactement ce qu'est une fenêtre qui revient.
    """
    time = Namespace("http://www.w3.org/2006/time#")
    periodes = set(graphe.subjects(RDF.type, time.ProperInterval))
    assert periodes, "aucune période : l'agrégation ne se dit plus"
    for p in periodes:
        assert next(graphe.objects(p, time.hasDurationDescription),
                    None) is not None, f"{p} : période sans durée"
    ete = CARD["period/from-05-01-to-11-30"]
    debut = next(graphe.objects(ete, time.hasBeginning))
    description = next(graphe.objects(debut, time.inDateTime))
    assert str(next(graphe.objects(description, time.month))) == "--05"
    assert str(next(graphe.objects(description, time.day))) == "---01"


def test_a_statistic_carries_its_window(graphe):
    """« un minimum » ne dit pas la variable ; « un minimum sur l'année
    hydrologique » la dit.

    C'est le modèle de CPM, celui des lignes directrices INSPIRE, et
    celui que Theia emploie avec des concepts comme « 1 day minimum ».
    Les mesures sont mutualisées : la même sert à toutes les variables
    qui l'emploient.
    """
    cpm = Namespace("http://purl.org/voc/cpm#")
    mesures = set(graphe.subjects(RDF.type, cpm.StatisticalMeasure))
    assert mesures, "aucune mesure statistique"
    for m in mesures:
        assert next(graphe.objects(m, cpm.aggregationTimePeriod),
                    None) is not None, f"{m} : mesure sans période"
        assert next(graphe.objects(m, SKOS.broader), None) is not None, (
            f"{m} : mesure qui ne dit pas de quelle statistique elle relève")
    portent = set(graphe.subjects(cpm.statisticalMeasure, None))
    assert len(portent) > 200, (
        "trop peu de variables portent une mesure : le filtre "
        "`method.aggregates` a-t-il changé ?")


def test_a_parameterised_constraint_carries_its_value(graphe):
    """« 10 » dans « fenêtre glissante de 10 jours » n'était lisible que
    par un humain. `cpm:value` en fait de la donnée."""
    cpm = Namespace("http://purl.org/voc/cpm#")
    fenetre = CARD["constraint/rolling-window-10"]
    assert str(next(graphe.objects(fenetre, cpm.value))) == "10"
    for c in graphe.subjects(RDF.type, cpm.Constraint):
        assert next(graphe.objects(c, cpm.value), None) is not None, (
            f"{c} : contrainte paramétrée sans valeur")


def test_a_family_is_a_set_of_variables(graphe):
    """Une famille n'est pas une variable : aucune fiche ne la calcule.

    I-ADOPT a la classe qu'il faut, `VariableSet`, et ses
    `hasApplicable…` disent ce que les membres partagent.
    """
    iop = Namespace("https://w3id.org/iadopt/ont/")
    familles = [s for s in graphe.subjects(RDF.type, iop.VariableSet)]
    assert len(familles) > 100, "les familles ne sont plus des VariableSet"
    for f in familles:
        assert (f, RDF.type, iop.Variable) not in graphe, (
            f"{f} : une famille se dit encore variable")
    une = CARD["family/flow.low-flows.magnitude.minimum.annual.series.q"]
    assert next(graphe.objects(une, iop.hasApplicableStatisticalModifier),
                None) is not None


def test_the_input_quantities_are_concepts(graphe):
    """`VCN10` n'est pas un débit, c'est une statistique d'un débit.

    L'alignement vers un `standard_name` CF n'a donc de sens que sur la
    grandeur d'entrée, et il fallait pour cela qu'elle existe comme
    concept. Le registre `inputs.yaml` la décrit depuis toujours.
    """
    q = CARD["input/Q"]
    assert (q, RDF.type, SKOS.Concept) in graphe
    assert str(next(graphe.objects(q, SKOS.notation))) == "Q"
    assert len(set(graphe.objects(q, SKOS.prefLabel))) == 2
    cf = [o for o in graphe.objects(q, SKOS.closeMatch)
          if "standard_name" in str(o)]
    assert cf, "Q n'est aligné sur aucun standard_name CF"
