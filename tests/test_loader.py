"""Tests du chargement des fiches YAML."""

import pytest

from card.extraction import _DEFAULT_CARD_DIR
from card.loader import load_card


def path_of(name):
    matches = list(_DEFAULT_CARD_DIR.rglob(f"{name}.yaml"))
    assert matches, f"fiche {name} introuvable"
    return matches[0]


def test_simple_card_structure():
    card = load_card(path_of("QA"))
    assert card["id"] == "QA"
    assert card["meta"]["global"]["input_vars"] == "Q"
    (p1,) = card["processes"]
    assert p1["name"] == "P1"
    assert p1["time_step"] == "year"          # défaut appliqué
    assert p1["sampling_period"] == "09-01"
    assert p1["max_na_pct"] == 3
    (entry,) = p1["func"]
    assert entry["name"] == "QA"
    assert entry["fn_name"] == "nanmean"
    assert entry["cols"] == ["Q"]
    assert entry["is_date"] is False


def test_defaults_applied():
    card = load_card(path_of("QA"))
    gl = card["meta"]["global"]
    assert gl["is_date"] is False              # défauts globaux
    assert gl["relative"] is True
    assert gl["is_experimental"] is False


def test_horizon_substitution():
    card = load_card(path_of("delta-QA_H"))
    p_last = card["processes"][-1]
    kwargs = p_last["func"][0]["kwargs"]
    assert kwargs["past"] == ["1976-01-01", "2005-08-31"]
    assert kwargs["future"] == ["2021-01-01", "2050-12-31"]


def test_adaptive_sampling_parsed():
    card = load_card(path_of("QMNA"))
    sp = card["processes"][1]["sampling_period"]
    assert sp["type"] == "adaptive"
    assert sp["func"]["fn_name"] == "nanmax"
    assert sp["func"]["cols"] == ["QMA"]


def test_is_date_flag():
    card = load_card(path_of("tQJXA"))
    entry = card["processes"][0]["func"][0]
    assert entry["fn_name"] == "nanargmax"
    assert entry["is_date"] is True


def test_positional_literal():
    card = load_card(path_of("delta-dtFlood_H"))
    entries = [e for p in card["processes"] for e in p["func"]
               if any(t == "lit" for t, _ in e["pos_args"])]
    assert entries, "littéral positionnel attendu (ratio, 'dQXA', 2)"
    assert ("lit", 2) in entries[0]["pos_args"]


def test_unknown_horizon_raises(tmp_path):
    bad = tmp_path / "bad.yaml"
    bad.write_text(
        "id: bad\nmeta: {en: {}, fr: {}, global: {}}\n"
        "process:\n  P1:\n    func:\n"
        "      x: [delta, \"Q\", \"date\", {past: $H9, future: $H1, relative: true}]\n"
    )
    with pytest.raises(ValueError, match="H9"):
        load_card(bad)
