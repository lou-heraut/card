# Copyright 2026      Louis Héraut <louis.heraut@inrae.fr>*1
#
# *1 INRAE, UR RiverLy, Villeurbanne, France
#
# This file is part of the card Python package.
#
# card is free software: you can redistribute it and/or modify it under
# the terms of the license in the LICENSE file of this repository.

"""Rendu texte d'une fiche : donner une fiche à LIRE, pas à déchiffrer.

Une fiche contient tout ce qu'il faut pour comprendre son calcul :
colonne d'entrée, fonctions et paramètres, pas de temps, fenêtre
d'échantillonnage, seuils de lacunes, et le chaînage d'un process à
l'autre. Aplati en liste de champs, cela se lit mal ; dessiné, cela se
voit.

Six principes.

**Rien qui ne soit dans la fiche.** La figure lit un fichier, elle ne
prédit pas une exécution. Elle a un temps annoncé l'axe d'une courbe,
deviné du nom de la variable, et une granularité déduite du pas de
temps : mesure faite, `time_step: none` donne une ligne pour BFM, 365
pour QJC10 et 1000 pour FDC, parce que cela dépend de ce que la fonction
retourne. Ce que la fiche ne détermine pas ne s'affiche plus, et ce qui
reste affiché a été vérifié par extraction réelle. Mieux vaut en dire
moins que le dire faux.

**La figure suit la forme de sortie**, qui est déjà une facette de la
classification. Une série se lit sur un axe de temps, d'où la bande de
douze mois. Un scalaire de changement compare deux fenêtres, d'où la
frise.

**Un kwarg qui nomme une colonne est une référence, pas un réglage.**
`delta(QA, date)` suivi de « d'après ref_start, ref_end » se lit, là où
l'appel brut fait cent caractères illisibles.

**Une enveloppe se déplie.** `over_period` sert à restreindre une
période ; afficher son nom cacherait que la fiche calcule une moyenne.
On montre la fonction enveloppée et la restriction en mention.

**Ce qui identifie est l'identifiant de la variable**, celui des
colonnes produites (`variable_en`), et jamais son nom traduit : un
lecteur francophone qui lit « CDC_p » ne le retrouverait pas dans ses
données, où la colonne s'appelle `FDC_p`. La prose est traduite, les
identifiants ne le sont pas ; le nom traduit reste affiché entre
parenthèses quand il diffère.

**Un symbole, un rôle.** Le point médian sépare des informations sur une
même ligne (et signe les unités, `m³·s⁻¹`) ; une puce ouvre un item de
liste ; les traits de casserole portent la chaîne de calcul. Un symbole
qui sert à deux choses ne se lit plus.

**Ce qu'une étape fait se lit dans la FICHE, jamais dans la fonction.**
La figure affichait sous chaque appel la première phrase de la docstring
de la fonction. Une docstring est attachée à une fonction, donc elle ne
peut dire que du général : `apply_threshold` mesure ici une durée de crue
et date ailleurs un début d'étiage, et aucune phrase unique ne sert les
deux. Elle lit maintenant `method`, écrit par étape et par colonne
produite (`card/method.py`), dont seule la moitié droite est affichée :
la maille d'agrégation est déjà DESSINÉE, ligne de grain et bande de
douze mois, et la réécrire serait une redite. Les docstrings n'ont rien
perdu, elles changent de destinataire (`card/docstring.py`).

Le rendu est généré depuis le YAML, jamais écrit à la main, et tout le
corpus passe, dans les deux langues.
"""

import datetime as _dt
import re
import textwrap

from . import method as _method
from .extraction import _meta_frame, resolve
from .loader import load_card
from .schema import input_registry

# Les initiales des douze mois coïncident en français et en anglais.
MOIS = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
PUCE = "▸"                  # item de liste
SEP = " · "                 # séparateur en ligne
SWH = "https://archive.softwareheritage.org/"
_EXP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")

# Prose de la figure, (fr, en). Les identifiants de variables, de
# fonctions et de colonnes n'entrent jamais ici : ils ne se traduisent
# pas.
_T = {
    "year": ("une valeur par année", "one value per year"),
    "month": ("une valeur par mois", "one value per month"),
    "yearday": ("une valeur par jour de l'année", "one value per day of year"),
    "year-month": ("une valeur par mois de chaque année",
                   "one value per month of each year"),
    "season": ("une valeur par saison", "one value per season"),
    "year-season": ("une valeur par saison de chaque année",
                    "one value per season of each year"),
    "transforme": ("transforme la série sans l'agréger, une valeur par jour",
                   "transforms the series without aggregating it, "
                   "one value per day"),
    "diffuse": ("une valeur unique par série, diffusée sur toute la chronique",
                "a single value per series, broadcast over the whole record"),
    "unique": ("aucune agrégation temporelle", "no temporal aggregation"),
    "sortie": ("sortie : {}", "output: {}"),
    "sortie_n": ("sortie : {} colonnes", "output: {} columns"),
    "l_annee": ("une ligne par année", "one row per year"),
    "l_mois": ("une ligne par mois", "one row per month"),
    "l_jour": ("une ligne par jour de l'année", "one row per day of year"),
    "l_annee_mois": ("une ligne par année, les mois en colonnes",
                     "one row per year, months as columns"),
    "l_annee_saisons": ("une ligne par année, les saisons en colonnes",
                        "one row per year, seasons as columns"),
    "l_saisons": ("une ligne par série, les saisons en colonnes",
                  "one row per series, seasons as columns"),
    "adaptatif": ("départ propre à chaque série (adaptatif), année complète",
                  "start specific to each series (adaptive), full year"),
    "annee": ("année complète, du {} au {}", "full year, from {} to {}"),
    "partielle": ("fenêtre partielle, du {} au {}",
                  "partial window, from {} to {}"),
    "restreint": ("restreint à la période demandée",
                  "restricted to the requested period"),
    "dapres": ("d'après {}", "from {}"),
    "sous": ("sous {}", "below {}"),
    "sorties": ("{} sorties : {}", "{} outputs: {}"),
    "sorties_n": ("{} sorties", "{} outputs"),
    "lacunes": ("max {} % de lacunes", "at most {} % missing"),
    "trou": ("max {} ans de trou", "at most a {}-year gap"),
    "facultatif": ("facultatif", "optional"),
    "facultatifs": ("facultatifs", "optional"),
    "compare": ("compare deux fenêtres, fournies en colonnes :",
                "compares two windows, supplied as columns:"),
    "longest": ("plus long épisode", "longest episode"),
    "first_ep": ("premier épisode", "first episode"),
    "last_ep": ("dernier épisode", "last episode"),
    "first": ("premier jour", "first day"),
    "last": ("dernier jour", "last day"),
    "length": ("durée", "duration"),
    "nanargmin": ("jour du minimum", "day of the minimum"),
    "nanargmax": ("jour du maximum", "day of the maximum"),
}


def t(cle, lang="fr", *args):
    s = _T[cle][0 if lang == "fr" else 1]
    return s.format(*args) if args else s


def unite(u):
    u = re.sub(r"\^\{([-\d]+)\}", lambda m: m.group(1).translate(_EXP), str(u))
    return u.replace(".", "·")


def _jour(d, lang):
    """Une date de fenêtre s'écrit MM-DD en anglais, DD-MM en français :
    c'est la convention des métadonnées, la figure la suit."""
    return f"{d[3:]}-{d[:2]}" if lang == "fr" else d


def _vide(x):
    return str(x) in ("", "nan", "None", "<NA>")


LARGEUR = 78          # une figure qui déborde du terminal ne se lit plus


def plie(texte, tete, suite=None):
    """Texte replié sous LARGEUR, `tete` en tête et `suite` en gouttière.

    Une fiche à douze sorties alignait 180 caractères sur une seule
    ligne : le terminal la coupait où il pouvait, c'est-à-dire au
    mauvais endroit.
    """
    suite = tete if suite is None else suite
    # Un identifiant ne se coupe pas : `delta-dtLF` scindé sur son tiret
    # devient deux mots qui n'existent pas.
    lignes = textwrap.wrap(texte, max(LARGEUR - len(tete), 20),
                           break_on_hyphens=False, break_long_words=False) or [""]
    return [tete + lignes[0]] + [suite + ligne for ligne in lignes[1:]]


def decoupe(p, lang="fr"):
    """Ce que fait vraiment le pas de temps, `none` recouvrant deux cas
    opposés : transformer la série sans l'agréger, ou la réduire d'un
    coup, puis diffuser le résultat quand il sert de seuil."""
    ts = p["time_step"]
    if ts != "none":
        return t(ts, lang)
    if p["keep"] == "all":
        # Réduire ou transformer se DÉCLARE (`is_transform`, posé à côté de
        # la fonction), cela ne se devine pas d'un nom. La version devinée
        # cherchait le préfixe `nan` et deux noms écrits en dur, dont
        # `quantile` : le renommage compute_Qp -> exceedance_quantile
        # (RENAMING.md) a laissé la chaîne derrière lui, et six fiches ont
        # annoncé « une valeur par jour » pour un seuil unique. Une chaîne
        # qui nomme une fonction est un lien que rien ne vérifie.
        # Le défaut est « réduit » : transformer est le cas rare et
        # délibéré, donc celui qui se déclare.
        transforme = bool(p["func"]) and all(
            getattr(resolve(e["fn_name"]), "is_transform", False)
            for e in p["func"])
        return t("transforme" if transforme else "diffuse", lang)
    return t("unique", lang)


def bande_annee(sp, lang="fr"):
    """Bande de 12 mois. Une année complète n'est pas un pavé plein : ce
    qui compte est OÙ elle commence, marqué d'un trait."""
    if sp is None:
        return []
    entete = "".join(f"{m}  " for m in MOIS)
    if isinstance(sp, dict):
        return [entete, "▓" * 36, t("adaptatif", lang)]
    if isinstance(sp, str):
        i = (int(sp[:2]) - 1) * 3
        b = "▓" * 36
        b = b[:i] + "┃" + b[i + 1:]
        deb = _dt.date(2001, int(sp[:2]), int(sp[3:]))
        veille = deb - _dt.timedelta(days=1)
        return [entete, b, t("annee", lang, _jour(sp, lang),
                             _jour(veille.strftime("%m-%d"), lang))]
    d, f = int(sp[0][:2]), int(sp[1][:2])

    def dedans(i):
        return (d <= i <= f) if d <= f else (i >= d or i <= f)

    b = "".join("▓▓▓" if dedans(i + 1) else "···" for i in range(12))
    i0, i1 = (d - 1) * 3, f * 3 - 1
    b = b[:i0] + "┃" + b[i0 + 1:i1] + "┃" + b[i1 + 1:]
    return [entete, b, t("partielle", lang, _jour(sp[0], lang),
                         _jour(sp[1], lang))]


def _seuil(nom, e, kwargs, lang):
    """Une fonction à seuil se lit par sa CONDITION, pas par ses réglages.

    `where='<='` plus `lim=upLim` décrivent une comparaison : l'écrire
    `VC10 <= upLim` dit en huit caractères ce que trois kwargs cachaient,
    et rend inutile la glose qui énumérait les valeurs possibles de
    `where`.
    """
    col = e["cols"][0] if e["cols"] else "X"
    if nom == "deficit_volume":
        lim = kwargs.pop("threshold", None)
        return [t("sous", lang, lim)] if lim else []
    op = kwargs.pop("where", "<=")
    lim = kwargs.pop("lim", None)
    bouts = [f"{col} {op} {lim}"] if lim else []
    sel = kwargs.pop("select", None)
    if sel:
        bouts.append(t(f"{sel}_ep", lang) if f"{sel}_ep" in _T
                     else t(sel, lang) if sel in _T else f"select={sel}")
    quoi = kwargs.pop("what", None)
    if quoi:
        bouts.append(t(quoi, lang) if quoi in _T else f"what={quoi}")
    return bouts


def _arguments(e):
    """Les arguments positionnels de l'appel, colonnes ET littéraux.

    Ne montrer que les colonnes faisait disparaître le reste du calcul :
    `[ratio_longest_run, "dQXA", 2]` s'affichait `ratio_longest_run(dQXA)`,
    et rien ne disait plus que le seuil de crue de dtFlood vaut la MOITIÉ
    du maximum annuel. C'était l'information la plus utile de la ligne.
    Un entier s'écrit sans décimale, `2` et non `2.0`, sinon la fiche
    semble dire une précision qu'elle n'a pas.
    """
    bouts = []
    for genre, valeur in e["pos_args"]:
        if genre == "col":
            bouts.append(str(valeur))
        elif isinstance(valeur, float) and valeur.is_integer():
            bouts.append(str(int(valeur)))
        else:
            bouts.append(str(valeur))
    return bouts


def appel(e, connues, lang="fr"):
    """(appel, références de colonnes, réglages, mention).

    `over_period` est une enveloppe : afficher son nom cacherait ce que
    la fiche calcule vraiment. On montre la fonction enveloppée et on
    renvoie la restriction en mention.
    """
    kwargs = dict(e["kwargs"])
    nom = e["fn_name"]
    mention = ""
    if nom == "over_period":
        nom = str(kwargs.pop("func", nom))
        mention = t("restreint", lang)
    regl = []
    if nom in ("apply_threshold", "deficit_volume"):
        regl = _seuil(nom, e, kwargs, lang)
    refs = []
    for k, v in kwargs.items():
        if isinstance(v, str) and (v in connues or v.lower() == "date"):
            refs.append(v)
        else:
            regl.append(f"{k}={v}")
    return f"{nom}({', '.join(_arguments(e))})", refs, regl, mention


def etapes(c, lang="fr"):
    connues = {v.rstrip("? ").strip()
               for v in str(c["meta"]["global"].get("input_vars", "")).split(",")}
    for p in c["processes"]:
        fns = [(e["name"], *appel(e, connues, lang)) for e in p["func"]]
        yield p["name"], fns, p
        connues |= {e["name"] for e in p["func"]}


def periodes_comparees(c):
    """Les bornes de période référencées par les fonctions, dans l'ordre :
    une fiche de changement compare deux fenêtres, il faut le montrer."""
    vues = []
    for p in c["processes"]:
        for e in p["func"]:
            for v in e["kwargs"].values():
                if isinstance(v, str) and v.endswith(("_start", "_end")) and v not in vues:
                    vues.append(v)
    return vues


# (time_step, compress) du dernier process -> granularité des lignes.
# Chaque entrée a été vérifiée par une extraction réelle, pas déduite :
# QA 13 lignes pour 12 années, QM 12, QJD 365, QMA_month et
# QSA_season une ligne par année, Bias_season une seule ligne.
_LIGNES = {
    ("year", False): "l_annee",
    ("month", False): "l_mois",
    ("yearday", False): "l_jour",
    ("year-month", True): "l_annee_mois",
    ("year-season", True): "l_annee_saisons",
    ("season", True): "l_saisons",
}


def bloc_sortie(c, meta, lang="fr"):
    """Ce que la fiche DÉCLARE produire, et rien de plus.

    Ce bloc annonçait l'axe d'une courbe, deviné du nom de la variable,
    et une granularité déduite du pas de temps. Mesure faite,
    `time_step: none` donne une ligne pour BFM, 365 pour QJC10 et 1000
    pour FDC : cela dépend de ce que la fonction retourne, pas de la
    fiche. La granularité n'est donc annoncée que pour les pas de temps
    où elle a été vérifiée, et l'axe d'une courbe ne l'est plus du tout.
    """
    p = c["processes"][-1]
    ids = [str(v) for v in meta["variable_en"]]
    cle = _LIGNES.get((p["time_step"], bool(p["compress"])))
    # Répéter le dernier nœud sans rien y ajouter alourdirait pour rien :
    # la ligne ne sert que si les colonnes diffèrent du nœud (mois
    # démultipliés) ou si la granularité des lignes est connue.
    out = []
    if cle or set(ids) != {e["name"] for e in p["func"]}:
        # Au-delà de six, l'en-tête les a déjà listées : les répéter ici
        # ferait deux fois douze noms pour une seule information.
        ligne = (t("sortie_n", lang, len(ids)) if len(ids) > 6
                 else t("sortie", lang, ", ".join(ids)))
        if cle:
            ligne += SEP + t(cle, lang)
        out = [""] + plie(ligne, "  ")
    bornes = periodes_comparees(c)
    if str(meta.iloc[0]["output_en"]) == "scalar" and len(bornes) >= 4:
        a, b = bornes[:2], bornes[2:4]
        out += ["", f"  {t('compare', lang)}",
                f"     ├── {a[0]} ─────── {a[1]} ──┤",
                f"                              ├── {b[0]} ─────── {b[1]} ──┤"]
    return out


def entete(c, meta, lang="fr"):
    """Titre, facettes, et la liste des sorties quand il y en a plusieurs.

    L'unité monte dans les facettes quand elle vaut pour toutes les
    sorties, et descend par sortie sinon : annoncer « jour de l'année »
    pour une fiche qui produit aussi un volume serait faux.
    """
    r = meta.iloc[0]
    ident = c["id"]
    # Aligner sous l'identifiant est joli tant qu'il est court ; `delta-
    # allLF_winter_H` pousserait la liste des sorties hors de l'écran.
    marge = " " * len(ident) if len(ident) <= 10 else " "
    ids = [str(v) for v in meta["variable_en"]]
    trads = [str(v) for v in meta["variable_fr" if lang == "fr" else "variable_en"]]
    unites = [unite(u) for u in meta["unit_fr" if lang == "fr" else "unit_en"]]
    noms = [str(n) for n in meta["name_fr" if lang == "fr" else "name_en"]]
    une_unite = len(set(unites)) == 1

    # Un nom UNIQUE pour plusieurs sorties est une convention du corpus,
    # pas un hasard : ce sont les coordonnées d'un même objet, les deux
    # axes d'une FDC. Ce nom EST le titre de la fiche, et le remplacer
    # par « 2 sorties : FDC_p, FDC_Q » perdait la seule phrase qui disait
    # de quoi la fiche parle.
    nom_commun = noms[0] if len(set(noms)) == 1 else None
    if nom_commun:
        titre = nom_commun
    elif len(meta) > 6:                  # la liste tient sur sa propre ligne
        titre = t("sorties_n", lang, len(meta))
    else:
        titre = t("sorties", lang, len(meta), ", ".join(ids))
    out = plie(titre, f"{ident}  ", f"{marge}  ")

    facettes = [r[f"phenomenon_{lang}"], r[f"season_{lang}"], r[f"output_{lang}"]]
    if une_unite and not _vide(unites[0]):
        facettes.insert(0, unites[0])
    out += plie(SEP.join(str(x) for x in facettes if not _vide(x)), f"{marge}  ")

    # Une description PAR SORTIE se lit sous sa sortie, pas au pied de la
    # figure : là, une seule des cinq s'afficherait et ferait passer
    # « décembre, janvier et février » pour la définition de la fiche
    # entière. Le pied ne reçoit donc que la description qui vaut pour
    # toutes, et celles qui diffèrent remontent ici.
    descs = [str(d) for d in meta[f"description_{lang}"]]
    par_sortie = descs if len(set(descs)) > 1 else [""] * len(descs)

    if 1 < len(meta) <= 6:
        for i, tr, u, n, d in zip(ids, trads, unites, noms, par_sortie):
            alias = f" ({tr})" if tr != i else ""
            mesure = "" if une_unite or _vide(u) else f" [{u}]"
            # Le nom déjà pris comme titre ne se répète pas sous chaque
            # sortie : la FDC l'affichait deux fois à l'identique.
            suite = "" if n == nom_commun else f"{SEP}{n}"
            out += plie(f"{i}{alias}{mesure}{suite}",
                        f"{marge}  {PUCE} ", f"{marge}    ")
            if not _vide(d):
                out += plie(d, f"{marge}    ", f"{marge}    ")
    elif len(meta) > 6:
        # Au-delà, les noms sont systématiques (un par mois, par saison) :
        # les lire ligne à ligne n'apprend rien de plus que la facette.
        # Leurs descriptions non plus, qui ne diffèrent que par le mois et
        # redisent le nom : douze d'entre elles feraient trente-six lignes
        # avant même la chaîne de calcul.
        out += plie(", ".join(ids), f"{marge}  {PUCE} ", f"{marge}    ")
    return out + [""]


def entrees(r, lang="fr"):
    """Ligne d'entrée : la variable avec son unité, les paramètres
    facultatifs annoncés comme tels plutôt que suffixés d'un `?`."""
    reg = input_registry()
    obl, opt = [], []
    for v in str(r["input_vars"]).split(","):
        v = v.strip()
        (opt if v.endswith("?") else obl).append(v.rstrip("? ").strip())

    def decore(v):
        u = unite((reg.get(v) or {}).get("unit") or "")
        return f"{v} [{u}]" if u else v

    ligne = SEP.join(decore(v) for v in obl)
    if opt:
        mot = t("facultatifs" if len(opt) > 1 else "facultatif", lang)
        ligne += f"{SEP}{', '.join(opt)} ({mot})"
    return "  " + ligne


def _sans_redite(regl, note, identifiants):
    """Un réglage que la phrase de la fiche dit déjà ne se répète pas.

    `p=0.01` sous « quantile à la probabilité de dépassement de 1 % » est
    du bruit : la phrase le dit mieux, et en toutes lettres. Les réglages
    que la phrase tait, eux, restent, car rien d'autre ne les dit
    (`select=dQXA`, `water_type=low`).

    Les identifiants sont retirés du texte d'abord : le « 10 » de `VC10`
    n'est pas le `k=10` d'une moyenne mobile.
    """
    if not note:
        return regl
    prose = note
    for nom in sorted((n for n in identifiants if any(c.isdigit() for c in n)),
                      key=len, reverse=True):
        prose = re.sub(rf"(?<![\w-]){re.escape(nom)}(?![\w-])", " ", prose)
    dits = {float(x.replace(",", ".")) for x in re.findall(r"\d+(?:[.,]\d+)?", prose)}
    garde = []
    for r in regl:
        try:
            v = float(r.split("=", 1)[-1])
        except ValueError:
            garde.append(r)
            continue
        if v not in dits and v * 100 not in dits:
            garde.append(r)
    return garde


def rendu(c, meta, lang="fr"):
    out = entete(c, meta, lang)
    out.append(entrees(meta.iloc[0], lang))
    identifiants = _method.known_names(c)
    for _, fns, p in etapes(c, lang):
        out.append("   │")
        multi = len(fns) > 1
        vues = set()                 # une note répétée n'est plus une note
        for sortie, ap, refs, regl, mention in fns:
            note = _method.step_text(c, lang, p, sortie)
            regl = _sans_redite(regl, note, identifiants)
            tete = f"{sortie} = " if multi else ""
            ligne = f"   ├─ {tete}{ap}" + (f"   {', '.join(regl)}" if regl else "")
            if len(ligne) <= LARGEUR:
                out.append(ligne)
            else:                        # les réglages passent en gouttière
                out.append(f"   ├─ {tete}{ap}")
                out += plie(", ".join(regl), "   │    ")
            annexes = []
            if mention:
                annexes.append(mention)
            if refs:
                annexes.append(t("dapres", lang, ", ".join(refs)))
            # La phrase de la FICHE, pas celle de la fonction. Une
            # docstring est attachée à une fonction, donc elle ne peut
            # dire que du général : `apply_threshold` mesurait ici une
            # durée de crue et datait ailleurs un début d'étiage, sous
            # la même glose. `method` est écrit par étape.
            if note:
                annexes.append(note)
            for a in annexes:
                if a in vues:
                    continue
                vues.add(a)
                out += plie(a, "   │    ")
        detail = [decoupe(p, lang)]
        if p["max_na_pct"] is not None:
            detail.append(t("lacunes", lang, p["max_na_pct"]))
        if p["max_na_years"] is not None:
            detail.append(t("trou", lang, p["max_na_years"]))
        out += plie(SEP.join(detail), "   │  ")
        for ligne in bande_annee(p["sampling_period"], lang):
            out.append(f"   │  {ligne}")
        out.append("   ▼")
        out += plie(", ".join(f[0] for f in fns), "  ")
    return "\n".join(out + bloc_sortie(c, meta, lang))


def figure(nom, path=None, lang="fr"):
    """Figure texte d'une fiche, prête à imprimer.

    Reprend ce que la liste de champs disait en plus : description
    éventuelle, version et identifiant pérenne, chemin dans le corpus.
    Rien n'est perdu, tout est mieux placé.
    """
    from .extraction import _find_cards, _DEFAULT_CARD_DIR, _corpus_path
    from . import suffix as _sfx
    if lang not in ("fr", "en"):
        raise ValueError(f"lang='{lang}' invalide : 'fr' ou 'en'.")
    trouve = _find_cards(path or _DEFAULT_CARD_DIR, [nom])
    c = load_card(trouve[nom])
    # forme par défaut d'une fiche à placeholders, jamais l'accolade
    ml = c["meta"][lang]
    c = {**c, "meta": {**c["meta"], lang: {
        **ml, **_sfx.apply(ml, _sfx.default_record(ml),
                           card_id=c.get("id"), lang=lang, key=None)}}}
    meta = _meta_frame(c)
    # Trois blocs séparés d'une ligne vide : la chaîne, la description,
    # la provenance. La séparation était comptée à la main et il en
    # manquait une, si bien que la description semblait continuer le bloc
    # de sortie.
    blocs = [rendu(c, meta, lang)]
    # Une description par sortie ne décrit pas la fiche : celle de la
    # première sortie affichée seule ferait passer « décembre, janvier et
    # février » pour la définition d'une fiche saisonnière entière.
    descs = {str(d) for d in meta[f"description_{lang}"] if not _vide(d)}
    if len(descs) == 1:
        blocs.append("\n".join(textwrap.wrap(
            descs.pop(), 70, initial_indent="  ", subsequent_indent="  ")))
    # Provenance. Un chemin de corpus (comme une URL) ne se coupe pas :
    # si `id v… · chemin` déborde, on met le chemin sur sa propre ligne.
    # L'identifiant pérenne sert à être ouvert : une URL est cliquable
    # dans un terminal, un swh:1:cnt: nu ne dit pas où le porter.
    ident = f"{c['id']} v{c.get('version')}"
    chemin = _corpus_path(c["path"])
    prov = (f"  {ident}{SEP}{chemin}" if len(ident) + len(SEP) + len(chemin) + 2 <= LARGEUR
            else f"  {ident}\n  {chemin}")
    blocs.append(f"{prov}\n  {SWH}{c.get('swhid')}")
    return "\n\n".join(blocs)
