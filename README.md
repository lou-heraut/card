# card [<img src="docs/img/flower_alt.png" align="right" width="160" height="160" alt="card"/>](https://github.com/lou-heraut/stase)

<!-- badges: start -->
[![tests](https://github.com/lou-heraut/card/actions/workflows/tests.yml/badge.svg)](https://github.com/lou-heraut/card/actions/workflows/tests.yml)
[![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue)](https://lifecycle.r-lib.org/articles/stages.html)
![](https://img.shields.io/github/last-commit/lou-heraut/card)
[![License: GPL v3](https://img.shields.io/badge/license-GPL--3.0-bd0000)](LICENSE)
<!-- badges: end -->

**card** calcule des variables hydroclimatiques prêtes à l'emploi :
237 fiches (étiages, crues, saisonnalité, changement climatique...)
définies en YAML et exécutées par le moteur
[stase](https://github.com/lou-heraut/stase). Vous choisissez vos
fiches, card fait le reste.

## Installation

```bash
pip install "stase @ git+https://github.com/lou-heraut/stase.git"
pip install "card @ git+https://github.com/lou-heraut/card.git"
```

## Démarrage rapide

```python
import numpy as np
import pandas as pd
import card

# une chronique journalière : une colonne datetime, une colonne texte
# (identifiant de série) et les colonnes numériques requises par les fiches
dates = pd.date_range("1990-01-01", "2020-12-31", freq="D")
data = pd.DataFrame({
    "date": dates,
    "Q": np.random.default_rng(0).gamma(2, 5, len(dates)),
    "id": "ma_station",
})

res = card.extract(data, cards=["QA", "VCN10"])
res["data"]["QA"]        # un DataFrame par fiche
res["meta"]              # métadonnées (une ligne par variable)

# tendance Mann-Kendall + pente de Sen sur le résultat (AR1 par défaut)
tr = card.trend(res)
tr["data"]["QA"]         # H, p-value, pente (absolue et relative)

# fenêtre annuelle : celle des fiches (adaptative pour étiages/crues),
# ou imposée pour la reproductibilité et la comparaison entre stations
card.extract(data, cards=["VCN10"], sampling_period="preferred")
card.extract(data, cards=["VCN10"], sampling_period="09-01")
```

Les fiches référencent les colonnes d'entrée par leur nom (`Q` pour le
débit, `T` pour la température...). Si vos colonnes s'appellent
autrement, passez `rename={"Qm3s": "Q"}` ; avec une seule colonne
numérique et une fiche à variable unique, la correspondance est
automatique (un warning le signale). Une colonne de dates en texte au
format ISO `YYYY-MM-DD` est convertie automatiquement.

Certaines fiches prennent en plus une entrée constante par station,
comme le débit seuil réglementaire `Q_lim` des fiches `rp-VCN10`,
`rp-VCN30` et `rp-QMNA` (période de retour d'un seuil donné par les
textes, l'inverse de `VCN10-5`) : une colonne `Q_lim` de valeur
constante dans le tableau d'entrée.

Une station a souvent plusieurs seuils. `suffix=` applique la fiche à
chacun en un appel, à partir d'une colonne par seuil (`Q_lim_DOE`,
`Q_lim_DCR`) :

```python
card.extract(data, cards=["rp-VCN10"], suffix=["DOE", "DCR"])
# -> colonnes rp-VCN10_DOE et rp-VCN10_DCR
```

La chronique `Q`, partagée par les deux calculs, n'est lue qu'une fois.
Chaque sortie a sa propre ligne dans `res["meta"]`, avec une colonne
`suffix` qui rappelle la variante. Pour que ces lignes portent un nom
lisible plutôt que la clé brute, nommez les variantes :

```python
card.extract(data, cards=["rp-VCN10"], suffix={
    "DOE": {"fr": {"name": "débit objectif d'étiage"}},
    "DCR": {"fr": {"name": "débit de crise"}},
})
# name_fr -> "Période de retour du débit objectif d'étiage au regard [...]"
```

Le même mécanisme sert à comparer deux jeux d'une même variable sur
n'importe quelle fiche, par exemple des colonnes `Q_obs` et `Q_sim`
avec `suffix=["obs", "sim"]`. `card.trend` suit ensuite ces variantes
sans qu'il faille les redéclarer.

## Trouver sa fiche

```python
card.list_cards()                          # les 237 fiches (une ligne par variable)
card.list_cards(phenomenon="basses eaux")  # filtre par phénomène (fr ou en)
card.list_cards(output="série")            # série, scalaire ou courbe
card.list_cards(season="estivale")         # fenêtre d'échantillonnage
card.list_cards(operator="delta")          # opérateur (delta, median, trend...)
card.list_cards(variable="VCN")            # filtre par nom de variable
card.list_cards(search="étiage")           # recherche plein texte fr/en
card.info("VCN10")                         # détail : méthode, classification...
```

Le catalogue complet est consultable en ligne :
[lou-heraut.github.io/card](https://lou-heraut.github.io/card/) ou
[docs/CARDS.md](docs/CARDS.md).

## Développer sa propre fiche

```python
card.copy_cards(["VCN10"], dest="./mes_fiches")   # partir d'un modèle
# ... éditer mes_fiches/001_VCN10.yaml (id, func, classification...)
card.extract(data, cards=["ma_fiche"], path="./mes_fiches")   # tester
```

Valider avant de proposer en contribution :

```bash
python -m card.schema ./mes_fiches   # structure, vocabulaire de
                                     # classification, entrées connues
```

Les règles de nommage et de rédaction sont dans
[docs/dev/NOMENCLATURE.md](docs/dev/NOMENCLATURE.md), la classification
dans [docs/dev/TOPICS.md](docs/dev/TOPICS.md) ; les unités des
variables d'entrée sont définies une fois pour toutes dans
`src/card/inputs.yaml`.

## Architecture

```
src/card/
  loader.py       # YAML vers processus : défauts, horizons $Hx, tuples func
  extraction.py   # card.extract : chaîne P1..Pn via stase.extract
  management.py   # card.list_cards, card.info, card.copy_cards
  functions/      # fonctions hydro (baseflow, return_level, NSE, KGE...)
  cards/          # les 237 fiches YAML (cards/<domaine>/<forme>/)
```

Toute la mécanique de données (sampling adaptatif, sorties
vectorielles, filtres de lacunes) est portée par le moteur stase.
card ne gère que les fiches et leurs métadonnées.

## Citer

Ce recueil est un logiciel scientifique : merci de le citer si vous
l'utilisez dans un travail publié.

```
Héraut L., Dorchies D., Sauquet É., Vidal J.-P., Horner I., Santos L.
(2026). card : recueil de fiches hydroclimatiques CARD (version 0.2.0).
Software Heritage : swh:1:rev:<commit>
https://github.com/lou-heraut/card
```

Le dépôt est archivé sur [Software
Heritage](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/lou-heraut/card),
qui donne un identifiant pérenne par révision. Métadonnées lisibles par
machine : `CITATION.cff` et `codemeta.json` à la racine ; GitHub propose
d'ailleurs « Cite this repository » à partir du premier.

Si vous citez un résultat produit par le service
[card-api](https://github.com/lou-heraut/card-api), chaque réponse porte
déjà le commit et le SWHID exacts du code qui l'a calculé, ainsi que la
version de chaque fiche employée : reprenez-les plutôt que ce modèle.

## Origine

card est le port Python du package R
[CARD](https://github.com/lou-heraut/CARD) (INRAE, UR RiverLy), validé
par comparaison croisée avec R sur le corpus complet des fiches. Le
détail de la validation et les divergences documentées sont dans
[docs/dev/ORIGINE_R.md](docs/dev/ORIGINE_R.md). Licence GPL-3,
auteurs dans le fichier AUTHORS.

## Développement

```bash
pip install -e . && pytest              # 79 tests
python -m card.schema                   # linter des 237 fiches YAML
python scripts/generate_catalog.py      # régénère docs/CARDS.md
```

CI : `.github/workflows/tests.yml` (pytest, linter de fiches, ruff).
Ce qui a changé et quand : [CHANGELOG.md](CHANGELOG.md). Correspondance
des noms R vers Python : `docs/dev/RENAMING.md`. Pistes ouvertes :
`docs/dev/CHANTIERS.md`.
