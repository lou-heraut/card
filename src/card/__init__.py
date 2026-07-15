"""card : variables hydroclimatiques prêtes à l'emploi, définies par des
fiches YAML et calculées par le moteur stase.

Usage :
    import card
    res = card.extract(data, cards=["QA", "VCN10"])
    card.list_cards(phenomenon="basses eaux")
    card.info("VCN10")
"""

from .extraction import extract  # noqa: F401
from .loader import load_card  # noqa: F401
from .management import copy_cards, info, list_cards  # noqa: F401

# Alias hérités du package R CARD (toujours valides)
from .extraction import CARD_extraction  # noqa: F401
from .management import (  # noqa: F401
    CARD_info,
    CARD_list_all,
    CARD_management,
)

__all__ = [
    "extract",
    "list_cards",
    "info",
    "copy_cards",
    "load_card",
    # alias héritage R
    "CARD_extraction",
    "CARD_list_all",
    "CARD_info",
    "CARD_management",
]

__version__ = "0.1.0"
