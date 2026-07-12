# Origine : conversion depuis le package R CARD

card est le port Python du package R
[CARD](https://github.com/lou-heraut/CARD) (INRAE, UR RiverLy). Les
fiches YAML de `src/card/cards/` sont la source de vérité ; les fiches R
de l'ancien package servent de référence de validation croisée.
L'historique de la refonte et les décisions associées sont dans
[ROADMAP.md](ROADMAP.md), la correspondance des noms de fonctions R vers
Python dans [RENAMING.md](RENAMING.md).

## Validation croisée R / Python (2026-07-11)

Corpus complet (215 fiches) exécuté via card/stase et comparé au package
R CARD sur données synthétiques (2 stations sur 131 ans) :

- **552 comparaisons identiques** (tolérance 1e-6) en mode parité
  rolling (`CARD_ROLL_COMPAT=rcpp`) ;
- 33 divergences résiduelles : comptage des lacunes autour des moyennes
  mobiles (R rend les NA invisibles au NApct après un rolling, RcppRoll
  convertit NA en NaN ; Python compte honnêtement, il est plus strict) ;
- 11 fiches plantent dans le package R lui-même (CR, CRS_season, FDC x5,
  QJC10, RA_ratio, RAl/RAs_ratio) : versions Python fonctionnelles,
  pas de référence possible.

```bash
cd tests
python3 make_test_data.py
Rscript run_R_corpus.R          # ~10 min, nécessite le package R CARD
python3 run_py_corpus.py        # rapport dans data/corpus_report.csv
CARD_ROLL_COMPAT=rcpp python3 run_py_corpus.py   # mode parité RcppRoll
```

Les références R (`tests/data/`, ~37 Mo) ne sont pas versionnées :
elles se régénèrent avec les commandes ci-dessus. La suite pytest est
autonome et n'en a pas besoin.

## Divergences assumées avec le R

- **Rolling centré** : convention pandas (`center=True`) ; pour k pair
  la série est décalée de +1 position par rapport à RcppRoll (dates
  dérivées d'un jour). Choix délibéré : l'outil Python standard prime
  sur la réplication d'un détail d'implémentation R. Bascule de
  vérification : `CARD_ROLL_COMPAT=rcpp`.
- **Comptage des lacunes** : Python compte les NaN induits par les
  moyennes mobiles (R ne les voit pas), il est légèrement plus strict
  près du seuil NApct.
- **Index 0-based** (`which.*NA`, apply_threshold first/last) : la
  chaîne complète avec la conversion is_date de stase redonne
  exactement les valeurs R.

## Noms hérités du R

L'API canonique est `card.extract`, `card.list_cards`, `card.info`,
`card.copy_cards`. Les noms du R restent valides en alias :
`CARD_extraction` (avec son paramètre `CARD_name`), `CARD_list_all`,
`CARD_info`, `CARD_management`.
