# card [<img src="docs/img/flower_alt.png" align="right" width="160" height="160" alt="card"/>](https://github.com/lou-heraut/stase)

<!-- badges: start -->
[![tests](https://github.com/lou-heraut/card/actions/workflows/tests.yml/badge.svg)](https://github.com/lou-heraut/card/actions/workflows/tests.yml)
[![Lifecycle: maturing](https://img.shields.io/badge/lifecycle-maturing-blue)](https://lifecycle.r-lib.org/articles/stages.html)
![](https://img.shields.io/github/last-commit/lou-heraut/card)
[![License: GPL v3](https://img.shields.io/badge/license-GPL--3.0-bd0000)](LICENSE)
<!-- badges: end -->

**card** computes ready-to-use hydroclimatic variables:
<!-- cards:count -->226 cards, 472 variables<!-- /cards:count -->
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

## Quick start

```python
import numpy as np
import pandas as pd
import card

# a daily record: a datetime column, a text column (series identifier)
# and the numeric columns the cards require. Here a synthetic series:
# seasonal, slowly decreasing.
dates = pd.date_range("1970-01-01", "2020-12-31", freq="D")
season = 1 + 0.6 * np.cos(2 * np.pi * (dates.dayofyear.to_numpy() - 30) / 365)
data = pd.DataFrame({
    "date": dates,
    "Q": (np.random.default_rng(0).gamma(2, 5, len(dates))
          * season * np.linspace(1.0, 0.75, len(dates))),
    "id": "my_station",
})

res = card.extract(data, cards=["QA", "VCN10"])
res["data"]["VCN10"]     # one DataFrame per card: id, date, value
res["meta"]              # one row per variable: unit, name, classification
```

Cards refer to input columns by name (`Q` for discharge, `T` for
temperature...). If your columns are named otherwise, pass
`rename={"Qm3s": "Q"}`; with a single numeric column and a
single-variable card, the match is automatic (a warning says so). A date
column given as text in ISO `YYYY-MM-DD` format is converted
automatically.

## Trend

```python
tr = card.trend(res)
tr["data"]["VCN10"][["id", "h", "p", "a", "a_relative"]]
#         id    h        p         a  a_relative
# my_station True 0.017107 -0.010074   -0.440127
```

`h` tells whether the trend is significant at the requested level, `a` is
the Sen slope in the unit of the variable per year, `a_relative` the same
as a percentage of the mean. The test accounts for first-order
autocorrelation by default, low-flow series showing it most often.

## Choosing the annual window

Low-flow and flood cards adapt their window to each series by default:
the year starts at the most favourable month, which avoids cutting an
event in two. To compare stations with one another, or to replay a
computation identically, the same window is imposed everywhere:

```python
card.extract(data, cards=["VCN10"], sampling_period="preferred")  # the one the card declares
card.extract(data, cards=["VCN10"], sampling_period="09-01")      # a chosen window
```

Only annual windows are overridden. A partial window, such as the
May-November of a summer card, is part of the definition of the variable
and is never touched.

## Cards with a parameter: thresholds and horizons

Some cards need a value that only you know. It is supplied as a column of
the input table, constant per series.

A regulatory threshold, for instance, for the `rp-` cards that give the
return period of a discharge set by law:

```python
d = data.assign(Q_lim=2.2)
card.extract(d, cards=["rp-VCN10"])["data"]["rp-VCN10"]
#         id  rp-VCN10
# my_station  2.302126      -> that threshold is reached about every 2.3 years
```

A station often has several thresholds. `suffix=` applies the card to
each of them in a single call, from one column per threshold:

```python
d = data.assign(Q_lim_DOE=2.2, Q_lim_DCR=1.7)
card.extract(d, cards=["rp-VCN10"], suffix=["DOE", "DCR"])["data"]["rp-VCN10"]
#         id  rp-VCN10_DOE  rp-VCN10_DCR
# my_station      2.302126     24.988053
```

The `Q` record, shared by both computations, is read only once. Each
output has its own row in `res["meta"]`, with a `suffix` column recalling
the variant. For those rows to carry a readable name rather than the raw
key, name the variants:

```python
card.extract(d, cards=["rp-VCN10"], suffix={
    "DOE": {"en": {"name": "low-flow objective"}},
    "DCR": {"en": {"name": "crisis flow threshold"}},
})
# name_en -> "Return period of the low-flow objective with respect to [...]"
```

A period, likewise, is supplied as columns rather than frozen in the
card. The `delta-` cards compare a reference with a horizon and therefore
take four bounds, which allows horizons specific to each station, defined
for instance by a warming level:

```python
h = data.assign(ref_start="1970-01-01", ref_end="2000-12-31",
                horizon_start="2001-01-01", horizon_end="2020-12-31")
card.extract(h, cards=["delta-QA_H"])["data"]["delta-QA_H"]
#         id   delta-QA
# my_station -14.671572     -> the mean flow drops by 14.7 % between the two periods
```

Several horizons in one call, with the same suffix mechanism:

```python
h = data.assign(
    ref_start_H1="1970-01-01", ref_end_H1="2000-12-31",
    horizon_start_H1="2001-01-01", horizon_end_H1="2010-12-31",
    ref_start_H2="1970-01-01", ref_end_H2="2000-12-31",
    horizon_start_H2="2011-01-01", horizon_end_H2="2020-12-31")
card.extract(h, cards=["delta-QA_H"], suffix=["H1", "H2"])["data"]["delta-QA_H"]
#         id  delta-QA_H1  delta-QA_H2
# my_station    -11.51997   -18.173351
```

Other cards compare nothing: they compute over **one** period, future or
observed. They then take `period_start` and `period_end`, and their
metadata speaks of a period rather than a horizon:

```python
p = data.assign(period_start_obs="1976-01-01", period_end_obs="2005-12-31",
                period_start_fin="2001-01-01", period_end_fin="2020-12-31")
card.extract(p, cards=["QM"], suffix={
    "obs": {"en": {"name": "the observed period 1976-2005"}},
    "fin": {"en": {"name": "the recent period 2001-2020"}},
})
# -> columns QM_obs and QM_fin
# name_en -> "Mean monthly discharge over the observed period 1976-2005"
```

These bounds are **optional** (`period_start?` in the card's inputs):
without them, the same card computes over the whole record and says so,
"Mean monthly discharge over the whole record". One card therefore
suffices where one per period used to be needed.

**The name you give a variant is taken as is**, and where it lands in the
sentence differs between the two families, so it is worth a look:

| family | the sentence reads | give a name like |
|---|---|---|
| period cards (`QM`, `FDC`...) | "over **{name}**" | a noun phrase with its article: "the observed period 1976-2005" |
| horizon cards (`delta-*_H`) | "the **{name}** horizon" | an adjective, no article: "near future", "2041-2070", "+2 °C warming" |

The French templates place the name after the noun (`l'horizon {name}`),
where an adjective reads naturally too. Keep horizon names short: "the
near future (2021-2050) horizon" is heavier than "the near future
horizon", and the period belongs in the card's own metadata anyway.

The same mechanism serves to compare two sets of one variable on any
card, for instance columns `Q_obs` and `Q_sim` with
`suffix=["obs", "sim"]`. `card.trend` then follows those variants without
having to redeclare them.

## What a result says about itself

`res["meta"]` does not only describe the variable, it identifies the
definition that produced it:

```python
res["meta"][["variable_en", "version", "swhid", "script_path"]]
# variable_en version                swhid                    script_path
#          QA     1.0 swh:1:cnt:e1197d4d… flow/mean-flows/series/QA.yaml
```

(the SWHID is abbreviated here: it is the hash of the card file, and it
changes with it.)

`version` is that of the card, which changes as soon as its outputs
change. `swhid` identifies the file itself in [Software
Heritage](https://archive.softwareheritage.org/): prefixing it with
`https://archive.softwareheritage.org/` gives the card as it was at the
time of the computation, even years later, and even if the repository has
changed since. Enough to archive a result without losing the definition
that goes with it.

That is the **definition**. Four more columns say which **software**
executed it:

```python
res["meta"][["card_version", "card_commit", "stase_version", "stase_commit"]]
# card_version card_commit stase_version stase_commit
#        0.4.0 64c4d50c07… 0.6.1         f3067f115a…
```

A version number is easy to read, but it designates a unique state only
on the day it is published: between two versions, dozens of commits carry
the same number. It is the **commit** that identifies exactly the code
that ran, and `swh:1:rev:` followed by that commit is its citable
Software Heritage identifier, on the same pattern as the card's.

The same values can be asked for on their own, without running a
computation:

```python
card.provenance()
# {'card_version': '0.4.0', 'card_commit': '64c4d50c07…',
#  'stase_version': '0.6.1', 'stase_commit': 'f3067f115a…'}
```

**An empty commit column is not a failure.** It says that the code that
ran came from a modified working copy, and therefore matches no published
commit exactly: that is the normal case while developing, and the signal
that such a result is not to be cited.

## Finding a card

```python
card.list_cards()                        # every variable, one per row
card.list_cards(phenomenon="low flows")  # by phenomenon (English or French)
card.list_cards(output="series")         # series, scalar or curve
card.list_cards(season="summer")         # sampling window
card.list_cards(operator="delta")        # operator (delta, median...)
card.list_cards(variable="VCN")          # by variable name
card.list_cards(search="annual minimum") # full text over English and French names
card.info("VCN10")                       # the card, drawn (see below)
```

Facets accept English as well as French (`output="series"` or
`output="série"`). Full-text search covers names, descriptions and
variable names: it only knows the words the cards use, and the
classification vocabulary is the safe path to find a family
(`phenomenon="low flows"` rather than "drought", which is not a word of
the collection).

The full catalogue is available online:
[lou-heraut.github.io/card](https://lou-heraut.github.io/card/), or as
files: [docs/CARDS.md](docs/CARDS.md) and its French counterpart
[docs/CARDS.fr.md](docs/CARDS.fr.md).

## Decoding a card name

Identifiers are not arbitrary: they read left to right, position by
position (Oberlin system). Once the grid is in mind, a name deciphers
without opening the card.

```
  Q      J        D          A            (+ prefix, + suffix)
quantity time-step statistic  season
```

- **Quantity**: `Q` discharge, `R` precipitation, `T` temperature, `ETP`
  evapotranspiration.
- **Time step**: `A` year, `M` month, `S` season, `J` day.
- **Order statistic**: `N` minimum, `D` median, `X` maximum, *nothing* =
  mean (implicit), `Pq` = percentile *q* %.
- **Prefix** (an extra operation, transforming the output): `delta-`
  change between two periods, `mean-`/`median-` inter-annual mean/median
  of a series, `rp-` return period, `alpha-` trend slope, `n-` count of
  years.
- **Suffix**: `-10` ten-year return period, `_summer`/`_winter`
  restricted season, `_H` projection horizon, `_month`/`_season` variant
  (one output per month / season).

A few names decoded:

| Name | Reading |
|---|---|
| `QA` | discharge, annual, mean (implicit): annual mean discharge |
| `QJXA` | discharge, daily, maximum, annual: annual maximum daily discharge |
| `QMNA` | discharge, monthly, minimum, annual: annual minimum of monthly discharges |
| `VCN10` | volume (mean over a continuous duration), min, 10 days: annual min of 10-day mean flow |
| `QJDC10` | discharge, daily, median, smoothed over 10 days: median daily regime smoothed over 10 days |
| `delta-QA_H` | change of `QA` between the historical period and horizon `H` |
| `rp-VCN10` | return period of a `VCN10` with respect to a supplied threshold |

The complete grid, with its special cases, is in
[docs/dev/NOMENCLATURE.md](docs/dev/NOMENCLATURE.md).

## Reading a card

`card.info` draws what the card computes, rather than listing its fields:
what classifies it, the chain of steps with their settings, the sampling
window over twelve months, and what comes out.

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

Each step carries, under an elbow, the sentence the **card** writes for
that column (its `method` field), and on the indented rank, marked `◦`,
the settings of the process. In the twelve-month band, `▓` marks a month
kept, `·` a month left out and `┃` a bound: a summer window gives
`············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···`. A card with several outputs
announces each with a `◇`, identifier first and translated name in
parentheses when it differs: those are the names of the columns you will
receive. The figure says only what the card determines, a process with
`time_step: none` announcing "no temporal aggregation" rather than a row
granularity, which there depends on what the function returns.

`card.info` accepts `lang="en"` and also returns the dict of fields,
unchanged, for code that depends on it. To read a card as it is written,
`card.load_card("VCN10")` returns the full dict (both languages, all
processes, the SWHID and the file path).

Three entry points depending on use:

```python
card.info("VCN10")               # prints the figure, returns the dict
card.info("VCN10", quiet=True)   # print nothing: just the dict
card.figure("VCN10")             # the figure as a STRING, to serve it
card.vocabulary()                # valid facet values (fr/en)
```

`card.figure` is what you need to display a card somewhere other than a
terminal (web page, notebook); `card.vocabulary` gives the closed list of
values `list_cards` accepts as filters, enough to populate a menu without
guessing them.

## Writing your own card

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

Naming and writing rules are in
[docs/dev/NOMENCLATURE.md](docs/dev/NOMENCLATURE.md), the classification
in [docs/dev/TOPICS.md](docs/dev/TOPICS.md); the units of input variables
are defined once and for all in `src/card/inputs.yaml`.

## Architecture

```
src/card/
  loader.py       # YAML to processes: defaults, $Hx horizons, func tuples
  extraction.py   # card.extract: chains P1..Pn through stase.extract
  management.py   # card.list_cards, card.info, card.copy_cards
  provenance.py   # which software computed, and how it is known
  functions/      # hydrological functions (baseflow, return_level, NSE, KGE...)
  cards/          # the YAML cards, filed by regime
                  #   (cards/<domain>/<phenomenon>/<form>/)
```

All the data machinery (adaptive sampling, vector outputs, gap filters)
is carried by the stase engine. card only handles the cards and their
metadata.

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
(2026). card: the CARD collection of hydroclimatic cards (version 0.4.0).
Software Heritage: swh:1:rev:<commit>
https://github.com/lou-heraut/card
```

The repository is archived on [Software
Heritage](https://archive.softwareheritage.org/browse/origin/directory/?origin_url=https://github.com/lou-heraut/card),
which gives a persistent identifier per revision. Machine-readable
metadata: `CITATION.cff` and `codemeta.json` at the root; GitHub offers
"Cite this repository" from the former.

If you are citing a result produced by the
[card-api](https://github.com/lou-heraut/card-api) service, every
response already carries the exact commit and SWHID of the code that
computed it, along with the version of each card used: take those rather
than this template.

## Origin

card is the Python port of the R package
[CARD](https://github.com/lou-heraut/CARD-R) (INRAE, UR RiverLy),
validated by cross-comparison with R over the complete collection of
cards. The details of the validation and the documented divergences are
in [docs/dev/ORIGINE_R.md](docs/dev/ORIGINE_R.md). GPL-3 licence, authors
in the AUTHORS file.

## Development

```bash
pip install -e . && pytest              # full suite
python -m card.schema                   # linter for the YAML cards
python scripts/generate_catalog.py      # regenerates both catalogues
```

CI: `.github/workflows/tests.yml` (pytest, card linter, ruff). What
changed and when: [CHANGELOG.md](CHANGELOG.md). R to Python name mapping:
`docs/dev/RENAMING.md`. Open leads: `docs/dev/CHANTIERS.md`.
