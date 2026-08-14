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
from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS, SKOS, XSD

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
CPM = Namespace("http://purl.org/voc/cpm#")
TIME = Namespace("http://www.w3.org/2006/time#")
# La mise en SKOS de l'ISO 25964, publiée par la DCMI. Elle apporte le
# TABLEAU (`ThesaurusArray`, sous-classe de `skos:Collection`) et de quoi
# le placer dans l'arbre sans prétendre que c'est un concept.
ISOTHES = Namespace("http://purl.org/iso25964/skos-thes#")

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

# Les trois facettes qui font l'ARBRE, et non un axe de filtrage. Elles
# vivent dans le schéma principal, pas dans un schéma de facette : c'est
# par elles qu'on descend jusqu'aux variables (grandeur -> phénomène ->
# variable), et un navigateur n'a pas d'autre porte d'entrée. Les quatre
# autres (`aspect`, `statistic`, `season`, `output`) restent des axes
# transverses, chacun dans son schéma.
ARBRE = ("domain", "phenomenon", "purpose")


def vocabulaire(g):
    """Les facettes et leurs valeurs : un schéma par facette."""
    for facette, valeurs in card.vocabulary().items():
        noeud = (CARD[""] if facette in ARBRE
                 else sous_schema(g, facette, facette,
                                  FACETTES_FR.get(facette, facette)))
        for cle, etiquettes in valeurs.items():
            concept = CARD[f"{facette}/{cle}"]
            g.add((concept, RDF.type, SKOS.Concept))
            # Une facette `statistic` EST un modificateur statistique au
            # sens d'I-ADOPT : le dire évite que `hasStatisticalModifier`
            # pointe vers un concept dont rien n'annonce le type.
            if facette == "statistic":
                g.add((concept, RDF.type, IOP.StatisticalModifier))
            g.add((concept, SKOS.inScheme, noeud))
            # Un phénomène pend sous sa grandeur, `arbre()` s'en charge :
            # l'annoncer ici en concept de tête ferait de lui une racine ET
            # un fils, ce que skosify signale à juste titre.
            if facette != "phenomenon":
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


def parent_de(ligne):
    """Sous quel concept de l'arbre pendent les variables de cette ligne.

    Le phénomène quand il y en a un, la finalité sinon. Les deux cas sont
    exclusifs et couvrent le corpus entier : une fiche qui déclare une
    `purpose` ne déclare ni `aspect` ni phénomène, parce qu'elle ne décrit
    pas un régime mais une comparaison (performance d'un modèle,
    sensibilité au climat). Rend aussi la facette employée, dont dépend
    ce que le libellé du tableau doit encore dire.
    """
    from card.schema import _slug_of
    for facette in ("phenomenon", "purpose"):
        brut = str(ligne.get(f"{facette}_en", "")).strip()
        cle = _slug_of(facette, brut) if brut else None
        if cle:
            return facette, CARD[f"{facette}/{cle}"]
    return None, None


def arbre(g, meta):
    """La colonne vertébrale : grandeur -> phénomène, et la soudure.

    Sans elle, le vocabulaire est un buisson : les familles étaient
    autant de racines, et la page d'accueil d'un navigateur les listait
    toutes, à plat, avec des libellés qui récitent des facettes. Personne
    n'entre par là.

    **Rien n'est déclaré ici, tout est mesuré.** Le rattachement d'un
    phénomène à une grandeur se lit dans les fiches, qui déclarent les
    deux ; le vérifier vaut mieux que l'écrire une seconde fois dans
    `topics.yaml`, où il pourrait mentir. Mesuré le 2026-08-14 : chacun
    des onze phénomènes n'apparaît que sous une seule grandeur.

    La seule chose qui vienne d'`alignments.yaml` est ce qui ne se déduit
    d'aucune fiche : la note de portée, et le `skos:broadMatch` vers le
    concept générique de Theia/OZCAR.
    """
    from card.schema import _slug_of
    grandeur_de = {}
    for _, ligne in meta.iterrows():
        facette, _ = parent_de(ligne)
        if facette != "phenomenon":
            continue
        phen = _slug_of("phenomenon", str(ligne["phenomenon_en"]).strip())
        for brut in str(ligne["domain_en"]).split(","):
            cle = _slug_of("domain", brut.strip()) if brut.strip() else None
            if cle:
                grandeur_de.setdefault(phen, set()).add(cle)

    for phen, grandeurs in sorted(grandeur_de.items()):
        if len(grandeurs) > 1:
            raise SystemExit(
                f"le phénomène « {phen} » apparaît sous plusieurs grandeurs "
                f"({', '.join(sorted(grandeurs))}) : l'arbre thématique "
                "suppose qu'un phénomène en a une seule")
        g.add((CARD[f"phenomenon/{phen}"], SKOS.broader,
               CARD[f"domain/{grandeurs.pop()}"]))

    # Un phénomène du vocabulaire qu'aucune fiche n'emploie n'a pas de
    # grandeur mesurable : il reste une racine plutôt que d'être rattaché
    # au jugé. Aucun cas aujourd'hui, la garde est pour demain.
    for cle in card.vocabulary()["phenomenon"]:
        if cle not in grandeur_de:
            sommet(g, CARD[f"phenomenon/{cle}"], CARD[""])

    for cle, entree in (ALIGNEMENTS.get("topics") or {}).items():
        noeud = CARD[f"domain/{cle}"]
        # Un rayon du catalogue EST un ensemble de variables, comme une
        # famille : I-ADOPT a la classe, autant la dire.
        g.add((noeud, RDF.type, IOP.VariableSet))
        for lang in ("en", "fr"):
            if entree.get(lang):
                g.add((noeud, SKOS.scopeNote,
                       Literal(entree[lang], lang=lang)))
        if entree.get("broad_match"):
            g.add((noeud, SKOS.broadMatch, uri(entree["broad_match"])))


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
        g.add((noeud, RDF.type, CPM.Constraint))
        g.add((noeud, SKOS.inScheme, CARD["scheme/constraint"]))
        g.add((noeud, SKOS.broader, CARD[f"constraint-family/{famille}"]))
        # La VALEUR, et pas seulement le libellé qui la contient. « 10 »
        # dans « fenêtre glissante de 10 jours » n'est lisible que par un
        # humain ; `cpm:value` en fait de la donnée, et c'est le point du
        # modèle CPM sur les contraintes. Une paire borne un intervalle,
        # d'où deux valeurs et non une chaîne.
        for part in (valeur if intervalle else [valeur]):
            g.add((noeud, CPM.value, Literal(part)))
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


# ── Le libellé de nœud d'un tableau ───────────────────────────────────
#
# Deux tables ÉCRITES ET RELUES, pas une grammaire. Une règle qui
# fabriquerait la phrase depuis les étiquettes se casserait au premier
# accord (« minimum annuel » mais « moyenne annuelle ») et surtout au
# premier sens : `saisonnalité × minimum` est « la date du minimum »,
# `durée × médiane` est « la médiane d'une durée », et aucune règle ne
# devine que l'aspect gouverne dans un cas et est gouverné dans l'autre.
#
# Les combinaisons sont peu nombreuses parce que les facettes sont
# petites : 31 couples (aspect, opération) et 13 couples (fenêtre,
# forme) couvrent le corpus entier. Chacun a été confronté aux noms de
# ses membres. **Un couple absent fait ÉCHOUER la génération** : c'est
# ce qui empêche une facette ajoutée demain de produire une phrase
# muette dont personne ne verrait qu'elle ment.
#
# La clé est le SLUG, jamais l'étiquette : une reformulation de
# `topics.yaml` ne doit pas casser ces tables.

QUANTITE = {
    # (aspect, statistique) : ce que la valeur EST
    ("magnitude", "sum"): ("Total", "Cumul"),
    ("magnitude", "mean"): ("Mean", "Moyenne"),
    ("magnitude", "median"): ("Inter-annual median", "Médiane inter-annuelle"),
    ("magnitude", "minimum"): ("Minimum", "Minimum"),
    ("magnitude", "maximum"): ("Maximum", "Maximum"),
    ("magnitude", "quantile"): ("Quantile", "Quantile"),
    ("magnitude", "change"): ("Change between two periods",
                              "Écart entre deux périodes"),
    ("magnitude", "ratio"): ("Ratio", "Rapport"),
    ("magnitude", "return-period"): ("Value for a given return period",
                                     "Valeur de période de retour donnée"),
    ("magnitude", "trend-slope"): ("Trend slope", "Pente de tendance"),
    ("magnitude", "trend-significance"): ("Trend significance",
                                          "Significativité de tendance"),
    ("magnitude", "slope"): ("Slope of a curve", "Pente d'une courbe"),
    ("magnitude", "filter"): ("Component separated by filtering",
                              "Composante séparée par filtrage"),
    ("duration", "threshold-exceedance"): ("Duration beyond a threshold",
                                           "Durée au-delà d'un seuil"),
    ("duration", "quantile"): ("Duration between two quantiles",
                               "Durée entre deux quantiles"),
    ("duration", "median"): ("Inter-annual median of a duration",
                             "Médiane inter-annuelle d'une durée"),
    ("duration", "change"): ("Change in duration between two periods",
                             "Écart de durée entre deux périodes"),
    ("timing", "minimum"): ("Date of the minimum", "Date du minimum"),
    ("timing", "maximum"): ("Date of the maximum", "Date du maximum"),
    ("timing", "quantile"): ("Date a quantile is reached",
                             "Date d'atteinte d'un quantile"),
    ("timing", "threshold-exceedance"): ("Date a threshold is crossed",
                                         "Date de franchissement d'un seuil"),
    ("timing", "median"): ("Inter-annual median of a date",
                           "Médiane inter-annuelle d'une date"),
    ("timing", "change"): ("Change in date between two periods",
                           "Écart de date entre deux périodes"),
    ("frequency", "threshold-exceedance"): ("Frequency of threshold exceedance",
                                            "Fréquence de dépassement d'un seuil"),
    ("frequency", "return-period"): ("Return period of a value",
                                     "Période de retour d'une valeur"),
    ("frequency", "change"): ("Change in frequency between two periods",
                              "Écart de fréquence entre deux périodes"),
    # Sans aspect : les fiches à `purpose`, qui comparent au lieu de
    # décrire un régime. La facette `aspect` leur est interdite.
    ("", "ratio"): ("Ratio", "Rapport"),
    ("", "bias"): ("Bias", "Biais"),
    ("", "efficiency"): ("Efficiency criterion", "Critère d'efficience"),
    ("", "elasticity"): ("Elasticity", "Élasticité"),
    ("", "correlation"): ("Correlation", "Corrélation"),
}

FORME = {
    # (fenêtre, forme) : combien de valeurs, et sur quoi elles portent.
    # `annual` et `record` ne disent PAS la même chose sur un scalaire :
    # le premier réduit une série déjà annuelle, le second la chronique
    # journalière entière, et c'est ce qui sépare `median-VCN10` de `Q90`.
    ("annual", "series"): ("one value per year", "une valeur par année"),
    ("annual", "scalar"): ("a single value, from the annual series",
                           "une valeur unique, sur la série annuelle"),
    ("summer", "series"): ("one value per year, summer window",
                           "une valeur par année, fenêtre estivale"),
    ("summer", "scalar"): ("a single value, summer window",
                           "une valeur unique, fenêtre estivale"),
    ("winter", "series"): ("one value per year, winter window",
                           "une valeur par année, fenêtre hivernale"),
    ("winter", "scalar"): ("a single value, winter window",
                           "une valeur unique, fenêtre hivernale"),
    ("by-month", "series"): ("one variable per month, one value per year",
                             "une variable par mois, une valeur par année"),
    ("by-month", "scalar"): ("one variable per month, a single value",
                             "une variable par mois, une valeur unique"),
    ("by-month", "curve"): ("one variable per month, a curve",
                            "une variable par mois, une courbe"),
    ("by-season", "series"): ("one variable per season, one value per year",
                              "une variable par saison, une valeur par année"),
    ("by-season", "scalar"): ("one variable per season, a single value",
                              "une variable par saison, une valeur unique"),
    ("record", "scalar"): ("a single value, over the whole record",
                           "une valeur unique, sur la chronique entière"),
    ("record", "curve"): ("a curve, over the whole record",
                          "une courbe, sur la chronique entière"),
}


def phases_de(ligne):
    """Les contraintes portées par les grandeurs d'entrée de cette ligne.

    Rien à deviner : `alignments.yaml` déclare que `Rl` est de la
    précipitation contrainte à la phase liquide et `Rs` à la phase
    solide. Sans elles, onze tableaux portent le libellé d'un voisin,
    « cumul annuel » ne distinguant pas la pluie de la neige.
    """
    trouvees = []
    for entree in str(ligne["input_vars"]).split(","):
        regle = ALIGNEMENTS["inputs"].get(entree.strip().rstrip("?").strip())
        cle = (regle or {}).get("constraint")
        if cle and cle not in trouvees:
            trouvees.append(cle)
    return sorted(trouvees)


def libelle_tableau(ligne, avec_grandeur):
    """Le libellé de nœud d'un tableau, en anglais puis en français.

    À gauche ce que la valeur EST, monté depuis les deux tables ; à droite
    ses coordonnées, qui restent les étiquettes des facettes parce qu'en
    prose elles répétaient la même chose sur presque chaque voisine.

    `avec_grandeur` est vrai pour les tableaux rangés sous une finalité :
    leur branche ne dit nulle part de quelle grandeur il s'agit, alors que
    ceux rangés sous un phénomène l'héritent de leur superordonné.
    """
    from card.schema import _slug_of

    def slug_facette(facette):
        brut = str(ligne.get(f"{facette}_en", "")).strip()
        return _slug_of(facette, brut) if brut else ""

    couple = (slug_facette("aspect"), slug_facette("statistic"))
    fenetre = (slug_facette("season"), slug_facette("output"))
    for table, cle, quoi in ((QUANTITE, couple, "(aspect, statistique)"),
                             (FORME, fenetre, "(fenêtre, forme)")):
        if cle not in table:
            raise SystemExit(
                f"couple {quoi} sans phrase : {cle}. Ajouter l'entrée dans "
                "generate_skos.py, après avoir lu les noms de ses membres.")
    phases = phases_de(ligne)
    phrases = []
    for rang, lang in enumerate(("en", "fr")):
        coordonnees = [str(ligne[f"season_{lang}"]), str(ligne[f"output_{lang}"])]
        if avec_grandeur and str(ligne.get(f"domain_{lang}", "")):
            coordonnees.insert(0, str(ligne[f"domain_{lang}"]))
        coordonnees += [ALIGNEMENTS["constraints"][c][lang] for c in phases]
        phrases.append(f"{QUANTITE[couple][rang]} ({', '.join(coordonnees)})")
    return phrases


def tableaux(g, meta):
    """Les familles, comme des TABLEAUX de thésaurus et non des concepts.

    Une famille regroupe les variables qui ne diffèrent que par un
    paramètre : `QNA`, `VCN3`, `VCN10`, `VCN30`. C'est une construction
    classique et normalisée, le *tableau* de l'ISO 25964, avec son
    *libellé de nœud* qui dit par quel caractère on divise. L'exemple
    canonique du guide SKOS est « lait par animal d'origine », qui
    regroupe lait de vache, de chèvre et de bufflonne.

    **Un libellé de nœud n'est PAS un concept**, et c'est tout l'objet de
    ce passage. Le guide SKOS le dit : le modéliser en concept est plus
    intuitif mais fait perdre de la justesse. Personne n'indexe une
    donnée avec « Minimum (annuelle, série) », on l'indexe avec `VCN10`.
    Jusqu'au 2026-08-14 la famille était un `skos:Concept` dans la chaîne
    `skos:broader`, ce qui affirmait « VCN10 est une sorte de Minimum
    (annuelle, série) ». C'était faux : un casier n'est pas un genre.

    Maintenant, deux affirmations séparées et chacune vraie : la variable
    est plus étroite que son PHÉNOMÈNE (`skos:broader`, posé par
    `variables()`), et elle est MEMBRE d'un tableau qui subdivise ce
    phénomène (`skos:member`, ici). `broader` se transmet, `member` non,
    et c'est exactement la différence qu'on voulait.

    Deux conséquences qui valent le changement :

    - le décompte des concepts devient honnête, 133 casiers en sortant ;
    - la hiérarchie ne passe plus par du CALCULÉ. Les familles se
      recalculent à chaque génération : tant qu'elles portaient la
      chaîne, une recompilation pouvait déplacer `VCN10` dans l'arbre.

    **Un tableau d'un seul membre ne subdivise rien** et n'est donc pas
    émis. Mesuré le 2026-08-14 : 65 des 133 familles sont dans ce cas, et
    37 d'entre elles le resteront, leur variable ne portant aucun
    paramètre (`QA`, `QMNA`, `QB-LH`, les huit fiches de finalité…). Les
    28 autres sont des trous de complétude du corpus, pas du vocabulaire.
    """
    from card.schema import _slug_of

    membres = {}
    for _, ligne in meta.iterrows():
        membres.setdefault(str(ligne["family"]), {})[
            str(ligne["variable_en"])] = ligne

    for cle, lignes in membres.items():
        if len(lignes) < 2:
            continue
        ligne = next(iter(lignes.values()))
        noeud = CARD[f"array/{cle}"]
        # Sous-classe de `skos:Collection`, et Skosmos sait l'afficher en
        # subdivision (option `skosmos:arrayClass`). Le type I-ADOPT reste :
        # il dit la même chose à un autre lecteur, et c'est lui qui porte
        # les `hasApplicable…`.
        g.add((noeud, RDF.type, ISOTHES.ThesaurusArray))
        g.add((noeud, RDF.type, IOP.VariableSet))
        g.add((noeud, SKOS.inScheme, CARD[""]))
        for nom in lignes:
            g.add((noeud, SKOS.member, CARD[f"variable/{nom}"]))
        # Le concept que ce tableau subdivise. `superOrdinate` a pour
        # domaine un tableau et pour portée un concept : c'est la seule
        # façon normalisée de placer une collection dans l'arbre, puisque
        # `skos:broader` lui est interdit.
        facette, parent = parent_de(ligne)
        if parent is not None:
            g.add((noeud, ISOTHES.superOrdinate, parent))
            g.add((parent, ISOTHES.subordinateArray, noeud))
        # Ce que les membres PARTAGENT, et rien d'autre.
        cle_stat = _slug_of("statistic",
                            str(ligne.get("statistic_en", "")).strip())
        if cle_stat:
            g.add((noeud, IOP.hasApplicableStatisticalModifier,
                   CARD[f"statistic/{cle_stat}"]))
        for entree in str(ligne["input_vars"]).split(","):
            regle = ALIGNEMENTS["inputs"].get(entree.strip().rstrip("?").strip())
            if not regle or regle.get("parameter"):
                continue
            if regle.get("property"):
                g.add((noeud, IOP.hasApplicableProperty, uri(regle["property"])))
            if regle.get("object"):
                g.add((noeud, IOP.hasApplicableObjectOfInterest,
                       uri(regle["object"])))
        # Le libellé de nœud dit le caractère de division : à gauche ce que
        # la valeur EST, à droite ses coordonnées. Seule la gauche gagnait à
        # devenir une phrase ; la droite, mise en prose, répétait « une
        # valeur unique, sur la série annuelle » sur presque chaque voisine.
        #
        # Le synonyme garde la liste des facettes, qui n'est pas une redite :
        # c'est ce qu'un lecteur tape dans une recherche.
        sous_finalite = facette != "phenomenon"
        phrases = libelle_tableau(ligne, sous_finalite)
        composants = (("domain",) if sous_finalite else ()) + (
            "aspect", "statistic", "season", "output")
        for rang, lang in enumerate(("en", "fr")):
            g.add((noeud, SKOS.prefLabel, Literal(phrases[rang], lang=lang)))
            morceaux = [str(ligne[f"{f}_{lang}"]) for f in composants
                        if str(ligne.get(f"{f}_{lang}", ""))]
            g.add((noeud, SKOS.altLabel,
                   Literal(" · ".join(morceaux) or cle, lang=lang)))
        g.add((noeud, SKOS.editorialNote, Literal(
            "Thesaurus array (ISO 25964): its members differ only by a "
            "parameter. A node label is not a concept, so it carries no "
            "skos:broader; the members are narrower than the phenomenon.",
            lang="en")))


def fenetre(process):
    """La période d'agrégation d'un process : (clé, début, fin, durée).

    La durée est en mois, sauf pour le jour. `None` quand le process
    n'agrège sur aucune fenêtre.

    Une fenêtre n'est PAS « une année ou pas » : c'est un DÉBUT et une
    DURÉE, et c'est ce qui permet de traiter du même geste l'année
    hydrologique, l'année civile et les fenêtres partielles d'étiage, qui
    durent six ou sept mois. Le corpus n'en compte que six.
    """
    sp, pas = process["sampling_period"], process["time_step"]
    if isinstance(sp, dict):            # {type: adaptive, func: …}
        return ("adaptive-year", None, None, 12)
    if isinstance(sp, (list, tuple)):
        debut, fin = str(sp[0]), str(sp[1])
        mois = (int(fin[:2]) - int(debut[:2])) % 12 + 1
        return (f"from-{debut}-to-{fin}", debut, fin, mois)
    if pas == "year":
        # Sans fenêtre déclarée, l'agrégation annuelle part du 1er janvier.
        debut = str(sp) if sp else "01-01"
        return (f"year-from-{debut}", debut, None, 12)
    if pas in ("year-month", "month"):
        return ("1-month", None, None, 1)
    if pas in ("year-season", "season"):
        return ("1-season", None, None, 3)
    if pas in ("yearday", "day"):
        return ("1-day", None, None, None)
    return None


_DUREES = {"1-month": ("1 month", "1 mois"),
           "1-season": ("1 season", "1 saison"),
           "1-day": ("1 day", "1 jour"),
           "adaptive-year": ("adaptive year, specific to each series",
                             "année adaptative, propre à chaque série")}


def periode(g, cle, debut, fin, mois):
    """Un concept de période, posé une fois, rendu à qui le demande.

    OWL-Time a exactement les deux pièces qu'il faut, dont un
    `DateTimeDescription` qui accepte un mois et un jour SANS année :
    c'est précisément ce qu'est une fenêtre qui revient chaque année.
    """
    from card.render import _jour
    noeud = CARD[f"period/{cle}"]
    if (noeud, RDF.type, SKOS.Concept) in g:
        return noeud
    g.add((noeud, RDF.type, SKOS.Concept))
    g.add((noeud, RDF.type, TIME.ProperInterval))
    g.add((noeud, SKOS.inScheme, CARD["scheme/period"]))
    sommet(g, noeud, CARD["scheme/period"])
    if cle in _DUREES:
        for lang, texte in zip(("en", "fr"), _DUREES[cle]):
            g.add((noeud, SKOS.prefLabel, Literal(texte, lang=lang)))
    elif fin:
        for lang in ("en", "fr"):
            g.add((noeud, SKOS.prefLabel, Literal(
                f"{_jour(debut, lang)} {'to' if lang == 'en' else 'au'} "
                f"{_jour(fin, lang)}", lang=lang)))
    else:
        for lang, mot in (("en", "year from"), ("fr", "année à partir du")):
            g.add((noeud, SKOS.prefLabel,
                   Literal(f"{mot} {_jour(debut, lang)}", lang=lang)))

    for propriete, date in ((TIME.hasBeginning, debut), (TIME.hasEnd, fin)):
        if not date:
            continue
        instant, description = BNode(), BNode()
        g.add((noeud, propriete, instant))
        g.add((instant, TIME.inDateTime, description))
        g.add((description, RDF.type, TIME.DateTimeDescription))
        g.add((description, TIME.month,
               Literal(f"--{date[:2]}", datatype=XSD.gMonth)))
        g.add((description, TIME.day,
               Literal(f"---{date[3:]}", datatype=XSD.gDay)))
    duree = BNode()
    g.add((noeud, TIME.hasDurationDescription, duree))
    g.add((duree, RDF.type, TIME.DurationDescription))
    if mois:
        g.add((duree, TIME.months, Literal(mois, datatype=XSD.decimal)))
    else:
        g.add((duree, TIME.days, Literal(1, datatype=XSD.decimal)))
    return noeud


def mesure_statistique(g, statistique, periode_noeud, climatologique):
    """La statistique ET sa fenêtre, en un concept, comme le fait CPM.

    Le modèle vient des lignes directrices INSPIRE : une mesure
    statistique est « une fonction sur un temps ou un espace », et elle
    porte donc sa période. Theia s'en sert de la même façon, avec des
    concepts comme « 1 day minimum ».

    Les mesures sont MUTUALISÉES : « minimum sur l'année hydrologique »
    est la même mesure pour les vingt variables qui l'emploient.
    """
    cle = f"{statistique}.{str(periode_noeud).rsplit('/', 1)[-1]}"
    noeud = CARD[f"measure/{cle}"]
    if (noeud, RDF.type, SKOS.Concept) in g:
        return noeud
    g.add((noeud, RDF.type, SKOS.Concept))
    g.add((noeud, RDF.type, CPM.StatisticalMeasure))
    g.add((noeud, SKOS.inScheme, CARD["scheme/statistic"]))
    g.add((noeud, SKOS.broader, CARD[f"statistic/{statistique}"]))
    g.add((noeud, CPM.aggregationTimePeriod, periode_noeud))
    for lang in ("en", "fr"):
        stat = next((o for o in g.objects(CARD[f"statistic/{statistique}"],
                                          SKOS.prefLabel) if o.language == lang),
                    Literal(statistique))
        fen = next((o for o in g.objects(periode_noeud, SKOS.prefLabel)
                    if o.language == lang), Literal(""))
        g.add((noeud, SKOS.prefLabel, Literal(f"{stat} · {fen}", lang=lang)))
    if climatologique:
        # CF nomme ce cas : une statistique calculée « over years », par
        # exemple une valeur par jour calendaire sur toute la chronique.
        for lang, texte in (
                ("en", "Computed over all years of the record "
                       "(CF: climatological statistic)."),
                ("fr", "Calculée sur toutes les années de la chronique "
                       "(CF : statistique climatologique).")):
            g.add((noeud, SKOS.editorialNote, Literal(texte, lang=lang)))
    return noeud


def agregation(fiche, colonne):
    """La période d'agrégation d'une colonne publiée, ou None.

    On prend le DERNIER process qui produit la colonne, et on ne retient
    que s'il AGRÈGE vraiment. `method.aggregates` sait faire la
    différence, et elle n'est pas cosmétique : `dtFlood` P3 résume une
    année de lignes en une valeur, `RAl_ratio` P2 divise deux séries déjà
    annuelles, et les deux portent `time_step: year`.
    """
    from card import method
    etats = method.grains(fiche)
    for i in range(len(fiche["processes"]) - 1, -1, -1):
        p = fiche["processes"][i]
        for col, entree in method.columns_and_entries(p):
            if col != colonne:
                continue
            if not method.aggregates(p, entree, etats[i]):
                return None
            # `month`, `season` et `yearday` rangent la chronique ENTIÈRE
            # par mois, saison ou jour calendaire : l'agrégation porte
            # aussi sur les années, ce que CF appelle une statistique
            # climatologique.
            return fenetre(p), p["time_step"] in ("month", "season", "yearday")
    return None


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


def entrees(g):
    """Un concept par grandeur d'entrée : ce dont tout le reste dérive.

    Le registre `inputs.yaml` les décrit depuis toujours, dans les deux
    langues et avec leur unité, et le thésaurus n'en disait rien : les
    variables pointaient directement chez Theia, si bien qu'aucun endroit
    ne portait ce que card entend par `Q`. C'est aussi le seul endroit
    où l'alignement vers un `standard_name` CF a un sens : `VCN10` n'est
    pas un débit, c'est une statistique d'un débit.

    Les paramètres de période (`ref_start`, `horizon_end`…) sont exclus :
    ce sont des dates fournies par l'appelant, pas des grandeurs.
    """
    from card.schema import input_registry
    schema_ = sous_schema(g, "input", "input quantity", "grandeur d'entrée")
    for symbole, decrit in input_registry().items():
        if decrit.get("type") == "date":
            continue
        noeud = CARD[f"input/{symbole}"]
        g.add((noeud, RDF.type, SKOS.Concept))
        g.add((noeud, RDF.type, IOP.Variable))
        g.add((noeud, SKOS.inScheme, schema_))
        sommet(g, noeud, schema_)
        g.add((noeud, SKOS.notation, Literal(symbole)))
        for lang in ("en", "fr"):
            if decrit.get(lang):
                g.add((noeud, SKOS.prefLabel, Literal(decrit[lang], lang=lang)))
        mesure(g, noeud, decrit.get("unit"))
        notation_officielle(g, noeud, symbole, "inputs")
        regle = ALIGNEMENTS["inputs"].get(symbole) or {}
        for champ, propriete in (("property", IOP.hasProperty),
                                 ("object", IOP.hasObjectOfInterest),
                                 ("same_as", SKOS.exactMatch),
                                 # CF nomme la GRANDEUR, pas la définition
                                 # de card : proche, pas identique.
                                 ("cf", SKOS.closeMatch)):
            if regle.get(champ):
                g.add((noeud, propriete, uri(regle[champ])))


def type_de_registre(nom):
    """L'URI du système de notation d'un registre, déduite de son nom.

    Rien à tenir à jour : ajouter un registre dans `alignments.yaml`
    suffit à ce qu'il sorte, avec son type et sa déclaration.
    """
    return CARD[f"notation/{nom.replace('_', '-')}"]


def codes_officiels(registre, section, cle):
    """Les codes d'un concept dans un registre, toujours en liste.

    Une entrée s'écrit indifféremment `Q: QmJ` ou `Q: [QJ, QmJ]`, parce
    que les deux registres n'ont pas la même pratique : le Sandre donne
    un code par grandeur, la grammaire du SCHAPI en donne plusieurs et
    déclare elle-même les raccourcis.
    """
    valeur = (registre.get(section) or {}).get(cle)
    if not valeur:
        return []
    return valeur if isinstance(valeur, list) else [valeur]


def notation_officielle(g, concept, cle, section):
    """Les notations officielles françaises, quand elles sont certaines.

    Une notation SKOS est un code dans un système de notation, et le
    système se dit par le TYPE du littéral : c'est la mécanique prévue
    pour qu'un même concept porte plusieurs codes sans qu'on les
    confonde. La notation propre à card reste un littéral nu, qui est la
    lecture par défaut du vocabulaire ; celles-ci s'annoncent.

    Deux registres coexistent en France, cf. `alignments.yaml`, et une
    variable peut porter plusieurs codes dans le même : ce sont leurs
    propres équivalences, pas les nôtres.

    **Un piège à connaître** : `QJ` désigne chez eux la chronique des
    débits moyens journaliers, et chez card le régime journalier
    inter-annuel. Même symbole, deux choses. C'est la raison pour
    laquelle ces tables sont écrites à la main et ne contiennent que ce
    que leur documentation et leur interface donnent.
    """
    for nom, registre in ALIGNEMENTS["notations"].items():
        type_ = type_de_registre(nom)
        for code in codes_officiels(registre, section, cle):
            g.add((concept, SKOS.notation, Literal(code, datatype=type_)))


def type_de_notation(g):
    """Déclare les systèmes de notation, sans quoi les types ne disent rien."""
    for nom, registre in ALIGNEMENTS["notations"].items():
        type_ = type_de_registre(nom)
        g.add((type_, RDF.type, RDFS.Datatype))
        source = registre["source"]
        for lang in ("en", "fr"):
            g.add((type_, RDFS.label, Literal(source[lang], lang=lang)))
        for lien in [source["url"]] + list(source.get("documents") or []):
            g.add((type_, RDFS.seeAlso, URIRef(lien)))


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


def variables(g, meta):
    """Un concept par variable produite, et sa ressource fiche."""
    cartes = _find_cards(_DEFAULT_CARD_DIR, None)
    par_fiche = {}
    chargees = {}
    for _, ligne in meta.iterrows():
        nom = str(ligne["variable_en"])
        fiche_source = chargees.setdefault(
            str(ligne["card"]), load_card(cartes[str(ligne["card"])]))
        concept = CARD[f"variable/{nom}"]
        g.add((concept, RDF.type, SKOS.Concept))
        g.add((concept, RDF.type, IOP.Variable))
        g.add((concept, SKOS.inScheme, CARD[""]))
        g.add((concept, SKOS.notation, Literal(nom)))
        notation_officielle(g, concept, nom, "variables")
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
        # La variable pend sous son PHÉNOMÈNE, en direct. Elle passait
        # avant par sa famille, ce qui affirmait qu'elle était une sorte de
        # casier de rangement (cf. `tableaux`). Le regroupement, lui, se dit
        # par `skos:member` et ne se transmet pas.
        _, parent = parent_de(ligne)
        if parent is None:
            sommet(g, concept, CARD[""])
        else:
            g.add((concept, SKOS.broader, parent))
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
        # La statistique ET sa fenêtre, quand l'étape terminale agrège
        # vraiment. Le modificateur seul dit « un minimum » ; la mesure
        # dit « un minimum sur l'année hydrologique », ce qui est la
        # variable.
        from card.schema import _slug_of as _slug_facette
        stat = _slug_facette("statistic",
                             str(ligne.get("statistic_en", "")).strip())
        agr = agregation(fiche_source, nom)
        if stat and agr and agr[0]:
            (cle_p, debut, fin, mois), climato = agr
            g.add((concept, CPM.statisticalMeasure, mesure_statistique(
                g, stat, periode(g, cle_p, debut, fin, mois), climato)))

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
            for auteur in fiche_source.get("authors") or []:
                g.add((noeud, DCTERMS.creator, Literal(auteur)))
            if fiche_source.get("date"):
                g.add((noeud, DCTERMS.created,
                       Literal(str(fiche_source["date"]))))
            for lang in ("en", "fr"):
                if str(ligne.get(f"method_{lang}", "")):
                    g.add((noeud, CARD["method"],
                           Literal(ligne[f"method_{lang}"], lang=lang)))
            for famille, valeur, unite in parametres_de(fiche_source):
                g.add((concept, IOP.hasConstraint,
                       contrainte_valeur(g, famille, valeur, unite)))


def main():
    graphe = Graph()
    graphe.bind("card", CARD)
    graphe.bind("iop", IOP)
    graphe.bind("skos", SKOS)
    graphe.bind("dcterms", DCTERMS)
    graphe.bind("isothes", ISOTHES)
    for prefixe, url in PREFIXES.items():
        graphe.bind(prefixe, Namespace(url))

    meta = card.list_cards()
    schema(graphe, card.__version__)
    vocabulaire(graphe)
    arbre(graphe, meta)
    sous_schema(graphe, "period", "aggregation period", "période d'agrégation")
    unites(graphe)
    type_de_notation(graphe)
    entrees(graphe)
    contraintes(graphe)
    tableaux(graphe, meta)
    variables(graphe, meta)

    SORTIE.write_text(graphe.serialize(format="turtle"), encoding="utf-8")
    concepts = len(set(graphe.subjects(RDF.type, SKOS.Concept)))
    arrays = len(set(graphe.subjects(RDF.type, ISOTHES.ThesaurusArray)))
    print(f"{SORTIE} : {len(graphe)} triplets, {concepts} concepts, "
          f"{arrays} tableaux")
    print(f"base d'URI PROVISOIRE : {BASE}  (rien n'est publié)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
