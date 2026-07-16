"""Tests d'intégration CARD_extraction sur un mini jeu de données (12 ans,
2 stations) — valeurs golden figées le 2026-07-12 (pile validée contre R)."""

import numpy as np
import pandas as pd
import pytest

from card import CARD_extraction


@pytest.fixture(scope="module")
def data():
    rng = np.random.default_rng(11)
    dates = pd.date_range("2000-01-01", "2011-12-31", freq="D")
    doy = dates.dayofyear.to_numpy()
    frames = []
    for sid, phase in {"A": 0.0, "B": 60.0}.items():
        q = 12 * (1 + 0.7 * np.sin(2 * np.pi * (doy - 120 + phase) / 365.25)) \
            * np.exp(rng.normal(0, 0.2, len(dates)))
        frames.append(pd.DataFrame({"date": dates, "Q": q, "id": sid}))
    return pd.concat(frames, ignore_index=True)


@pytest.fixture(scope="module")
def result(data):
    return CARD_extraction(data, cards=["QA", "tQJXA", "dtLF", "QMNA"])


def station_a(result, name):
    df = result["data"][name]
    return df[df.id == "A"][df.columns[-1]]


def test_qa_golden(result):
    qa = station_a(result, "QA")
    assert qa.iloc[1] == pytest.approx(12.308461765486385)
    assert qa.iloc[3] == pytest.approx(11.99128764432392)


def test_tqjxa_golden(result):
    t = station_a(result, "tQJXA")
    assert t.iloc[1] == 228
    assert t.iloc[3] == 187


def test_dtlf_golden(result):
    # chaîne 4 processus : rolling + adaptatif + colonne creuse + seuil
    dt = station_a(result, "dtLF")
    assert dt.iloc[1] == pytest.approx(1.0)
    assert dt.iloc[3] == pytest.approx(2.0)


def test_qmna_golden(result):
    # year-month fan-out + compaction colonne creuse + adaptatif
    q = station_a(result, "QMNA")
    assert q.iloc[1] == pytest.approx(3.943845238916542)
    assert q.iloc[3] == pytest.approx(3.8560648432740825)


def test_metaex_structure(result):
    meta = result["meta"]
    assert set(meta.variable_en) >= {"QA", "tQJXA", "dtLF", "QMNA"}
    assert (meta[meta.variable_en == "QA"].unit_en == "m^{3}.s^{-1}").all()


def test_extract_only_metadata(data):
    res = CARD_extraction(data, cards=["QA"], metadata_only=True)
    assert "data" not in res
    assert len(res["meta"]) == 1
