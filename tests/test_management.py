"""Tests de CARD_list_all et CARD_management."""

import pytest

from card import CARD_list_all, CARD_management


def test_list_all_covers_corpus():
    meta = CARD_list_all()
    assert meta.script_path.nunique() >= 210
    assert len(meta) >= 580                    # une ligne par variable
    assert not meta.variable_en.isna().any()


def test_management_copies_with_ids(tmp_path):
    dest = tmp_path / "WIP"
    CARD_management(cards={"analyse": ["QA", "QMNA"]}, dest=dest)
    files = sorted(p.relative_to(dest).as_posix() for p in dest.rglob("*.yaml"))
    assert files == ["001_analyse/001_QA.yaml", "001_analyse/002_QMNA.yaml"]


def test_management_refuses_overwrite(tmp_path):
    dest = tmp_path / "WIP"
    CARD_management(cards=["QA"], dest=dest)
    with pytest.raises(FileExistsError):
        CARD_management(cards=["QA"], dest=dest)
    CARD_management(cards=["QA"], dest=dest, overwrite=True)
