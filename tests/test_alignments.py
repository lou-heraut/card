# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""`alignments.yaml` : ce qui n'est pas dérivable des fiches.

Un fichier de correspondances est un endroit où l'on écrit des choses que
personne ne relit. Ce qui est mesuré ici est donc sa COHÉRENCE avec le
reste du dépôt, pas son contenu :

- toute variable d'entrée du registre y est traitée, sans oubli ;
- toute clé citée est un vrai slug de `topics.yaml` ;
- tout paramètre listé est effectivement employé par une fiche, et
  aucun paramètre employé n'est laissé sans décision ;
- les préfixes utilisés sont déclarés.

La résolution RÉSEAU des URIs de Theia n'est pas testée ici : un test qui
sort sur le réseau échoue les jours où le service tousse, et ce n'est pas
ce qu'on veut apprendre. `scripts/verifie_alignements.py` le fait à la
demande.
"""

import collections
import pathlib

import yaml

import card
from card.extraction import _DEFAULT_CARD_DIR, _find_cards
from card.loader import load_card
from card.schema import input_registry

RACINE = pathlib.Path(__file__).resolve().parent.parent
ALIGNEMENTS = yaml.safe_load(
    (RACINE / "src" / "card" / "alignments.yaml").read_text(encoding="utf-8"))


def test_every_input_variable_is_accounted_for():
    """Une entrée oubliée est une variable sans propriété I-ADOPT.

    `hasProperty` et `hasObjectOfInterest` sont OBLIGATOIRES dans le
    cadre : une entrée non traitée rendrait ses variables invalides.
    """
    registre = input_registry()
    mesurees = {k for k, v in registre.items()
                if not (isinstance(v, dict) and v.get("type") == "date")}
    traitees = set(ALIGNEMENTS["inputs"])
    assert mesurees - traitees == set(), (
        f"entrées de inputs.yaml sans alignement : {mesurees - traitees}")
    assert traitees - mesurees == set(), (
        f"alignements sans entrée au registre : {traitees - mesurees}")


def test_the_statistic_keys_are_real_slugs():
    """Un slug mal orthographié aligne un concept qui n'existe pas."""
    vocabulaire = set(card.vocabulary()["statistic"])
    declarees = set(ALIGNEMENTS["statistic"])
    assert declarees <= vocabulaire, (
        f"clés hors vocabulaire `statistic` : {declarees - vocabulaire}")


def test_every_parameter_of_the_corpus_is_decided():
    """Un paramètre ni sémantique ni ignoré serait traité au hasard.

    Le générateur lit les `func` des process : tout nom de kwarg qu'il y
    rencontre doit avoir été rangé d'un côté ou de l'autre, sans quoi
    son sort dépendrait de l'ordre du code.
    """
    employes = collections.Counter()
    for _, chemin in _find_cards(_DEFAULT_CARD_DIR, None).items():
        for p in load_card(chemin)["processes"]:
            for e in p["func"]:
                for nom in (e.get("kwargs") or {}):
                    employes[nom] += 1
    decides = set(ALIGNEMENTS["parameters"]) | set(
        ALIGNEMENTS["ignored_parameters"])
    indecis = set(employes) - decides
    assert not indecis, f"paramètres employés sans décision : {sorted(indecis)}"


def test_no_parameter_is_declared_twice():
    """Sémantique ET ignoré : le générateur trancherait tout seul."""
    deux = set(ALIGNEMENTS["parameters"]) & set(
        ALIGNEMENTS["ignored_parameters"])
    assert not deux, f"paramètres des deux côtés : {sorted(deux)}"


def test_declared_parameters_are_actually_used():
    """Un paramètre déclaré mais absent du corpus est une ligne morte."""
    employes = set()
    for _, chemin in _find_cards(_DEFAULT_CARD_DIR, None).items():
        for p in load_card(chemin)["processes"]:
            for e in p["func"]:
                employes |= set(e.get("kwargs") or {})
    morts = set(ALIGNEMENTS["parameters"]) - employes
    assert not morts, f"paramètres déclarés, jamais employés : {sorted(morts)}"


def test_every_prefix_used_is_declared():
    """Un préfixe non déclaré rend une URI illisible pour un moissonneur."""
    prefixes = set(ALIGNEMENTS["namespaces"])
    texte = (RACINE / "src" / "card" / "alignments.yaml").read_text(
        encoding="utf-8")
    utilises = set()
    for ligne in texte.splitlines():
        ligne = ligne.split("#", 1)[0]
        for mot in ligne.replace(":", ": ").split():
            if mot.count(":") == 0 and "_" in mot:
                continue
        for mot in ligne.split():
            if ":" in mot and not mot.endswith(":") and "//" not in mot:
                utilises.add(mot.split(":")[0].strip())
    inconnus = {p for p in utilises if p not in prefixes} - {
        "en", "fr", "unit", "family", "provenance", "property", "object",
        "same_as", "parameter", "constraint", "literal_only"}
    assert not inconnus, f"préfixes utilisés non déclarés : {sorted(inconnus)}"


def test_the_constraint_families_are_all_referenced():
    """Une famille de contrainte sans membre est du vocabulaire mort."""
    familles = set(ALIGNEMENTS["constraint_families"])
    citees = {v["family"] for v in ALIGNEMENTS["parameters"].values()}
    citees |= {v["family"] for v in ALIGNEMENTS["constraints"].values()}
    # `sampling-window` sert aux fenêtres lues dans meta.sampling_period,
    # qui ne passent pas par la table des paramètres.
    orphelines = familles - citees - {"sampling-window"}
    assert not orphelines, f"familles sans membre : {sorted(orphelines)}"


def test_every_unit_of_the_corpus_is_declared():
    """Une unité inconnue de la table est une unité perdue à l'export.

    Douze unités distinctes pour 472 variables : la table se tient à la
    main, et c'est le seul endroit où un code UCUM est écrit. Le
    calculer depuis la chaîne de l'unité serait le piège d'`operator`,
    une valeur que rien ne vérifie.
    """
    import card

    employees = {str(u).strip() for u in card.list_cards()["unit_en"]}
    manquantes = employees - set(ALIGNEMENTS["units"])
    assert not manquantes, (
        f"unités du corpus absentes d'alignments.yaml : {sorted(manquantes)}")
    mortes = set(ALIGNEMENTS["units"]) - employees
    assert not mortes, f"unités déclarées, jamais employées : {sorted(mortes)}"


def test_a_unit_is_either_a_measure_or_a_value_type():
    """Trois des douze « unités » du corpus n'en sont pas.

    Un jour de l'année est une position dans un cycle, un booléen est un
    type de valeur. Les deux se déclarent par `value_type`, et jamais en
    même temps qu'un code UCUM : une chose est mesurée dans une unité,
    ou elle ne l'est pas.
    """
    for texte, regle in ALIGNEMENTS["units"].items():
        mesure = bool(regle.get("ucum"))
        typee = bool(regle.get("value_type"))
        assert mesure != typee, (
            f"{texte!r} : déclarer soit `ucum`, soit `value_type`, "
            f"jamais les deux ni aucun")
        if regle.get("qudt"):
            assert mesure, f"{texte!r} : une URI QUDT sans code UCUM"
