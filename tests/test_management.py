"""Tests de CARD_list_all et CARD_management."""

import pytest

from card import CARD_list_all, CARD_management, extract, list_cards


def test_what_is_listed_can_be_extracted():
    """L'enchaînement le plus naturel du paquet doit marcher.

    On liste une famille, on la calcule. Il échouait : `list_cards()`
    rend une ligne par VARIABLE, `extract()` attend un nom de FICHE, et
    le fan-out par mois ou par saison les sépare (`mean-TMA_jan` est une
    variable de la fiche `mean-TMA_month`). Mesuré le 2026-08-11 : 343
    des 472 variables listées ne portent pas le nom de leur fiche, soit
    73 %, donc ce n'est pas un cas de bord.

    La colonne `card` est ce qu'`extract` accepte, et ce test l'éprouve
    plutôt que de le promettre : tout ce qui est listé est chargeable, et
    tout ce qui est listé ressort. Sans calcul, `metadata_only` suffit.
    """
    meta = list_cards()
    assert (meta["card"] != meta["variable_en"]).any(), (
        "sans fiche multi-sorties, la colonne ne prouve rien")

    sortie = extract(None, cards=sorted(meta["card"].unique()),
                     metadata_only=True)["meta"]
    assert set(sortie["variable_en"]) >= set(meta["variable_en"])


def test_list_all_covers_corpus():
    meta = CARD_list_all()
    assert meta.script_path.nunique() >= 210
    # une ligne par variable ; les fiches _H collapsées exposent leur
    # variable de base (l'horizon est devenu un suffixe), d'où ~482
    assert len(meta) >= 470
    assert not meta.variable_en.isna().any()


def test_management_copies_without_numbering_by_default(tmp_path):
    """Le nom de fichier d'une copie doit rester l'identifiant de la
    fiche : le linter exige l'égalité des deux, et une copie numérotée
    échouait donc dès le premier contrôle."""
    dest = tmp_path / "WIP"
    CARD_management(cards={"analyse": ["QA", "QMNA"]}, dest=dest)
    files = sorted(p.relative_to(dest).as_posix() for p in dest.rglob("*.yaml"))
    assert files == ["analyse/QA.yaml", "analyse/QMNA.yaml"]


def test_management_numbering_stays_available(tmp_path):
    """La numérotation garde son usage : ordonner un dossier de travail."""
    dest = tmp_path / "WIP"
    CARD_management(cards={"analyse": ["QA", "QMNA"]}, dest=dest, numbered=True)
    files = sorted(p.relative_to(dest).as_posix() for p in dest.rglob("*.yaml"))
    assert files == ["001_analyse/001_QA.yaml", "001_analyse/002_QMNA.yaml"]


def test_management_refuses_overwrite(tmp_path):
    dest = tmp_path / "WIP"
    CARD_management(cards=["QA"], dest=dest)
    with pytest.raises(FileExistsError):
        CARD_management(cards=["QA"], dest=dest)
    CARD_management(cards=["QA"], dest=dest, overwrite=True)
