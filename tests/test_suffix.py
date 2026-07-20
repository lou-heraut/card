"""Suffixes de scénario et métadonnées évolutives (CHANTIERS §9).

Le mécanisme est confiné aux métadonnées : stase éclate les valeurs au
niveau colonne, card en dérive une ligne de méta par variable réellement
sortie. Les tests vérifient donc deux choses distinctes : que les
VALEURS d'une extraction multi-seuils sont identiques à celles de N
extractions mono-seuil, et que les PHRASES restent lisibles dans tous
les régimes (sans suffixe, avec suffixe nommé, avec suffixe nu).
"""

import numpy as np
import pandas as pd
import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import extract
from card.schema import validate_card


def _data(thresholds):
    """Chronique journalière avec une colonne constante par seuil."""
    dates = pd.date_range("1980-01-01", "2009-12-31", freq="D")
    rng = np.random.default_rng(7)
    q = 5 + 20 * rng.gamma(2.0, 1.0, len(dates))
    df = pd.DataFrame({"date": dates, "Q": q, "id": "S1"})
    for name, value in thresholds.items():
        df[name] = value
    return df


def _meta_of(res, variable):
    rows = res["meta"][res["meta"]["variable_en"] == variable]
    assert len(rows) == 1, f"{variable} : {len(rows)} ligne(s) de méta"
    return rows.iloc[0]


# --- Valeurs : le multi-seuils ne doit rien changer aux nombres --------

def test_multi_threshold_equals_separate_single_extractions():
    both = extract(_data({"Q_lim_DOE": 22.0, "Q_lim_DCR": 19.5}),
                   cards=["rp-VCN10"], suffix=["DOE", "DCR"])["data"]["rp-VCN10"]

    for key, value in (("DOE", 22.0), ("DCR", 19.5)):
        one = extract(_data({"Q_lim": value}),
                      cards=["rp-VCN10"])["data"]["rp-VCN10"]
        assert both[f"rp-VCN10_{key}"].to_numpy() == pytest.approx(
            one["rp-VCN10"].to_numpy(), nan_ok=True, rel=0, abs=0)


def test_shared_series_is_not_fanned_out():
    """Seule la colonne qui varie est éclatée : Q reste partagée."""
    res = extract(_data({"Q_lim_DOE": 22.0, "Q_lim_DCR": 19.5}),
                  cards=["rp-VCN10"], suffix=["DOE", "DCR"])
    cols = set(res["data"]["rp-VCN10"].columns)
    assert {"rp-VCN10_DOE", "rp-VCN10_DCR"} <= cols
    assert "rp-VCN10" not in cols


def test_unsuffixed_card_in_the_same_call_stays_single():
    """Une fiche dont aucune référence ne varie sort une seule fois."""
    res = extract(_data({"Q_lim_DOE": 22.0, "Q_lim_DCR": 19.5}),
                  cards=["rp-VCN10", "QA"], suffix=["DOE", "DCR"])
    assert list(res["data"]["QA"].columns).count("QA") == 1
    assert (res["meta"]["variable_en"] == "QA").sum() == 1


# --- Une ligne de méta par variable ------------------------------------

def test_one_meta_row_per_suffixed_variable():
    res = extract(_data({"Q_lim_DOE": 22.0, "Q_lim_DCR": 19.5}),
                  cards=["rp-VCN10"], suffix=["DOE", "DCR"])
    meta = res["meta"]
    assert set(meta["variable_en"]) == {"rp-VCN10_DOE", "rp-VCN10_DCR"}
    assert set(meta["suffix"]) == {"DOE", "DCR"}
    assert meta["variable_fr"].tolist() == ["rp-VCN10_DOE", "rp-VCN10_DCR"]
    # Deux lignes ne peuvent pas porter le même nom : c'est l'ambiguïté
    # que le mécanisme existe pour lever.
    assert meta["name_en"].nunique() == 2
    assert meta["name_fr"].nunique() == 2


def test_call_labels_win_over_the_key():
    res = extract(_data({"Q_lim_DOE": 22.0}), cards=["rp-VCN10"], suffix={
        "DOE": {"en": {"name": "low-flow target discharge"},
                "fr": {"name": "débit objectif d'étiage"}},
    })
    row = _meta_of(res, "rp-VCN10_DOE")
    assert row["name_en"].startswith(
        "Return period of the low-flow target discharge with respect to")
    assert row["name_fr"].startswith(
        "Période de retour du débit objectif d'étiage au regard des")
    # {suffix.short} n'a pas été fourni : repli sur la clé, pas sur le
    # défaut de la fiche (sinon DOE et DCR auraient la même phrase).
    assert "return period of the DOE threshold" in row["method_en"]


def test_bare_key_is_used_when_no_label_is_given():
    res = extract(_data({"Q_lim_DOE": 22.0}), cards=["rp-VCN10"],
                  suffix=["DOE"])
    row = _meta_of(res, "rp-VCN10_DOE")
    assert "Return period of the DOE with respect to" in row["name_en"]
    assert "{" not in row["name_en"] and "{" not in row["method_en"]


# --- Invariant : jamais d'accolade en sortie, et un défaut lisible ----

def test_no_suffix_gives_the_declared_default_sentence():
    res = extract(_data({"Q_lim": 22.0}), cards=["rp-VCN10"])
    row = _meta_of(res, "rp-VCN10")
    assert row["name_en"] == (
        "Return period of the station's regulatory threshold discharge "
        "with respect to the annual minima of 10-day mean flows")
    assert row["name_fr"].startswith(
        "Période de retour du débit seuil réglementaire de la station")
    assert "return period of the Q_lim threshold" in row["method_en"]
    assert row["suffix"] == ""


def test_metadata_only_matches_the_suffixless_extraction():
    computed = extract(_data({"Q_lim": 22.0}), cards=["rp-VCN10"])["meta"]
    declared = extract(_data({"Q_lim": 22.0}), cards=["rp-VCN10"],
                       metadata_only=True)["meta"]
    pd.testing.assert_frame_equal(computed, declared)


def test_no_placeholder_survives_anywhere_in_the_corpus_metadata():
    meta = extract(pd.DataFrame(), cards=None, metadata_only=True)["meta"]
    for col in meta.columns:
        if meta[col].dtype == object:
            leaked = meta[col].astype(str).str.contains(r"\{suffix", na=False)
            assert not leaked.any(), f"{col} : {meta.loc[leaked, col].tolist()}"


# --- Fiche sans placeholder : le cas obs/sim sur tout le corpus --------

def test_card_without_placeholder_gets_its_name_completed():
    dates = pd.date_range("1980-01-01", "2009-12-31", freq="D")
    rng = np.random.default_rng(3)
    df = pd.DataFrame({"date": dates, "id": "S1",
                       "Q_obs": 5 + rng.gamma(2.0, 1.0, len(dates)),
                       "Q_sim": 5 + rng.gamma(2.0, 1.0, len(dates))})
    res = extract(df, cards=["QA"], suffix={
        "obs": "observation", "sim": "simulation"})

    assert set(res["data"]["QA"].columns) >= {"QA_obs", "QA_sim"}
    row = _meta_of(res, "QA_sim")
    assert row["name_en"] == "Annual mean daily discharge (simulation)"
    assert row["suffix"] == "sim"
    # description et method ne sont pas touchés : seul le name sert de
    # titre de graphique.
    assert "(simulation)" not in row["method_en"]


# --- Erreurs et lint ---------------------------------------------------

def test_missing_field_raises_a_pointed_error(tmp_path):
    card = tmp_path / "cards" / "flow" / "scalar"
    card.mkdir(parents=True)
    (card / "demo.yaml").write_text(
        'id: demo\nversion: "1.0"\nauthors: ["t"]\ndate: "2026-07-20"\n'
        "meta:\n"
        "  en:\n    variable: demo\n    unit: m\n"
        "    name: Demo for the {suffix.period} window\n"
        "    classification: {domain: flow, season: annual, output: scalar}\n"
        "    suffix_default: {period: all periods}\n"
        "  fr:\n    variable: demo\n    unit: m\n"
        "    name: Démo sur la fenêtre {suffix.period}\n"
        "    classification: {domain: débit, season: annuelle, output: scalaire}\n"
        "    suffix_default: {period: toutes périodes}\n"
        "  global:\n    input_vars: Q\n"
        "process:\n  P1:\n    func:\n      demo: [nanmean, \"Q\"]\n",
        encoding="utf-8")

    df = _data({})
    df["Q_H1"] = df["Q"]
    with pytest.raises(ValueError, match="ne fournit pas 'period'"):
        extract(df, cards=["demo"], path=str(tmp_path / "cards"),
                suffix=["H1"])


def test_lint_rejects_a_placeholder_without_default(tmp_path):
    p = tmp_path / "orphan.yaml"
    p.write_text(
        'id: orphan\nversion: "1.0"\nauthors: ["t"]\ndate: "2026-07-20"\n'
        "meta:\n"
        "  en:\n    variable: orphan\n    unit: m\n"
        "    name: Return period of the {suffix.name}\n"
        "    classification: {domain: flow, season: annual, output: scalar}\n"
        "  fr:\n    variable: orphan\n    unit: m\n"
        "    name: Période de retour du {suffix.name}\n"
        "    classification: {domain: débit, season: annuelle, output: scalaire}\n"
        "  global:\n    input_vars: Q\n"
        "process:\n  P1:\n    func:\n      orphan: [nanmean, \"Q\"]\n",
        encoding="utf-8")
    issues = validate_card(p)
    assert any("suffix_default" in i for i in issues)


def test_lint_rejects_a_dead_suffix_vocabulary(tmp_path):
    """Le cas horizon_labels : un champ déclaré que rien n'utilise."""
    p = tmp_path / "dead.yaml"
    p.write_text(
        'id: dead\nversion: "1.0"\nauthors: ["t"]\ndate: "2026-07-20"\n'
        "meta:\n"
        "  en:\n    variable: dead\n    unit: m\n    name: Plain name\n"
        "    classification: {domain: flow, season: annual, output: scalar}\n"
        "    suffix_default: {name: unused}\n"
        "  fr:\n    variable: dead\n    unit: m\n    name: Nom simple\n"
        "    classification: {domain: débit, season: annuelle, output: scalaire}\n"
        "  global:\n    input_vars: Q\n"
        "process:\n  P1:\n    func:\n      dead: [nanmean, \"Q\"]\n",
        encoding="utf-8")
    issues = validate_card(p)
    assert any("champ mort" in i for i in issues)
