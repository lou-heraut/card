"""Tests des aides à la prise en main : rename, affectation automatique,
vérification amont des input_vars, découverte des fiches."""

import numpy as np
import pandas as pd
import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
import card
from card import extract, info, list_cards


def _daily(colname="Q"):
    dates = pd.date_range("2000-01-01", "2009-12-31", freq="D")
    q = np.random.default_rng(0).gamma(2.0, 5.0, len(dates))
    return pd.DataFrame({"date": dates, colname: q, "id": "S1"})


# ── correspondance des colonnes ──────────────────────────────────────────────

def test_rename_maps_columns():
    res = extract(_daily("Qm3s"), cards=["QA"],
                  rename={"Qm3s": "Q"}, verbose=False)
    assert len(res["dataEX"]["QA"]) > 0


def test_rename_unknown_column_raises():
    with pytest.raises(ValueError, match="introuvables"):
        extract(_daily(), cards=["QA"],
                rename={"debit": "Q"}, verbose=False)


def test_auto_assign_single_numeric_column():
    with pytest.warns(UserWarning, match="Affectation automatique"):
        res = extract(_daily("Qm3s"), cards=["QA"], verbose=False)
    ref = extract(_daily(), cards=["QA"], verbose=False)
    pd.testing.assert_frame_equal(res["dataEX"]["QA"], ref["dataEX"]["QA"])


def test_missing_input_vars_clear_error():
    data = _daily("Qm3s")
    data["T"] = 15.0     # 2 colonnes numériques → pas d'affectation auto
    with pytest.raises(ValueError, match="rename="):
        extract(data, cards=["QA"], verbose=False)


# ── découverte des fiches ────────────────────────────────────────────────────

def test_list_all_filters():
    full = list_cards()
    by_phen = list_cards(phenomenon="basses eaux")
    by_phen_en = list_cards(phenomenon="low flows")
    by_out = list_cards(output="curve")
    by_op = list_cards(operator="delta")
    by_var = list_cards(variable="VCN10")
    assert 0 < len(by_phen) < len(full)
    assert len(by_phen) == len(by_phen_en)
    assert set(by_out.variable_en.str.replace(r"_(p|Q)$", "", regex=True))
    assert 0 < len(by_op) < len(full)
    assert (by_op.operator == "delta").all()
    assert 0 < len(by_var) < len(by_phen)
    assert by_var.variable_en.str.contains("VCN10").all()


def test_card_info(capsys):
    meta = info("QA")
    out = capsys.readouterr().out
    assert meta["input_vars"].startswith("Q [m^{3}.s^{-1}]")
    assert meta["id"] == "QA"
    assert "QA" in out and "input_vars" in out


def test_card_info_unknown_raises():
    with pytest.raises(FileNotFoundError):
        info("FICHE_INEXISTANTE")


# ── alias hérités du R ───────────────────────────────────────────────────────

def test_r_aliases_still_work():
    assert card.CARD_extraction is card.extract
    assert card.CARD_list_all is card.list_cards
    assert card.CARD_info is card.info
    assert card.CARD_management is card.copy_cards
    # l'ancien paramètre CARD_name= reste accepté et prioritaire
    res = card.CARD_extraction(_daily(), CARD_name=["QA"], verbose=False)
    assert "QA" in res["dataEX"]
