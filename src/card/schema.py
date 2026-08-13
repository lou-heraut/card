# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
# *2 INRAE, UMR G-Eau, Montpellier, France
# *3 IRSTEA, France
#
# This file is part of the card Python package (Python port of the
# CARD R package).
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.
#
# card is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.

"""Validation structurelle des fiches CARD YAML (linter, sans dépendance).

Usage :
    from card.schema import validate_card, lint_cards
    issues = validate_card("QA.yaml")          # liste de problèmes (vide = ok)
    report = lint_cards()                       # {fiche: [issues]} sur le corpus

    python -m card.schema                       # linter en ligne de commande

Contrôles :
- structure (id, meta en/fr/global, process P1..Pn consécutifs) ;
- tuples func bien formés et fonctions résolubles (card.functions/numpy) ;
- champs process valides (time_step, keep, max_na_pct, sampling_period) ;
- cohérence des longueurs des listes meta (variable/name/...) ;
- cohérence fenêtre meta ↔ process : une fenêtre partielle déclarée en
  meta doit se retrouver dans un sampling_period de process (le contrôle
  qui aurait détecté la perte de borne de fin sur 29 fiches) ;
- classification (docs/dev/TOPICS.md) : présence des facettes requises,
  valeurs au vocabulaire (topics.yaml), appariement en/fr, aspect
  interdit quand purpose est présent.
"""

import copy
import datetime as _dt
import re
from pathlib import Path

import yaml

from . import method as _method
from . import suffix as _sfx
from .extraction import _DEFAULT_CARD_DIR, resolve
from .loader import load_card

_VOCAB_PATH = Path(__file__).parent / "topics.yaml"
_VOCAB = None
_INPUTS_PATH = Path(__file__).parent / "inputs.yaml"
_INPUTS = None


def _vocab():
    global _VOCAB
    if _VOCAB is None:
        _VOCAB = yaml.safe_load(_VOCAB_PATH.read_text(encoding="utf-8"))
    return _VOCAB


def vocabulary():
    """Controlled vocabulary of the classification.

    Returns
    -------
    dict
        `{facet: {slug: {"en": label, "fr": label, ...}}}`. This is
        the closed list of values a `classification` block may take,
        and therefore also the list of valid filters for
        `card.list_cards`.

    Notes
    -----
    The key is a neutral slug: the identifier of the concept, stable
    when a label is reworded, usable as a directory name and one day as
    a URI. `en` and `fr` are two labels of equal standing, neither
    language being the identifier.

    Public so that a client, a web service or a form, can offer the
    right values instead of guessing them.
    """
    return copy.deepcopy(_vocab())


def _slug_of(facette, etiquette):
    """Slug déclaré d'une étiquette (quelle que soit sa langue), ou None.

    Le slug n'est plus dérivé du libellé anglais : il est déclaré dans
    topics.yaml, donc un libellé peut être reformulé sans déplacer les
    dossiers ni changer l'identité du concept.
    """
    for slug, entry in _vocab().get(facette, {}).items():
        if etiquette in (slug, entry.get("en"), entry.get("fr")):
            return slug
    return None


def input_registry():
    """Registre {variable d'entrée: {unit, en, fr}} (inputs.yaml)."""
    global _INPUTS
    if _INPUTS is None:
        _INPUTS = yaml.safe_load(_INPUTS_PATH.read_text(encoding="utf-8"))
    return _INPUTS


def _check_inputs(card, issues):
    raw = card["meta"]["global"].get("input_vars", "X")
    for var in str(raw).split(","):
        var = var.strip().rstrip("?").strip()      # `?` = entrée facultative
        if var and var != "X" and var not in input_registry():
            issues.append(
                f"input_vars: '{var}' absent du registre des entrées "
                "(src/card/inputs.yaml)"
            )

_VALID_TIME_STEPS = {"year", "year-month", "month", "year-season",
                     "season", "yearday", "none"}
_MMDD = re.compile(r"^\d{2}-\d{2}$")


def _parse_mmdd(s):
    if not isinstance(s, str) or not _MMDD.match(s):
        return None
    m, d = int(s[:2]), int(s[3:])
    try:
        return _dt.date(2001, m, d)      # année non bissextile de référence
    except ValueError:
        return None


def _is_full_year_window(start, end):
    """[start, end] couvre-t-il toute l'année (end = veille de start) ?"""
    ds, de = _parse_mmdd(start), _parse_mmdd(end)
    if ds is None or de is None:
        return None                       # non analysable (ex. 02-28(29))
    return de == ds - _dt.timedelta(days=1) or (ds, de) == (
        _dt.date(2001, 1, 1), _dt.date(2001, 12, 31))


def _check_meta_lists(meta_lang, prefix, issues):
    variable = meta_lang.get("variable")
    if variable is None:
        issues.append(f"{prefix}: champ 'variable' manquant")
        return
    if isinstance(variable, list):
        n = len(variable)
        for field in ("name", "description", "method", "sampling_period"):
            v = meta_lang.get(field)
            if isinstance(v, list) and not (
                    v and isinstance(v[0], str) and len(v) == 2
                    and field == "sampling_period"):
                if len(v) not in (n, 2):
                    issues.append(
                        f"{prefix}.{field}: liste de longueur {len(v)} "
                        f"pour {n} variables"
                    )
        return

    # Variable unique : une métadonnée en liste ne peut pas être publiée
    # en entier, seul son premier élément le serait. C'est ce qui a fait
    # annoncer « l'horizon proche » à 14 fiches d'horizon quel que soit
    # l'horizon calculé, après leur passage à une sortie unique
    # (2026-07-22). Un choix entre plusieurs libellés se fait par
    # placeholder {suffix.X}, pas par liste.
    for field in ("name", "description", "method"):
        v = meta_lang.get(field)
        if isinstance(v, list):
            issues.append(
                f"{prefix}.{field}: liste de {len(v)} éléments pour une "
                f"variable unique ; seul le premier serait publié"
            )


# Ce que chaque unité du corpus autorise comme expression relative.
# `relative` d'une fiche est un RACCOURCI : la variable annonce ce qu'elle
# permet, pour que `stase`, une figure ou l'API n'aient pas à raisonner
# sur l'unité. Cette table ne remplace pas le champ, elle le VÉRIFIE.
#
#   True  : la grandeur admet une expression relative. Zéro vrai, et
#           valeur dépendant de la taille du bassin, donc seul le
#           pourcentage permet de comparer le Rhône et un ruisseau.
#   False : soit le zéro est conventionnel (une date part du 1er janvier,
#           un °C du point de fusion), soit la grandeur est déjà
#           comparable telle quelle (une lame d'eau en mm est divisée par
#           la surface, une durée en jours ne dépend pas du bassin), soit
#           elle est déjà sans dimension ou déjà relative.
#           TOUT CE QUI SE MESURE EN TEMPS est ici : jour, date, durée,
#           nombre d'années, période de retour.
#   None  : la question ne se pose pas, ce n'est pas une grandeur mesurée
#           (le verdict d'un test de Mann-Kendall, un test de robustesse).
_UNITE_RELATIVE = {
    "m^{3}.s^{-1}":           True,
    "m^{3}.s^{-1}.year^{-1}": True,
    "m^{3}.s^{-1}.mm^{-1}":   True,
    "hm^{3}":                 True,
    "%":                      True,   # un écart en % suppose une base
                                      # extensive : c'est elle qu'on décrit
    "mm":                     False,
    "day":                    False,
    "yearday":                False,
    "year":                   False,
    "°C":                     False,
    "without unit":           False,
    "bool":                   None,
}


def _check_relative(card, path, prefix, issues):
    """`relative` est écrit, et il s'accorde avec l'unité.

    Le champ est un raccourci à destination des consommateurs, donc il ne
    vaut que si on peut lui faire confiance sans le vérifier. Deux règles
    l'assurent.

    **Il est ÉCRIT**, `true` compris, comme `time_step`. On omet un défaut
    qui veut dire « rien de particulier » ; on écrit un défaut qui est un
    CHOIX. Avant le 2026-08-13, `true` n'existait que comme défaut et
    n'était écrit nulle part : « j'ai décidé que oui » et « personne n'a
    rien écrit » étaient indiscernables, ce qui est le pire défaut
    possible pour un champ dont tout l'intérêt est de porter une décision.
    C'est ainsi que `RMAs_month` a annoncé douze variables relatives
    pendant des années, seule de sa famille, faute d'une ligne oubliée
    dans la fiche R d'origine.

    **Il s'accorde avec l'unité**, qui détermine la propriété. Une fiche
    qui s'en écarte est presque toujours une distraction ; si elle a une
    vraie raison, c'est la table `_UNITE_RELATIVE` qu'il faut corriger, au
    vu de la raison.
    """
    en = (card.get("meta") or {}).get("en") or {}
    variable = en.get("variable")
    variables = variable if isinstance(variable, list) else [variable]
    n = len(variables)
    gl = (card.get("meta") or {}).get("global") or {}
    # La PRÉSENCE se lit dans le YAML brut : `load_card` fusionne les
    # défauts, donc la fiche chargée porte toujours un `relative`, et le
    # contrôle serait vide. Même raison que `_check_time_step_ecrit`.
    brut = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    brut_global = ((brut or {}).get("meta") or {}).get("global") or {}
    if "relative" not in brut_global:
        issues.append(
            f"{prefix}.relative: non écrit. Ce champ s'écrit TOUJOURS, "
            "`true` compris : c'est une décision sur ce que la variable "
            "autorise, et son absence se lit comme un oubli."
        )
        return
    valeurs = gl["relative"]
    valeurs = valeurs if isinstance(valeurs, list) else [valeurs] * n
    unites = en.get("unit")
    unites = unites if isinstance(unites, list) else [unites] * n
    for i, var in enumerate(variables):
        if i >= len(valeurs) or i >= len(unites):
            continue                      # longueur déjà signalée
        unite = str(unites[i])
        if unite not in _UNITE_RELATIVE:
            issues.append(
                f"{prefix}.unit de '{var}': unité '{unite}' hors de la "
                f"table _UNITE_RELATIVE ; la classer avant de l'employer"
            )
            continue
        attendu = _UNITE_RELATIVE[unite]
        if valeurs[i] != attendu:
            issues.append(
                f"{prefix}.relative de '{var}': {valeurs[i]!r} pour une "
                f"unité '{unite}' (attendu {attendu!r})"
            )


def _check_lacunes_ecrites(card, path, issues):
    """Les seuils de lacunes s'écrivent là où ils ont un sens.

    Ce ne sont pas des réglages fins : le corpus n'emploie qu'une valeur
    pour chacun, 3 et 10. Ce sont des CRITÈRES de méthode, et leur silence
    change les valeurs publiées sans que rien ne le dise.

    Deux règles, que le corpus suivait déjà sans les écrire nulle part :

    - **`max_na_years` est un critère sur la CHRONIQUE** : plus longue
      suite d'années manquantes tolérée avant que stase ne tronque la
      série autour du trou. Une fois par fiche, donc, pas une fois par
      process. C'est ce qui trompe à la lecture : il paraît absent de 97
      process alors qu'il est écrit une fois pour la fiche entière.
    - **`max_na_pct` est un critère sur la CASE** : part de valeurs
      manquantes tolérée dans un pas de temps. Il ne se pose que pour un
      process qui range du JOURNALIER dans des cases. Sur `RAl_ratio` P2,
      qui divise deux séries déjà annuelles, un pourcentage de jours
      manquants ne veut rien dire, et l'écrire serait du bruit.

    Ce que l'absence coûtait, mesuré le 2026-08-13 : `dtFlood` calculait
    son maximum annuel sur une année même privée de la moitié de ses
    jours, quand la fiche jumelle `dtLF` écartait la même année. L'écart
    venait du corpus R et personne ne pouvait le voir, chaque fiche étant
    par ailleurs valide.

    Un seuil DÉLIBÉRÉMENT absent s'écrit `null` : `QJ` range ses valeurs
    par jour calendaire, si bien qu'une case contient une quarantaine
    d'ANNÉES et non 365 jours, et la valeur 3 y écarterait un jour dès
    qu'une seule année manque. Un `null` écrit est une décision, une
    absence est un silence.
    """
    brut = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    procs_brut = (brut.get("process") or {})

    combien = sum(1 for p in procs_brut.values()
                  if isinstance(p, dict) and "max_na_years" in p)
    if combien != 1:
        issues.append(
            f"max_na_years écrit {combien} fois : il s'écrit UNE fois par "
            "fiche, c'est un critère sur la chronique et non sur un pas "
            "de temps."
        )

    _CASES = {"year", "year-month", "month", "year-season", "season", "yearday"}
    # Colonnes réellement DENSES, c'est-à-dire portant une valeur par pas
    # de temps d'entrée. `method.grains()` dit qu'un process `keep: all`
    # rediffuse sa valeur sur la grille d'entrée et garde donc le grain de
    # ses entrées : vrai d'une fonction qui TRANSFORME (`quickflow` rend un
    # point par jour), faux d'une fonction qui RÉDUIT (`nanmax` sous
    # `keep: all` rend un point par an posé sur une grille journalière,
    # mesuré à 99,7 % de NaN sur `dtFlood`). Compter ces NaN de structure
    # comme des lacunes rejetterait toutes les années : c'est ce qui vidait
    # la fiche quand un seuil était posé sur son P3.
    denses = {v.strip().rstrip("? ").strip()
              for v in str(card["meta"]["global"].get("input_vars", "")).split(",")}
    for (nom, raw), proc in zip(procs_brut.items(), card["processes"]):
        if proc["time_step"] in _CASES:
            journalier = any(col in denses
                             for _, e in _method.columns_and_entries(proc)
                             for col in _method._entrees(e))
        else:
            journalier = False
        for colonne, e in _method.columns_and_entries(proc):
            fn = e.get("fn")
            if getattr(fn, "is_transform", False):
                denses.add(colonne)
        if journalier and "max_na_pct" not in (raw or {}):
            issues.append(
                f"process.{nom}: 'max_na_pct' non écrit alors que ce "
                f"process range du journalier en '{proc['time_step']}'. "
                "Il s'écrit toujours ici, `null` compris quand on ne veut "
                "délibérément aucun filtrage : son absence se lit comme "
                "un oubli et change les valeurs publiées."
            )


def _check_global_lists(card, prefix, issues):
    """Une liste de `meta.global` a autant de valeurs que de variables.

    `_check_meta_lists` tenait déjà cette règle, mais seulement sur les
    blocs de LANGUE : `meta.global` n'a jamais été mesuré. Trois fiches
    `delta-allLF_*` y déclaraient encore 15 valeurs pour 5 variables,
    restées de l'époque où elles sortaient 5 variables fois 3 horizons ;
    la conversion au modèle suffixe du 2026-07-22 a réduit les sorties
    sans retailler ces listes. Le code prend les n premières, si bien que
    `delta-dtLF` et `delta-vLF` se publiaient en DATES, avec la palette
    des dates, alors que ce sont une durée et un volume. Rien ne
    rougissait : chaque fiche était par ailleurs valide.
    """
    en = (card.get("meta") or {}).get("en") or {}
    variable = en.get("variable")
    n = len(variable) if isinstance(variable, list) else 1
    gl = (card.get("meta") or {}).get("global") or {}
    for champ in ("is_date", "relative", "is_experimental", "palette", "source"):
        v = gl.get(champ)
        if not isinstance(v, list):
            continue
        if champ == "palette" and v and not isinstance(v[0], list):
            continue                      # une seule palette, en couleurs
        if len(v) != n:
            issues.append(
                f"{prefix}.{champ}: {len(v)} valeurs pour {n} variable(s)"
            )


def _check_is_date(card, path, prefix, issues):
    """`is_date` vaut exactement « la variable est de l'aspect timing ».

    Mesuré sur le corpus le 2026-08-13 : 52 variables `timing`, toutes à
    `true`, et aucune des 405 autres ne l'est. La règle n'est donc pas
    une préférence, c'est ce que le corpus fait déjà partout.

    Ne pas lire `is_date` comme « l'unité est une date » : `delta-tVCX10`
    est un écart de dates, exprimé en jours, et il reste `timing` donc
    `true`. Ce que le champ dit est de quel AXE la variable parle, ce qui
    commande aussi sa palette.
    """
    en = (card.get("meta") or {}).get("en") or {}
    variable = en.get("variable")
    variables = variable if isinstance(variable, list) else [variable]
    n = len(variables)
    aspect = (en.get("classification") or {}).get("aspect")
    aspects = aspect if isinstance(aspect, list) else [aspect] * n
    gl = (card.get("meta") or {}).get("global") or {}
    # Écrit TOUJOURS, comme `time_step` et `relative` : la présence se lit
    # dans le YAML brut, `load_card` fusionnant les défauts.
    brut = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}
    if "is_date" not in (((brut.get("meta") or {}).get("global")) or {}):
        issues.append(
            f"{prefix}.is_date: non écrit. Ce champ s'écrit TOUJOURS, "
            "`false` compris : il dit de quel axe parle la variable, et "
            "son absence se lit comme un oubli."
        )
        return
    dates = gl.get("is_date", False)
    dates = dates if isinstance(dates, list) else [dates] * n
    for i, var in enumerate(variables):
        if i >= len(aspects) or i >= len(dates):
            continue                      # longueur déjà signalée
        attendu = str(aspects[i]).strip().lower() == "timing"
        if bool(dates[i]) != attendu:
            issues.append(
                f"{prefix}.is_date de '{var}': {bool(dates[i])} pour un "
                f"aspect '{aspects[i]}' (attendu {attendu})"
            )


def _windows_in_processes(processes):
    """Fenêtres [début, fin] présentes dans les sampling_period process."""
    windows = set()
    for proc in processes:
        sp = proc["sampling_period"]
        if isinstance(sp, list) and len(sp) == 2 \
                and all(isinstance(x, str) for x in sp):
            windows.add(tuple(sp))
    return windows


def _check_time_step_ecrit(path, issues):
    """`time_step` s'écrit toujours, même quand il vaut le défaut.

    Un défaut qui veut dire « rien de particulier » s'omet : `keep: null`,
    `compress: false`, `max_na_*: null`. Un défaut qui est un CHOIX parmi
    sept valeurs, non : son absence se lit comme un oubli, pas comme
    « annuel ». Le champ était écrit 296 fois et tu 208 dans le même
    corpus, pour le même champ, selon sa seule valeur (2026-08-04).

    C'est le cœur de l'agrégation, et la fiche est de la DONNÉE : elle
    doit porter ce qu'elle affirme sans qu'on ait à connaître un défaut
    de code pour la lire.
    """
    brut = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    for nom, proc in (brut.get("process") or {}).items():
        if isinstance(proc, dict) and "time_step" not in proc:
            issues.append(
                f"process.{nom}: 'time_step' non écrit. Ce champ s'écrit "
                "toujours, y compris pour sa valeur par défaut 'year' : "
                "c'est le cœur de l'agrégation, et son absence se lit "
                "comme un oubli."
            )


def _check_method(card, issues):
    """`method` indexé par process, puis par colonne produite.

    La forme cible est une table de tables : un process, une colonne, une
    phrase (docs/dev/archive/PLAN_METHOD.md). Le corpus migre fiche par fiche, si
    bien que les formes héritées (chaîne numérotée, ou liste d'une chaîne
    par sortie) restent tolérées ici et publiées telles quelles ; elles ne
    seront refusées qu'une fois la dernière fiche migrée.

    Ce qui est contrôlé n'est pas le texte mais la CORRESPONDANCE : une
    phrase par colonne réellement produite, ni plus ni moins. Une phrase
    orpheline signale une colonne disparue du process, une colonne muette
    signale une fonction ajoutée sans sa phrase. Aucune des deux ne se
    voit à la lecture d'une fiche de cinq process.
    """
    attendus = [p["name"] for p in card["processes"]]
    par_process = {p["name"]: p for p in card["processes"]}
    formes = {}

    for lang in ("en", "fr"):
        table = card["meta"][lang].get("method")
        formes[lang] = isinstance(table, dict)
        if not isinstance(table, dict):
            continue
        prefixe = f"meta.{lang}.method"

        manquants = [p for p in attendus if p not in table]
        surnumeraires = [p for p in table if p not in attendus]
        if manquants:
            issues.append(f"{prefixe}: process sans phrase : {manquants}")
        if surnumeraires:
            issues.append(
                f"{prefixe}: entrée(s) ne désignant aucun process : "
                f"{surnumeraires}")

        for nom in attendus:
            if nom not in table:
                continue
            entree = table[nom]
            if not isinstance(entree, dict):
                issues.append(
                    f"{prefixe}.{nom}: attendu une table indexée par colonne "
                    f"produite, reçu {type(entree).__name__}")
                continue
            produites = _method.produced_columns(par_process[nom])
            muettes = [c for c in produites if c not in entree]
            orphelines = [c for c in entree if c not in produites]
            if muettes:
                issues.append(
                    f"{prefixe}.{nom}: colonne(s) sans phrase : {muettes}")
            if orphelines:
                issues.append(
                    f"{prefixe}.{nom}: phrase(s) sans colonne produite : "
                    f"{orphelines} (produites : {produites})")
            for col, texte in entree.items():
                if isinstance(texte, str) and texte.count(" - ") != 1:
                    issues.append(
                        f"{prefixe}.{nom}.{col}: attendu une moitié gauche et "
                        "une moitié droite séparées par ' - ', une fois")

    if formes["en"] != formes["fr"]:
        issues.append(
            "meta.method: une langue est migrée et pas l'autre ; les deux "
            "portent les mêmes clés ou aucune")
    elif formes["en"]:
        # Les clés sont des identifiants de process et de colonnes, donc
        # elles ne se traduisent pas : les deux langues doivent les avoir
        # à l'identique, à tous les niveaux.
        en, fr = card["meta"]["en"]["method"], card["meta"]["fr"]["method"]
        for nom in sorted(set(en) & set(fr)):
            a, b = en[nom], fr[nom]
            if isinstance(a, dict) and isinstance(b, dict) and set(a) != set(b):
                issues.append(
                    f"meta.method.{nom}: clés en/fr différentes "
                    f"({sorted(set(a) ^ set(b))})")


_MOT = r"(?<![\w-]){}(?![\w-])"


def _check_method_chain(card, issues):
    """Un nom cité doit avoir été présenté.

    Les clés lèvent l'ambiguïté machine et accordent `method` à
    `process`, mais la valeur PUBLIÉE ne les montre pas : un lecteur
    reçoit des phrases numérotées, et « sous upLim » à l'étape 4 ne se
    lit que si une étape antérieure a écrit `upLim`. La prose du process
    qui produit une colonne la nomme donc, dès lors qu'une étape
    ultérieure la cite.

    C'est la contrepartie de la migration : les incises `(série des X)`
    présentaient ce nom, à trois orthographes près, et les retirer aurait
    laissé quatre-vingts références pendantes (mesuré le 2026-08-03).
    Elles sont revenues sous une orthographe unique, et cette règle
    empêche la relecture éditoriale de les reperdre.
    """
    for lang in ("en", "fr"):
        table = card["meta"][lang].get("method")
        if not isinstance(table, dict):
            continue
        prose = []
        for p in card["processes"]:
            e = table.get(p["name"])
            valeurs = e.values() if isinstance(e, dict) else [e]
            prose.append(" ".join(
                str(v).split(" - ", 1)[-1] for v in valeurs if v is not None))

        for i, p in enumerate(card["processes"]):
            for colonne in _method.produced_columns(p):
                motif = _MOT.format(re.escape(colonne))
                if not any(re.search(motif, t) for t in prose[i + 1:]):
                    continue
                if re.search(motif, prose[i]):
                    continue
                issues.append(
                    f"meta.{lang}.method.{p['name']}: '{colonne}' est cité "
                    "plus loin mais la phrase qui le produit ne le nomme "
                    "pas ; la chaîne publiée ne se lit pas seule"
                )


# Moitié gauche attendue pour un process qui agrège, par pas de temps,
# (en, fr). Vocabulaire fermé : on n'en ajoute pas, on n'en change pas.
_FORME_AGREGATION = {
    "none": ("no temporal aggregation", "aucune agrégation temporelle"),
    "year": ("annual aggregation", "agrégation annuelle"),
    "year-month": ("monthly aggregation for each year",
                   "agrégation mensuelle par année"),
    "month": ("monthly aggregation", "agrégation mensuelle"),
    "year-season": ("seasonal annual aggregation",
                    "agrégation annuelle saisonnalisée"),
    "season": ("seasonal aggregation", "agrégation saisonnière"),
    "yearday": ("aggregation by day of the year",
                "agrégation par jour de l'année"),
}
_SANS_AGREGATION = _FORME_AGREGATION["none"]

# La fenêtre et la restriction de période complètent la forme sans la
# changer : on les met de côté avant de comparer.
_ORNEMENT = re.compile(r"\s*\[.*?\]|\s+(?:sur|over)\s+\{suffix\.[^}]*\}")


def _check_left_half(card, issues):
    """La moitié gauche affirme, le process calcule : on confronte.

    C'est le seul contrôle croisé qui existe sur `method`, et il n'existe
    que parce que la phrase est ÉCRITE : une phrase générée serait
    d'accord avec le code par construction, y compris quand le code a
    tort. Sans ce test, l'affirmation dérive en silence, ce qui s'est
    produit (huit `agrégation mensuelle` pour un calcul par année, restés
    jusqu'à ce que quelqu'un fasse le croisement à la main).

    Le pas de temps ne suffit pas à conclure : un process qui opère sur
    des séries déjà à son propre pas n'agrège rien, et le dit (cf.
    `method.grains`).
    """
    etats = _method.grains(card)
    for lang in ("en", "fr"):
        table = card["meta"][lang].get("method")
        if not isinstance(table, dict):
            continue
        i_lang = 0 if lang == "en" else 1
        for p, connus in zip(card["processes"], etats):
            attendu_agrege = _FORME_AGREGATION.get(p["time_step"])
            if attendu_agrege is None:
                continue                      # pas de temps hors vocabulaire
            entrees = table.get(p["name"])
            if not isinstance(entrees, dict):
                continue          # forme signalée par _check_method
            for colonne, entree in _method.columns_and_entries(p):
                texte = entrees.get(colonne)
                if not isinstance(texte, str) or " - " not in texte:
                    continue
                agrege = _method.aggregates(p, entree, connus)
                attendu = (attendu_agrege if agrege else _SANS_AGREGATION)[i_lang]
                ecrit = _ORNEMENT.sub("", texte.split(" - ", 1)[0]).strip()
                if ecrit != attendu:
                    issues.append(
                        f"meta.{lang}.method.{p['name']}.{colonne}: la moitié "
                        f"gauche dit '{ecrit}' là où le process calcule "
                        f"'{attendu}' (time_step: {p['time_step']}"
                        + ("" if agrege else ", sans changement de grain") + ")"
                    )


_NOMBRE = re.compile(r"\d+(?:[.,]\d+)?")


def _check_numbers(card, issues):
    """Un nombre écrit dans la prose doit exister dans le process.

    La charte veut les paramètres numériques en clair, « sur 10 jours »,
    « de période de retour 5 ans », « d'au moins 20 mm ». Un nombre écrit
    à la main est un nombre qui peut mentir, et rien ne le vérifiait :
    `delta-VCX10_H` annonçait en anglais une moyenne mobile sur 3 jours
    pour un `k: 10`, sur une fiche dont le titre disait bien 10 jours.

    Le contrôle est dans ce sens et pas dans l'autre. Exiger qu'un
    paramètre du process se retrouve dans la phrase serait faux : `Q50A`
    appelle « médiane » le quantile à 50 %, et a raison. Exiger qu'un
    nombre ÉCRIT soit vrai n'a, lui, aucune exception : mesuré sur le
    corpus entier, ce contrôle ne trouve que l'erreur.

    Les identifiants sont retirés d'abord : le « 10 » de `VC10` n'est pas
    une durée.
    """
    noms = sorted((n for n in _method.known_names(card) if any(
        c.isdigit() for c in n)), key=len, reverse=True)
    for lang in ("en", "fr"):
        table = card["meta"][lang].get("method")
        if not isinstance(table, dict):
            continue
        for p in card["processes"]:
            entrees = table.get(p["name"])
            if not isinstance(entrees, dict):
                continue
            for colonne, entree in _method.columns_and_entries(p):
                texte = entrees.get(colonne)
                if not isinstance(texte, str):
                    continue
                prose = texte.split(" - ", 1)[-1]
                for nom in noms:
                    prose = re.sub(rf"(?<![\w-]){re.escape(nom)}(?![\w-])",
                                   " ", prose)
                valeurs = [v for v in list(entree["kwargs"].values())
                           + [x for genre, x in entree["pos_args"]
                              if genre == "lit"]
                           if isinstance(v, (int, float))
                           and not isinstance(v, bool)]
                connus = {float(v) for v in valeurs} | {float(v) * 100
                                                        for v in valeurs}
                for brut in _NOMBRE.findall(prose):
                    if float(brut.replace(",", ".")) not in connus:
                        issues.append(
                            f"meta.{lang}.method.{p['name']}.{colonne}: la "
                            f"phrase écrit {brut}, que "
                            f"{entree['fn_name']} ne reçoit pas "
                            f"(valeurs du process : "
                            f"{sorted(connus) or 'aucune'})"
                        )


def _check_window_coherence(card, issues):
    """Fenêtre partielle en meta.en.sampling_period → un process doit
    porter la même fenêtre (sauf time_steps saisonniers/mensuels, gérés
    par Seasons ou le découpage temporel)."""
    sp = card["meta"]["en"].get("sampling_period")
    if not (isinstance(sp, list) and len(sp) == 2
            and all(isinstance(x, str) for x in sp)):
        return                           # texte libre, liste de listes...
    full = _is_full_year_window(sp[0], sp[1])
    if full is None or full:
        return
    exempt_steps = {"year-month", "month", "year-season", "season", "yearday"}
    if all(p["time_step"] in exempt_steps for p in card["processes"]):
        return
    if tuple(sp) not in _windows_in_processes(card["processes"]):
        issues.append(
            f"meta.en.sampling_period {sp} est une fenêtre partielle mais "
            "aucun process ne porte cette fenêtre en sampling_period "
            "(borne de fin perdue ?)"
        )


# Noms d'agrégation à sémantique NaN ambiguë (numpy strict, pandas
# skipna, builtins dépendants de l'ordre...) : les fiches doivent dire
# ce qu'elles font, la variante nan* porte la sémantique dans son nom.
_AMBIGUOUS_FN_NAMES = {"mean", "median", "std", "var", "sum", "max",
                       "min", "amax", "amin", "argmax", "argmin"}


def _check_process(proc, issues):
    name = proc["name"]
    if proc["time_step"] not in _VALID_TIME_STEPS:
        issues.append(f"{name}.time_step invalide : {proc['time_step']!r}")

    keep = proc["keep"]
    if keep is not None and keep != "all" and not isinstance(keep, list):
        issues.append(f"{name}.keep invalide : {keep!r}")

    napct = proc["max_na_pct"]
    if napct is not None and not (isinstance(napct, (int, float))
                                  and 0 <= napct <= 100):
        issues.append(f"{name}.max_na_pct invalide : {napct!r}")

    sp = proc["sampling_period"]
    if isinstance(sp, str) and _parse_mmdd(sp) is None:
        issues.append(f"{name}.sampling_period invalide : {sp!r}")
    elif isinstance(sp, list):
        if len(sp) != 2 or any(_parse_mmdd(x) is None for x in sp):
            issues.append(f"{name}.sampling_period invalide : {sp!r}")

    for entry in proc["func"]:
        try:
            resolve(entry["fn_name"])
        except KeyError:
            issues.append(
                f"{name}.func.{entry['name']}: fonction inconnue "
                f"'{entry['fn_name']}'"
            )
        if entry["fn_name"] in _AMBIGUOUS_FN_NAMES:
            issues.append(
                f"{name}.func.{entry['name']}: '{entry['fn_name']}' a une "
                "sémantique NaN ambiguë ; utiliser la variante "
                f"'nan{entry['fn_name'].lstrip('a')}' (skipna explicite) "
                "ou une fonction card.functions"
            )
    if isinstance(sp, dict):
        try:
            resolve(sp["func"]["fn_name"])
        except KeyError:
            issues.append(
                f"{name}.sampling_period: fonction inconnue "
                f"'{sp['funct']['fn_name']}'"
            )


# Convention des fenêtres adaptatives : le sens de l'adaptatif (couper
# l'année là où le phénomène est absent) et la fenêtre fixe de repli
# (preferred_sampling_period, prise par sampling_period="preferred" à
# l'extraction) sont fixés par le PHÉNOMÈNE, pas fiche par fiche.
_ADAPTIVE_BY_PHENOMENON = {
    "low flows":  ("nanmax", "01-01"),
    "high flows": ("nanmin", "09-01"),
}


def _check_adaptive_convention(card, issues):
    adaptive_fns = {proc["sampling_period"]["func"]["fn_name"]
                    for proc in card["processes"]
                    if isinstance(proc["sampling_period"], dict)}
    if not adaptive_fns:
        return
    preferred = card["meta"]["global"].get("preferred_sampling_period")
    if not preferred:
        issues.append(
            "sampling_period adaptatif sans "
            "meta.global.preferred_sampling_period : la fenêtre fixe de "
            "repli est requise (cf. sampling_period='preferred')"
        )
    phen = card["meta"]["en"].get("classification", {}).get("phenomenon")
    for p in (phen if isinstance(phen, list) else [phen] if phen else []):
        conv = _ADAPTIVE_BY_PHENOMENON.get(p)
        if conv is None:
            continue
        fn_expected, pref_expected = conv
        if adaptive_fns != {fn_expected}:
            issues.append(
                f"adaptatif {sorted(adaptive_fns)} incompatible avec "
                f"phenomenon '{p}' (convention : {fn_expected})"
            )
        if preferred and preferred != pref_expected:
            issues.append(
                f"preferred_sampling_period {preferred!r} incompatible "
                f"avec phenomenon '{p}' (convention : '{pref_expected}')"
            )


_CL_KEYS = ("domain", "phenomenon", "aspect", "statistic", "season",
            "output", "purpose")
# `statistic` est REQUISE, et c'est la règle déjà écrite pour `time_step` :
# une facette dont l'ABSENCE voudrait dire quelque chose ne sait pas
# distinguer un choix d'un oubli. Le vocabulaire porte donc `filter` pour
# les sorties qui viennent d'une séparation d'hydrogramme et non d'une
# statistique, plutôt que de les laisser sans facette.
_CL_REQUIRED = ("domain", "statistic", "season", "output")


def _check_classification(card, issues):
    vocab = _vocab()
    cl_en = card["meta"]["en"].get("classification")
    cl_fr = card["meta"]["fr"].get("classification")
    if not isinstance(cl_en, dict) or not isinstance(cl_fr, dict):
        issues.append("classification manquante (bloc requis en meta.en ET meta.fr)")
        return
    for lang, cl in (("en", cl_en), ("fr", cl_fr)):
        for k in cl:
            if k not in _CL_KEYS:
                issues.append(f"classification.{lang}: clé inconnue '{k}'")
        for k in _CL_REQUIRED:
            if k not in cl:
                issues.append(f"classification.{lang}: facette requise '{k}' absente")
    if set(cl_en) != set(cl_fr):
        issues.append("classification: clés différentes entre en et fr")
        return
    if "purpose" in cl_en and "aspect" in cl_en:
        issues.append("classification: aspect interdit quand purpose est présent")
    if "purpose" not in cl_en and "aspect" not in cl_en:
        issues.append("classification: aspect requis (sauf purpose présent)")

    for key in cl_en:
        ven, vfr = cl_en[key], cl_fr.get(key)
        len_ = isinstance(ven, list)
        if len_ != isinstance(vfr, list) or (len_ and len(ven) != len(vfr)):
            issues.append(f"classification.{key}: formes en/fr différentes")
            continue
        pairs = zip(ven, vfr) if len_ else [(ven, vfr)]
        for e, f in pairs:
            # La clé du vocabulaire est un slug : on retrouve le concept par
            # son étiquette anglaise, pas par la clé.
            entry = next((v for v in vocab.get(key, {}).values()
                          if v.get("en") == e), None)
            if entry is None:
                issues.append(f"classification.{key}: '{e}' hors vocabulaire")
            elif entry["fr"] != f:
                issues.append(
                    f"classification.{key}: '{e}' apparié à '{f}' "
                    f"(attendu '{entry['fr']}')"
                )


def _check_suffix(card, issues):
    """Placeholders {suffix.X} et vocabulaire de suffixes.

    Garantit qu'aucune accolade ne peut sortir non résolue : une fiche
    qui utilise un placeholder déclare son défaut, dans chaque langue.
    Une fiche reste ainsi lisible seule, et metadata_only, l'extraction
    sans suffixe et le catalogue produisent la même phrase.
    """
    used_any = False
    for lang in ("en", "fr"):
        meta_lang = card["meta"][lang]
        used = _sfx.card_fields_used(meta_lang)
        declared = meta_lang.get("suffix_default")
        used_any = used_any or bool(used)

        if used and not declared:
            issues.append(
                f"meta.{lang}: placeholder {{suffix}} utilisé sans "
                f"'suffix_default' (champs requis : {sorted(used)})"
            )
        elif used:
            manquants = sorted(f for f in used if f not in declared)
            if manquants:
                issues.append(
                    f"meta.{lang}.suffix_default: champs manquants "
                    f"{manquants} (utilisés par un placeholder)"
                )
        if declared and not isinstance(declared, dict):
            issues.append(f"meta.{lang}.suffix_default: dict attendu")

        suffixes = meta_lang.get("suffixes")
        if suffixes is not None:
            if not isinstance(suffixes, dict):
                issues.append(f"meta.{lang}.suffixes: dict attendu")
            else:
                for key, rec in suffixes.items():
                    if not isinstance(rec, dict):
                        issues.append(
                            f"meta.{lang}.suffixes.{key}: dict de champs attendu"
                        )

    if not used_any:
        for lang in ("en", "fr"):
            for field in ("suffix_default", "suffixes"):
                if card["meta"][lang].get(field) is not None:
                    issues.append(
                        f"meta.{lang}.{field}: déclaré mais aucun placeholder "
                        "{suffix} ne l'utilise (champ mort)"
                    )

    keys_en = set((card["meta"]["en"].get("suffixes") or {}))
    keys_fr = set((card["meta"]["fr"].get("suffixes") or {}))
    if keys_en != keys_fr:
        issues.append(
            f"meta.suffixes: clés en/fr différentes "
            f"({sorted(keys_en ^ keys_fr)})"
        )


_VERSION_RE = re.compile(r"^\d+\.\d+(\.\d+)?$")


def _check_version(card, issues):
    """La version d'une fiche est `majeur.mineur`, plus un `.patch`
    optionnel. Majeur = les SORTIES ont changé, mineur = method ou
    description, patch = le reste. Le champ doit être une chaîne : sans
    guillemets, YAML lit 1.10 comme le nombre 1.1, et deux versions
    distinctes deviennent la même."""
    v = card.get("version")
    if v is None:
        issues.append("champ 'version' manquant")
        return
    if not isinstance(v, str):
        issues.append(
            f"version {v!r} non citée : mettre des guillemets, sinon YAML la "
            "lit comme un nombre et 1.10 devient 1.1"
        )
        return
    if not _VERSION_RE.match(v):
        issues.append(
            f"version '{v}' mal formée : attendu majeur.mineur[.patch], "
            "chiffres uniquement"
        )
    elif v.endswith(".0") and v.count(".") == 2:
        issues.append(
            f"version '{v}' : un patch nul ne s'écrit pas, "
            f"utiliser '{v[:-2]}'"
        )


def validate_card(path) -> list[str]:
    """Retourne la liste des problèmes détectés (vide si la fiche est valide)."""
    issues: list[str] = []
    try:
        card = load_card(path)
    except Exception as e:
        return [f"chargement impossible : {type(e).__name__}: {e}"]

    if not card.get("id"):
        issues.append("champ 'id' manquant")
    if Path(path).stem != card.get("id"):
        issues.append(
            f"id '{card.get('id')}' ≠ nom de fichier '{Path(path).stem}'"
        )
    _check_version(card, issues)

    for lang in ("en", "fr"):
        _check_meta_lists(card["meta"][lang], f"meta.{lang}", issues)
    _check_global_lists(card, "meta.global", issues)
    _check_is_date(card, path, "meta.global", issues)
    _check_relative(card, path, "meta.global", issues)
    _check_lacunes_ecrites(card, path, issues)

    var_en = card["meta"]["en"].get("variable")
    var_fr = card["meta"]["fr"].get("variable")
    if isinstance(var_en, list) != isinstance(var_fr, list) or (
            isinstance(var_en, list) and len(var_en) != len(var_fr or [])):
        issues.append("meta: variable en/fr de formes différentes")

    for proc in card["processes"]:
        _check_process(proc, issues)

    _check_time_step_ecrit(path, issues)
    _check_method(card, issues)
    _check_method_chain(card, issues)
    _check_left_half(card, issues)
    _check_numbers(card, issues)
    _check_window_coherence(card, issues)
    _check_adaptive_convention(card, issues)
    _check_classification(card, issues)
    _check_path_coherence(card, Path(path), issues)
    _check_inputs(card, issues)
    _check_suffix(card, issues)
    return issues


def _slug(s, facette=None):
    """Étiquette de classification -> nom de dossier.

    Le slug est DÉCLARÉ dans topics.yaml (clé du concept) : on le lit là,
    on ne le recalcule pas depuis l'anglais. Repli sur une slugification
    naïve seulement si le concept est hors vocabulaire (le linter le
    signale par ailleurs)."""
    if not isinstance(s, str):
        return s
    if facette:
        declared = _slug_of(facette, s)
        if declared:
            return declared
    return s.replace(" ", "-").replace("'", "")


def _check_path_coherence(card, path, issues):
    """L'arborescence cards/<domain>/<phénomène-ou-purpose>/<output>/ doit
    refléter la classification (domaine et groupe premiers si listes).
    Ignoré hors d'un dossier 'cards' (fiches de test, copies utilisateur)."""
    parts = path.resolve().parts
    if "cards" not in parts or parts.index("cards") != len(parts) - 5:
        return
    cl = card["meta"]["en"].get("classification")
    if not isinstance(cl, dict):
        return                            # déjà signalé par ailleurs
    dom = cl.get("domain")
    dom = dom[0] if isinstance(dom, list) else dom
    facette = "phenomenon" if cl.get("phenomenon") else "purpose"
    grp = cl.get("phenomenon") or cl.get("purpose")
    grp = grp[0] if isinstance(grp, list) else grp
    expected = (dom, _slug(grp, facette), cl.get("output"))
    actual = parts[-4:-1]
    if expected != actual and None not in expected:
        issues.append(
            f"chemin cards/{'/'.join(actual)}/ ≠ classification "
            f"(attendu cards/{'/'.join(str(e) for e in expected)}/)"
        )


# Ce qu'une variable EST, et qui ne peut donc pas dépendre de la fiche
# qui la produit. Le reste (`method`, `functions`, `input_vars`, `swhid`,
# `version`, `family`) diverge légitimement : une fiche groupée calcule
# plus de choses, lit plus d'entrées, et doit désambiguïser ses phrases
# de méthode (« sum » seul contre « sum of total precipitation »).
_PARTAGES_LANG = ("name", "description", "unit")
_PARTAGES_CLASS = ("domain", "phenomenon", "aspect", "statistic",
                   "season", "output", "purpose")
_PARTAGES_GLOBAL = ("is_date", "relative", "palette")


def _libelles_par_variable(root):
    """{(variable, champ): {valeur: [fiches]}} sur tout le corpus.

    Une fiche multi-sorties apparie ses listes par INDICE : la n-ième
    variable porte le n-ième name. Une métadonnée scalaire vaut pour
    toutes les sorties de la fiche.
    """
    table = {}

    def note(var, champ, valeur, fiche):
        if valeur is None or (isinstance(valeur, str) and not valeur.strip()):
            return
        table.setdefault((str(var), champ), {}) \
             .setdefault(str(valeur), []).append(fiche)

    for p in sorted(root.rglob("*.yaml")):
        try:
            card = yaml.safe_load(p.read_text(encoding="utf-8"))
        except Exception:
            continue          # la fiche est déjà en défaut par ailleurs
        if not isinstance(card, dict):
            continue
        meta = card.get("meta") or {}
        reference = (meta.get("en") or {}).get("variable")
        n = len(reference) if isinstance(reference, list) else 1

        def ieme(v, i):
            """La i-ème valeur d'une liste appariée aux variables ; une
            valeur scalaire vaut pour toutes les sorties."""
            if isinstance(v, list):
                return v[i] if i < len(v) else None
            return v

        for lang in ("en", "fr"):
            bloc = meta.get(lang) or {}
            variables = bloc.get("variable")
            if variables is None:
                continue
            if not isinstance(variables, list):
                variables = [variables]
            classification = bloc.get("classification") or {}
            for i, var in enumerate(variables):
                for champ in _PARTAGES_LANG:
                    note(var, f"meta.{lang}.{champ}",
                         ieme(bloc.get(champ), i), p.stem)
                for champ in _PARTAGES_CLASS:
                    note(var, f"classification.{lang}.{champ}",
                         ieme(classification.get(champ), i), p.stem)

        # `meta.global` n'est pas traduit : indexé sur les variables `en`
        gl = meta.get("global") or {}
        variables = reference if isinstance(reference, list) else [reference]
        for i, var in enumerate(variables):
            for champ in _PARTAGES_GLOBAL:
                v = gl.get(champ)
                if champ == "palette" and isinstance(v, list) \
                        and v and not isinstance(v[0], list):
                    v = [v] * n           # une seule palette pour toutes
                note(var, f"meta.global.{champ}", ieme(v, i), p.stem)
    return table


def _check_libelles_partages(root, report):
    """Deux fiches produisant la MÊME variable en disent la même chose.

    Le corpus produit exprès certaines variables deux fois, par une fiche
    seule et par une fiche groupée (`vLF` et `allLF`), parce qu'on veut
    parfois un lot et parfois une variable seule. Rien n'obligeait alors
    les deux à s'accorder, et le corpus avait dérivé de trois façons :
    sept variables portaient deux `name` ou `description` anglais (le
    français restant d'accord avec lui-même, donc une dérive de
    traduction) ; `RAs` était classée dans deux phénomènes ; six
    variables recevaient deux `is_date` et deux palettes.

    Rien de tout cela n'était visible fiche par fiche : chacune était
    valide, seul le corpus vu d'ensemble ne l'était pas. C'est pourquoi
    la règle vit ici et non dans `validate_card`. Les conséquences se
    voyaient en aval : un catalogue affichant deux noms pour une variable,
    et le vocabulaire SKOS deux `prefLabel` dans une même langue, ce
    qu'interdit la norme. Trouvé le 2026-08-12 par `tests/test_skos.py`,
    élargi le 2026-08-13 à tout ce qui décrit ce qu'une variable EST.
    """
    for (var, champ), valeurs in sorted(_libelles_par_variable(root).items()):
        if len(valeurs) < 2:
            continue
        versions = "  |  ".join(
            f"{'/'.join(fiches)}: {t!r}" for t, fiches in sorted(valeurs.items())
        )
        for fiches in valeurs.values():
            for fiche in fiches:
                report.setdefault(fiche, []).append(
                    f"{champ} de '{var}': deux valeurs selon la fiche qui "
                    f"la produit  ->  {versions}"
                )


def lint_cards(CARD_path=None) -> dict:
    """Valide toutes les fiches d'une arborescence.
    Retourne {nom_de_fiche: [issues]} pour les fiches en défaut."""
    root = Path(CARD_path) if CARD_path else _DEFAULT_CARD_DIR
    report = {}
    for p in sorted(root.rglob("*.yaml")):
        issues = validate_card(p)
        if issues:
            report[p.stem] = issues
    _check_libelles_partages(root, report)
    return report


def main():
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else None
    report = lint_cards(path)
    if not report:
        print("✓ toutes les fiches sont valides")
        return 0
    for name, issues in report.items():
        for issue in issues:
            print(f"✗ {name}: {issue}")
    print(f"\n{len(report)} fiche(s) en défaut")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
