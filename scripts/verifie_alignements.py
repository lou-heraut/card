#!/usr/bin/env python3
# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Résout les URIs externes de `alignments.yaml`, sur le réseau.

    python scripts/verifie_alignements.py

Séparé de la suite de tests, et c'est délibéré : un test qui sort sur le
réseau échoue les jours où le service d'en face tousse, et ce qu'on
apprend alors n'est pas ce qu'on voulait savoir. `tests/test_alignments.py`
vérifie la COHÉRENCE interne du fichier ; ce script vérifie que les
concepts visés existent encore chez eux.

À lancer avant une publication, et le jour où un alignement paraît
douteux. Sortie non nulle si une URI ne résout pas.
"""

import json
import pathlib
import sys
import urllib.error
import urllib.parse
import urllib.request

import yaml

RACINE = pathlib.Path(__file__).resolve().parent.parent
REST = ("https://in-situ.theia-land.fr/skosmos/rest/v1/"
        "theia_ozcar_thesaurus/label")


def libelle(uri, delai=20):
    """Libellé du concept, ou None s'il ne résout pas."""
    url = f"{REST}?{urllib.parse.urlencode({'uri': uri, 'lang': 'en'})}"
    try:
        with urllib.request.urlopen(url, timeout=delai) as reponse:
            return json.load(reponse).get("prefLabel")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def uris(alignements):
    """(où, uri) pour chaque référence externe du fichier."""
    prefixes = alignements["namespaces"]
    trouvees = []
    for section in ("inputs", "statistic"):
        for cle, valeur in (alignements.get(section) or {}).items():
            for champ, brut in (valeur or {}).items():
                if not isinstance(brut, str) or ":" not in brut:
                    continue
                prefixe, reste = brut.split(":", 1)
                if prefixe in prefixes:
                    trouvees.append((f"{section}.{cle}.{champ}",
                                     prefixes[prefixe] + reste))
    return trouvees


def main():
    alignements = yaml.safe_load(
        (RACINE / "src" / "card" / "alignments.yaml").read_text(
            encoding="utf-8"))
    references = uris(alignements)
    print(f"{len(references)} références externes à résoudre\n")
    manquantes = []
    for ou, uri in references:
        nom = libelle(uri)
        if nom is None:
            manquantes.append((ou, uri))
            print(f"  ÉCHEC  {ou:28} {uri}")
        else:
            print(f"  ok     {ou:28} {nom}")
    if manquantes:
        print(f"\n{len(manquantes)} référence(s) ne résolvent pas.")
        print("Soit le service est indisponible, soit le concept a bougé.")
        return 1
    print("\nToutes les références résolvent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
