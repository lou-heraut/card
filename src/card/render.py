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

Trois principes.

**La figure suit la forme de sortie**, qui est déjà une facette de la
classification. Une série se lit sur un axe de temps, d'où la bande de
douze mois. Un scalaire de changement compare deux fenêtres, d'où la
frise. Une courbe a son propre axe, qu'il faut nommer. Rien à inventer :
le corpus classe déjà ses fiches ainsi.

**Un kwarg qui nomme une colonne est une référence, pas un réglage.**
`delta(QA, date)` suivi de « d'après ref_start, ref_end » se lit, là où
l'appel brut fait cent caractères illisibles.

**Une enveloppe se déplie.** `over_period` sert à restreindre une
période ; afficher son nom cacherait que la fiche calcule une moyenne.
On montre la fonction enveloppée et la restriction en mention.

Le rendu est généré depuis le YAML, jamais écrit à la main, et les 225
fiches du corpus passent.
"""

import datetime as _dt
import re
import textwrap

from .extraction import _meta_frame, resolve
from .loader import load_card

MOIS = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
_EXP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def unite(u):
    u = re.sub(r"\^\{([-\d]+)\}", lambda m: m.group(1).translate(_EXP), str(u))
    return u.replace(".", "·")


def decoupe(p):
    """Ce que fait vraiment le pas de temps, `none` recouvrant deux cas
    opposés : transformer la série sans l'agréger, ou la réduire d'un
    coup."""
    ts = p["time_step"]
    if ts != "none":
        return {"year": "une valeur par année", "month": "une valeur par mois",
                "yearday": "une valeur par jour de l'année",
                "year-month": "une valeur par mois de chaque année",
                "season": "une valeur par saison",
                "year-season": "une valeur par saison de chaque année"}[ts]
    if p["keep"] == "all":
        return "transforme la série sans l'agréger, une valeur par jour"
    return "une seule valeur pour toute la chronique"


def bande_annee(sp):
    """Bande de 12 mois. Une année complète n'est pas un pavé plein : ce
    qui compte est OÙ elle commence, marqué d'un trait."""
    if sp is None:
        return []
    entete = "".join(f"{m}  " for m in MOIS)
    if isinstance(sp, dict):
        return [entete, "▓" * 36,
                "départ propre à chaque série (adaptatif), année complète"]
    if isinstance(sp, str):
        i = (int(sp[:2]) - 1) * 3
        b = "▓" * 36
        b = b[:i] + "┃" + b[i + 1:]
        deb = _dt.date(2001, int(sp[:2]), int(sp[3:]))
        veille = deb - _dt.timedelta(days=1)
        return [entete, b,
                f"année complète, du {sp} au {veille.strftime('%m-%d')}"]
    d, f = int(sp[0][:2]), int(sp[1][:2])
    def dedans(i):
        return (d <= i <= f) if d <= f else (i >= d or i <= f)

    b = "".join("▓▓▓" if dedans(i + 1) else "···" for i in range(12))
    i0, i1 = (d - 1) * 3, f * 3 - 1
    b = b[:i0] + "┃" + b[i0 + 1:i1] + "┃" + b[i1 + 1:]
    return [entete, b, f"fenêtre partielle, du {sp[0]} au {sp[1]}"]


def appel(e, connues):
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
        mention = "restreint à la période demandée"
    refs, regl = [], []
    for k, v in kwargs.items():
        if isinstance(v, str) and (v in connues or v.lower() == "date"):
            refs.append(v)
        else:
            regl.append(f"{k}={v}")
    return f"{nom}({', '.join(e['cols'])})", refs, regl, mention


def glose(nom_fn):
    if nom_fn.startswith("nan") or nom_fn in ("ratio", "difference"):
        return ""
    doc = (resolve(nom_fn).__doc__ or "").strip()
    doc = re.sub(r"\s+", " ", doc.split(".")[0].split("\n\n")[0]).strip(" .")
    return doc if len(doc) < 120 else ""


def etapes(c):
    connues = {v.rstrip("? ").strip()
               for v in str(c["meta"]["global"].get("input_vars", "")).split(",")}
    for p in c["processes"]:
        fns = [(e["name"], *appel(e, connues)) for e in p["func"]]
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


def figure_sortie(c, meta):
    """La figure dépend de la FORME de sortie."""
    forme = str(meta.iloc[0]["output_fr"])
    bornes = periodes_comparees(c)
    if forme == "scalaire" and len(bornes) >= 4:
        a, b = bornes[:2], bornes[2:4]
        return ["", "  compare deux fenêtres, fournies en colonnes :",
                f"     ├── {a[0]} ─────── {a[1]} ──┤",
                f"                              ├── {b[0]} ─────── {b[1]} ──┤"]
    if forme == "scalaire":
        return ["", "  sortie : un nombre par série"]
    if forme == "courbe":
        n = len(meta)
        axe = ("probabilité de dépassement" if any("fdc" in str(v).lower()
               or "FDC" in str(v) for v in meta["variable_en"])
               else "jour de l'année")
        return ["", f"  sortie : une courbe en {n} coordonnée{'s' if n > 1 else ''}, "
                f"indexée par {axe}"]
    return ["", f"  sortie : une série, {decoupe(c['processes'][-1]).lower()}"]


def rendu(c, meta, compact=False):
    r = meta.iloc[0]
    ident = c["id"]
    fac = " · ".join(str(x) for x in (unite(r["unit_fr"]), r["phenomenon_fr"],
                                      r["season_fr"], r["output_fr"]) if str(x))
    titre = str(r["name_fr"])
    if len(meta) > 1:
        noms = ", ".join(str(v) for v in meta["variable_fr"])
        titre = f"{len(meta)} sorties : {noms}"
    out = [f"{ident}  {textwrap.shorten(titre, 68 - len(ident))}",
           f"{' ' * len(ident)}  {fac}", ""]
    if len(meta) > 1:
        for v, n in zip(meta["variable_fr"], meta["name_fr"]):
            out.insert(-1, f"{' ' * len(ident)}  · {v} : {textwrap.shorten(str(n), 56)}")
    ent = [v.strip() for v in str(r["input_vars"]).split(",")]
    out.append("  " + " · ".join(ent[:1] + [e.split(" ")[0] for e in ent[1:]]))
    for nom_p, fns, p in etapes(c):
        out.append("   │")
        for sortie, ap, refs, regl, mention in fns:
            out.append(f"   ├─ {ap}" + (f"   {', '.join(regl)}" if regl else ""))
            if mention:
                out.append(f"   │    {mention}")
            if refs:
                out.append(f"   │    d'après {', '.join(refs)}")
            gl = glose(ap.split("(")[0])
            if gl and not compact:
                for ligne in textwrap.wrap(gl, 62):
                    out.append(f"   │    {ligne}")
        detail = [decoupe(p)]
        if p["max_na_pct"] is not None:
            detail.append(f"max {p['max_na_pct']} % de lacunes")
        if p["max_na_years"] is not None:
            detail.append(f"max {p['max_na_years']} ans de trou")
        out.append(f"   │  {' · '.join(detail)}")
        for ligne in bande_annee(p["sampling_period"]):
            out.append(f"   │  {ligne}")
        out.append("   ▼")
        out.append("  " + ", ".join(f[0] for f in fns))
    return "\n".join(out + figure_sortie(c, meta))


def figure(nom, path=None, lang="fr", compact=False):
    """Figure texte d'une fiche, prête à imprimer.

    Reprend ce que la liste de champs disait en plus : description
    éventuelle, version et identifiant pérenne, chemin dans le corpus.
    Rien n'est perdu, tout est mieux placé.
    """
    from .extraction import _find_cards, _DEFAULT_CARD_DIR, _corpus_path
    from . import suffix as _sfx
    trouve = _find_cards(path or _DEFAULT_CARD_DIR, [nom])
    c = load_card(trouve[nom])
    # forme par défaut d'une fiche à placeholders, jamais l'accolade
    ml = c["meta"][lang]
    c = {**c, "meta": {**c["meta"], lang: {
        **ml, **_sfx.apply(ml, _sfx.default_record(ml),
                           card_id=c.get("id"), lang=lang, key=None)}}}
    meta = _meta_frame(c)
    if lang == "en":                      # _meta_frame rend les deux langues
        meta = meta.rename(columns=lambda x: x.replace("_en", "_fr")
                           if x.endswith("_en") else x)
    corps = rendu(c, meta, compact)
    pied = []
    desc = str(meta.iloc[0].get("description_fr") or "")
    if desc:
        pied += [""] + textwrap.wrap(desc, 70, initial_indent="  ",
                                     subsequent_indent="  ")
    pied += ["", f"  {c['id']} v{c.get('version')}  ·  {_corpus_path(c['path'])}",
             f"  {c.get('swhid')}"]
    return corps + "\n".join(pied)
