# card

**CARD** — extraction de variables hydroclimatiques définies par des
fiches YAML, exécutées par le moteur [stase](https://github.com/<owner>/stase).

- **[Catalogue des fiches](CARDS.md)** — les 215 fiches (588 variables)
  par thème, avec leurs entrées requises.
- [Dépôt GitHub](https://github.com/<owner>/card) — code, fiches YAML,
  installation.

```python
from card import CARD_extraction, CARD_info, CARD_list_all
CARD_info("QA")                    # détail d'une fiche
CARD_list_all(topic="Low Flows")   # explorer par thème
```
