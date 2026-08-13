# Write your own card

A card is a YAML file. Writing one takes minutes, and nothing has to be
compiled: the collection shipped with the package and the cards in your
own folder are read the same way.

Do it when the variable you need does not exist, or exists with settings
that are not yours: another sampling window, another threshold, another
duration.

## Start from a card that already works

```python
import card

card.copy_cards(["VCN10"], dest="./my_cards")
```

Pick the closest model rather than an empty file. Everything in a card is
optional to *read* and mandatory to *get right*, so starting from
something the linter already accepts saves the whole first round.

Then edit `my_cards/VCN10.yaml`: **rename the `id` and the file the same
way**, the two must match.

## The anatomy of a card

This is `QA`, the annual mean daily discharge, in full. Every card has
these four parts, in this order.

```yaml
id: QA                        # the symbol, and the file name
version: "1.0"                # major if the OUTPUTS change
authors: ["Louis Héraut (INRAE, UR RiverLy)"]
date: "2026-04-30"

meta:
  en:                         # what a person reads, in English
    variable: QA
    unit: "m^{3}.s^{-1}"
    name: Annual mean daily discharge
    description: ""           # empty when the name already says it all
    method:                   # one sentence per column produced
      P1:
        QA: annual aggregation [09-01, 08-31] - mean
    sampling_period: ["09-01", "08-31"]
    classification:           # the facets, validated against the vocabulary
      domain: flow
      phenomenon: mean flows
      aspect: magnitude
      statistic: mean
      season: annual
      output: series

  fr:                         # the same, in French, field for field
    ...

  global:                     # neither English nor French
    input_vars: Q             # the columns `data` must carry
    preferred_sampling_period: "09-01"
    is_date: false
    relative: true

process:                      # the calculation, step by step
  P1:
    func:
      QA: [nanmean, "Q"]      # [function, *columns, kwargs?]
    time_step: year
    sampling_period: "09-01"
    max_na_pct: 3             # a year with more than 3 % gaps is dropped
    max_na_years: 10          # a series missing 10 years is dropped
```

Three things are worth knowing before you change any of it.

**`meta` is written twice, once per language, field for field.** A card
that says something in English and something else in French is a card
that will be read two different ways. The linter compares the two.

**`method` is written for people, one sentence per column produced.** It
is what the [drawn card](catalogue.md) prints, and the linter confronts
it with what `process` actually does: change the calculation without
changing the sentence and it will say so.

**Four fields are always written, even for their default value**:
`time_step`, `is_date`, `relative`, and `max_na_pct` wherever daily
values are being binned. The rule is simple: a default that means
"nothing special" is omitted, a default that is a **choice** is written,
because otherwise its absence reads as an oversight. A card is data, and
it should carry what it claims without anyone having to know a default
buried in the code.

## Check it, then run it

```bash
python -m card.schema ./my_cards
```

The linter is strict on purpose, and it is the fastest teacher available:
it checks that the folder matches the classification, that every input
exists in the registry, that the `method` sentences match what `process`
does, that adaptive windows follow the convention of their phenomenon,
and that both languages agree.

```python
res = card.extract(data, cards=["QA20"], path="./my_cards")
```

`path` is all it takes: your folder replaces the shipped collection, and
everything else behaves identically, metadata and provenance included.

## Contributing it back

If the variable is of general interest, it belongs in the collection
rather than in your folder. Open a pull request on
[the repository](https://github.com/lou-heraut/card) with the card and
its entry in the changelog.

Two documents rule what gets accepted, both readable without building
anything:
[NOMENCLATURE.md](https://github.com/lou-heraut/card/blob/main/docs/dev/NOMENCLATURE.md)
for how a symbol is built and how a card is written, and
[TOPICS.md](https://github.com/lou-heraut/card/blob/main/docs/dev/TOPICS.md)
for the classification. Input units are defined once and for all in
`src/card/inputs.yaml`.
