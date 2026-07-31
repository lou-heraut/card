"""Non-régression des fiches qui divergent VOLONTAIREMENT du R.

`tests/data/py_golden/` fige la sortie Python des fiches dont la parité
avec le paquet R a été rompue sciemment (motif de chacune dans
`tests/data/known_divergences.yaml`, raisonnement dans
`docs/dev/ORIGINE_R.md`). Ces fiches ne peuvent pas être jugées contre le
golden R : sans golden Python, rien ne les tient.

Ces fichiers existaient déjà mais n'étaient lus que par
`tests/run_py_corpus.py`, un script, que la CI ne lance pas (elle
n'appelle que `pytest`). Ils ne gardaient donc rien : constaté le
2026-07-31, en cherchant ce qui protégeait les fiches `fQ*` après le
changement de dénominateur de `exceedance_frequency`. Ce fichier les
branche sur la suite.
"""

import pathlib
import warnings

import numpy as np
import pandas as pd
import pytest
import yaml

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import extract
from card.extraction import _DEFAULT_CARD_DIR, _find_cards

DONNEES = pathlib.Path(__file__).parent / "data"
GOLDEN = DONNEES / "py_golden"
FICHES = sorted(p.stem for p in GOLDEN.glob("*.csv"))

# Bornes d'horizon rejouées à l'identique de run_py_corpus.py : les fiches
# à suffixe reçoivent leurs périodes en colonnes d'entrée.
HORIZON_COLS = {
    "ref_start": "1976-01-01", "ref_end": "2005-08-31",
    "horizon_start_H1": "2021-01-01", "horizon_end_H1": "2050-12-31",
    "horizon_start_H2": "2041-01-01", "horizon_end_H2": "2070-12-31",
    "horizon_start_H3": "2070-01-01", "horizon_end_H3": "2099-12-31",
}
HORIZON_SUFFIX = ["H1", "H2", "H3"]


def test_le_manifeste_et_les_golden_se_correspondent():
    """Un golden sans motif déclaré est une divergence qu'on a oublié
    d'expliquer ; un motif sans golden est une fiche que plus rien ne tient."""
    manifeste = set(yaml.safe_load(
        (DONNEES / "known_divergences.yaml").read_text(
            encoding="utf-8")))
    fichiers = set(FICHES)
    assert manifeste == fichiers, (
        f"golden sans motif : {sorted(fichiers - manifeste)} ; "
        f"motif sans golden : {sorted(manifeste - fichiers)}")


@pytest.mark.parametrize("nom", FICHES)
def test_la_fiche_rend_toujours_son_golden(nom):
    """Valeurs figées : toute dérive est un changement de résultat, donc
    une décision, donc quelque chose qui se voit et se documente."""
    warnings.filterwarnings("ignore")
    donnees = pd.read_csv(DONNEES / "test_data.csv",
                          parse_dates=["date"])
    dossier = pathlib.Path(_find_cards(_DEFAULT_CARD_DIR, [nom])[nom]).parent

    if nom.endswith("_H"):
        for col, val in HORIZON_COLS.items():
            donnees[col] = pd.Timestamp(val)
        obtenu = extract(donnees, cards=[nom], path=dossier,
                         suffix=HORIZON_SUFFIX)["data"][nom]
    else:
        obtenu = extract(donnees, cards=[nom], path=dossier)["data"][nom]

    attendu = pd.read_csv(GOLDEN / f"{nom}.csv")
    assert list(obtenu.columns) == list(attendu.columns), (
        f"{nom} : colonnes {list(obtenu.columns)} contre "
        f"{list(attendu.columns)} dans le golden")
    assert len(obtenu) == len(attendu), f"{nom} : {len(obtenu)} lignes contre " \
                                        f"{len(attendu)}"

    for col in attendu.columns:
        if col in ("id", "date"):
            assert (obtenu[col].astype(str).to_numpy()
                    == attendu[col].astype(str).to_numpy()).all(), f"{nom}.{col}"
            continue
        a = pd.to_numeric(obtenu[col], errors="coerce").to_numpy(dtype=float)
        b = pd.to_numeric(attendu[col], errors="coerce").to_numpy(dtype=float)
        assert np.allclose(a, b, rtol=1e-9, atol=1e-12, equal_nan=True), (
            f"{nom}.{col} a dérivé : écart max "
            f"{np.nanmax(np.abs(a - b))}")
