# Package functions

The functions you call. Everything else in the package is machinery: it
is readable in the repository, and it is not documented here.

Their docstrings are what `help(card.extract)` prints, rendered as a
page. If the two ever disagree, the docstring is right and this page is
stale.

## Computing

::: card.extract
::: card.trend

## Discovering the collection

::: card.list_cards
::: card.info
::: card.figure
::: card.vocabulary

## Working with cards

::: card.copy_cards
::: card.load_card
::: card.provenance

!!! note "Older names still work"
    `CARD_extraction`, `CARD_list_all`, `CARD_info` and `CARD_management`
    are aliases of `extract`, `list_cards`, `info` and `copy_cards`, kept
    so that scripts written against the R package keep running.
