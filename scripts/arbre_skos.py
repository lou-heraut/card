#!/usr/bin/env python3
# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Imprime `docs/card.ttl` en arbre, pour qu'un humain puisse le lire.

    python scripts/arbre_skos.py                 # grandeurs et phénomènes
    python scripts/arbre_skos.py --lang en       # en anglais
    python scripts/arbre_skos.py -d 2            # + les tableaux
    python scripts/arbre_skos.py -d 3 "basses"   # une branche, jusqu'au bout

Un fichier Turtle est illisible : ses concepts sortent dans l'ordre
alphabétique de leurs URIs, la hiérarchie n'y est qu'une propriété parmi
d'autres, et rien ne dit par où entrer. Ce script rend la seule chose
qu'on veut voir avant de publier, l'arbre tel qu'un navigateur SKOS
l'affichera : les concepts de tête, ce qui pend dessous, et combien de
variables porte chaque branche.

**Il ne vérifie rien et n'échoue jamais**, c'est une paire de lunettes.
Ce qui garde le fichier honnête est ailleurs : `tests/test_skos.py` pour
la fraîcheur, `python -m card.schema` pour les fiches, et `skosify` pour
la qualité SKOS.
"""

import argparse
import pathlib
import sys

from rdflib import Graph, Namespace
from rdflib.namespace import SKOS

RACINE = pathlib.Path(__file__).resolve().parent.parent
FICHIER = RACINE / "docs" / "card.ttl"
CARD = Namespace("https://example.invalid/card/")
ISOTHES = Namespace("http://purl.org/iso25964/skos-thes#")


def etiquette(g, concept, lang):
    """Le libellé d'un concept, dans la langue demandée sinon l'autre."""
    labels = {o.language: str(o) for o in g.objects(concept, SKOS.prefLabel)}
    return (labels.get(lang) or labels.get("en") or labels.get("fr")
            or str(concept).replace(str(CARD), "card:"))


def variables_sous(g, concept, vus=None):
    """Les variables qui pendent sous ce concept, à toute profondeur.

    Rend un ENSEMBLE et non un compte : une variable peut pendre sous
    deux branches, et les additionner ferait mentir le total.
    """
    vus = set() if vus is None else vus
    if concept in vus:
        return set()
    vus.add(concept)
    trouvees = set()
    for enfant in g.subjects(SKOS.broader, concept):
        if "/variable/" in str(enfant):
            trouvees.add(enfant)
        trouvees |= variables_sous(g, enfant, vus)
    return trouvees


def branche(g, concept, lang, profondeur, marge="", niveau=0):
    """Une ligne par concept, et le trait qui dit à qui il appartient.

    Deux sortes d'enfants, et elles ne sont pas de même nature. Les
    TABLEAUX subdivisent le concept sans en être des sortes : ils sont
    entre crochets, et leurs membres pendent dessous. Les concepts plus
    étroits qu'aucun tableau ne range viennent ensuite, à plat.
    """
    tableaux = sorted(g.objects(concept, ISOTHES.subordinateArray),
                      key=lambda c: etiquette(g, c, lang))
    ranges = {m for t in tableaux for m in g.objects(t, SKOS.member)}
    seuls = sorted((c for c in g.subjects(SKOS.broader, concept)
                    if c not in ranges),
                   key=lambda c: etiquette(g, c, lang))
    nombre = len(variables_sous(g, concept))
    print(f"{marge}{etiquette(g, concept, lang)}"
          f"{f'  [{nombre}]' if nombre else ''}")
    enfants = [(t, True) for t in tableaux] + [(c, False) for c in seuls]
    if niveau >= profondeur:
        if enfants:
            print(f"{marge}   … {len(tableaux)} tableau"
                  f"{'x' if len(tableaux) > 1 else ''}, "
                  f"{len(seuls)} concept{'s' if len(seuls) > 1 else ''}")
        return
    for rang, (enfant, est_tableau) in enumerate(enfants):
        suite = marge + ("   " if rang == len(enfants) - 1 else "│  ")
        if not est_tableau:
            branche(g, enfant, lang, profondeur, suite, niveau + 1)
            continue
        membres = sorted(g.objects(enfant, SKOS.member),
                         key=lambda c: etiquette(g, c, lang))
        print(f"{suite[:-3]}{'   ' if rang == len(enfants) - 1 else '│  '}"
              f"[{etiquette(g, enfant, lang)}]  ({len(membres)})")
        if niveau + 1 > profondeur:
            continue
        for i, m in enumerate(membres):
            print(f"{suite}{'   ' if i == len(membres) - 1 else '│  '}"
                  f"{etiquette(g, m, lang)}")


def main():
    analyseur = argparse.ArgumentParser(
        description="Imprime le thésaurus de card en arbre.")
    analyseur.add_argument(
        "racine", nargs="?",
        help="n'imprimer que la branche dont le libellé commence ainsi")
    analyseur.add_argument("--lang", default="fr", choices=("fr", "en"))
    # Un niveau par défaut : grandeur puis phénomène, ce qui tient à
    # l'écran. 2 ajoute les tableaux et leurs membres.
    analyseur.add_argument("-d", "--profondeur", type=int, default=1)
    options = analyseur.parse_args()

    if not FICHIER.exists():
        raise SystemExit(f"{FICHIER} absent : lancer generate_skos.py")
    g = Graph()
    g.parse(FICHIER, format="turtle")

    sommets = sorted(g.objects(CARD[""], SKOS.hasTopConcept),
                     key=lambda c: etiquette(g, c, options.lang))
    if options.racine:
        cible = options.racine.lower()
        sommets = [c for c in g.subjects(SKOS.prefLabel, None)
                   if etiquette(g, c, options.lang).lower().startswith(cible)]
        if not sommets:
            raise SystemExit(f"aucun concept ne commence par « {cible} »")
        # Un libellé exact l'emporte : « débit de base » vise le phénomène,
        # pas la variable « Débit de base (Lyne et Hollick) », qui commence
        # pourtant par les mêmes mots.
        exacts = [c for c in sommets
                  if etiquette(g, c, options.lang).lower() == cible]
        sommets = sorted(set(exacts or sommets),
                         key=lambda c: etiquette(g, c, options.lang))
    else:
        # Le schéma n'est le `broader` de personne : les variables se
        # ramassent branche par branche, sinon le total vaut zéro.
        total = set()
        for sommet in sommets:
            total |= variables_sous(g, sommet)
        print(f"card:  ({len(sommets)} concepts de tête, "
              f"{len(total)} variables)")

    for sommet in sommets:
        branche(g, sommet, options.lang, options.profondeur)
    return 0


if __name__ == "__main__":
    sys.exit(main())
