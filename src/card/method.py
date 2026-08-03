# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Le `method` d'une fiche : une phrase par colonne produite.

`method` dit, en langage humain, ce que fait CETTE fiche à chaque étape.
Il est indexé par process (`P1`, `P2`, …) puis par colonne produite, si
bien qu'un afficheur peut demander « la phrase de P4 pour startLF » au
lieu de se rabattre sur la docstring d'une fonction, qui ne peut parler
que du général. Conception : docs/dev/PLAN_METHOD.md.

**Ce qu'est une colonne produite.** Elle se lit dans le `process`, sans
données : c'est la clé de `func`, suffixée par saison ou par mois quand
le process porte `compress`. C'est `compress` qui décide, pas le pas de
temps : la même fiche sans lui rend une colonne et une ligne par saison
(format long), avec lui rend une colonne par saison. Vérifié par
extraction réelle le 2026-08-03.

**Pourquoi la colonne et pas la clé de `func`.** Parce que `QSA` n'est
pas une colonne : la sortie s'appelle `QSA_DJF`, `QSA_MAM`, … et porte
une ligne de méta par saison. Indexer par `QSA` mettrait un texte dans
la fiche pour quatre colonnes, et laisserait le code fabriquer les trois
autres. La fiche est dimensionnée comme sa sortie.

**Ce que ce module s'autorise.** Coller bout à bout des phrases toutes
écrites dans la fiche, avec leur numéro d'étape, pour remplir la case
`method_fr` d'une ligne de méta. Rien d'autre. Déduire une phrase d'un
paramètre du process serait fabriquer du texte que la fiche doit porter
elle-même, et détruirait au passage le seul contrôle qui existe sur elle :
une phrase écrite peut contredire le code, donc révéler un bug, là où une
phrase générée est d'accord avec lui par construction.

Les formes héritées (une chaîne numérotée, ou une liste de chaînes, une
par sortie) restent publiées telles quelles le temps que le corpus migre
fiche par fiche. Elles disparaîtront avec la dernière fiche non migrée.
"""

import re

# Suffixes mensuels de stase, dans l'ordre du calendrier.
MOIS = ("jan", "feb", "mar", "apr", "may", "jun",
        "jul", "aug", "sep", "oct", "nov", "dec")

_SAISONNIER = ("season", "year-season")
_MENSUEL = ("month", "year-month")


def _fanout(process):
    """Suffixes que `compress` ajoute aux colonnes, ou () s'il n'ajoute rien."""
    if not process["compress"]:
        return ()
    if process["time_step"] in _SAISONNIER:
        return tuple(process["seasons"])
    if process["time_step"] in _MENSUEL:
        return MOIS
    return ()


def columns_and_entries(process):
    """(colonne produite, entrée `func` qui la produit), dans l'ordre.

    Le lien entre une colonne et son entrée est ce qui permet de remonter
    la chaîne : l'entrée déclare ses colonnes d'ENTRÉE, donc de quoi la
    colonne est faite, donc quelle phrase du process amont la concerne.
    """
    suffixes = _fanout(process) or (None,)
    return [(e["name"] if s is None else f"{e['name']}_{s}", e)
            for e in process["func"] for s in suffixes]


def produced_columns(process):
    """Colonnes que ce process produit, dans l'ordre de la sortie.

    Sans `compress`, ce sont les clés de `func` telles quelles. Avec, et
    seulement si le pas de temps porte une saison ou un mois, chaque clé
    se démultiplie : `QSA` donne `QSA_DJF`, `QSA_MAM`, … On énumère par
    fonction puis par saison, ce qui garde ensemble les colonnes d'une
    même fonction. Vérifié sur le corpus le 2026-08-03 : cet ordre
    reproduit exactement `meta.en.variable` sur les 226 fiches, donc la
    publication et le linter parlent de la même liste.

    `compress` avec un pas de temps sans saison ni mois (le P5 de
    median-allLF) ne démultiplie rien : il n'y a pas de dimension à
    aplatir.
    """
    return [colonne for colonne, _ in columns_and_entries(process)]


def output_columns(card):
    """Colonnes de sortie de la fiche : celles du dernier process.

    Mesuré sur le corpus le 2026-08-03 : elles coïncident exactement avec
    `meta.en.variable`, ordre compris, sur les 226 fiches.
    """
    return produced_columns(card["processes"][-1])


def _entrees(entree):
    """Colonnes dont part une entrée `func`, positionnelles et kwargs."""
    cols = list(entree["cols"])
    cols += [v for v in entree["kwargs"].values() if isinstance(v, str)]
    return cols


def grains(card):
    """Grain temporel connu AVANT chaque process, dans l'ordre.

    Une colonne d'entrée est journalière. Une colonne produite porte le
    pas de temps de son process, SAUF si le process garde toutes les
    lignes (`keep: all`) : la valeur est alors rediffusée sur la grille
    d'entrée, et la colonne reste au grain de ses entrées.

    Cette exception n'est pas un détail : c'est elle qui distingue
    `dtFlood` P3, qui réduit vraiment une année de lignes à une valeur,
    de `RAl_ratio` P2, qui divise deux séries déjà annuelles. Les deux
    ont `time_step: year`, et seul le premier agrège. Sans cette
    distinction, la moitié gauche de l'un des deux paraîtrait fausse.
    """
    connus = {v.strip().rstrip("? ").strip(): "day"
              for v in str(card["meta"]["global"].get("input_vars", "")).split(",")}
    etats = []
    for p in card["processes"]:
        etats.append(dict(connus))
        sortant = {}
        for colonne, entree in columns_and_entries(p):
            amont = {connus.get(c) for c in _entrees(entree)} - {None}
            rediffuse = p["keep"] == "all" and len(amont) == 1
            sortant[colonne] = amont.pop() if rediffuse else p["time_step"]
        connus.update(sortant)
    return etats


def aggregates(process, entree, connus):
    """Ce process change-t-il le grain de cette colonne ?

    Faux quand toutes ses entrées sont déjà au pas de temps qu'il
    déclare : l'étape opère alors sans rien agréger.
    """
    amont = {connus.get(c) for c in _entrees(entree)} - {None}
    return not (len(amont) == 1 and amont.pop() == process["time_step"])


def known_names(card):
    """Tous les identifiants qu'une phrase de la fiche peut citer.

    Colonnes d'entrée, colonnes produites, clés de `func`, colonnes
    référencées en argument, variables de sortie. Sert à distinguer un
    NOMBRE d'un chiffre pris dans un nom : le « 10 » de `VC10` n'est pas
    une durée, et le lire comme telle ferait rougir un contrôle pour
    deux cents phrases justes.
    """
    noms = {v.strip().rstrip("? ").strip()
            for v in str(card["meta"]["global"].get("input_vars", "")).split(",")}
    for p in card["processes"]:
        noms |= set(produced_columns(p))
        for entree in p["func"]:
            noms.add(entree["name"])
            noms |= set(_entrees(entree))
    variable = card["meta"]["en"].get("variable")
    noms |= set(variable if isinstance(variable, list) else [variable])
    return {n for n in noms if n}


def _joint(textes):
    """Plusieurs colonnes d'un même process, en une étape lisible.

    Les doublons partent d'abord : une même phrase posée sur plusieurs
    colonnes est la règle, pas l'exception, et `RAT_ET0` P1 produit deux
    colonnes d'une seule opération. Reste le cas de deux gestes distincts
    à la même maille, `epsilon_R_season` calculant un débit moyen et des
    précipitations moyennes sur la même fenêtre : la maille s'écrit une
    fois et les deux gestes se suivent, plutôt que de republier la
    fenêtre deux fois dans la même ligne.
    """
    textes = list(dict.fromkeys(textes))
    if len(textes) < 2:
        return textes[0] if textes else ""
    gauches = {t.split(" - ", 1)[0] for t in textes if " - " in t}
    if len(gauches) == 1 and all(" - " in t for t in textes):
        gauche = gauches.pop()
        return f"{gauche} - " + " ; ".join(t.split(" - ", 1)[1] for t in textes)
    return " ; ".join(textes)


def _steps_for(card, table, colonne):
    """Les phrases de la chaîne qui aboutit à `colonne`, une par process.

    On remonte la chaîne, du dernier process au premier, en gardant les
    colonnes dont dépend la sortie demandée. C'est nécessaire dès qu'un
    process amont produit plusieurs colonnes : `delta-allLF_H` calcule
    cinq dates en P4 et cinq changements en P5, et la méthode de
    `delta-startLF` ne doit citer que `startLF`, pas les cinq. Prendre
    « les colonnes produites ici » aurait recollé les cinq phrases.

    Les liens sont ceux que la fiche DÉCLARE : une entrée `func` dit de
    quelles colonnes elle part, en positionnel comme en kwarg. Rien n'est
    deviné, et un process qui ne touche aucune colonne d'intérêt (cas non
    rencontré dans le corpus) rend tout ce qu'il a plutôt que rien.

    Les doublons sont écartés en chemin, et ce n'est pas cosmétique : une
    même phrase posée sur plusieurs colonnes est la règle, pas
    l'exception, et `RAT_ET0` P1 produit deux colonnes d'une seule
    opération.
    """
    interet = {colonne}
    lignes = []
    for p in reversed(card["processes"]):
        entrees = table.get(p["name"])
        paires = columns_and_entries(p)
        vises = [(c, e) for c, e in paires if c in interet] or paires

        if isinstance(entrees, str):       # phrase valant pour tout le process
            textes = [entrees]
        else:
            entrees = entrees or {}
            textes = [str(entrees[c]) for c, _ in vises if c in entrees]
        lignes.append(_joint(textes))

        amont = set()
        for _, e in vises:
            amont |= set(e["cols"])
            amont |= {v for v in e["kwargs"].values() if isinstance(v, str)}
        interet = amont or interet
    return list(reversed(lignes))


def step_text(card, lang, process, func_name):
    """Ce que la fiche dit de CETTE étape, pour un dessin.

    Seule la moitié droite est rendue : une figure dessine déjà
    l'agrégation, sa ligne de grain et sa bande de douze mois, et
    réafficher « agrégation annuelle » y serait la redite que la charte
    de rédaction interdit.

    La présentation finale, `… (VC10)`, tombe : elle existe pour que la
    chaîne PUBLIÉE se lise sans les clés, alors qu'une figure dessine le
    nœud produit juste en dessous. La dire deux fois à trois lignes
    d'intervalle n'apprend rien.

    Un nœud de figure porte le nom d'une entrée `func`, qui peut couvrir
    plusieurs colonnes quand le process est `compress` : les textes
    distincts se suivent, les identiques ne comptent qu'une fois.
    """
    table = card["meta"][lang].get("method")
    if not isinstance(table, dict):
        return ""
    entrees = table.get(process["name"])
    if isinstance(entrees, str):
        return entrees.split(" - ", 1)[-1].strip()
    if not isinstance(entrees, dict):
        return ""
    textes = []
    for colonne, entree in columns_and_entries(process):
        if entree["name"] != func_name or colonne not in entrees:
            continue
        texte = str(entrees[colonne]).split(" - ", 1)[-1].strip()
        textes.append(re.sub(rf"\s*\({re.escape(colonne)}\)$", "", texte))
    return " ; ".join(dict.fromkeys(t for t in textes if t))


def published(card, lang):
    """Valeur publiée de `method`, une chaîne par colonne de sortie.

    C'est la forme que consomment `card.extract` et `card.info` : les
    étapes numérotées, séparées par des retours à la ligne, telles
    qu'elles se lisent depuis toujours. Seule la fiche change de forme,
    pas sa sortie.
    """
    meta_lang = card["meta"][lang]
    table = meta_lang.get("method")
    sorties = output_columns(card)

    if not isinstance(table, dict):
        # Formes héritées : publiées telles quelles. Une chaîne unique
        # vaut pour toutes les sorties, une liste en donne une par
        # sortie, quitte à répéter la dernière si elle est plus courte.
        if isinstance(table, list):
            return [table[min(i, len(table) - 1)] for i in range(len(sorties))]
        return [table if table is not None else ""] * len(sorties)

    return ["\n".join(f"{i}. {texte}" for i, texte
                      in enumerate(_steps_for(card, table, col), start=1))
            for col in sorties]
