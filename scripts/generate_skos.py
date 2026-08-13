#!/usr/bin/env python3
# Copyright 2021-2026 Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Produit `docs/card.ttl`, le corpus en SKOS et I-ADOPT.

    python scripts/generate_skos.py

**RIEN N'EST PUBLIÉ.** La base d'URI est manifestement fausse
(`https://example.invalid/`, un domaine que la RFC 2606 réserve et qui ne
résoudra jamais), pour que personne ne cite par mégarde une adresse
plausible avant que la question des identifiants pérennes soit tranchée
avec les interlocuteurs concernés. Cf. `docs/dev/PLAN_SITE_SKOS.md`.

Ce que le fichier contient, et d'où vient chaque chose : la table de
référence est dans le plan, section « Tous les champs du thésaurus ».
En deux phrases : **le concept est la VARIABLE**, pas la fiche, et tout
ce qui le décrit se lit dans les fiches ; ce qui ne s'en déduit pas
(alignements externes, familles de contrainte, paramètres sémantiques)
vient de `src/card/alignments.yaml`.

Quatre choses que ce script ne fait PAS, chacune pour une raison écrite
dans le plan :

- il n'invente aucune définition quand `description` est vide, ce qui est
  le cas de 202 variables : le corpus ne la remplit que si le `name` ne
  suffit pas, et `card:method` porte de toute façon l'énoncé du calcul ;
- il ne lit aucune statistique dans la chaîne de process : elle est
  DÉCLARÉE dans la facette `statistic` ;
- il ne devine rien depuis un nom de variable ;
- il ne supprime jamais un concept, la dépréciation étant prévue mais
  sans objet tant qu'aucune fiche n'est retirée.
"""

import datetime as dt
import pathlib
import sys

import yaml
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS

import card
from card.extraction import _DEFAULT_CARD_DIR, _find_cards
from card.loader import load_card

RACINE = pathlib.Path(__file__).resolve().parent.parent
SORTIE = RACINE / "docs" / "card.ttl"

# Où lire une fiche, et où résoudre un identifiant Software Heritage. Une
# ressource qui ne mène nulle part n'est pas une ressource : le chemin
# relatif qu'on publiait avant (`flow/low-flows/…`) ne s'ouvrait pour
# personne.
DEPOT = "https://github.com/lou-heraut/card/blob/main/src/card/cards/"
SWH = "https://archive.softwareheritage.org/"

# Base PROVISOIRE et manifestement fausse : `.invalid` est réservé par la
# RFC 2606 et ne résoudra jamais. À remplacer le jour où l'hébergement
# et les identifiants sont tranchés, et pas avant.
BASE = "https://example.invalid/card/"
CARD = Namespace(BASE)
IOP = Namespace("https://w3id.org/iadopt/ont/")
QUDT = Namespace("http://qudt.org/schema/qudt/")
VANN = Namespace("http://purl.org/vocab/vann/")

ALIGNEMENTS = yaml.safe_load(
    (RACINE / "src" / "card" / "alignments.yaml").read_text(encoding="utf-8"))
PREFIXES = ALIGNEMENTS["namespaces"]


def uri(valeur):
    """`theia:c_1234` -> URIRef complète, ou None."""
    if not isinstance(valeur, str) or ":" not in valeur:
        return None
    prefixe, reste = valeur.split(":", 1)
    if prefixe not in PREFIXES:
        raise SystemExit(f"préfixe non déclaré dans alignments.yaml : {prefixe}")
    return URIRef(PREFIXES[prefixe] + reste)


def slug(texte):
    """Fragment d'URI depuis un texte libre : minuscules et tirets."""
    return "-".join(str(texte).lower().split())


def sous_schema(g, cle, titre_en, titre_fr):
    """Un schéma de concepts par facette, plus un pour les contraintes.

    Sans ça, `skosify` signale 188 « concepts orphelins » : des concepts
    qu'aucun `skos:broader` ne rattache, donc qu'aucun navigateur ne sait
    par où prendre. Découper par facette est aussi ce que la conception
    prévoyait dès l'origine, chaque facette étant un axe indépendant.
    """
    noeud = CARD[f"scheme/{cle}"]
    g.add((noeud, RDF.type, SKOS.ConceptScheme))
    for propriete in (DCTERMS.title, RDFS.label):
        g.add((noeud, propriete, Literal(titre_en, lang="en")))
        g.add((noeud, propriete, Literal(titre_fr, lang="fr")))
    return noeud


def sommet(g, concept, schema_):
    """Concept de tête : le point d'entrée d'une hiérarchie."""
    g.add((concept, SKOS.topConceptOf, schema_))
    g.add((schema_, SKOS.hasTopConcept, concept))


def schema(g, version):
    """Les métadonnées du vocabulaire lui-même, qu'on oublie toujours."""
    g.add((CARD[""], RDF.type, SKOS.ConceptScheme))
    for propriete in (DCTERMS.title, RDFS.label):
        g.add((CARD[""], propriete,
               Literal("card: hydroclimatic variable definitions", lang="en")))
        g.add((CARD[""], propriete,
               Literal("card : définitions de variables hydroclimatiques",
                       lang="fr")))
    g.add((CARD[""], DCTERMS.creator, Literal("INRAE, UR RiverLy")))
    g.add((CARD[""], DCTERMS.license,
           URIRef("https://www.etalab.gouv.fr/licence-ouverte-open-licence")))
    for lang in ("en", "fr"):
        g.add((CARD[""], DCTERMS.rights, Literal(
            "Licence Ouverte 2.0 (Etalab), compatible CC-BY 4.0", lang=lang)))
    g.add((CARD[""], OWL.versionInfo, Literal(version)))
    g.add((CARD[""], DCTERMS.modified,
           Literal(dt.date.today().isoformat())))
    g.add((CARD[""], DCTERMS.publisher, Literal("INRAE, UR RiverLy")))
    for lang in ("en", "fr"):
        g.add((CARD[""], DCTERMS.language, Literal(lang)))
    # `vann:` est le vocabulaire d'annotation des vocabulaires : ces deux
    # lignes disent à un outil tiers comment nous nommer, et sans elles
    # il affiche une URI nue là où on lit `card:VCN10`.
    g.add((CARD[""], VANN.preferredNamespacePrefix, Literal("card")))
    g.add((CARD[""], VANN.preferredNamespaceUri, Literal(BASE)))


FACETTES_FR = {"domain": "grandeur", "phenomenon": "phénomène",
               "aspect": "dimension analysée", "statistic": "opération",
               "season": "fenêtre d'échantillonnage", "output": "forme",
               "purpose": "finalité"}


def vocabulaire(g):
    """Les facettes et leurs valeurs : un schéma par facette."""
    for facette, valeurs in card.vocabulary().items():
        noeud = sous_schema(g, facette, facette,
                            FACETTES_FR.get(facette, facette))
        for cle, etiquettes in valeurs.items():
            concept = CARD[f"{facette}/{cle}"]
            g.add((concept, RDF.type, SKOS.Concept))
            g.add((concept, SKOS.inScheme, noeud))
            sommet(g, concept, noeud)
            for lang in ("en", "fr"):
                if etiquettes.get(lang):
                    g.add((concept, SKOS.prefLabel,
                           Literal(etiquettes[lang], lang=lang)))
            # `cf` et `iha` nomment le terme équivalent d'un vocabulaire
            # externe : c'est un alignement, pas une étiquette de plus.
            for source, note in (("cf", "CF cell_methods"),
                                 ("iha", "IHA")):
                if etiquettes.get(source):
                    g.add((concept, SKOS.editorialNote, Literal(
                        f"{note}: {etiquettes[source]}", lang="en")))
            aligne = (ALIGNEMENTS.get(facette) or {}).get(cle, {})
            if aligne.get("same_as"):
                g.add((concept, SKOS.exactMatch, uri(aligne["same_as"])))


def contraintes(g):
    """Familles de contrainte et contraintes nommées, définies par card."""
    schema_ = sous_schema(g, "constraint", "constraint", "contrainte")
    for cle, etiquettes in ALIGNEMENTS["constraint_families"].items():
        noeud = CARD[f"constraint-family/{cle}"]
        g.add((noeud, RDF.type, SKOS.Concept))
        g.add((noeud, RDF.type, IOP.Constraint))
        g.add((noeud, SKOS.inScheme, schema_))
        sommet(g, noeud, schema_)
        for lang in ("en", "fr"):
            g.add((noeud, SKOS.prefLabel,
                   Literal(etiquettes[lang], lang=lang)))
    for cle, entree in ALIGNEMENTS["constraints"].items():
        noeud = CARD[f"constraint/{cle}"]
        g.add((noeud, RDF.type, SKOS.Concept))
        g.add((noeud, RDF.type, IOP.Constraint))
        g.add((noeud, SKOS.inScheme, schema_))
        g.add((noeud, SKOS.broader,
               CARD[f"constraint-family/{entree['family']}"]))
        for lang in ("en", "fr"):
            g.add((noeud, SKOS.prefLabel, Literal(entree[lang], lang=lang)))


def contrainte_valeur(g, famille, valeur, unite):
    """Concept de contrainte pour une VALEUR de paramètre, créé au besoin.

    `k: 10` donne « 10 day rolling window ». Le concept est partagé par
    toutes les variables qui portent la même valeur, d'où l'identifiant
    construit sur la famille et la valeur, et non sur la variable.
    """
    # Un paramètre peut être une PAIRE : `fdc_slope(p=(0.33, 0.66))` borne
    # un segment de courbe. C'est une contrainte d'intervalle, pas deux
    # contraintes ni une valeur unique.
    intervalle = isinstance(valeur, (list, tuple)) and len(valeur) == 2
    cle = (f"{famille}-{slug(valeur[0])}-{slug(valeur[1])}" if intervalle
           else f"{famille}-{slug(valeur)}")
    noeud = CARD[f"constraint/{cle}"]
    if (noeud, RDF.type, SKOS.Concept) not in g:
        familles = ALIGNEMENTS["constraint_families"][famille]
        g.add((noeud, RDF.type, SKOS.Concept))
        g.add((noeud, RDF.type, IOP.Constraint))
        g.add((noeud, SKOS.inScheme, CARD["scheme/constraint"]))
        g.add((noeud, SKOS.broader, CARD[f"constraint-family/{famille}"]))
        gabarits = ((("en", "{famille} between {valeur}"),
                     ("fr", "{famille} entre {valeur}")) if intervalle else
                    (("en", "{valeur}{unite} {famille}"),
                     ("fr", "{famille} de {valeur}{unite}")))
        for lang, gabarit in gabarits:
            # L'unité est bilingue : « 10 day rolling window » d'un côté,
            # « fenêtre glissante de 10 jours » de l'autre. Sans ça le
            # libellé français portait un mot anglais.
            unite = unite or {}
            mot = unite.get(lang, "")
            # Le français accorde l'unité au nombre, l'anglais ne le fait
            # pas dans un adjectif composé (« 10 day rolling window »).
            # `invariable` est DÉCLARÉ : « an » et « mm » font deux
            # caractères chacun, aucune règle de forme ne les sépare.
            if (lang == "fr" and mot and not unite.get("invariable")
                    and isinstance(valeur, (int, float))
                    and not isinstance(valeur, bool) and abs(valeur) > 1):
                mot += "s"
            affiche = (f"{valeur[0]} and {valeur[1]}" if intervalle
                       and lang == "en" else
                       f"{valeur[0]} et {valeur[1]}" if intervalle else valeur)
            g.add((noeud, SKOS.prefLabel, Literal(gabarit.format(
                valeur=affiche, unite=f" {mot}" if mot else "",
                famille=familles[lang]), lang=lang)))
    return noeud


def parametres_de(carte):
    """(famille, valeur, unité) des paramètres SÉMANTIQUES d'une fiche.

    Seuls les LITTÉRAUX comptent : `lim: 20` est une contrainte, `lim:
    upLim` est une référence à une colonne amont que le loader a laissée
    en chaîne. Un identifiant Python est donc écarté.
    """
    table = ALIGNEMENTS["parameters"]
    trouves = []
    for processus in carte["processes"]:
        for entree in processus["func"]:
            for nom, valeur in (entree.get("kwargs") or {}).items():
                regle = table.get(nom)
                if regle is None:
                    continue
                if isinstance(valeur, str):
                    continue              # référence de colonne, pas un littéral
                if isinstance(valeur, bool):
                    continue
                trouves.append((regle["family"], valeur, regle.get("unit")))
    return trouves


def familles(g, meta):
    """Un concept parent par famille, et le rattachement des variables.

    Le parent n'a pas de fiche : c'est un concept sémantique, « la
    famille des VCN » existe sans qu'on la calcule jamais. Son libellé
    est GÉNÉRÉ depuis ses composants, parce qu'un parent EST ses
    composants et qu'un libellé qui les récite ne peut pas dériver.
    """
    vus = {}
    for _, ligne in meta.iterrows():
        cle = str(ligne["family"])
        noeud = CARD[f"family/{cle}"]
        if cle not in vus:
            vus[cle] = noeud
            g.add((noeud, RDF.type, SKOS.Concept))
            g.add((noeud, RDF.type, IOP.Variable))
            g.add((noeud, SKOS.inScheme, CARD[""]))
            # Les familles sont les points d'entrée du schéma : les
            # variables pendent sous elles, rien ne pend sous elles-mêmes.
            sommet(g, noeud, CARD[""])
            # Liste de composants, jamais une phrase : une phrase générée
            # se casse en français à la première question d'accord
            # (« minimum annuel » mais « moyenne annuelle »). Le séparateur
            # dit franchement qu'on énumère, ce qui est la vérité.
            for lang in ("en", "fr"):
                morceaux = [str(ligne[f"{f}_{lang}"])
                            for f in ("domain", "phenomenon", "statistic",
                                      "season", "output")
                            if str(ligne.get(f"{f}_{lang}", ""))]
                g.add((noeud, SKOS.prefLabel,
                       Literal(" · ".join(morceaux) or cle, lang=lang)))
            g.add((noeud, SKOS.editorialNote, Literal(
                "Generated parent: the variables of this family differ "
                "only by a parameter. Its label enumerates its components.",
                lang="en")))
    return vus


def unites(g):
    """Les unités que card doit définir lui-même, et rien d'autre.

    QUDT est une liste de 2 575 unités nommées : sept des nôtres y sont,
    trois n'y sont pas (`hm³` et les deux unités composées). Pour
    celles-là card définit sa propre unité, à partir du seul code UCUM,
    qui est une grammaire et les compose toutes. Même doctrine que pour
    les contraintes : on réemploie quand ça existe, on définit quand ça
    n'existe pas, on n'invente jamais une URI chez quelqu'un d'autre.

    Ces unités ne sont PAS des `skos:Concept` : une unité n'est pas une
    notion du vocabulaire de card, c'est une ressource à laquelle une
    variable renvoie.
    """
    from card.render import unite as rendu
    for texte, regle in ALIGNEMENTS["units"].items():
        if regle.get("qudt") or not regle.get("ucum"):
            continue
        noeud = CARD[f"unit/{regle['ucum']}"]
        g.add((noeud, RDF.type, QUDT.Unit))
        g.add((noeud, RDFS.label, Literal(rendu(texte))))
        g.add((noeud, QUDT.ucumCode, Literal(regle["ucum"])))
        if regle.get("kind"):
            g.add((noeud, QUDT.hasQuantityKind, uri(regle["kind"])))


def mesure(g, concept, unite_en):
    """Ce que valent les nombres d'une variable : unité, grandeur, ou type.

    Trois des douze « unités » du corpus n'en sont pas. Un jour de
    l'année est une position dans un cycle, un booléen est un type de
    valeur : les publier comme des unités serait faux, et OWL-Time comme
    XSD ont le terme juste.
    """
    regle = ALIGNEMENTS["units"].get(str(unite_en or "").strip())
    if not regle:
        return
    if regle.get("value_type"):
        g.add((concept, CARD["valueType"], uri(regle["value_type"])))
        return
    if regle.get("qudt"):
        g.add((concept, QUDT.hasUnit, uri(regle["qudt"])))
    elif regle.get("ucum"):
        g.add((concept, QUDT.hasUnit, CARD[f"unit/{regle['ucum']}"]))
    # La grandeur se DÉCLARE : une unité de QUDT en porte souvent
    # plusieurs (`M3-PER-SEC` en déclare quatre, dont « vitesse volumique
    # du son »), donc elle ne se déduit pas de l'unité.
    if regle.get("kind"):
        g.add((concept, QUDT.hasQuantityKind, uri(regle["kind"])))


def variables(g, meta, parents):
    """Un concept par variable produite, et sa ressource fiche."""
    cartes = _find_cards(_DEFAULT_CARD_DIR, None)
    par_fiche = {}
    for _, ligne in meta.iterrows():
        nom = str(ligne["variable_en"])
        concept = CARD[f"variable/{nom}"]
        g.add((concept, RDF.type, SKOS.Concept))
        g.add((concept, RDF.type, IOP.Variable))
        g.add((concept, SKOS.inScheme, CARD[""]))
        g.add((concept, SKOS.notation, Literal(nom)))
        for lang in ("en", "fr"):
            if str(ligne.get(f"name_{lang}", "")):
                # SKOS n'admet qu'un `prefLabel` par langue et par
                # concept. Or 28 variables sont produites par DEUX fiches,
                # et sept d'entre elles portent des libellés qui
                # divergent : la même variable y est décrite deux fois,
                # autrement. Le premier vu devient le terme retenu, l'autre
                # un synonyme, ce qui ne perd rien et respecte la norme.
                # L'ordre de `list_cards` est stable, donc le choix aussi.
                etiquette = Literal(ligne[f"name_{lang}"], lang=lang)
                deja = [o for o in g.objects(concept, SKOS.prefLabel)
                        if o.language == lang]
                propriete = SKOS.altLabel if deja else SKOS.prefLabel
                if etiquette not in deja:
                    g.add((concept, propriete, etiquette))
            # Vide sur 202 variables, et c'est la règle du corpus : on
            # n'invente pas de texte pour combler.
            if str(ligne.get(f"description_{lang}", "")):
                g.add((concept, SKOS.definition,
                       Literal(ligne[f"description_{lang}"], lang=lang)))
        g.add((concept, SKOS.broader, parents[str(ligne["family"])]))
        mesure(g, concept, ligne.get("unit_en"))

        # Composants I-ADOPT, depuis les entrées et la facette statistique
        for entree in str(ligne["input_vars"]).split(","):
            entree = entree.strip().rstrip("?").strip()
            regle = ALIGNEMENTS["inputs"].get(entree)
            if not regle or regle.get("parameter"):
                continue
            if regle.get("property"):
                g.add((concept, IOP.hasProperty, uri(regle["property"])))
            if regle.get("object"):
                g.add((concept, IOP.hasObjectOfInterest,
                       uri(regle["object"])))
            if regle.get("constraint"):
                g.add((concept, IOP.hasConstraint,
                       CARD[f"constraint/{regle['constraint']}"]))
        for facette, propriete in (("statistic", IOP.hasStatisticalModifier),
                                   ("domain", DCTERMS.subject),
                                   ("phenomenon", DCTERMS.subject),
                                   ("aspect", DCTERMS.subject),
                                   ("season", DCTERMS.subject),
                                   ("output", DCTERMS.subject),
                                   ("purpose", DCTERMS.subject)):
            from card.schema import _slug_of
            for brut in str(ligne.get(f"{facette}_en", "")).split(","):
                brut = brut.strip()
                cle = _slug_of(facette, brut) if brut else None
                if cle:
                    g.add((concept, propriete, CARD[f"{facette}/{cle}"]))

        # La ou LES fiches qui la définissent : le lien n'est pas un à un
        fiche = str(ligne["card"])
        g.add((concept, RDFS.isDefinedBy, CARD[f"card/{fiche}"]))
        if fiche not in par_fiche:
            par_fiche[fiche] = ligne
            noeud = CARD[f"card/{fiche}"]
            source = load_card(cartes[fiche])
            g.add((noeud, DCTERMS.title, Literal(fiche)))
            g.add((noeud, OWL.versionInfo, Literal(str(ligne["version"]))))
            if str(ligne.get("swhid", "")):
                # L'identifiant, et l'adresse où il se résout : un
                # `swh:1:cnt:…` est exact mais muet, et le fichier qu'il
                # désigne s'ouvre en un clic.
                g.add((noeud, DCTERMS.identifier, Literal(ligne["swhid"])))
                g.add((noeud, RDFS.seeAlso, URIRef(SWH + ligne["swhid"])))
            if str(ligne.get("script_path", "")):
                g.add((noeud, DCTERMS.source,
                       URIRef(DEPOT + str(ligne["script_path"]))))
            # Qui a écrit cette définition, et quand. Une fiche est de la
            # donnée : elle se cite comme telle.
            for auteur in source.get("authors") or []:
                g.add((noeud, DCTERMS.creator, Literal(auteur)))
            if source.get("date"):
                g.add((noeud, DCTERMS.created, Literal(str(source["date"]))))
            for lang in ("en", "fr"):
                if str(ligne.get(f"method_{lang}", "")):
                    g.add((noeud, CARD["method"],
                           Literal(ligne[f"method_{lang}"], lang=lang)))
            for famille, valeur, unite in parametres_de(source):
                g.add((concept, IOP.hasConstraint,
                       contrainte_valeur(g, famille, valeur, unite)))


def main():
    graphe = Graph()
    graphe.bind("card", CARD)
    graphe.bind("iop", IOP)
    graphe.bind("skos", SKOS)
    graphe.bind("dcterms", DCTERMS)
    for prefixe, url in PREFIXES.items():
        graphe.bind(prefixe, Namespace(url))

    meta = card.list_cards()
    schema(graphe, card.__version__)
    vocabulaire(graphe)
    unites(graphe)
    contraintes(graphe)
    parents = familles(graphe, meta)
    variables(graphe, meta, parents)

    SORTIE.write_text(graphe.serialize(format="turtle"), encoding="utf-8")
    concepts = len(set(graphe.subjects(RDF.type, SKOS.Concept)))
    print(f"{SORTIE} : {len(graphe)} triplets, {concepts} concepts, "
          f"{len(parents)} familles")
    print(f"base d'URI PROVISOIRE : {BASE}  (rien n'est publié)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
