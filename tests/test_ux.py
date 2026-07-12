"""Tests des aides à la prise en main : rename, affectation automatique,
vérification amont des input_vars, découverte des fiches."""

import numpy as np
import pandas as pd
import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import CARD_extraction, CARD_info, CARD_list_all


def _daily(colname="Q"):
    dates = pd.date_range("2000-01-01", "2009-12-31", freq="D")
    q = np.random.default_rng(0).gamma(2.0, 5.0, len(dates))
    return pd.DataFrame({"date": dates, colname: q, "id": "S1"})


# ── correspondance des colonnes ──────────────────────────────────────────────

def test_rename_maps_columns():
    res = CARD_extraction(_daily("Qm3s"), CARD_name=["QA"],
                          rename={"Qm3s": "Q"}, verbose=False)
    assert len(res["dataEX"]["QA"]) > 0


def test_rename_unknown_column_raises():
    with pytest.raises(ValueError, match="introuvables"):
        CARD_extraction(_daily(), CARD_name=["QA"],
                        rename={"debit": "Q"}, verbose=False)


def test_auto_assign_single_numeric_column():
    with pytest.warns(UserWarning, match="Affectation automatique"):
        res = CARD_extraction(_daily("Qm3s"), CARD_name=["QA"], verbose=False)
    ref = CARD_extraction(_daily(), CARD_name=["QA"], verbose=False)
    pd.testing.assert_frame_equal(res["dataEX"]["QA"], ref["dataEX"]["QA"])


def test_missing_input_vars_clear_error():
    data = _daily("Qm3s")
    data["T"] = 15.0     # 2 colonnes numériques → pas d'affectation auto
    with pytest.raises(ValueError, match="rename="):
        CARD_extraction(data, CARD_name=["QA"], verbose=False)


# ── découverte des fiches ────────────────────────────────────────────────────

def test_list_all_filters():
    full = CARD_list_all()
    by_topic = CARD_list_all(topic="Low Flows")
    by_var = CARD_list_all(variable="VCN10")
    assert 0 < len(by_topic) < len(full)
    assert 0 < len(by_var) < len(by_topic)
    assert by_var.variable_en.str.contains("VCN10").all()


def test_card_info(capsys):
    info = CARD_info("QA")
    out = capsys.readouterr().out
    assert info["input_vars"] == "Q"
    assert info["id"] == "QA"
    assert "QA" in out and "input_vars" in out


def test_card_info_unknown_raises():
    with pytest.raises(FileNotFoundError):
        CARD_info("FICHE_INEXISTANTE")
