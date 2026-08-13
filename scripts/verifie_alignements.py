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


def libelle_skosmos(uri, delai=20):
    """Libellé chez Theia, dont le Skosmos a un point REST dédié."""
    url = f"{REST}?{urllib.parse.urlencode({'uri': uri, 'lang': 'en'})}"
    try:
        with urllib.request.urlopen(url, timeout=delai) as reponse:
            return json.load(reponse).get("prefLabel")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
        return None


def libelle_rdf(uri, delai=30):
    """Libellé d'une ressource qui se sert elle-même en RDF.

    C'est le cas de QUDT et d'OWL-Time : on demande du Turtle, on lit le
    libellé de la ressource visée. Pas de point d'API à connaître, c'est
    le web sémantique tel qu'il est censé fonctionner.
    """
    from rdflib import Graph, URIRef
    from rdflib.namespace import RDFS, SKOS
    requete = urllib.request.Request(uri, headers={"Accept": "text/turtle"})
    try:
        with urllib.request.urlopen(requete, timeout=delai) as reponse:
            g = Graph().parse(data=reponse.read(), format="turtle")
    except Exception:
        return None
    sujet = URIRef(uri)
    for propriete in (RDFS.label, SKOS.prefLabel):
        for o in g.objects(sujet, propriete):
            if getattr(o, "language", None) in (None, "en"):
                return str(o)
    return None


# Comment résoudre, selon le préfixe. `xsd:` en est absent à dessein :
# un type de données n'est pas une ressource qui porte un libellé.
RESOLVEURS = {
    "theia": libelle_skosmos,
    "qudt": libelle_rdf, "unit": libelle_rdf, "quantitykind": libelle_rdf,
    "time": libelle_rdf,
}


def uris(alignements):
    """(où, uri, résolveur) pour chaque référence externe du fichier."""
    prefixes = alignements["namespaces"]
    trouvees = []
    for section in ("inputs", "statistic", "units"):
        for cle, valeur in (alignements.get(section) or {}).items():
            for champ, brut in (valeur or {}).items():
                if not isinstance(brut, str) or ":" not in brut:
                    continue
                prefixe, reste = brut.split(":", 1)
                if prefixe in prefixes and prefixe in RESOLVEURS:
                    trouvees.append((f"{section}.{cle}.{champ}",
                                     prefixes[prefixe] + reste,
                                     RESOLVEURS[prefixe]))
    return trouvees


def main():
    alignements = yaml.safe_load(
        (RACINE / "src" / "card" / "alignments.yaml").read_text(
            encoding="utf-8"))
    references = uris(alignements)
    print(f"{len(references)} références externes à résoudre\n")
    manquantes = []
    for ou, uri, resolveur in references:
        nom = resolveur(uri)
        if nom is None:
            manquantes.append((ou, uri))
            print(f"  ÉCHEC  {ou:34} {uri}")
        else:
            print(f"  ok     {ou:34} {nom}")
    if manquantes:
        print(f"\n{len(manquantes)} référence(s) ne résolvent pas.")
        print("Soit le service est indisponible, soit le concept a bougé.")
        return 1
    print("\nToutes les références résolvent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
