"""card : variables hydroclimatiques prêtes à l'emploi, définies par des
fiches YAML et calculées par le moteur stase.

Usage :
    import card
    res = card.extract(data, cards=["QA", "VCN10"])
    card.trend(res)
    card.list_cards(phenomenon="basses eaux")
    card.info("VCN10")
"""

from .extraction import extract  # noqa: F401
from .loader import load_card  # noqa: F401
from .management import copy_cards, info, list_cards  # noqa: F401
# figure() rend la fiche dessinée en CHAÎNE, sans rien imprimer : c'est ce
# qu'il faut pour la servir (web, notebook), là où info() imprime pour un
# humain devant un terminal et retourne le dict.
from .render import figure  # noqa: F401
from .schema import vocabulary  # noqa: F401
from .trend import trend  # noqa: F401

# Alias hérités du package R CARD (toujours valides)
from .extraction import CARD_extraction  # noqa: F401
from .management import (  # noqa: F401
    CARD_info,
    CARD_list_all,
    CARD_management,
)

__all__ = [
    "extract",
    "trend",
    "list_cards",
    "info",
    "figure",
    "vocabulary",
    "copy_cards",
    "load_card",
    # alias héritage R
    "CARD_extraction",
    "CARD_list_all",
    "CARD_info",
    "CARD_management",
]

__version__ = "0.1.0"
