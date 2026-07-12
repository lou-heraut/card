"""Rend card et stase importables sans installation (usage développeur).

Pour un environnement installé : pip install -e ../../EXstat_project/stase -e .
"""

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_CARD_SRC = _HERE.parent / "src"
_EXSTAT_SRC = _HERE.parent.parent.parent / "EXstat_project" / "stase" / "src"

for p in (str(_CARD_SRC), str(_EXSTAT_SRC)):
    if p not in sys.path:
        sys.path.insert(0, p)
