# card <img src="img/flower_alt.png" align="right" width="140" height="140" alt=""/>

Ready-to-use **hydroclimatic variables**: low flows, floods, seasonality,
climate change. Each one is defined by a YAML card, and computed the same
way whether you call it from Python, from R or over the web.

**[Browse the catalogue](catalogue.md)** · **[read a name](grammar.md)**

## Start here

```python
import card

low = card.list_cards(phenomenon="low flows", output="series")
res = card.extract(data, cards=low["card"].unique())
```

```r
library(card4r)

low <- card_list(phenomenon = "basses eaux", output = "serie")
res <- card_extract(data, cards = unique(low$card))
```

`data` is a table with `id`, `date` and one column per input quantity
(`Q` for discharge, `R` for precipitation, `T` for temperature). The
result carries the values **and** the metadata of every variable it
produced.

No installation at all: `card-api` computes the same variables on Hub'Eau
discharge data, over a URL.

```bash
curl "https://card-api.riverly.inrae.fr/v1/extract?stations=K027401001&cards=VCN10"
```

## Names are meant to be read

From left to right: quantity (`Q` discharge, `R` precipitation, `T`
temperature), time step (`A` year, `M` month, `J` day), order statistic
(`N` minimum, `D` median, `X` maximum, nothing = mean), season. A prefix
transforms the output (`delta-` change between two periods, `rp-` return
period), a suffix qualifies it (`_summer`, `_H` projection horizon).

So `QJXA` is the annual maximum daily discharge, and `delta-QA_H` the
change of the annual mean between a reference period and a horizon. The
[full guide](grammar.md) takes five minutes.

## Where to go next

| | |
|---|---|
| **[Catalogue](catalogue.md)** | every variable, filterable, in both languages |
| **[Reading a name](grammar.md)** | the grammar, in one page |
| **[Functions](functions/hydrological.md)** | what the cards compute, and the functions you call |
| **[Ecosystem](ecosystem.md)** | card, card4r, card-api, stase, and which door to take |

Installation, examples and how to write your own card are in each
repository's README. This page only points the way.
