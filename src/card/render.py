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

# Mise en page. Les étiquettes s'alignent à DROITE contre la colonne des
# valeurs : l'œil descend une colonne nette au lieu de sauter d'un mot à
# l'autre. L'arbre se pose un peu à gauche de cette colonne, assez pour
# ne pas flotter au milieu, assez peu pour rester dans le bloc.
COL_ETIQ = 15
COL_VAL = COL_ETIQ + 3
COL_ARBRE = COL_ETIQ - 3
GESTE = "└─ "               # ce que l'étape fait, la phrase de la fiche
SORTIE = "◇ "               # une sortie de la fiche, en tête de figure
REGLAGE = " ◦ "             # un paramètre : décalé d'un cran, il se pose
                            #   sous la BARRE du └─ et non sous son angle,
                            #   qui est structurel et pend sous l'appel
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
    "unique": ("aucune agrégation temporelle", "no temporal aggregation"),
    "sortie": ("sortie : {}", "output: {}"),
    "l_annee": ("une ligne par année", "one row per year"),
    "l_mois": ("une ligne par mois", "one row per month"),
    "l_jour": ("une ligne par jour de l'année", "one row per day of year"),
    "l_annee_mois": ("une ligne par année, les mois en colonnes",
                     "one row per year, months as columns"),
    "l_annee_saisons": ("une ligne par année, les saisons en colonnes",
                        "one row per year, seasons as columns"),
    "l_saisons": ("une ligne par série, les saisons en colonnes",
                  "one row per series, seasons as columns"),
    "restreint": ("restreint à la période demandée",
                  "restricted to the requested period"),
    "dapres": ("d'après {}", "from {}"),
    "sous": ("sous {}", "below {}"),
    "sorties": ("{} sorties : {}", "{} outputs: {}"),
    "sorties_n": ("{} sorties", "{} outputs"),
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
    # Étiquettes : une valeur seule ne se devine pas, « jour » ne dit
    # pas s'il s'agit d'une unité ou d'un thème.
    "e_phenomene": ("phénomène", "phenomenon"),
    "e_saison": ("saison", "season"),
    "e_forme": ("forme", "form"),
    "e_unite": ("unité", "unit"),
    "e_but": ("finalité", "purpose"),
    "e_entree": ("entrée", "input"),
    "e_entrees": ("entrées", "inputs"),
    "jour_seul": ("une valeur par jour", "one value per day"),
    "diffusee": ("une seule valeur, répétée sur toute la chronique",
                 "a single value, repeated over the whole record"),
    "f_adaptative": ("fenêtre adaptative, propre à chaque série",
                     "adaptive window, specific to each series"),
    "f_annee": ("fenêtre du {} au {}", "window from {} to {}"),
    "f_partielle": ("fenêtre partielle, du {} au {}",
                    "partial window, from {} to {}"),
    "coupee": ("coupée au-delà de {} années manquantes",
               "cut beyond {} missing years"),
    "lacunes_max": ("au plus {} % de lacunes", "at most {} % missing"),
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
        return t("jour_seul" if transforme else "diffusee", lang)
    return t("unique", lang)


def bande_annee(sp, lang="fr"):
    """Bande de 12 mois. Une année complète n'est pas un pavé plein : ce
    qui compte est OÙ elle commence, marqué d'un trait."""
    if sp is None:
        return []
    entete = "".join(f"{m}  " for m in MOIS)
    if isinstance(sp, dict):
        return [entete, "▓" * 36, t("f_adaptative", lang)]
    if isinstance(sp, str):
        i = (int(sp[:2]) - 1) * 3
        b = "▓" * 36
        b = b[:i] + "┃" + b[i + 1:]
        deb = _dt.date(2001, int(sp[:2]), int(sp[3:]))
        veille = deb - _dt.timedelta(days=1)
        return [entete, b, t("f_annee", lang, _jour(sp, lang),
                             _jour(veille.strftime("%m-%d"), lang))]
    d, f = int(sp[0][:2]), int(sp[1][:2])

    def dedans(i):
        return (d <= i <= f) if d <= f else (i >= d or i <= f)

    b = "".join("▓▓▓" if dedans(i + 1) else "···" for i in range(12))
    i0, i1 = (d - 1) * 3, f * 3 - 1
    b = b[:i0] + "┃" + b[i0 + 1:i1] + "┃" + b[i1 + 1:]
    return [entete, b, t("f_partielle", lang, _jour(sp[0], lang),
                         _jour(sp[1], lang))]


def _seuil(nom, e, kwargs, lang):
    """Une fonction à seuil se lit par sa CONDITION, pas par ses réglages.

    `where='<='` plus `lim=upLim` décrivent une comparaison : l'écrire
    `VC10 <= upLim` dit en huit caractères ce que trois kwargs cachaient,
    et rend inutile la glose qui énumérait les valeurs possibles de
    `where`.
    """
    col = e["cols"][0] if e["cols"] else "X"
    if "threshold" in kwargs:
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
    # Rien ne se déduit d'un NOM de fonction : une chaîne qui en nomme
    # une est un lien que ni l'import, ni le linter, ni les tests ne
    # suivent, et c'est ce qui a fait mentir ce module deux fois en
    # juillet 2026. Ce qui se lit, c'est l'APPEL. Une fonction qui reçoit
    # une autre fonction en kwarg est une enveloppe ; une fonction qui
    # reçoit `lim` ou `threshold` compare à un seuil.
    if callable(kwargs.get("func")) or isinstance(kwargs.get("func"), str):
        nom = str(kwargs.pop("func", nom))
        mention = t("restreint", lang)
    regl = []
    if "lim" in kwargs or "threshold" in kwargs:
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


def frise(c, meta, lang="fr"):
    """Les deux fenêtres qu'une fiche de changement compare.

    Une fiche `delta-` calcule un écart entre une période de référence et
    un horizon, et c'est la seule chose que la chaîne de calcul ne montre
    pas : les bornes arrivent en colonnes d'entrée, jamais en paramètres.
    D'où ce dessin, qui les met face à face.

    Les deux barres se décalent pour se chevaucher, et les tirets se
    règlent sur la place restante : quatre noms de bornes tiennent dans
    la largeur, quels qu'ils soient.
    """
    if str(meta.iloc[0]["output_en"]) != "scalar":
        return []
    bornes = periodes_comparees(c)
    if len(bornes) < 4:
        return []
    a, b = bornes[:2], bornes[2:4]
    marge = 7
    decalage = 8
    # place restante une fois posés les deux couples et le décalage
    fixe = sum(len(x) for x in a + b) + marge + decalage + 16
    tirets = max((LARGEUR - fixe) // 2, 3)

    def barre(depart, fin):
        return f"├─ {depart} " + "─" * tirets + f" {fin} ─┤"

    return ["", *plie(t("compare", lang), " " * 5 + SORTIE, " " * 7),
            " " * marge + barre(*a),
            " " * (marge + decalage + len(a[0]) + tirets) + barre(*b)]


def cadre(ident, titre):
    """Identité de la fiche, encadrée : identifiant à gauche, nom à droite.

    Le cadre est étiré à la largeur de la figure, identique d'une fiche à
    l'autre : on reconnaît une figure de fiche d'un coup d'œil. Un titre
    trop long se replie DANS le cadre plutôt que de l'élargir.
    """
    # Largeur INTÉRIEURE du cadre, celle des tirets de la bordure. Tout
    # le reste s'en déduit, sinon le contenu et le bord se décalent.
    dedans = LARGEUR - 6
    ECART = 3            # respiration minimale entre l'identifiant et le nom
    # `place` est la colonne où le titre s'aligne à droite ; il se replie
    # plus tôt, pour que l'écart existe toujours. Confondre les deux
    # collait le nom à l'identifiant ET décalait le bord du cadre.
    place = dedans - 2 - len(ident)
    lignes = textwrap.wrap(titre, max(place - ECART, 20)) or [""]
    out = ["  ╭" + "─" * (dedans + 2) + "╮",
           f"  │  {ident}{lignes[0]:>{place}}  │"]
    for suite in lignes[1:]:
        out.append(f"  │  {'':{len(ident)}}{suite:>{place}}  │")
    return out + ["  ╰" + "─" * (dedans + 2) + "╯"]


def etiquette(cle, valeur, lang="fr"):
    """« phénomène ─ hautes eaux » : la valeur ne se devine plus.

    Les étiquettes s'alignent à DROITE contre la colonne des valeurs. La
    valeur, elle, garde sa casse d'origine : ce sont des mots-clés du
    vocabulaire de classification, pas des phrases.
    """
    e = t(cle, lang)
    return plie(str(valeur), f"{e:>{COL_ETIQ}} ─ ", " " * COL_VAL)


def entete(c, meta, lang="fr"):
    """Cadre d'identité, description, puis les facettes en étiquettes."""
    r = meta.iloc[0]
    ids = [str(v) for v in meta["variable_en"]]
    trads = [str(v) for v in meta["variable_fr" if lang == "fr" else "variable_en"]]
    unites = [unite(u) for u in meta["unit_fr" if lang == "fr" else "unit_en"]]
    noms = [str(n) for n in meta["name_fr" if lang == "fr" else "name_en"]]
    une_unite = len(set(unites)) == 1
    nom_commun = noms[0] if len(set(noms)) == 1 else None

    out = cadre(c["id"], nom_commun or t("sorties_n", lang, len(meta)))

    # Ce qui dit de quoi parle la fiche vient juste sous le titre : sa
    # description quand elle en a une, sinon la liste de ses sorties. Les
    # facettes, qui la classent, viennent après.
    descs = [str(d) for d in meta[f"description_{lang}"]]
    commune = descs[0] if len(set(descs)) == 1 and not _vide(descs[0]) else None

    if commune:
        out += [""] + plie(commune, " " * 5, " " * 5)
    if len(meta) > 1:
        # Un tableau ne se lit que si ses colonnes s'alignent : chacune
        # prend la largeur de son plus long contenu, calculée avant
        # d'écrire la première ligne.
        par_sortie = descs if len(set(descs)) > 1 else [""] * len(descs)
        for i, tr, u, n, d in zip(ids, trads, unites, noms, par_sortie):
            out.append("")
            libelle = f" ({tr})" if tr != i else ""
            out += plie(f"{i}{libelle}", " " * 5 + SORTIE, " " * 7)
            if n != nom_commun:
                out += plie(n, " " * 7, " " * 7)
            if not _vide(d):
                out += plie(d, " " * 7, " " * 7)
            # Ce qui varie d'une sortie à l'autre reprend une étiquette,
            # exactement comme les facettes en tête : l'étiquette
            # apparaît là où la valeur seule ne se devine pas.
            if not une_unite and not _vide(u):
                out += etiquette("e_unite", u, lang)

    out.append("")
    for cle, valeur in (("e_phenomene", r[f"phenomenon_{lang}"]),
                        ("e_saison", r[f"season_{lang}"]),
                        ("e_forme", r[f"output_{lang}"]),
                        ("e_but", r[f"purpose_{lang}"])):
        if not _vide(valeur):
            out += etiquette(cle, valeur, lang)
    if une_unite and not _vide(unites[0]):
        out += etiquette("e_unite", unites[0], lang)
    out += etiquette("e_entree" if str(r["input_vars"]).count(",") == 0
                     else "e_entrees", entrees(r, lang), lang)
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

    ligne = ", ".join(decore(v) for v in obl)
    if opt:
        mot = t("facultatifs" if len(opt) > 1 else "facultatif", lang)
        ligne += f", {', '.join(opt)} ({mot})"
    return ligne


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
    """La chaîne de calcul, posée un peu à gauche de la colonne des valeurs.

    Chaque information commence par une MAJUSCULE et un repli s'indente
    de trois : une ligne qui continue se reconnaît sans marqueur, ce qui
    évite d'en inventer un de plus. Le `└─` pend sous l'appel et porte la
    phrase de la fiche ; le `◦` ouvre un paramètre du process.
    """
    marge = " " * COL_ARBRE
    out = entete(c, meta, lang)
    identifiants = _method.known_names(c)
    for _, fns, p in etapes(c, lang):
        out.append(f"{marge}╷")
        multi = len(fns) > 1
        for sortie, ap, refs, regl, mention in fns:
            note = _method.step_text(c, lang, p, sortie)
            regl = _sans_redite(regl, note, identifiants)
            # Un appel ouvre une petite branche : ses réglages et ses
            # mentions pendent sous un `│` qui continue, et la phrase de
            # la fiche la FERME par un `└─`. Sans cette continuité, les
            # lignes d'un appel se confondaient avec celles du suivant
            # dès qu'une étape en portait plusieurs.
            tete = f"{sortie} = " if multi else ""
            out.append(f"{marge}├── {tete}{ap}")
            branche = f"{marge}│   │  "
            # Ces lignes recopient l'appel : ce sont des fragments, pas
            # des phrases, donc pas de majuscule. Seules la phrase de la
            # fiche et les faits machine en prennent une.
            for a in (x for x in [", ".join(regl) if regl else "",
                                  mention,
                                  t("dapres", lang, ", ".join(refs)) if refs else ""]
                      if x):
                out += plie(a, branche, branche)
            if note:
                out += plie(_majuscule(note), f"{marge}│   {GESTE}",
                            f"{marge}│   {' ' * 3}")
        for fait in _faits(p, lang):
            out += plie(_majuscule(fait), f"{marge}│   {REGLAGE}",
                        f"{marge}│   {' ' * 3}")
        bande = bande_annee(p["sampling_period"], lang)
        if bande:
            mois, dessin, legende = bande[0], bande[1], bande[-1]
            out.append(f"{marge}│   {REGLAGE}{mois}")
            out.append(f"{marge}│   {' ' * 3}{dessin}")
            out += plie(_majuscule(legende), f"{marge}│   {' ' * 3}",
                        f"{marge}│   {' ' * 3}")
        out.append(f"{marge}▼")
        out += plie(", ".join(f[0] for f in fns), " " * (COL_ARBRE - 1))
    return "\n".join(out + frise(c, meta, lang))


def _majuscule(s):
    """Une information affichée est une phrase : elle prend sa majuscule.

    Le YAML, lui, reste en minuscule : une étape de `method` y est une
    phrase nominale dans une énumération. La capitale appartient à
    l'affichage, pas à la donnée.
    """
    return s[:1].upper() + s[1:] if s else s


def _faits(p, lang):
    """Les faits machine d'un process, un par item, jamais joints.

    Les joindre par un séparateur produisait une longue ligne qui se
    repliait, et le dernier mot orphelin se lisait comme un item de plus.
    """
    faits = [decoupe(p, lang)]
    if p["max_na_pct"] is not None:
        faits.append(t("lacunes_max", lang, p["max_na_pct"]))
    if p["max_na_years"] is not None:
        faits.append(t("coupee", lang, p["max_na_years"]))
    return faits


def figure(nom, path=None, lang="fr"):
    """Draw one card as text, ready to print.

    Parameters
    ----------
    nom : str
        Name of the card, such as ``"QA"``, ``"VCN10"``.
    path : str or pathlib.Path, optional
        Directory of YAML cards. Defaults to the cards shipped with the
        package.
    lang : {"fr", "en"}, default "fr"
        Language the figure is drawn in.

    Returns
    -------
    str
        The figure. Nothing is printed: this is what a web service
        needs, and what :func:`card.info` prints for a human.

    Notes
    -----
    The drawing carries what a flat list of fields could not place: the
    description when there is one, the version and the permanent
    identifier of the card file, and its path inside the corpus. Each
    step reads the sentence the CARD itself writes for that column.
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
    # La provenance se pose sous un filet, pas dans un cadre : le cadre
    # est réservé à l'identité, en haut. Un second l'aurait concurrencée.
    corps = rendu(c, meta, lang)
    ident = f"v{c.get('version')}"
    chemin = _corpus_path(c["path"])
    # Un chemin de corpus ne se coupe pas, comme une URL : s'il déborde
    # avec le numéro de version, il prend sa propre ligne.
    pied = ["  " + "─" * (LARGEUR - 4),
            f"  {ident}   {chemin}",
            f"  {SWH}{c.get('swhid')}"]
    return corps + "\n\n" + "\n".join(pied)
