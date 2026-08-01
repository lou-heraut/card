"""Rendu texte d'une fiche.

Le rendu est généré depuis le YAML : il doit tenir sur n'importe quelle
fiche du corpus, sans exception, sinon il ne sert à rien.
"""

import pytest

from card.extraction import _DEFAULT_CARD_DIR
from card.render import figure, rendu
from card.loader import load_card
from card.extraction import _meta_frame


def _toutes():
    return sorted(p.stem for p in _DEFAULT_CARD_DIR.rglob("*.yaml"))


def test_le_corpus_entier_se_rend():
    """Aucune fiche ne doit faire tomber le rendu."""
    echecs = []
    for p in sorted(_DEFAULT_CARD_DIR.rglob("*.yaml")):
        try:
            c = load_card(p)
            assert rendu(c, _meta_frame(c))
        except Exception as e:                       # noqa: BLE001
            echecs.append(f"{p.stem}: {type(e).__name__}: {e}")
    assert not echecs, echecs[:5]


@pytest.mark.parametrize("lang", ["fr", "en"])
def test_le_corpus_entier_se_rend_dans_les_deux_langues(lang):
    """Une langue à moitié rendue vaut moins qu'une seule langue."""
    echecs = []
    for p in sorted(_DEFAULT_CARD_DIR.rglob("*.yaml")):
        try:
            figure(p.stem, lang=lang)
        except Exception as e:                       # noqa: BLE001
            echecs.append(f"{p.stem}: {type(e).__name__}: {e}")
    assert not echecs, echecs[:5]


def test_la_prose_suit_la_langue():
    """Métadonnées anglaises et prose française feraient du franglais."""
    f = figure("QA", lang="en")
    assert "one value per year" in f and "Annual mean" in f
    assert "année" not in f


def test_l_identifiant_prime_sur_le_nom_traduit():
    """Le lecteur retrouvera FDC_p dans ses données, jamais CDC_p."""
    f = figure("FDC")
    assert "2 sorties : FDC_p, FDC_Q" in f
    assert "CDC_p" in f, "le nom traduit reste visible, entre parenthèses"
    assert "sorties : CDC_p" not in f


def test_l_unite_descend_par_sortie_quand_elle_varie():
    """allLF sort trois dates, une durée et un volume : annoncer une
    seule unité en tête serait faux."""
    f = figure("allLF")
    assert "[jour de l'année]" in f and "[hm³]" in f
    assert "jour de l'année · basses eaux" not in f


def test_une_fonction_a_seuil_montre_sa_condition():
    """`where='<='` plus `lim=upLim` est une comparaison, pas deux
    réglages ; et la fiche a choisi son opérateur, lister les autres
    n'apprend rien."""
    f = figure("allLF")
    assert "VC10 <= upLim" in f
    assert "'>='" not in f, "l'énumération des where possibles est du bruit"
    assert f.count("Analyse des épisodes") == 1, "une glose répétée n'est plus une glose"


def test_chaque_sortie_dit_de_quelle_fonction_elle_vient():
    assert "startLF = apply_threshold(VC10)" in figure("allLF")


def test_la_description_d_une_seule_sortie_ne_decrit_pas_la_fiche():
    """QSA_season : « décembre, janvier et février » décrit DJF, pas la
    fiche entière."""
    assert "décembre" not in figure("QSA_season")
    assert "Courbe des quantiles" in figure("FDC"), "commune : elle reste"


def test_l_identifiant_perenne_est_ouvrable():
    assert "https://archive.softwareheritage.org/swh:1:cnt:" in figure("QA")


def test_la_figure_tient_dans_un_terminal():
    """Seule l'URL de l'archive dépasse : la couper la rendrait
    inutilisable, c'est le prix d'un lien qui s'ouvre."""
    debords = []
    for p in sorted(_DEFAULT_CARD_DIR.rglob("*.yaml")):
        for lang in ("fr", "en"):
            for ligne in figure(p.stem, lang=lang).splitlines():
                if len(ligne) > 80 and "archive.softwareheritage" not in ligne:
                    debords.append(f"{p.stem}/{lang} ({len(ligne)}) : {ligne}")
    assert not debords, debords[:5]


def test_un_identifiant_ne_se_coupe_pas_en_deux():
    f = figure("delta-allLF_winter_H")
    assert "delta-\n" not in f


def test_la_date_suit_la_convention_de_la_langue():
    """MM-DD en anglais, DD-MM en français, comme les métadonnées."""
    assert "du 01-09 au 31-08" in figure("QA")
    assert "from 09-01 to 08-31" in figure("QA", lang="en")


@pytest.mark.parametrize("nom", ["QA", "VCN10", "delta-QA_H", "FDC", "allLF"])
def test_la_figure_porte_sa_provenance(nom):
    f = figure(nom)
    assert nom in f
    assert "swh:1:cnt:" in f, "l'identifiant pérenne doit être dans la figure"
    assert "{suffix" not in f, "jamais l'accolade brute"


def test_la_bande_marque_les_bornes():
    """Une fenêtre partielle montre ses deux bornes, une année complète
    montre son départ : une barre pleine n'apprendrait rien."""
    assert "┃" in figure("QNA_summer")          # début et fin
    assert "┃" in figure("QA")                  # départ de l'année hydro
    assert figure("QNA_summer").count("┃") == 2


def test_l_enveloppe_de_periode_est_depliee():
    """over_period sert à restreindre ; afficher son nom cacherait que
    la fiche calcule une médiane."""
    f = figure("QJD")
    assert "nanmedian(Q)" in f
    assert "over_period" not in f


def test_la_figure_suit_la_forme_de_sortie():
    assert "compare deux fenêtres" in figure("delta-QA_H")     # scalaire
    assert "sortie : QA · une ligne par année" in figure("QA")  # série


def test_la_figure_n_invente_pas_l_axe_d_une_courbe():
    """Il n'est écrit nulle part dans la fiche : le deviner du nom de la
    variable rendait « jour de l'année » sur toute courbe non-FDC."""
    for nom in ("FDC", "BFM", "QJC10", "QJD", "QJDC10"):
        assert "indexée par" not in figure(nom)


def test_la_granularite_n_est_annoncee_que_si_la_fiche_la_determine():
    """`time_step: none` donne 1 ligne pour BFM, 365 pour QJC10 et 1000
    pour FDC : la fiche ne le dit pas, la figure non plus."""
    for nom in ("BFM", "QJC10", "FDC"):
        assert "ligne par" not in figure(nom)
    assert "une ligne par jour de l'année" in figure("QJD")
    assert "les mois en colonnes" in figure("QMA_month")
    assert "une ligne par mois" in figure("QM")


def test_les_colonnes_demultipliees_sont_dites():
    """La fiche déclare un calcul `QMA`, l'extraction rend douze
    colonnes : la figure doit montrer les douze, une seule fois."""
    f = figure("QMA_month")
    assert "QMA_jan" in f and "QMA_dec" in f
    assert "sortie : 12 colonnes" in f
    assert f.count("QMA_dec") == 1, "l'en-tête les liste déjà"


def test_info_imprime_la_figure_et_rend_le_dict(capsys):
    from card.management import info
    d = info("VCN10")
    sortie = capsys.readouterr().out
    assert "▼" in sortie and "swh:1:cnt:" in sortie
    assert d["id"] == "VCN10" and d["version"]


def test_les_metadonnees_brutes_sont_accessibles_par_nom():
    """La figure est une lecture ; il faut aussi pouvoir lire la fiche
    telle qu'elle est écrite, sans passer par un chemin de fichier."""
    from card import load_card
    c = load_card("QA")
    assert c["id"] == "QA" and c["meta"]["fr"]["variable"] == "QA"
    assert str(c["path"]).endswith("flow/mean-flows/series/QA.yaml")
    assert load_card(c["path"])["swhid"] == c["swhid"]


def test_figure_est_publique_et_muette(capsys):
    """Servir la figure (web, notebook) demande une CHAÎNE, pas un print :
    info() imprime pour un humain, figure() rend pour un programme."""
    import card
    f = card.figure("QA")
    assert isinstance(f, str) and "QA" in f and "▼" in f
    assert capsys.readouterr().out == "", "figure() ne doit rien imprimer"


def test_info_quiet_rend_le_dict_sans_imprimer(capsys):
    """Un service web n'a pas de terminal : la figure partirait dans les
    logs à chaque requête, calculée pour rien."""
    import card
    d = card.info("QA", quiet=True)
    assert d["id"] == "QA"
    assert capsys.readouterr().out == ""
    card.info("QA")                       # défaut inchangé : ça imprime
    assert "▼" in capsys.readouterr().out


def _fonctions_du_corpus():
    from card.extraction import _find_cards
    fns = set()
    for chemin in _find_cards(_DEFAULT_CARD_DIR, None).values():
        for proc in load_card(chemin)["processes"]:
            fns |= {e["fn_name"] for e in proc["func"]}
    return sorted(fns)


def test_aucune_glose_ne_vient_dune_docstring_etrangere():
    """La figure ne doit jamais servir la prose de référence de numpy.

    La règle cherchait le préfixe `nan` dans le NOM, ce qui visait juste
    par accident : elle muselait au passage `nansum_strict`, qui est de
    card. Elle regarde désormais à QUI appartient la fonction.
    """
    from card.extraction import resolve
    from card.render import glose

    fuites = []
    for nom in _fonctions_du_corpus():
        module = getattr(resolve(nom), "__module__", "")
        if not module.startswith("card") and glose(nom):
            fuites.append(f"{nom} ({module}) : {glose(nom)!r}")
    assert not fuites, "\n".join(fuites)


def test_les_fonctions_de_card_ne_sont_muselees_que_sciemment():
    """Museler une glose est un choix éditorial, donc il se DÉCLARE.

    `glose_inutile` se pose à côté de la fonction : un renommage emporte
    la déclaration avec lui, là où une liste de noms dans render.py
    serait restée en arrière sans que rien ne rougisse.
    """
    from card.extraction import resolve
    from card.render import glose

    for nom in _fonctions_du_corpus():
        fn = resolve(nom)
        if not getattr(fn, "__module__", "").startswith("card"):
            continue
        if getattr(fn, "glose_inutile", False):
            assert glose(nom) == "", f"{nom} est déclarée muette et parle"
            continue
        # Les autres peuvent rendre une glose vide (docstring trop longue,
        # cf. CHANTIERS), mais jamais parce qu'un nom figure quelque part.
        assert fn.__doc__, f"{nom} n'a pas de docstring et n'est pas déclarée muette"


def test_le_decoupeur_ne_coupe_pas_sur_une_abreviation():
    """« et al. » ne termine pas une phrase, « ex. » non plus.

    Le découpeur cherchait un point suivi d'une espace : la glose de RAT
    s'arrêtait après « (Nicolle et al », la parenthèse ouverte était
    tranchée de force, et il ne restait que le sigle.
    """
    from card.render import _premiere_phrase

    assert _premiere_phrase(
        "Truc (Nicolle et al. 2020) : machin. Suite."
    ) == "Truc (Nicolle et al. 2020) : machin"
    assert _premiere_phrase(
        "Médiane cyclique, ex. une date. Suite."
    ) == "Médiane cyclique, ex. une date"
    assert _premiere_phrase("Sans point final") == "Sans point final"
    assert _premiere_phrase("Une phrase. Une autre.") == "Une phrase"


def test_toute_fonction_de_card_employee_par_le_corpus_a_une_glose():
    """Une figure qui n'explique rien ne sert à rien.

    Une glose vide ne se remarque pas : la ligne manque, et personne ne
    sait qu'elle devrait être là. Trois causes l'ont produite, toutes
    corrigées le 2026-07-31 : un point pris dans une abréviation, une
    première phrase qui était en fait un paragraphe, et le musellement
    accidentel des fonctions dont le nom commence par `nan`. Le seul
    silence acceptable est celui qu'on a déclaré.
    """
    from card.extraction import resolve
    from card.render import glose

    muettes = []
    for nom in _fonctions_du_corpus():
        fn = resolve(nom)
        if not getattr(fn, "__module__", "").startswith("card"):
            continue
        if getattr(fn, "glose_inutile", False):
            continue
        if not glose(nom):
            premiere = len((fn.__doc__ or "").strip().split("\n\n")[0])
            muettes.append(
                f"{nom} : glose vide (premier paragraphe de {premiere} "
                f"caractères). Raccourcir sa PREMIÈRE phrase, ou la "
                f"déclarer `glose_inutile` si l'appel se suffit.")
    assert not muettes, "\n".join(muettes)


def test_les_blocs_de_langue_se_decoupent_comme_annonce():
    """La règle de lecture doit tenir sur un cas construit.

    Un marqueur en marge ouvre un bloc, les lignes indentées le
    continuent, une ligne revenue en marge sans marqueur est une note
    hors langue.
    """
    from card.render import _blocs

    b = _blocs("""
    en: First sentence.

        Second paragraph.

    fr: Première phrase.

        Second paragraphe.

    Note hors langue.
    """)
    assert set(b) == {"en", "fr"}
    assert b["en"] == "First sentence.\n\nSecond paragraph."
    assert b["fr"] == "Première phrase.\n\nSecond paragraphe."
    # Une docstring sans marqueur reste lisible : pas de bloc, et le
    # texte sert pour toutes les langues (fonction écrite par un tiers).
    assert _blocs("Juste une phrase.") == {}


def test_chaque_fonction_de_card_a_ses_deux_blocs_de_langue():
    """Une figure anglaise ne doit pas servir de la prose française.

    Les gloses viennent des docstrings : sans traduction, la figure
    anglaise les affichait telles quelles, seul morceau de la figure à ne
    pas passer par la table `_T`. Les deux langues vivent maintenant dans
    la docstring, `en:` puis `fr:` comme dans les fiches, à égalité.

    `glose(lang="en")` retombe sur l'autre langue quand un bloc manque,
    ce qui rend service à une fonction écrite par un tiers mais passerait
    inaperçu dans le corpus : d'où ce test.
    """
    from card.extraction import resolve
    from card.render import LANGUES, _blocs, glose

    manquantes = []
    for nom in _fonctions_du_corpus():
        fn = resolve(nom)
        if not getattr(fn, "__module__", "").startswith("card"):
            continue
        if getattr(fn, "glose_inutile", False):
            continue
        blocs = _blocs(fn.__doc__ or "")
        absents = [x for x in LANGUES if x not in blocs]
        if absents:
            manquantes.append(
                f"{nom} : pas de bloc {absents} dans sa docstring, la figure "
                f"affichera l'autre langue")
        elif not all(glose(nom, x) for x in LANGUES):
            manquantes.append(f"{nom} : un bloc présent mais glose vide")
    assert not manquantes, "\n".join(manquantes)


def test_la_glose_anglaise_diffère_bien_de_la_française():
    """Un bloc `en:` recopié du français est un oubli, pas une traduction."""
    from card.extraction import resolve
    from card.render import glose

    identiques = []
    for nom in _fonctions_du_corpus():
        fn = resolve(nom)
        if not getattr(fn, "__module__", "").startswith("card"):
            continue
        if getattr(fn, "glose_inutile", False):
            continue
        fr, en = glose(nom, "fr"), glose(nom, "en")
        # Quelques gloses sont légitimement identiques (formules pures) ;
        # aucune ne l'est aujourd'hui, et si cela arrive un jour c'est une
        # décision à prendre, pas un état à subir en silence.
        if fr and en and fr == en:
            identiques.append(nom)
    assert not identiques, (
        f"{identiques} : glose anglaise identique à la française. Traduire, "
        f"ou déclarer la fonction `glose_inutile` si l'appel se suffit.")
