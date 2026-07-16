"""Paramètre sampling_period= de card.extract : écrase la fenêtre
annuelle des fiches ('preferred' = fenêtre fixe déclarée par la fiche,
'MM-DD' = fenêtre imposée), sans toucher les fenêtres partielles."""

import warnings

import numpy as np
import pandas as pd
import pytest

import conftest  # noqa: F401  (chemins card/stase sans installation)
from card import extract


def _daily_seasonal():
    """Chronique avec régime marqué : minimum mensuel en juin,
    maximum en décembre."""
    dates = pd.date_range("1990-01-01", "2019-12-31", freq="D")
    doy = dates.day_of_year.to_numpy()
    rng = np.random.default_rng(2)
    q = 10 + 8 * np.cos(2 * np.pi * (doy - 350) / 365.25) \
        + rng.normal(0, 0.5, len(dates))
    return pd.DataFrame({"date": dates, "Q": np.maximum(q, 0.1), "id": "S1"})


def _window_month(res, name):
    return res["data"][name]["date"].dt.month.mode()[0]


def test_adaptive_default_versus_preferred_and_explicit():
    data = _daily_seasonal()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        adaptive = extract(data, cards=["QJXA"])
        preferred = extract(data, cards=["QJXA"], sampling_period="preferred")
        explicit = extract(data, cards=["QJXA"], sampling_period="10-01")
    assert _window_month(adaptive, "QJXA") == 6      # mois du min (juin)
    assert _window_month(preferred, "QJXA") == 9     # preferred 09-01
    assert _window_month(explicit, "QJXA") == 10


def test_partial_windows_untouched():
    data = _daily_seasonal()
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ref = extract(data, cards=["dtLF_winter"])
        ovr = extract(data, cards=["dtLF_winter"], sampling_period="preferred")
    pd.testing.assert_frame_equal(ref["data"]["dtLF_winter"],
                                  ovr["data"]["dtLF_winter"])


def test_preferred_keeps_fixed_window_without_preferred():
    """Fiche à fenêtre fixe sans preferred déclaré (RA) : 'preferred'
    conserve sa fenêtre, l'extraction du catalogue entier reste possible."""
    data = _daily_seasonal().rename(columns={"Q": "R"})
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        ref = extract(data, cards=["RA"])
        ovr = extract(data, cards=["RA"], sampling_period="preferred")
    pd.testing.assert_frame_equal(ref["data"]["RA"], ovr["data"]["RA"])


def test_invalid_value_raises():
    with pytest.raises(ValueError, match="preferred"):
        extract(_daily_seasonal(), cards=["QA"], sampling_period="septembre")
