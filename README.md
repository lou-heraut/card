# card [<img src="https://raw.githubusercontent.com/lou-heraut/card/main/docs/img/flower_alt.png" align="right" width="160" height="160" alt="card"/>](https://github.com/lou-heraut/stase)

<!-- badges: start -->
[![tests](https://github.com/lou-heraut/card/actions/workflows/tests.yml/badge.svg)](https://github.com/lou-heraut/card/actions/workflows/tests.yml)
[![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue)](https://lifecycle.r-lib.org/articles/stages.html)
![](https://img.shields.io/github/last-commit/lou-heraut/card)
[![License: GPL v3](https://img.shields.io/badge/license-GPL--3.0-bd0000)](https://github.com/lou-heraut/card/blob/main/LICENSE)
<!-- badges: end -->

**card** computes ready-to-use hydroclimatic variables:
<!-- cards:count -->226 cards, 444 variables<!-- /cards:count -->
(low flows, floods, seasonality, climate change...) defined in YAML and
executed by the [stase](https://github.com/lou-heraut/stase) engine. You
pick your cards, card does the rest.

## Installation

```bash
pip install "stase @ git+https://github.com/lou-heraut/stase.git"
pip install "card-stase @ git+https://github.com/lou-heraut/card.git"
```

In that order: `stase` is not published on PyPI, so card installed alone
would not know where to find its engine. The install name is
`card-stase`, the name `card` being already taken on PyPI; the import
name stays `card`. Without git on the machine, the same packages install
from repository archives:

```bash
pip install https://github.com/lou-heraut/stase/archive/refs/heads/main.tar.gz \
            https://github.com/lou-heraut/card/archive/refs/heads/main.tar.gz
```

**From R**, the same collection is used through
[card4r](https://github.com/lou-heraut/card4r), which calls card rather
than rewriting it, and provisions Python on its own:

```r
remotes::install_github("lou-heraut/card4r")
```

## Using card

### A first extraction

The examples below run on a real record: the Yzeron at Craponne, a
periurban catchment west of Lyon, gauged since 1970. The data comes from
[Hub'Eau](https://hubeau.eaufrance.fr/), the French open hydrological
API, which needs no key.

```python
import json
import urllib.request
import pandas as pd
import card

url = ("https://hubeau.eaufrance.fr/api/v2/hydrometrie/obs_elab"
       "?code_entite=V301501001&grandeur_hydro_elab=QmnJ"
       "&date_debut_obs_elab=1970-01-01&size=20000")
obs = pd.DataFrame(json.load(urllib.request.urlopen(url))["data"])

data = pd.DataFrame({
    "date": pd.to_datetime(obs["date_obs_elab"]),
    "Q": obs["resultat_obs_elab"] / 1000,          # Hub'Eau serves L/s
    "id": obs["code_station"],
})
# 19273 daily values, 1970-01-01 to 2022-10-26
```

Three columns are all card needs: a date, a series identifier, and the
numeric columns the cards ask for (`Q` for discharge, `T` for
temperature, `R` for precipitation). Then:

```python
res = card.extract(data, cards=["QA", "VCN10"])

res["data"]["QA"]
#         id       date       QA
# V301501001 1969-09-01      NaN
# V301501001 1970-09-01 0.296784
# V301501001 1971-09-01 0.278617

res["data"]["VCN10"]
#         id       date  VCN10
# V301501001 1969-02-01    NaN
# V301501001 1970-02-01 0.0155
# V301501001 1971-02-01 0.0213
```

One DataFrame per card. The first row is empty because the record starts
mid-year, and the two cards do not use the same window: `QA` runs over
the hydrological year starting in September, `VCN10` starts its year at
the month of highest flows, February here. Both are explained below.

The extraction also prints a warning, *19 missing time steps inserted*. A
record of 53 years has holes; card materialises them as gaps rather than
ignoring them, and counts them against the tolerance each card declares.
Silence would have been the worrying answer.

Alongside the values, `res["meta"]` holds one row per variable produced:

```python
res["meta"][["variable_en", "unit_en", "name_en", "output_en", "version"]]
# variable_en      unit_en                                      name_en output_en version
#          QA m^{3}.s^{-1}                  Annual mean daily discharge    series     1.0
#       VCN10 m^{3}.s^{-1} Annual minimum of 10-day mean daily discharge    series     1.1
```

That table is the point of the collection: the numbers never travel
alone. It carries the unit, the name in both languages, the
classification, the method step by step, and what it takes to trace the
computation, which the last section of this part covers.

If your columns are named otherwise, pass `rename={"Qm3s": "Q"}`; with a
single numeric column and a single-variable card, the match is automatic
and a warning says so. A date column given as text in ISO `YYYY-MM-DD`
format is converted automatically.

### Finding your variable

The whole collection is browsable online:
**[the catalogue](https://lou-heraut.github.io/card/CARDS)**, and
[in French](https://lou-heraut.github.io/card/CARDS.fr). From Python:

```python
card.list_cards()                        # every variable, one per row
card.list_cards(phenomenon="low flows")  # by hydrological phenomenon
card.list_cards(output="series")         # a series, versus a scalar or a curve
card.list_cards(statistic="change")      # the change between two periods
card.list_cards(season="summer")         # restricted sampling window
card.list_cards(variable="VCN")          # by variable name
card.list_cards(search="annual minimum") # over names and descriptions
card.info("VCN10")                       # one card, drawn
```

Facets accept English as well as French (`output="series"` or
`output="série"`). The classification vocabulary is the safe path to a
family: `phenomenon="low flows"` rather than "drought", which is not a
word the cards use. `card.vocabulary()` gives the closed list of values
each facet accepts, enough to populate a menu without guessing.

**Selecting a family is also how you compute one.** The listing has one
row per variable; the `card` column says which card produces it, and
that is what `extract` takes:

```python
low = card.list_cards(phenomenon="low flows", output="series")
res = card.extract(data, cards=low["card"].unique())
```

The two names differ whenever one card produces several columns:
`mean-TMA_jan` is a variable of the card `mean-TMA_month`.

**Names are systematic, so they can be read** rather than looked up.
Left to right:

```
  Q      J        D          A            (+ prefix, + suffix)
quantity time-step statistic  season
```

- **Quantity**: `Q` discharge, `R` precipitation, `T` temperature, `ETP`
  evapotranspiration.
- **Time step**: `A` year, `M` month, `S` season, `J` day.
- **Order statistic**: `N` minimum, `D` median, `X` maximum, *nothing* =
  mean, `Pq` = percentile *q* %.
- **Prefix**, an extra operation on the output: `delta-` change between
  two periods, `mean-`/`median-` inter-annual, `rp-` return period,
  `alpha-` trend slope, `n-` count of years.
- **Suffix**, a qualifier: `-10` ten-year return period,
  `_summer`/`_winter`, `_H` projection horizon, `_month`/`_season` one
  output per month or season.

| Name | Reading |
|---|---|
| `QA` | discharge, annual, mean: annual mean discharge |
| `QJXA` | discharge, daily, maximum, annual |
| `QMNA` | discharge, monthly, minimum, annual |
| `VCN10` | volume over a continuous duration, minimum, 10 days |
| `delta-QA_H` | change of `QA` between a reference period and horizon `H` |
| `rp-VCN10` | return period of a `VCN10` against a supplied threshold |

The complete grammar, with its special cases, is in
[NOMENCLATURE.md](https://github.com/lou-heraut/card/blob/main/docs/dev/NOMENCLATURE.md).

### Trend

```python
tr = card.trend(res)

tr["data"]["VCN10"][["id", "h", "p", "a", "a_relative"]]
#         id    h        p         a  a_relative
# V301501001 True 0.056716 -0.000115   -1.069519
```

The low flows of this catchment decline by about **1.1 % per year** over
the record. `h` says whether the trend is significant at the requested
level, `0.1` by default, `a` is the Sen slope in the unit of the variable
per year, and `a_relative` the same as a percentage of the mean. The test
accounts for first-order autocorrelation by default, low-flow series
showing it most often.

### Choosing the annual window

Low-flow and flood cards adapt their window to each series by default:
the year starts at the most favourable month, which avoids cutting an
event in two. That is why `VCN10` above is dated in February. To compare
stations with one another, or to replay a computation identically, the
same window is imposed everywhere:

```python
card.extract(data, cards=["VCN10"], sampling_period="preferred")
#         id       date  VCN10
# V301501001 1970-01-01 0.0155      -> same values, January window
```

Only annual windows are overridden. A partial window, such as the
May-November of a summer card, is part of the definition of the variable
and is never touched.

### Cards that need a parameter

Some cards need a value that only you know: a regulatory threshold, the
bounds of a projection horizon. It is supplied as a column of the input
table, constant per series, rather than frozen into the card.

```python
# a threshold: how often does the low flow fall below 10 L/s?
card.extract(data.assign(Q_lim=0.010), cards=["rp-VCN10"])["data"]["rp-VCN10"]
#         id  rp-VCN10
# V301501001  1.483522      -> reached about every 1.5 years

# a horizon: how much did the mean flow change between two periods?
periods = data.assign(ref_start="1970-01-01", ref_end="1999-12-31",
                      horizon_start="2000-01-01", horizon_end="2022-10-26")
card.extract(periods, cards=["delta-QA_H"])["data"]["delta-QA_H"]
#         id   delta-QA
# V301501001 -12.813051    -> the mean flow lost 12.8 % between the two periods
```

A station often has several thresholds, and a study several horizons.
`suffix=` applies the card to each of them in one call, from one column
per variant (`Q_lim_DOE`, `Q_lim_DCR`), and gives each output its own row
in `res["meta"]`. The shared record is read only once. Naming the
variants makes those rows readable:

```python
card.extract(d, cards=["rp-VCN10"], suffix={
    "DOE": {"en": {"name": "low-flow objective"}},
    "DCR": {"en": {"name": "crisis flow threshold"}},
})
# name_en -> "Return period of the low-flow objective in the distribution of [...]"
```

The name you give lands in a different place depending on the family, so
it is worth a look: period cards read "over **{name}**" and want a noun
phrase with its article, "the observed period 1976-2005"; horizon cards
read "the **{name}** horizon" and want an adjective, "near future". Cards
whose period bounds are optional compute over the whole record without
them, and say so.

### What a result says about itself

`res["meta"]` does not only describe the variable, it identifies both the
**definition** that produced it and the **software** that ran:

```python
res["meta"][["variable_en", "version", "swhid", "card_commit", "stase_commit"]]
# variable_en version               swhid card_commit stase_commit
#          QA     1.0 swh:1:cnt:e1197d4d…           …            …
```

`version` is that of the card, which changes as soon as its outputs
change. `swhid` identifies the card file in [Software
Heritage](https://archive.softwareheritage.org/): prefixing it with
`https://archive.softwareheritage.org/` gives the card as it was at the
time of the computation, even years later.

The two commits identify the code. A version number is easy to read, but
it designates a unique state only on the day it is published: between two
releases, dozens of commits carry the same number. `swh:1:rev:` followed
by a commit is its citable Software Heritage identifier, on the same
pattern as the card's. `card.provenance()` returns the same values
without running a computation.

**An empty commit column is not a failure.** It says the code came from a
modified working copy and matches no published commit, which is the
normal case while developing, and the signal that such a result is not to
be cited.

## What a card is

### Anatomy of a card

A card is a YAML file. Here is `QA`, the annual mean discharge:

```yaml
id: QA
version: "1.0"
authors: ["Louis Héraut (INRAE, UR RiverLy)"]
date: "2026-04-30"

meta:
  en:
    variable: QA
    unit: "m^{3}.s^{-1}"
    name: Annual mean daily discharge
    description: ""
    method:
      P1:
        QA: annual aggregation [09-01, 08-31] - mean
    sampling_period: ["09-01", "08-31"]
    classification:
      domain: flow
      phenomenon: mean flows
      aspect: magnitude
      season: annual
      output: series

  fr:
    variable: QA
    name: Moyenne annuelle du débit journalier
    ...                                    # same fields, French labels

  global:
    input_vars: Q
    preferred_sampling_period: "09-01"
    palette: ["#452C1A", "#7F4A23", ...]

process:
  P1:
    func:
      QA: [nanmean, "Q"]
    time_step: year
    sampling_period: "09-01"
    max_na_pct: 3
    max_na_years: 10
```

Two parts, and the split matters.

**`meta` is written for people.** Everything a reader needs, in both
languages at equal standing: the unit, the name, the description when the
name is not enough, and `method`, one sentence per column produced, which
is what the drawn figure displays. `classification` places the card on
controlled facets, checked against a central vocabulary, and the folder
path must match it: `flow/mean-flows/series/QA.yaml`. None of this is
decoration, it is the metadata that travels with your results.

**`process` is what runs.** One block per step, `P1` then `P2` if the
computation chains. `func` names the function and the columns it takes,
resolved first among card's hydrological functions then among numpy, so
`nanmean` is the real numpy one. `time_step` and `sampling_period` set
the aggregation, `max_na_pct` and `max_na_years` the tolerance to gaps.

A card with several steps simply adds `P2`, taking as input the column
`P1` produced. That is how `VCN10` works: a 10-day moving average, then
the annual minimum of it.

### Reading a card from Python

`card.info` draws what a card computes rather than listing its fields:

```
  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN10                    Annual minimum of 10-day mean daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN10

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/VCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:17009e1e8ed488f299499c441bd8a5a41410f28d
```

Each step carries the sentence the **card** writes for that column, and
on the indented rank, marked `◦`, the settings of the process. In the
twelve-month band, `▓` marks a month kept and `·` a month left out: a
summer window gives `············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···`.

```python
card.info("VCN10")               # prints the figure, returns the dict
card.info("VCN10", lang="en")    # the same in English
card.info("VCN10", quiet=True)   # print nothing: just the dict
card.figure("VCN10")             # the figure as a STRING, to serve it
card.load_card("VCN10")          # the card as written, both languages
```

### Writing your own

```python
card.copy_cards(["VCN10"], dest="./my_cards")   # start from a model

# ... edit my_cards/VCN10.yaml: rename the id AND the file,
# adjust func, classification, metadata in both languages

card.extract(data, cards=["VCN20"], path="./my_cards")      # test it
```

Validate before proposing a contribution:

```bash
python -m card.schema ./my_cards   # structure, classification vocabulary,
                                   # known inputs, window consistency,
                                   # version
```

The linter is strict on purpose: it checks that the folder matches the
classification, that every input exists in the registry, that the
`method` sentences match what `process` actually does, and that adaptive
windows follow the convention of their phenomenon. Naming and writing
rules are in
[NOMENCLATURE.md](https://github.com/lou-heraut/card/blob/main/docs/dev/NOMENCLATURE.md),
the classification in
[TOPICS.md](https://github.com/lou-heraut/card/blob/main/docs/dev/TOPICS.md); input units
are defined once and for all in `src/card/inputs.yaml`.

## The ecosystem

| | |
|---|---|
| **card** | the card collection, in Python (you are here) |
| [stase](https://github.com/lou-heraut/stase) | the aggregation and trend engine |
| [card4r](https://github.com/lou-heraut/card4r) | the same collection, called from R |
| [card-api](https://github.com/lou-heraut/card-api) | the web service, on Hub'Eau discharge data |
| [CARD-R](https://github.com/lou-heraut/CARD-R) · [EXstat](https://github.com/lou-heraut/EXstat) | the historical R packages, superseded |

## Citing

This collection is scientific software: please cite it if you use it in
published work.

```
Héraut L., Dorchies D., Sauquet É., Vidal J.-P., Horner I., Santos L.
(2026). card: the CARD collection of hydroclimatic cards (version 0.13.0).
Software Heritage: swh:1:rev:<commit>
https://github.com/lou-heraut/card
```

The repository is archived on [Software
Heritage](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/lou-heraut/card),
which gives a persistent identifier per revision. Machine-readable
metadata: `CITATION.cff` and `codemeta.json` at the root.

If you are citing a result produced by the
[card-api](https://github.com/lou-heraut/card-api) service, every
response already carries the exact commit and SWHID of the code that
computed it, along with the version of each card used: take those rather
than this template.

## Origin

card is the Python port of the R package
[CARD](https://github.com/lou-heraut/CARD-R) (INRAE, UR RiverLy),
validated by cross-comparison with R over the complete collection. The
details of the validation and the documented divergences are in
[ORIGINE_R.md](https://github.com/lou-heraut/card/blob/main/docs/dev/ORIGINE_R.md). GPL-3
licence, authors in the AUTHORS file.

## Development

```bash
pip install -e . && pytest              # full suite
python -m card.schema                   # linter for the YAML cards
python scripts/generate_catalog.py      # regenerates both catalogues
make                                    # every everyday command, listed
```

```
src/card/
  loader.py       # YAML to processes: defaults, $Hx horizons, func tuples
  extraction.py   # card.extract: chains P1..Pn through stase.extract
  management.py   # card.list_cards, card.info, card.copy_cards
  provenance.py   # which software computed, and how it is known
  functions/      # hydrological functions (baseflow, return_level, NSE, KGE...)
  cards/          # the YAML cards, filed by regime
```

All the data machinery (adaptive sampling, vector outputs, gap filters)
is carried by the stase engine. card only handles the cards and their
metadata.

CI: `.github/workflows/tests.yml` (pytest, card linter, ruff). What
changed and when:
[CHANGELOG.md](https://github.com/lou-heraut/card/blob/main/CHANGELOG.md).
R to Python name mapping:
[RENAMING.md](https://github.com/lou-heraut/card/blob/main/docs/dev/RENAMING.md). Open
leads: [CHANTIERS.md](https://github.com/lou-heraut/card/blob/main/docs/dev/CHANTIERS.md).
