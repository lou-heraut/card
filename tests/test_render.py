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
    f = figure("median-QJ")
    assert "nanmedian(Q)" in f
    assert "over_period" not in f


def test_la_figure_suit_la_forme_de_sortie():
    assert "compare deux fenêtres" in figure("delta-QA_H")     # scalaire
    assert "indexée par" in figure("FDC")                       # courbe
    assert "une série" in figure("QA")                          # série


def test_info_imprime_la_figure_et_rend_le_dict(capsys):
    from card.management import info
    d = info("VCN10")
    sortie = capsys.readouterr().out
    assert "▼" in sortie and "swh:1:cnt:" in sortie
    assert d["id"] == "VCN10" and d["version"]
