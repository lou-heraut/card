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
