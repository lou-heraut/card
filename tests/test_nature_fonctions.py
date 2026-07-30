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
import pytest

from card.extraction import _DEFAULT_CARD_DIR, _find_cards, resolve
from card.loader import load_card

N = 365 * 5
_jours = np.arange(N)
# Chronique de synthèse : positive (les fonctions de débit divisent et
# passent au log), saisonnière, et sans lacune. On ne teste pas ici la
# valeur rendue, seulement sa FORME.
SERIE = 10 + 8 * np.sin(2 * np.pi * _jours / 365.25) + 0.5 * ((_jours * 37) % 11)

# Fonctions dont la nature dépend des ARGUMENTS, pas de la fonction :
# `ratio(a, b)` et `difference(a, b)` rendent une série quand on leur
# donne deux séries, un scalaire quand on leur donne deux scalaires ou
# quand `first=True`. Aucun booléen posé sur la fonction ne dirait le
# vrai dans les deux cas. Elles ne servent jamais en `none`/`all`
# aujourd'hui, où l'ambiguïté compterait : le test du bas veille à ce
# que cela reste vrai.
NATURE_VARIABLE = {"ratio", "difference"}

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

    On dédoublonne sur (fonction, arguments, nombre de colonnes) : 226
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
                       len(e["cols"]), bool(colonnes))
                vus.setdefault(cle, (dict(e["kwargs"]), len(e["cols"]),
                                     bool(colonnes), set()))
                vus[cle][3].add(nom)
                if none_all:
                    vus[cle][3].add(f"{nom} [none/all]")
            connues |= {e["name"] for e in proc["func"]}
    return [(cle[0], *reste) for cle, reste in sorted(vus.items())]


def _mesure(fn_name, kwargs, ncols):
    """Longueur de sortie contre longueur d'entrée, en vrai.

    Rend True (transforme), False (réduit), ou None si la fonction n'a
    pas pu être appelée telle quelle.
    """
    fn = resolve(fn_name)
    args = [SERIE.copy() * (1 + 0.1 * i) for i in range(max(ncols, 1))]
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
            mesures = [_mesure(e["fn_name"], dict(e["kwargs"]), len(e["cols"]))
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
    for fn_name, kwargs, ncols, ref_colonne, fiches in USAGES:
        if ref_colonne or fn_name in NATURE_VARIABLE:
            continue
        mesure = _mesure(fn_name, kwargs, ncols)
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
    for fn_name, kwargs, ncols, ref_colonne, fiches in USAGES:
        if not any(f.endswith("[none/all]") for f in fiches):
            continue
        if fn_name in HORS_MESURE:
            continue
        if ref_colonne or _mesure(fn_name, kwargs, ncols) is None:
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


@pytest.mark.parametrize("fn_name", sorted(NATURE_VARIABLE))
def test_les_fonctions_a_nature_variable_ne_servent_pas_en_none_all(fn_name):
    """`ratio` et `difference` suivent la forme de leurs entrées.

    Tant qu'elles ne servent pas en `none`/`all`, la figure n'a pas à
    trancher. Le jour où l'une y sert, ce test rougit et il faudra
    décider ce qu'on affiche, en regardant les arguments de l'appel.
    """
    coupables = [sorted(fiches)[0] for nom, _, _, _, fiches in USAGES
                 if nom == fn_name
                 and any(f.endswith("[none/all]") for f in fiches)]
    assert not coupables, (
        f"{fn_name} sert en time_step=none/keep=all ({coupables}), où sa "
        f"nature dépend des arguments. Décider ce que la figure annonce "
        f"avant d'aller plus loin.")


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
            # à défaut d'usage, avec ses seuls défauts.
            essais = [(u[1], u[2]) for u in USAGES if u[0] == nom] or [({}, 1)]
            if not any(_mesure(nom, kw, n) is True for kw, n in essais):
                non_verifiees.append(f"{module_nom}.{nom}")
    assert not non_verifiees, (
        f"{sorted(set(non_verifiees))} déclarent is_transform = True sans "
        f"qu'aucune mesure ne le confirme.")
