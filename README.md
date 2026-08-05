# card [<img src="docs/img/flower_alt.png" align="right" width="160" height="160" alt="card"/>](https://github.com/lou-heraut/stase)

<!-- badges: start -->
[![tests](https://github.com/lou-heraut/card/actions/workflows/tests.yml/badge.svg)](https://github.com/lou-heraut/card/actions/workflows/tests.yml)
[![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue)](https://lifecycle.r-lib.org/articles/stages.html)
![](https://img.shields.io/github/last-commit/lou-heraut/card)
[![License: GPL v3](https://img.shields.io/badge/license-GPL--3.0-bd0000)](LICENSE)
<!-- badges: end -->

**card** calcule des variables hydroclimatiques prêtes à l'emploi :
<!-- cards:count -->226 fiches, 472 variables<!-- /cards:count -->
(étiages, crues, saisonnalité, changement climatique...) définies en YAML
et exécutées par le moteur [stase](https://github.com/lou-heraut/stase).
Vous choisissez vos fiches, card fait le reste.

## Installation

```bash
pip install "stase @ git+https://github.com/lou-heraut/stase.git"
pip install "card-stase @ git+https://github.com/lou-heraut/card.git"
```

Dans cet ordre : `stase` n'est pas publié sur PyPI, donc card installé
seul ne saurait pas où trouver son moteur. Le nom d'installation est
`card-stase`, le nom `card` étant déjà pris sur PyPI ; le nom d'import
reste `card`. Sans git sur la machine, les mêmes paquets s'installent
depuis les archives du dépôt :

```bash
pip install https://github.com/lou-heraut/stase/archive/refs/heads/main.tar.gz \
            https://github.com/lou-heraut/card/archive/refs/heads/main.tar.gz
```

## Démarrage rapide

```python
import numpy as np
import pandas as pd
import card

# une chronique journalière : une colonne datetime, une colonne texte
# (identifiant de série) et les colonnes numériques requises par les fiches.
# Ici une série synthétique : saisonnière, en baisse lente.
dates = pd.date_range("1970-01-01", "2020-12-31", freq="D")
saison = 1 + 0.6 * np.cos(2 * np.pi * (dates.dayofyear.to_numpy() - 30) / 365)
data = pd.DataFrame({
    "date": dates,
    "Q": (np.random.default_rng(0).gamma(2, 5, len(dates))
          * saison * np.linspace(1.0, 0.75, len(dates))),
    "id": "ma_station",
})

res = card.extract(data, cards=["QA", "VCN10"])
res["data"]["VCN10"]     # un DataFrame par fiche : id, date, valeur
res["meta"]              # une ligne par variable : unité, nom, classification
```

Les fiches référencent les colonnes d'entrée par leur nom (`Q` pour le
débit, `T` pour la température...). Si vos colonnes s'appellent
autrement, passez `rename={"Qm3s": "Q"}` ; avec une seule colonne
numérique et une fiche à variable unique, la correspondance est
automatique (un avertissement le signale). Une colonne de dates en texte
au format ISO `YYYY-MM-DD` est convertie automatiquement.

## Tendance

```python
tr = card.trend(res)
tr["data"]["VCN10"][["id", "h", "p", "a", "a_relative"]]
#         id    h        p         a  a_relative
# ma_station True 0.017107 -0.010074   -0.440127
```

`h` dit si la tendance est significative au seuil demandé, `a` est la
pente de Sen dans l'unité de la variable et par an, `a_relative` la même
en pourcentage de la moyenne. Le test tient compte de l'autocorrélation
d'ordre 1 par défaut, les séries d'étiage en présentant le plus souvent.

## Choisir la fenêtre annuelle

Les fiches de basses eaux et de crue adaptent par défaut leur fenêtre à
chaque série : l'année démarre au mois le plus favorable, ce qui évite de
couper un événement en deux. Pour comparer des stations entre elles ou
rejouer un calcul à l'identique, on impose la même fenêtre partout :

```python
card.extract(data, cards=["VCN10"], sampling_period="preferred")  # celle déclarée par la fiche
card.extract(data, cards=["VCN10"], sampling_period="09-01")      # une fenêtre choisie
```

Seules les fenêtres annuelles sont écrasées. Une fenêtre partielle, comme
le mai-novembre d'une fiche estivale, fait partie de la définition de la
variable et n'est jamais touchée.

## Fiches à paramètre : seuils et horizons

Certaines fiches ont besoin d'une valeur que vous seul connaissez. Elle
se fournit comme une colonne du tableau d'entrée, constante par série.

Un seuil réglementaire, par exemple, pour les fiches `rp-` qui donnent la
période de retour d'un débit donné par les textes :

```python
d = data.assign(Q_lim=2.2)
card.extract(d, cards=["rp-VCN10"])["data"]["rp-VCN10"]
#         id  rp-VCN10
# ma_station  2.302126      -> ce seuil est atteint environ tous les 2,3 ans
```

Une station a souvent plusieurs seuils. `suffix=` applique la fiche à
chacun en un seul appel, à partir d'une colonne par seuil :

```python
d = data.assign(Q_lim_DOE=2.2, Q_lim_DCR=1.7)
card.extract(d, cards=["rp-VCN10"], suffix=["DOE", "DCR"])["data"]["rp-VCN10"]
#         id  rp-VCN10_DOE  rp-VCN10_DCR
# ma_station      2.302126     24.988053
```

La chronique `Q`, partagée par les deux calculs, n'est lue qu'une fois.
Chaque sortie a sa propre ligne dans `res["meta"]`, avec une colonne
`suffix` qui rappelle la variante. Pour que ces lignes portent un nom
lisible plutôt que la clé brute, nommez les variantes :

```python
card.extract(d, cards=["rp-VCN10"], suffix={
    "DOE": {"fr": {"name": "débit objectif d'étiage"}},
    "DCR": {"fr": {"name": "débit de crise"}},
})
# name_fr -> "Période de retour du débit objectif d'étiage au regard [...]"
```

Une période, de même, se fournit en colonnes plutôt que d'être figée dans
la fiche. Les fiches `delta-` comparent une référence à un horizon et
prennent donc quatre bornes, ce qui permet des horizons propres à chaque
station, par exemple définis par un degré de réchauffement :

```python
h = data.assign(ref_start="1970-01-01", ref_end="2000-12-31",
                horizon_start="2001-01-01", horizon_end="2020-12-31")
card.extract(h, cards=["delta-QA_H"])["data"]["delta-QA_H"]
#         id   delta-QA
# ma_station -14.671572     -> le module baisse de 14,7 % entre les deux périodes
```

Plusieurs horizons en un appel, avec le même mécanisme de suffixe :

```python
h = data.assign(
    ref_start_H1="1970-01-01", ref_end_H1="2000-12-31",
    horizon_start_H1="2001-01-01", horizon_end_H1="2010-12-31",
    ref_start_H2="1970-01-01", ref_end_H2="2000-12-31",
    horizon_start_H2="2011-01-01", horizon_end_H2="2020-12-31")
card.extract(h, cards=["delta-QA_H"], suffix=["H1", "H2"])["data"]["delta-QA_H"]
#         id  delta-QA_H1  delta-QA_H2
# ma_station    -11.51997   -18.173351
```

D'autres fiches ne comparent rien : elles calculent sur **une** période,
qu'elle soit future ou observée. Elles prennent alors `period_start` et
`period_end`, et leur métadonnée parle de période et non d'horizon :

```python
p = data.assign(period_start_obs="1976-01-01", period_end_obs="2005-12-31",
                period_start_fin="2001-01-01", period_end_fin="2020-12-31")
card.extract(p, cards=["QM"], suffix={
    "obs": {"fr": {"name": "la période observée 1976-2005"}},
    "fin": {"fr": {"name": "la période récente 2001-2020"}},
})
# -> colonnes QM_obs et QM_fin
# name_fr -> "Débit moyen mensuel sur la période observée 1976-2005"
```

Ces bornes sont **facultatives** (`period_start?` dans les entrées de la
fiche) : sans elles, la même fiche calcule sur toute la chronique et
l'annonce, « Débit moyen mensuel sur la chronique entière ». Une fiche
suffit donc là où il en fallait une par période. Le nom que vous donnez à
une variante est repris tel quel, article compris : écrivez « la période
observée » ou « le futur lointain » selon ce qui se lit le mieux.

Le même mécanisme sert à comparer deux jeux d'une même variable sur
n'importe quelle fiche, par exemple des colonnes `Q_obs` et `Q_sim` avec
`suffix=["obs", "sim"]`. `card.trend` suit ensuite ces variantes sans
qu'il faille les redéclarer.

## Ce qu'un résultat dit de lui-même

`res["meta"]` ne décrit pas seulement la variable, il identifie la
définition qui l'a produite :

```python
res["meta"][["variable_fr", "version", "swhid", "script_path"]]
# variable_fr version                swhid                    script_path
#          QA     1.0 swh:1:cnt:e1197d4d… flow/mean-flows/series/QA.yaml
```

(le SWHID est abrégé ici : c'est le hash du fichier de fiche, il change
avec elle.)

`version` est celle de la fiche, qui change dès que ses sorties changent.
`swhid` identifie le fichier lui-même dans [Software
Heritage](https://archive.softwareheritage.org/) : en collant
`https://archive.softwareheritage.org/` devant, on obtient la fiche telle
qu'elle était au moment du calcul, même des années plus tard, et même si
le dépôt a changé depuis. De quoi archiver un résultat sans perdre la
définition qui va avec.

Ça, c'est la **définition**. Quatre colonnes de plus disent quel
**logiciel** l'a exécutée :

```python
res["meta"][["card_version", "card_commit", "stase_version", "stase_commit"]]
# card_version card_commit stase_version stase_commit
#        0.3.1 c015502385… 0.6.1         836dfae29f…
```

Le numéro de version se lit facilement, mais il ne désigne un état unique
que le jour où il est publié : entre deux versions, des dizaines de
commits portent le même numéro. C'est le **commit** qui identifie
exactement le code qui a tourné, et `swh:1:rev:` suivi de ce commit en
est l'identifiant Software Heritage citable, sur le même modèle que
celui de la fiche.

Les mêmes valeurs se demandent seules, sans lancer de calcul :

```python
card.provenance()
# {'card_version': '0.3.1', 'card_commit': 'c015502385…',
#  'stase_version': '0.6.1', 'stase_commit': '836dfae29f…'}
```

**Une colonne de commit vide n'est pas une panne.** Elle dit que le code
qui a tourné venait d'une copie de travail modifiée, donc qu'il ne
correspond exactement à aucun commit publié : c'est le cas normal pendant
qu'on développe, et le signal qu'un tel résultat ne se cite pas.

## Trouver sa fiche

```python
card.list_cards()                          # toutes les variables, une par ligne
card.list_cards(phenomenon="basses eaux")  # filtre par phénomène (fr ou en)
card.list_cards(output="série")            # série, scalaire ou courbe
card.list_cards(season="estivale")         # fenêtre d'échantillonnage
card.list_cards(operator="delta")          # opérateur (delta, median...)
card.list_cards(variable="VCN")            # filtre par nom de variable
card.list_cards(search="minimum annuel")   # recherche dans les noms fr et en
card.info("VCN10")                         # la fiche, dessinée (voir plus bas)
```

Les facettes acceptent le français comme l'anglais (`output="série"` ou
`output="series"`). La recherche plein texte porte sur les noms, les
descriptions et les noms de variables : elle ne connaît que les mots
employés par les fiches, et le vocabulaire de la classification est le
chemin sûr pour trouver une famille (`phenomenon="basses eaux"` plutôt
que « étiage », qui n'est pas un mot du corpus).

Le catalogue complet est consultable en ligne :
[lou-heraut.github.io/card](https://lou-heraut.github.io/card/) ou
[docs/CARDS.md](docs/CARDS.md).

## Décoder un nom de fiche

Les identifiants ne sont pas arbitraires : ils se lisent de gauche à
droite, position par position (système Oberlin). Une fois la grille en
tête, un nom se déchiffre sans ouvrir la fiche.

```
  Q      J        D          A            (+ préfixe, + suffixe)
grandeur pas-de-temps  statistique   saison
```

- **Grandeur** : `Q` débit, `R` précipitations, `T` température, `ETP`
  évapotranspiration.
- **Pas de temps** : `A` année, `M` mois, `S` saison, `J` jour.
- **Statistique d'ordre** : `N` minimum, `D` médiane, `X` maximum,
  *rien* = moyenne (implicite), `Pq` = percentile *q* %.
- **Préfixe** (opération en plus, transforme la sortie) : `delta-`
  changement entre deux périodes, `mean-`/`median-` moyenne/médiane
  inter-annuelle d'une série, `rp-` période de retour, `alpha-` pente de
  tendance, `n-` dénombrement d'années.
- **Suffixe** : `-10` période de retour 10 ans, `_summer`/`_winter`
  saison restreinte, `_H` horizon de projection, `_month`/`_season`
  déclinaison (une sortie par mois / saison).

Quelques noms décodés :

| Nom | Lecture |
|---|---|
| `QA` | débit, annuel, moyenne (implicite) : moyenne annuelle du débit |
| `QJXA` | débit, journalier, maximum, annuel : débit journalier maximal annuel |
| `QMNA` | débit, mensuel, minimum, annuel : minimum annuel des débits mensuels |
| `VCN10` | volume (moyenne sur durée continue), min, 10 jours : min annuel du débit moyen sur 10 j |
| `QJDC10` | débit, journalier, médiane, lissé 10 j : régime journalier médian lissé sur 10 jours |
| `delta-QA_H` | changement de `QA` entre historique et horizon `H` |
| `rp-VCN10` | période de retour d'un `VCN10` au regard d'un seuil fourni |

La grille complète, avec les cas particuliers, est dans
[docs/dev/NOMENCLATURE.md](docs/dev/NOMENCLATURE.md).

## Lire une fiche

`card.info` dessine ce que la fiche calcule, plutôt que d'en lister les
champs : ce qui la classe, la chaîne des étapes avec leurs réglages, la
fenêtre d'échantillonnage sur douze mois, et ce qui est produit.

```
  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN10    Minimum annuel de la moyenne sur 10 jours du débit journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN10

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/VCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:17009e1e8ed488f299499c441bd8a5a41410f28d
```

Chaque étape porte, sous un coude, la phrase que la **fiche** écrit pour
cette colonne (son champ `method`), et sur le rang décalé, marqués `◦`,
les réglages du process. Dans la bande de douze mois, `▓` marque un mois
retenu, `·` un mois écarté et `┃` une borne : une fenêtre estivale donne
`············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···`. Une fiche à plusieurs sorties les
annonce chacune par un `◇`, identifiant d'abord et nom traduit entre
parenthèses quand il diffère : ce sont les noms des colonnes que vous
recevrez. La figure ne dit que ce que la fiche détermine, un process
`time_step: none` annonçant « aucune agrégation temporelle » plutôt
qu'une granularité de lignes, qui dépend là de ce que la fonction rend.

`card.info` accepte `lang="en"` et retourne par ailleurs le dict des
champs, inchangé, pour le code qui en dépend. Pour lire une fiche telle
qu'elle est écrite, `card.load_card("VCN10")` rend le dict complet
(les deux langues, tous les processus, le SWHID et le chemin du
fichier).

Trois entrées selon l'usage :

```python
card.info("VCN10")               # imprime la figure, retourne le dict
card.info("VCN10", quiet=True)   # ne rien imprimer : juste le dict
card.figure("VCN10")             # la figure en CHAÎNE, pour la servir
card.vocabulary()                # valeurs valides des facettes (fr/en)
```

`card.figure` est ce qu'il faut pour afficher une fiche ailleurs qu'un
terminal (page web, notebook) ; `card.vocabulary` donne la liste fermée
des valeurs que `list_cards` accepte en filtre, de quoi peupler un menu
sans les deviner.

## Développer sa propre fiche

```python
card.copy_cards(["VCN10"], dest="./mes_fiches")   # partir d'un modèle

# ... éditer mes_fiches/VCN10.yaml : renommer l'id ET le fichier,
# ajuster func, classification, métadonnées des deux langues

card.extract(data, cards=["VCN20"], path="./mes_fiches")      # tester
```

Valider avant de proposer en contribution :

```bash
python -m card.schema ./mes_fiches   # structure, vocabulaire de
                                     # classification, entrées connues,
                                     # cohérence des fenêtres, version
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
  cards/          # les fiches YAML, rangées par régime
                  #   (cards/<domaine>/<phénomène>/<forme>/)
```

Toute la mécanique de données (sampling adaptatif, sorties
vectorielles, filtres de lacunes) est portée par le moteur stase.
card ne gère que les fiches et leurs métadonnées.

## Citer

Ce recueil est un logiciel scientifique : merci de le citer si vous
l'utilisez dans un travail publié.

```
Héraut L., Dorchies D., Sauquet É., Vidal J.-P., Horner I., Santos L.
(2026). card : recueil de fiches hydroclimatiques CARD (version 0.4.0).
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
pip install -e . && pytest              # suite complète
python -m card.schema                   # linter des fiches YAML
python scripts/generate_catalog.py      # régénère docs/CARDS.md
```

CI : `.github/workflows/tests.yml` (pytest, linter de fiches, ruff).
Ce qui a changé et quand : [CHANGELOG.md](CHANGELOG.md). Correspondance
des noms R vers Python : `docs/dev/RENAMING.md`. Pistes ouvertes :
`docs/dev/CHANTIERS.md`.
