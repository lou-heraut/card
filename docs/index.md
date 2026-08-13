# `card` <img src="img/flower_alt.png" align="right" width="140" height="140" alt=""/>

Ready-to-use **hydroclimatic variables**: low flows, floods, seasonality,
climate change. Each one is defined by a YAML card, and computed the same
way whether you call it from Python, from R or over the web.

**[Browse the catalogue](catalogue.md)** · **[read a symbol](symbols.md)**

## Start here

**In Python**, with the `card` package:

```python
import card

low = card.list_cards(phenomenon="low flows", output="series")
res = card.extract(data, cards=low["card"].unique())
```

**In R**, the same three lines through the `card4r` front end:

```r
library(card4r)

low <- card_list(phenomenon = "basses eaux", output = "serie")
res <- card_extract(data, cards = unique(low$card))
```

Both give the same numbers, because both run the same cards through the
same engine. `data` is a table with `id`, `date` and one column per input
quantity (`Q` for discharge, `R` for precipitation, `T` for temperature).
The result carries the values **and** the metadata of every variable it
produced.

**Without installing anything**, `card-api` computes the same variables
on Hub'Eau discharge data, over a URL:

```bash
curl "https://card-api.riverly.inrae.fr/v1/extract?stations=K027401001&cards=VCN10"
```

## Symbols are meant to be read

From left to right: quantity (`Q` discharge, `R` precipitation, `T`
temperature), time step (`A` year, `M` month, `J` day), order statistic
(`N` minimum, `D` median, `X` maximum, nothing = mean), season. A prefix
transforms the output (`delta-` change between two periods, `rp-` return
period), a suffix qualifies it (`_summer`, `_H` projection horizon).

So `QJXA` is the annual maximum daily discharge, and `delta-QA_H` the
change of the annual mean between a reference period and a horizon. The
[full guide](symbols.md) takes five minutes.

## Where to go next

| | |
|---|---|
| **[Catalogue](catalogue.md)** | every variable, filterable, in both languages, one page per card |
| **[Symbols](symbols.md)** | how a symbol is built, in one page |
| **[Toolbox](toolbox.md)** | the operations a card declares, `baseflow` to `return_level` |
| **[Write your own card](contribute.md)** | copy one, change it, check it |
| **[Python functions](functions.md)** | the dozen functions you call |
| **[Ecosystem](ecosystem.md)** | card, card4r, card-api, stase, and which door to take |

Installation and examples are in each repository's README. This page only
points the way.
