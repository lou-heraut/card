"""Rend la suite exécutable telle quelle : imports, puis jeu de données.

Pour un environnement installé : pip install -e ../../EXstat_project/stase -e .
"""

import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_CARD_SRC = _HERE.parent / "src"
_EXSTAT_SRC = _HERE.parent.parent.parent / "EXstat_project" / "stase" / "src"
# scripts/ : les générateurs sont testables comme le reste, sans quoi ce
# qu'ils produisent n'est vérifié par personne (cf. test_catalogue.py).
_SCRIPTS = _HERE.parent / "scripts"

for p in (str(_CARD_SRC), str(_EXSTAT_SRC), str(_SCRIPTS)):
    if p not in sys.path:
        sys.path.insert(0, p)


def _jeu_de_donnees():
    """Fabrique `tests/data/test_data.csv` s'il manque.

    Ce fichier pèse dix-huit mégaoctets et il est entièrement DÉRIVABLE :
    `make_test_data.py` le reconstruit à l'octet près depuis une graine
    fixe. Il est donc hors git (`.gitignore`), et c'est le bon choix.

    Mais rien ne le fabriquait ailleurs que sur la machine qui l'avait
    déjà. `test_py_golden.py`, arrivé le 2026-07-31 pour que la CI lise
    enfin les golden Python, a rendu la CI rouge à chaque poussée : dix-
    huit `FileNotFoundError` là où la suite passait en local. Quiconque
    clone le dépôt tombait sur le même mur.

    Le générer ici plutôt que dans le workflow répare les deux d'un coup,
    et garde la vérité au même endroit que les tests qui en dépendent.
    """
    csv = _HERE / "data" / "test_data.csv"
    if csv.exists():
        return
    sys.path.insert(0, str(_HERE))
    import make_test_data

    make_test_data.main()


_jeu_de_donnees()
