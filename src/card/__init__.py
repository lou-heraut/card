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
# Quel logiciel a calculé : les mêmes valeurs que les colonnes de `meta`,
# disponibles seules. Importé APRÈS extraction, qui charge le module du
# même nom : c'est cette ligne qui doit gagner, pour que `card.provenance`
# soit la fonction et non son module.
from .provenance import provenance  # noqa: F401
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
    "provenance",
    # alias héritage R
    "CARD_extraction",
    "CARD_list_all",
    "CARD_info",
    "CARD_management",
]

# Écrit par scripts/set_version.py, jamais à la main :
# tests/test_citation.py refuse le désaccord avec pyproject.
__version__ = "0.8.0"
