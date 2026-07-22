"""Tests de CARD_list_all et CARD_management."""

import pytest

from card import CARD_list_all, CARD_management


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
