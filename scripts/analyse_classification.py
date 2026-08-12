#!/usr/bin/env python3
# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Mesure la santé de la classification à facettes.

    python scripts/analyse_classification.py

Trois questions qu'on se pose à chaque fois qu'on veut ajouter, retirer
ou fusionner une facette, et auxquelles on répondait jusqu'ici par des
scripts jetables. Les chiffres ne sont écrits nulle part dans la doc,
volontairement : ils bougent avec le corpus, et une valeur recopiée
finit par mentir. C'est la commande qui fait foi.

**1. Redondance.** Connaître la facette A donne-t-il la facette B ? Une
paire à 100 % signifie qu'une des deux ne dit rien de plus que l'autre,
donc qu'il faut la retirer ou la redéfinir. Mesuré comme la part des
valeurs de A qui n'admettent qu'une seule valeur de B.

**2. Pouvoir de résolution.** En combien de groupes distincts les
facettes découpent-elles le corpus, et que reste-t-il d'indistinct ? Une
classification n'a pas à identifier une variable, c'est le rôle du nom ;
mais savoir CE QUI reste indistinct dit où sont les trous. Les causes
connues sont séparées : le fan-out mensuel ou saisonnier, dont le membre
n'est porté que par le nom, et le paramètre numérique (`VCN10` contre
`VCN3`), qui n'est porté nulle part ailleurs.

**3. Colonnes dérivées.** `operator` est calculé depuis le PRÉFIXE de
l'identifiant, pas déclaré. On vérifie s'il reste une information qu'il
serait seul à porter : si les facettes déclarées le déterminent
entièrement, c'est une dette à retirer.
"""

import collections
import itertools
import re
import sys

import card

FACETTES = ["domain_en", "phenomenon_en", "aspect_en", "statistic_en",
            "season_en", "output_en", "purpose_en"]

_MOIS = re.compile(r"_(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)$")
_SAISON = re.compile(r"_(DJF|MAM|JJA|SON)$")
_CHIFFRE = re.compile(r"\d")


def _colonne(d, nom):
    return d[nom].fillna("").astype(str)


def redondance(d):
    """Part des valeurs de A qui n'admettent qu'une valeur de B."""
    print("1. REDONDANCE  (A connu → B connu)\n")
    fortes = []
    for a, b in itertools.permutations(FACETTES, 2):
        groupes = collections.defaultdict(set)
        for x, y in zip(_colonne(d, a), _colonne(d, b)):
            groupes[x].add(y)
        part = sum(len(v) == 1 for v in groupes.values()) / len(groupes)
        if part >= 0.90:
            fortes.append((part, a, b))
    for part, a, b in sorted(fortes, reverse=True):
        verdict = "REDONDANTE" if part == 1 else "très liée"
        print(f"   {a:16} → {b:16} {part:6.0%}   {verdict}")
    if not any(p == 1 for p, _, _ in fortes):
        print("   aucune paire totalement redondante")
    return any(p == 1 for p, _, _ in fortes)


def resolution(d):
    """Groupes que les facettes ne distinguent pas, et pourquoi."""
    print("\n2. POUVOIR DE RÉSOLUTION\n")
    groupes = collections.defaultdict(list)
    for _, ligne in d.iterrows():
        cle = tuple(str(ligne[c]) for c in FACETTES)
        groupes[cle].append(ligne["variable_en"])

    seules = sum(1 for v in groupes.values() if len(v) == 1)
    print(f"   {len(d)} variables → {len(groupes)} combinaisons")
    print(f"   {seules} variables distinguées seules")

    causes = collections.Counter()
    for membres in groupes.values():
        if len(membres) == 1:
            continue
        socles = {_MOIS.sub("", _SAISON.sub("", m)) for m in membres}
        if len(socles) < len(membres):
            causes["fan-out mois ou saison (le membre n'est que dans le nom)"] \
                += len(membres)
        elif all(_CHIFFRE.search(m) for m in membres):
            causes["paramètre numérique (VCN10 contre VCN3)"] += len(membres)
        else:
            causes["fiches distinctes de mêmes facettes"] += len(membres)
    for cause, n in causes.most_common():
        print(f"     {n:4}  {cause}")


def colonnes_derivees(d):
    """`operator` porte-t-il encore une information propre ?"""
    print("\n3. COLONNES DÉRIVÉES\n")
    if "operator" not in d.columns:
        print("   `operator` a été retiré : plus rien à vérifier")
        return
    cle = list(zip(_colonne(d, "statistic_en"), _colonne(d, "output_en"),
                   _colonne(d, "aspect_en")))
    groupes = collections.defaultdict(set)
    for k, op in zip(cle, _colonne(d, "operator")):
        groupes[k].add(op)
    ambigus = {k: v for k, v in groupes.items() if len(v) > 1}
    print(f"   {len(groupes)} triplets (statistic, output, aspect)")
    if ambigus:
        print(f"   {len(ambigus)} laissent `operator` ambigu :")
        for k, v in ambigus.items():
            print(f"     {k} → {sorted(v)}")
    else:
        print("   AUCUN ne laisse `operator` ambigu : la colonne est "
              "entièrement déterminée")
        print("   par des facettes déclarées, donc elle ne porte plus "
              "d'information propre.")


def main():
    d = card.list_cards()
    doublon = redondance(d)
    resolution(d)
    colonnes_derivees(d)
    return 1 if doublon else 0


if __name__ == "__main__":
    sys.exit(main())
