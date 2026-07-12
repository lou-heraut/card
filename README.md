# card

[![tests](https://github.com/lou-heraut/card/actions/workflows/tests.yml/badge.svg)](https://github.com/lou-heraut/card/actions/workflows/tests.yml)

**CARD** — *CARD Aggregates Recursive Diagnostics*.

<!-- Figure d'illustration (à déposer dans docs/img/, cf. docs/img/README.md) :
![Exemple de variables CARD](docs/img/overview.png)
-->

Package Python d'extraction de variables hydroclimatiques définies
par des fiches de paramétrisation YAML (`src/card/cards/`), exécutées par le
moteur [stase](../../EXstat_project/stase).

Successeur du package R CARD (`CARD_project/CARD/`) — les fiches YAML sont
la source de vérité ; les fiches R restent la référence de validation.

## Utilisation

```python
import pandas as pd
from card import CARD_extraction, CARD_info, CARD_list_all

data = pd.DataFrame({"date": ..., "Q": ..., "id": ...})
res = CARD_extraction(data, CARD_name=["QA", "dtLF"])
res["dataEX"]["QA"]      # un DataFrame par fiche
res["metaEX"]            # métadonnées (une ligne par variable)
```

Les fiches référencent les colonnes d'entrée par leur nom (`input_vars`,
ex. `Q`). Si vos colonnes s'appellent autrement :
`CARD_extraction(data, rename={"Qm3s": "Q"})` — et si les données n'ont
qu'une colonne numérique pour une fiche à variable unique, la
correspondance est automatique (signalée par un warning). Une colonne de
dates en texte au format ISO `YYYY-MM-DD` est convertie automatiquement.

## Explorer les fiches

```python
CARD_list_all()                        # les ~215 fiches (une ligne par variable)
CARD_list_all(topic="Low Flows")       # filtre par thème
CARD_list_all(variable="VCN")          # filtre par nom de variable
CARD_list_all(search="étiage")         # recherche plein texte fr/en
CARD_info("VCN10")                     # détail d'une fiche (méthode, entrées...)
```

Catalogue complet consultable sur GitHub : [docs/CARDS.md](docs/CARDS.md)
(généré par `scripts/generate_catalog.py`, à relancer après modification
des fiches).

## Installation

Depuis GitHub (pas de publication PyPI pour l'instant) :

```bash
pip install "stase @ git+https://github.com/lou-heraut/stase.git"
pip install "card @ git+https://github.com/lou-heraut/card.git"
```

Pour le développement : ajouter `src/` de card **et** de stase au
PYTHONPATH (cf. `tests/conftest.py`), ou
`pip install -e ../../EXstat_project/stase -e .` dans un venv.

## Architecture

```
src/card/
  loader.py       # YAML → processus : défauts, horizons $Hx, tuples funct
  extraction.py   # CARD_extraction : chaîne P1..Pn via stase.process_extraction
                  #   + resolve() : nom YAML = vrai nom Python
                  #   (card.functions, puis numpy en repli — pas de registre)
  management.py   # CARD_list_all, CARD_info, CARD_management
  functions/      # fonctions hydro (delta, return_level, baseflow, bias,
                  #   apply_threshold... — correspondance R : docs/dev/RENAMING.md)
  cards/          # les fiches YAML (arborescence thématique)
tests/
  make_test_data.py   # données synthétiques 2 stations, 1970-2100
  run_R_corpus.R      # référence R corpus complet (package R CARD)
  run_py_corpus.py    # exécution Python + comparaison → corpus_report.csv
  validate_R.R / validate_py.py   # harnais 5 fiches de référence
```

Toute la mécanique de données (sampling adaptatif, sorties vectorielles,
kwargs-colonnes, colonnes creuses, filtres de lacunes) est portée par le
moteur stase — card ne gère que les fiches et leurs métadonnées.

## Tests

```bash
.python_env/bin/python -m pytest        # 40 tests rapides (~5 s)
.python_env/bin/python -m card.schema   # linter des 215 fiches YAML
```

Le linter vérifie structure, résolution des fonctions et cohérence des
fenêtres meta ↔ process (le contrôle qui aurait détecté le bug historique
des 29 fiches). La validation croisée contre R (ci-dessous) reste l'outil
de validation lourde.

## Validation croisée R ↔ Python (2026-07-11)

Corpus complet (~215 fiches) exécuté via card/stase et comparé au package
R CARD sur données synthétiques (2 stations × 131 ans) :

- **552 comparaisons identiques** (tol 1e-6) en mode parité rolling
  (`CARD_ROLL_COMPAT=rcpp`) ;
- 33 divergences résiduelles : comptage des lacunes autour des moyennes
  mobiles (R rend les NA invisibles au NApct après un rolling — RcppRoll
  convertit NA→NaN ; Python compte honnêtement, plus strict) ;
- 11 fiches crashent dans le package R lui-même (CR, CRS_season, FDC×5,
  QJC10, RA_ratio, RAl/RAs_ratio) — versions Python fonctionnelles, pas de
  référence possible.

```bash
cd tests
python3 make_test_data.py
Rscript run_R_corpus.R          # ~10 min
python3 run_py_corpus.py        # rapport → data/corpus_report.csv
CARD_ROLL_COMPAT=rcpp python3 run_py_corpus.py   # mode parité RcppRoll
```

## Divergences assumées avec le R

- **Rolling centré** : convention pandas (`center=True`) ; pour k pair la
  série est décalée de +1 position vs RcppRoll (dates dérivées ±1 jour).
  Choix délibéré : l'outil Python standard prime sur la réplication d'un
  détail d'implémentation R. Bascule de vérification : `CARD_ROLL_COMPAT=rcpp`.
- **Comptage des lacunes** : Python compte les NaN induits par les
  moyennes mobiles (R ne les voit pas) — légèrement plus strict près du
  seuil NApct.
- **Index 0-based** (`which.*NA`, apply_threshold first/last) : la chaîne
  complète avec la conversion is_date de stase redonne exactement les
  valeurs R.

## Suite

Historique de la refonte et décisions : `docs/dev/ROADMAP.md` (phases A-D
terminées). Correspondance des noms R → Python : `docs/dev/RENAMING.md`.
CI : `.github/workflows/tests.yml` (pytest + linter de fiches + ruff).
