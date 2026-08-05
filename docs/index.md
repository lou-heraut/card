# card <img src="img/flower_alt.png" align="right" width="140" height="140" alt=""/>

Ready-to-use **hydroclimatic variables**: low flows, floods, seasonality,
climate change. Each one is defined by a YAML card, and computed the same
way whether you call it from Python, from R or over the web.

## Browse the catalogue

- **[Catalogue](CARDS.md)** · every variable, by domain and phenomenon,
  with the input columns it needs.
- **[Catalogue en français](CARDS.fr.md)** · le même, dans l'autre langue
  du corpus.

**Names are systematic, so they can be read.** From left to right:
quantity (`Q` discharge, `R` precipitation, `T` temperature), time step
(`A` year, `M` month, `J` day), order statistic (`N` minimum, `D` median,
`X` maximum, nothing = mean), season. A prefix transforms the output
(`delta-` change between two periods, `rp-` return period), a suffix
qualifies it (`_summer`, `_H` projection horizon).

So `QJXA` is the annual maximum daily discharge, and `delta-QA_H` the
change of the annual mean between a reference period and a horizon. The
full grammar is in [NOMENCLATURE.md](dev/NOMENCLATURE.md).

## Pick your door

| | |
|---|---|
| **[card](https://github.com/lou-heraut/card)** | in Python, on your own data |
| **[card4r](https://github.com/lou-heraut/card4r)** | in R, calling the same collection |
| **[card-api](https://github.com/lou-heraut/card-api)** | over the web, on Hub'Eau discharge data |

Installation, examples and how to write your own card are in each
repository's README. This page only points the way.
