# Reading a name

Names in the collection are **systematic**, so a name can be read rather
than looked up. `QJXA` is not a code to memorise: it is four decisions
written side by side.

## The four positions

Read left to right. Each position answers one question.

| | question | values |
|---|---|---|
| 1 | which quantity? | `Q` discharge · `R` precipitation · `T` temperature · `ETP` evapotranspiration |
| 2 | over what time step? | `J` day · `M` month · `S` season · `A` year |
| 3 | which order statistic? | `N` minimum · `D` median · `X` maximum · *nothing* mean |
| 4 | which season? | *nothing* whole year · `_summer` · `_winter` · `_DJF`… |

So:

```
QJXA   =  Q      J        X         A
          flow · daily · maximum · annual     the annual maximum daily flow

TMA    =  T      M        (rien)    A
          temp · monthly · mean   · annual    monthly mean air temperature

VCN10  =  V         C            N         10
          volume · consecutive · minimum · over 10 days
```

`VCN10` is the odd one, and it is the historical French hydrological
notation kept on purpose: *volume consécutif minimal sur 10 jours*, the
annual minimum of the 10-day moving average. Its family (`QNA`, `VCN3`,
`VCN10`, `VCN30`) is the same concept at four durations.

## Prefixes transform, suffixes qualify

A **prefix** changes what the number *is*:

| prefix | what it produces | example |
|---|---|---|
| `delta-` | the change between a reference period and a horizon | `delta-QA` |
| `median-`, `mean-` | the inter-annual reduction of a series to one value | `median-VCN10` |
| `rp-` | the return period of a value | `rp-VCN10` |
| `alpha-` | the trend slope over the series | `alpha-QA` |
| `n-` | a count of years | `n-QJXA-10` |

A **suffix** qualifies the same quantity:

| suffix | meaning |
|---|---|
| `_summer`, `_winter` | restricted sampling window |
| `_jan`…`_dec`, `_DJF`… | one value per month or per season |
| `_H` | computed over a projection horizon |
| `-10`, `-5` | return period in years, as in `VCN10-5` |

Put together, `delta-VCN10_summer` reads: *the change, between a
reference period and a horizon, of the annual minimum of the 10-day mean
discharge, over the summer window.*

## What a card says beyond its name

A name carries the definition, not the whole method. Three fields of each
card are written for people, at three levels of detail:

- **name** — short, sometimes vernacular: *Duration of low flows*.
- **description** — what the variable *is*, scientifically, and it is
  filled only when the name does not already carry it.
- **method** — the aggregation, step by step, one sentence per column
  produced, with the parameters.

`card.info("VCN10")` prints all three, drawn as the chain of steps that
computes it.

!!! note "The full grammar"
    This page is the reading guide. The complete rules, including the
    Oberlin system it derives from and the cases it does not cover, live
    in [NOMENCLATURE.md](https://github.com/lou-heraut/card/blob/main/docs/dev/NOMENCLATURE.md)
    in the repository.
