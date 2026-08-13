# Ecosystem

Four repositories, one collection of cards. A card is written once and
computed identically wherever you call it from.

```
        the cards            the engine
        ┌────────┐          ┌────────┐
        │  card  │─────────▶│ stase  │
        └────────┘          └────────┘
          ▲    ▲
   ┌──────┘    └───────┐
┌────────┐        ┌──────────┐
│ card4r │        │ card-api │
└────────┘        └──────────┘
   in R            over the web
```

## Which door to take

| you want | take | what it costs |
|---|---|---|
| your own data, in Python | [card](https://github.com/lou-heraut/card) | `pip install`, nothing else |
| your own data, in R | [card4r](https://github.com/lou-heraut/card4r) | one `install_github`, Python provisioned for you |
| Hub'Eau discharge, no install | [card-api](https://card-api.riverly.inrae.fr) | a URL, no account, no key |
| a large volume, repeatedly | card, locally | no quota, no network |

`card4r` is a **thin front end**: it calls card, it does not reimplement
it. Both give the same numbers, because both run the same cards through
the same engine.

## The engine

[stase](https://github.com/lou-heraut/stase) does the aggregation:
sampling windows, missing-data thresholds, seasonal and monthly fan-out,
trend testing. It knows nothing about cards. card translates a card into
what stase expects, which is why a card can change without touching the
engine, and the engine can improve without touching 226 cards.

## Every result says how it was made

A result carries its own provenance, and none of it is typed by hand:

- the **card version** of each variable, and the `swhid` of the card file
  itself, so a definition can be retrieved exactly as it was;
- the **commit** of card and of stase, with their Software Heritage
  identifiers, all three repositories being archived there.

```python
res = card.extract(data, cards=["VCN10"])
res["meta"][["variable_en", "version", "swhid", "card_commit"]]
```

Three levels of traceability, therefore: the definition, the collection,
and the engine.

## Citing

Each repository carries a `CITATION.cff`, which GitHub turns into a ready
citation, and a `codemeta.json`. Version numbers exist for citation; day
to day, the commit is what identifies a state.

!!! note "Where the reasoning lives"
    Design notes, open leads and the record of every renaming stay in the
    repositories, under `docs/dev/`. They are working documents, not a
    showcase, and they are readable on GitHub without building anything.
