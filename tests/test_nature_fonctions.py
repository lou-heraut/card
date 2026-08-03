"""Réduire ou transformer : la nature d'une fonction, VÉRIFIÉE.

`decoupe()` de `render.py` doit dire, pour un process `time_step: none`
et `keep: all`, si la fonction rend une valeur par pas de temps ou une
valeur unique diffusée sur la chronique. Elle lit pour cela
`is_transform`, propriété déclarée à côté de la fonction.

Ce fichier existe parce que la version précédente devinait cette nature
d'après le NOM (préfixe `nan`, plus deux noms écrits en dur). Le
renommage `compute_Qp` vers `exceedance_quantile` a laissé l'un de ces
noms derrière lui et six fiches ont annoncé « une valeur par jour » à
propos d'un seuil unique. La suite de tests était verte avant le
correctif et l'est restée après : elle ne couvrait pas le comportement.

D'où le parti pris ici : **ne rien croire sur parole, mesurer.** On
appelle chaque fonction avec les arguments que le corpus lui passe
vraiment, et on regarde si la sortie a la longueur de l'entrée. Une
déclaration fausse, une déclaration oubliée, ou une fonction ajoutée
sans verdict font rougir, sans qu'aucune liste de noms n'ait à être
tenue à jour à la main.
"""

import numpy as np

from card.extraction import _DEFAULT_CARD_DIR, _find_cards, resolve
from card.loader import load_card

N = 365 * 5
_jours = np.arange(N)
# Chronique de synthèse : positive (les fonctions de débit divisent et
# passent au log), saisonnière, et sans lacune. On ne teste pas ici la
# valeur rendue, seulement sa FORME.
SERIE = 10 + 8 * np.sin(2 * np.pi * _jours / 365.25) + 0.5 * ((_jours * 37) % 11)

# Le corpus n'emploie pas toutes les fonctions du paquet, alors qu'elles
# sont publiques (`card.functions`) et disponibles à qui écrit ses propres
# fiches. Celles-là n'ont pas d'appel réel dont s'inspirer : on donne ici
# de quoi les appeler, (kwargs, arguments positionnels). C'est le prix pour
# le test reste TOTAL, sans quoi une déclaration posée sur une fonction
# inemployée ne serait jamais confrontée à la réalité.
DEUX_SERIES = [("col", "a"), ("col", "b")]
RECETTES_HORS_CORPUS = {
    "difference": ({}, DEUX_SERIES),
    "circular_difference": ({"periodicity": 365.25}, DEUX_SERIES),
    "circular_ratio": ({"periodicity": 365.25}, DEUX_SERIES),
}

# Fonctions qu'on ne peut pas appeler hors du moteur : leurs arguments
# désignent des COLONNES (seuils, bornes de période, dates), que seule
# l'extraction sait fournir. Elles sont donc classées à la main, et cet
# ensemble est vérifié plus bas : il ne peut pas grossir en silence.
HORS_MESURE = {
    "apply_threshold",     # lim=, where=, dates=, period_* : colonnes
    "deficit_volume",      # threshold= : colonne
    "delta",               # ref_*/horizon_* : colonnes de bornes
    "elasticity",          # Q=, X= : colonnes
    "exceedance_frequency",  # threshold= : colonne
    "over_period",         # func= enveloppée, dates=, period_* : colonnes
    "return_period",       # threshold= : colonne
    # dates=/period_* sont des colonnes. Classée à la main le 2026-07-30 :
    # ajuste une loi (Gumbel ou log-normale) sur la série et rend LA valeur
    # de période de retour. Elle réduit, donc rien à déclarer.
    "return_level",
}


def _usages():
    """Chaque appel DISTINCT du corpus, avec son contexte.

    On dédoublonne sur (fonction, kwargs, arguments positionnels) : 226
    fiches font beaucoup d'appels identiques, et c'est l'appel qui se
    mesure, pas la fiche.
    """
    vus = {}
    for nom, chemin in sorted(_find_cards(_DEFAULT_CARD_DIR, None).items()):
        c = load_card(chemin)
        connues = {v.rstrip("? ").strip() for v in
                   str(c["meta"]["global"].get("input_vars", "")).split(",")}
        for proc in c["processes"]:
            none_all = (str(proc.get("time_step")) == "none"
                        and str(proc.get("keep")) == "all")
            for e in proc["func"]:
                # Un kwarg textuel qui nomme une colonne connue est une
                # RÉFÉRENCE, pas un réglage : même règle que render.appel.
                colonnes = {k for k, v in e["kwargs"].items()
                            if isinstance(v, str)
                            and (v in connues or v.lower() == "date")}
                cle = (e["fn_name"], repr(sorted(e["kwargs"].items())),
                       repr(e["pos_args"]), bool(colonnes))
                vus.setdefault(cle, (dict(e["kwargs"]), list(e["pos_args"]),
                                     bool(colonnes), set()))
                vus[cle][3].add(nom)
                if none_all:
                    vus[cle][3].add(f"{nom} [none/all]")
            connues |= {e["name"] for e in proc["func"]}
    return [(cle[0], *reste) for cle, reste in sorted(vus.items())]


def _mesure(fn_name, kwargs, pos_args):
    """Longueur de sortie contre longueur d'entrée, en vrai.

    `pos_args` vient de la fiche : ('col', nom) devient une chronique,
    ('lit', valeur) reste le littéral. Passer les littéraux compte : sans
    eux, `ratio(dQXA, 2, first=True)` ne s'appelait pas, la mesure rendait
    None, et l'ambiguïté de nature passait sous le radar.

    Rend True (transforme), False (réduit), ou None si la fonction n'a
    pas pu être appelée telle quelle.
    """
    fn = resolve(fn_name)
    args, i = [], 0
    for genre, valeur in (pos_args or [("col", "X")]):
        if genre == "col":
            args.append(SERIE.copy() * (1 + 0.1 * i))
            i += 1
        else:
            args.append(valeur)
    try:
        sortie = fn(*args, **kwargs)
    except Exception:                                # noqa: BLE001
        return None
    return np.ndim(sortie) > 0 and len(np.atleast_1d(sortie)) == N


USAGES = _usages()


def test_decoupe_annonce_la_nature_reellement_mesuree():
    """Le test de bout en bout : ce que la FIGURE affiche contre le fait.

    Les autres tests vérifient les déclarations ; celui-ci vérifie qu'on
    s'en sert. C'est le seul qui aurait rougi le jour du renommage, parce
    qu'il ne demande pas à `decoupe()` d'où elle tient son verdict, mais
    si son verdict est vrai.
    """
    from card.render import decoupe, t

    menteuses = []
    for nom, chemin in sorted(_find_cards(_DEFAULT_CARD_DIR, None).items()):
        c = load_card(chemin)
        for proc in c["processes"]:
            if not (str(proc.get("time_step")) == "none"
                    and str(proc.get("keep")) == "all"):
                continue
            mesures = [_mesure(e["fn_name"], dict(e["kwargs"]), e["pos_args"])
                       for e in proc["func"]]
            if any(m is None for m in mesures):
                continue        # hors de portée, couvert par le test suivant
            attendu = t("transforme" if all(mesures) else "diffuse")
            obtenu = decoupe(proc)
            if obtenu != attendu:
                menteuses.append(
                    f"{nom} {proc['name']} "
                    f"({', '.join(e['fn_name'] for e in proc['func'])}) : "
                    f"la figure annonce {obtenu!r}, la mesure dit {attendu!r}")
    assert not menteuses, "\n".join(menteuses)


def test_les_natures_declarees_sont_confirmees_par_la_mesure():
    """`is_transform` doit dire ce que la fonction fait, pas l'inverse.

    On n'exige pas que toutes les fonctions soient mesurables : on exige
    que celles qui le sont soient d'accord avec leur déclaration.
    """
    desaccords = []
    for fn_name, kwargs, pos_args, ref_colonne, fiches in USAGES:
        if ref_colonne:
            continue
        mesure = _mesure(fn_name, kwargs, pos_args)
        if mesure is None:
            continue
        declare = bool(getattr(resolve(fn_name), "is_transform", False))
        if declare != mesure:
            desaccords.append(
                f"{fn_name}{kwargs} : is_transform={declare}, mesuré={mesure} "
                f"(ex. {sorted(fiches)[0]}). "
                + ("Poser `is_transform = True` à côté de la fonction."
                   if mesure else
                   "Retirer `is_transform`, la fonction réduit."))
    assert not desaccords, "\n".join(desaccords)


def test_toute_fonction_employee_en_none_all_a_un_verdict_verifie():
    """Le cas où `decoupe()` consulte la nature ne tolère pas d'angle mort.

    C'est le garde-fou qui manquait : une fonction ajoutée ou renommée,
    employée en `time_step: none` / `keep: all` et que la mesure
    n'atteint pas, doit être classée à la main ICI, sciemment.
    """
    aveugles = []
    for fn_name, kwargs, pos_args, ref_colonne, fiches in USAGES:
        if not any(f.endswith("[none/all]") for f in fiches):
            continue
        if fn_name in HORS_MESURE:
            continue
        if ref_colonne or _mesure(fn_name, kwargs, pos_args) is None:
            aveugles.append(
                f"{fn_name}{kwargs} sert en none/all (ex. "
                f"{sorted(fiches)[0]}) sans que la mesure l'atteigne. "
                f"La classer dans HORS_MESURE avec sa raison, après avoir "
                f"vérifié à la main ce que la figure doit annoncer.")
    assert not aveugles, "\n".join(aveugles)


def test_hors_mesure_ne_contient_que_des_fonctions_reellement_hors_mesure():
    """Une exception qui n'en est plus une doit sortir de la liste.

    Sinon HORS_MESURE devient le dépotoir qu'on n'ose plus vider, et le
    test d'au-dessus perd sa force au fil des ans.
    """
    perimees = []
    for fn_name in sorted(HORS_MESURE):
        usages = [u for u in USAGES if u[0] == fn_name]
        assert usages, f"{fn_name} n'est plus employée par le corpus"
        if all(not u[3] and _mesure(fn_name, u[1], u[2]) is not None
               for u in usages):
            perimees.append(fn_name)
    assert not perimees, (
        f"{perimees} se mesurent maintenant : les retirer de HORS_MESURE.")


def test_une_fonction_na_quune_seule_nature_quels_que_soient_ses_arguments():
    """Une fonction transforme, ou elle réduit. Jamais les deux.

    C'est la règle qui rend `is_transform` énonçable : un booléen posé sur
    une fonction ne peut pas décrire deux comportements. `ratio` en avait
    deux, séparés par un drapeau `first`, et il a fallu le scinder en
    `ratio` et `ratio_longest_run` (2026-07-31, RENAMING.md).

    Le test ne nomme personne : il mesure chaque fonction avec CHACUN des
    jeux d'arguments que le corpus lui passe, et refuse qu'une même
    fonction change de nature d'un appel à l'autre. Un drapeau du même
    genre, réintroduit demain sous un autre nom, rougirait ici.
    """
    natures = {}
    for fn_name, kwargs, pos_args, ref_colonne, fiches in USAGES:
        if ref_colonne:
            continue
        mesure = _mesure(fn_name, kwargs, pos_args)
        if mesure is None:
            continue
        natures.setdefault(fn_name, {}).setdefault(mesure, []).append(
            f"{kwargs} (ex. {sorted(fiches)[0]})")

    ambigues = []
    for fn_name, par_nature in sorted(natures.items()):
        if len(par_nature) > 1:
            ambigues.append(
                f"{fn_name} transforme avec {par_nature[True]} et réduit "
                f"avec {par_nature[False]}. Scinder en deux fonctions : "
                f"la nature ne peut pas dépendre d'un argument.")
    assert not ambigues, "\n".join(ambigues)


def test_les_transformations_declarees_le_sont_a_bon_escient():
    """Une déclaration `is_transform = True` inutile est un mensonge dormant.

    Elle ne se voit pas tant que la fonction ne sert pas en `none`/`all`,
    et affirme alors une valeur par pas de temps sans que rien ne l'ait
    vérifié. Toute déclaration du paquet doit donc être mesurable.
    """
    import inspect

    from card import functions

    non_verifiees = []
    for module_nom in dir(functions):
        module = getattr(functions, module_nom)
        if not inspect.ismodule(module):
            continue
        for nom, obj in vars(module).items():
            if not (inspect.isfunction(obj)
                    and getattr(obj, "is_transform", False)):
                continue
            # On la mesure avec les arguments que le corpus lui donne ;
            # à défaut d'usage, avec la recette déclarée ci-dessus.
            essais = ([(u[1], u[2]) for u in USAGES if u[0] == nom]
                      or ([RECETTES_HORS_CORPUS[nom]]
                          if nom in RECETTES_HORS_CORPUS else []))
            if not essais:
                non_verifiees.append(
                    f"{module_nom}.{nom} (aucun usage du corpus, aucune "
                    f"recette : en ajouter une à RECETTES_HORS_CORPUS)")
            elif not any(_mesure(nom, kw, n) is True for kw, n in essais):
                non_verifiees.append(f"{module_nom}.{nom} (mesure démentie)")
    assert not non_verifiees, (
        f"{sorted(set(non_verifiees))} déclarent is_transform = True sans "
        f"qu'aucune mesure ne le confirme.")
