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

Cinq principes.

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

Le rendu est généré depuis le YAML, jamais écrit à la main, et les 225
fiches du corpus passent, dans les deux langues.
"""

import datetime as _dt
import re
import textwrap

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
        reduit = all(e["fn_name"].startswith("nan")
                     or e["fn_name"] in ("quantile", "return_level")
                     for e in p["func"])
        return t("diffuse" if reduit else "transforme", lang)
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
    return f"{nom}({', '.join(e['cols'])})", refs, regl, mention


def glose(nom_fn):
    """Première phrase de la docstring, moins l'énumération des valeurs
    possibles d'un paramètre : la fiche en a déjà choisi une, lister les
    autres n'apprend rien sur ce qu'elle calcule."""
    if nom_fn.startswith("nan") or nom_fn in ("ratio", "difference"):
        return ""
    doc = (resolve(nom_fn).__doc__ or "").strip()
    doc = re.sub(r"\s+", " ", doc.split("\n\n")[0])
    # Couper à la première phrase, mais « (ex. » n'en termine pas une :
    # BFM s'affichait « ... des débits de base agrégés (ex », parenthèse
    # ouverte et phrase tranchée au milieu.
    coupe = re.split(r"\.(?:\s|$)", doc)[0]
    if coupe.count("(") > coupe.count(")"):
        coupe = coupe[:coupe.rfind("(")]
    doc = re.sub(r"\s*\([^()]*['\"][^()]*\)", "", coupe).strip(" .")
    return doc if len(doc) < 120 else ""


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

    if len(meta) == 1:
        titre = noms[0]
    elif len(meta) > 6:                  # la liste tient sur sa propre ligne
        titre = t("sorties_n", lang, len(meta))
    else:
        titre = t("sorties", lang, len(meta), ", ".join(ids))
    out = plie(titre, f"{ident}  ", f"{marge}  ")

    facettes = [r[f"phenomenon_{lang}"], r[f"season_{lang}"], r[f"output_{lang}"]]
    if une_unite and not _vide(unites[0]):
        facettes.insert(0, unites[0])
    out += plie(SEP.join(str(x) for x in facettes if not _vide(x)), f"{marge}  ")

    if 1 < len(meta) <= 6:
        for i, tr, u, n in zip(ids, trads, unites, noms):
            alias = f" ({tr})" if tr != i else ""
            mesure = "" if une_unite or _vide(u) else f" [{u}]"
            out += plie(f"{i}{alias}{mesure}{SEP}{n}",
                        f"{marge}  {PUCE} ", f"{marge}    ")
    elif len(meta) > 6:
        # Au-delà, les noms sont systématiques (un par mois, par saison) :
        # les lire ligne à ligne n'apprend rien de plus que la facette.
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


def rendu(c, meta, lang="fr"):
    out = entete(c, meta, lang)
    out.append(entrees(meta.iloc[0], lang))
    for _, fns, p in etapes(c, lang):
        out.append("   │")
        multi = len(fns) > 1
        vues = set()                 # une glose répétée n'est plus une glose
        for sortie, ap, refs, regl, mention in fns:
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
            gl = glose(ap.split("(")[0])
            if gl:
                annexes.append(gl)
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
    corps = rendu(c, meta, lang)
    pied = []
    # Une description par sortie ne décrit pas la fiche : celle de la
    # première sortie affichée seule ferait passer « décembre, janvier et
    # février » pour la définition d'une fiche saisonnière entière.
    descs = {str(d) for d in meta[f"description_{lang}"] if not _vide(d)}
    if len(descs) == 1:
        pied += [""] + textwrap.wrap(descs.pop(), 70, initial_indent="  ",
                                     subsequent_indent="  ")
    # L'identifiant pérenne sert à être ouvert : une URL est cliquable
    # dans un terminal, un swh:1:cnt: nu ne dit pas où le porter.
    if not pied:
        pied = [""]
    pied += ["", f"  {c['id']} v{c.get('version')}{SEP}{_corpus_path(c['path'])}",
             f"  {SWH}{c.get('swhid')}"]
    return corps + "\n".join(pied)
