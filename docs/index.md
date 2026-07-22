# card <img src="img/flower_alt.png" align="right" width="140" height="140" alt=""/>

**card** : extraction de variables hydroclimatiques définies par des
fiches YAML, exécutées par le moteur [stase](https://github.com/lou-heraut/stase).

- **[Catalogue des fiches](CARDS.md)** : les 225 fiches (471 variables)
  par thème, avec leurs entrées requises.
- [Dépôt GitHub](https://github.com/lou-heraut/card) : code, fiches YAML,
  installation.

```python
import card
card.info("QA")                       # détail d'une fiche
card.list_cards(phenomenon="basses eaux")   # explorer par phénomène
```
