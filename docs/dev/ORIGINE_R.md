> **Statut : norme en vigueur.** Origine R du corpus de fiches, principes
> de la conversion, validation croisée et divergences assumées. Le
> fichier de même nom dans stase traite du moteur. Journal daté des
> livraisons : `CHANGELOG.md` à la racine du dépôt.

# Origine : conversion depuis le package R CARD

card est le port Python du package R
[CARD](https://github.com/lou-heraut/CARD) (INRAE, UR RiverLy). Les
fiches YAML de `src/card/cards/` sont la source de vérité ; les fiches R
de l'ancien package servent de référence de validation croisée. La
correspondance des noms R vers Python est dans
[RENAMING.md](RENAMING.md), le déroulé de la refonte dans
[archive/ROADMAP.md](archive/ROADMAP.md).

## Principes de la conversion (actés le 2026-07-11)

- **Python natif d'abord** : une fonction R custom est remplacée par son
  équivalent numpy, scipy ou pandas dès que le résultat est identique ou
  très proche. Pas de wrapper cosmétique, la fiche référence le vrai nom
  Python (`nanmean`, `nanargmax`), et la résolution se fait par espace de
  noms (`card.functions` puis numpy).
- **Corrections bienvenues** : franglais, documentation, noms de
  paramètres flous. Python a vocation à remplacer R, la refonte est
  l'occasion d'assainir plutôt que de recopier.
- **Frontière card / stase** : card porte les métadonnées, les fiches et
  les fonctions hydrologiques ; stase porte toute la gestion de données
  et d'agrégation, y compris l'échantillonnage adaptatif et les sorties
  vectorielles. Un mécanisme de moteur qui remonte dans card est un
  signe que la frontière a été franchie au mauvais endroit.
- **Anciennes fiches R** : pas de réparation. Elles servent à la
  vérification croisée, ce n'est pas une fin en soi (11 d'entre elles
  plantent dans le paquet R lui-même, voir plus bas).

## Validation croisée R / Python (2026-07-11)

Corpus complet (215 fiches) exécuté via card/stase et comparé au package
R CARD sur données synthétiques (2 stations sur 131 ans) :

- **552 comparaisons identiques** (tolérance 1e-6) en mode parité
  rolling (`CARD_ROLL_COMPAT=rcpp`) ;
- 33 divergences résiduelles : comptage des lacunes autour des moyennes
  mobiles (R rend les NA invisibles au NApct après un rolling, RcppRoll
  convertit NA en NaN ; Python compte honnêtement, il est plus strict) ;
- 11 fiches plantent dans le package R lui-même (CR, CRS_season, FDC x5,
  QJC10, RA_ratio, RAl/RAs_ratio) : pas de référence croisée possible.
  **Cause diagnostiquée le 2026-07-22** (R 4.x, dplyr 1.2.1), deux
  familles :
  - *retour vectoriel* (FDC x5, QJC10, RAl_ratio, RAs_ratio) : la
    fonction rend plus d'une valeur par groupe, et `dplyr::summarise`
    exige une taille 1 depuis dplyr 1.1, en renvoyant vers `reframe()`.
    Ces fiches ONT fonctionné : `summarise` acceptait un retour
    multi-lignes avant cette version. Elles ne sont pas mal écrites, le
    moteur R a vieilli sous elles ;
  - *`get()` sur un premier argument incorrect* (CR, CRS_season,
    RA_ratio), dans la résolution des arguments du moteur R.

  Côté Python, seules les FDC plantaient, pour une raison sans rapport
  (colonne imposée par le moteur à une fonction qui n'en déclare aucune),
  corrigée le 2026-07-22. Les autres tournent.

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
- **Régime médian renommé `median-QJ`/`median-QJC5` → `QJD`/`QJDC10`** :
  le préfixe `median-` est réservé aux réductions `f(série) → scalaire`,
  la médiane d'un régime devient la statistique d'ordre `D` en position 3
  (NOMENCLATURE §4, §6). `QJD` (régime médian brut) apparie
  `QJD`↔`median-QJ` par le calcul, valeurs identiques. La fiche lissée a
  divergé plus loin : renommée `QJDC10`, sa **fenêtre de lissage passe de
  5 à 10 jours** (harmonisée sur `QJC10`, son pendant moyen), donc elle
  n'a plus de golden R comparable (R lisse sur 5). De plus la fiche R
  `median-QJC5` utilise `keep = "all"` et son golden porte deux colonnes
  (brut + lissé) ; la fiche Python n'en sort qu'une. Trois divergences
  assumées, donc : nom, fenêtre, colonne unique.

## Noms hérités du R

L'API canonique est `card.extract`, `card.list_cards`, `card.info`,
`card.copy_cards` ; les noms du R restent valides en alias. Table
complète, paramètres compris : [RENAMING.md](RENAMING.md).
