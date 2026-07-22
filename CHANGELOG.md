# Journal des modifications

Évolutions notables de `card` : les fiches du recueil comme la
bibliothèque. Format inspiré de [Keep a
Changelog](https://keepachangelog.com/fr/1.1.0/).

**Numérotation.** SemVer avec la convention du 0.x : tant que le premier
chiffre vaut 0, un changement incompatible incrémente le **deuxième**
(0.1 vers 0.2), le reste incrémente le troisième. Chaque version est
étiquetée dans git (`vX.Y.Z`) : un numéro qui ne correspond à aucun tag
ne désigne rien d'installable, donc rien d'épinglable. Les sections
antérieures à 0.2.0 restent datées, elles n'ont jamais porté de numéro.

Ne pas confondre avec la version d'une **fiche** (champ `version:` de son
YAML) : la fiche versionne une définition, le paquet versionne le code et
le corpus. Une fiche passe au majeur quand ses **sorties** changent, au
mineur pour sa méthode ou sa description, au patch pour le reste ; sa
version voyage dans les métadonnées de sortie, si bien qu'un résultat dit
avec quelle définition il a été calculé.

Le paquet n'est pas encore publié sur PyPI (installation depuis GitHub,
nom en attente d'une demande PEP 541). Le moteur `stase` tient son propre
journal.

Chaque entrée dit ce qui a changé et renvoie au document qui l'explique.
Rien n'est recopié ici : une information recopiée finit par mentir à un
des deux endroits.

## 0.2.0 (2026-07-22)

### Ajouté

- La **version d'une fiche** atteint enfin les métadonnées de sortie,
  comme une colonne `version`. Un résultat dit désormais avec quelle
  définition il a été calculé, ce qui est la condition pour qu'un export
  soit reproductible et citable. Le champ existait dans les 237 fiches et
  la règle d'incrémentation était tenue depuis des semaines, mais
  `load_card` ne lisait pas le champ : il n'atteignait ni les
  métadonnées, ni le service web, ni personne.
- Le linter contrôle ce champ, ce qu'il ne faisait pas du tout : présence,
  format `majeur.mineur[.patch]`, et chaîne citée. Sans guillemets, YAML
  lit `1.10` comme le nombre `1.1`, et deux versions distinctes se
  confondent silencieusement.

### Modifié

- Dépendance montée à `stase>=0.5.0`, la version qui apporte le rôle
  `param_cols` dont les fiches `_H` dépendent depuis le 2026-07-21. La
  contrainte précédente était satisfaite par une version qui n'avait pas
  la fonctionnalité.
- Documentation de développement restructurée : un rôle par fichier, un
  bandeau de statut en tête, les documents d'époque rangés dans
  `docs/dev/archive/` au lieu d'être supprimés. Ce qui est daté vit ici,
  ce qui fait autorité vit dans une normative, ce qui est mort vit dans
  l'archive.
- `docs/dev/VALIDATION_R.md` renommé `docs/dev/ORIGINE_R.md` : rôle
  identique au fichier de ce nom dans stase (origine R, validation
  croisée, divergences assumées).

### Corrigé

- Affirmations démenties par le code : les clés `dataEX`/`metaEX` étaient
  présentées comme des alias vivants alors qu'elles sont purgées depuis
  le 2026-07-16, et le caractère relatif comme passant par le paramètre
  `meta=` de stase, retiré en stase 0.4.0.
- Décompte des fiches recopié dans trois documents et faux dans les
  trois. `scripts/generate_catalog.py` resynchronise désormais celui de
  `docs/index.md`, la dérive ne peut plus revenir.
- `n-VCN10-5_H` portait la version « 1.1.0 » quand les 236 autres fiches
  écrivent « 1.1 ». Sans contrôle du format, personne ne pouvait le voir.

## 2026-07-21

### Ajouté

- Les 59 fiches `_H` reçoivent leurs bornes d'horizon comme colonnes
  d'entrée fournies par l'appelant, au lieu d'un `$H` écrit en dur dans
  la fiche. `delta` prend quatre bornes (`ref_start`, `ref_end`,
  `horizon_start`, `horizon_end`) ; `return_level` et `apply_threshold`
  gagnent `period_start` et `period_end`. Sorties inchangées, vérifié à
  l'exact sur les 59 fiches. Débloque les horizons par degré de
  réchauffement, dont les bornes varient d'une série à l'autre.
- Goldens Python pour les 12 fiches qui divergent volontairement de R.
  Elles sortent de la comparaison à R, qui ne pouvait que produire un
  écart permanent, et sont jugées contre leur propre sortie de référence.
  Le corpus distingue maintenant une divergence attendue d'une
  régression.

### Corrigé

- Cause des 4 divergences VCN restées longtemps non rattachées :
  convention de moyenne mobile à **fenêtre paire**. `rollmean_center`
  suit pandas (`center=True`), R (RcppRoll) centre une position à côté.
  Le décalage d'un jour ne change pas le minimum annuel mais bascule
  celui d'une fenêtre saisonnière quand il tombe au bord.

Détail : `docs/dev/RENAMING.md` (2026-07-21), `docs/dev/ORIGINE_R.md`,
`tests/data/known_divergences.yaml`.

## 2026-07-20

### Ajouté

- Suffixes de scénario : `card.extract(..., suffix=["DOE", "DCR"])`
  applique une même fiche à plusieurs variantes d'une entrée en un seul
  appel, sur des colonnes `Q_lim_DOE`/`Q_lim_DCR`, ou `obs`/`sim` sur
  n'importe quelle fiche. Le fan-out des valeurs est fait par stase au
  niveau colonne ; card n'ajoute que les métadonnées, si bien qu'aucun
  placeholder ne peut changer un calcul. Une variable suffixée est une
  autre variable, donc une autre ligne de `meta`, plus une colonne
  `suffix`.
- `card.trend` suit les suffixes tout seul, en lisant cette colonne.
- Fiches `rp-` (période de retour d'un seuil réglementaire), qui sont le
  cas d'usage d'origine du mécanisme.

### Modifié

- La dépendance à stase, jusque-là sans contrainte, est épinglée à
  `>= 0.4.0` : c'est la version qui rend le moteur agnostique de card
  (retrait de son paramètre `meta=`) et lève l'ambiguïté d'unité de ses
  colonnes de tendance.
- Empaquetage : `inputs.yaml` et `topics.yaml` embarqués dans la
  distribution, ils manquaient à l'installation.

Détail : docstring de `src/card/suffix.py`, `docs/dev/RENAMING.md`
(deux entrées du 2026-07-20).

## 2026-07-18

### Ajouté

- 8 fiches comblant les trous relevés à l'inventaire familles x
  déclinaisons (lot climatologique saisonnier et mensuel, cases isolées
  `median-`).

### Corrigé

- Sommes de l'évapotranspiration rendues strictes : une année entièrement
  lacunaire est une lacune, pas un cumul nul.
- Sorties `mean-RSA_*` et orientation de plusieurs palettes.
- `return_period` : le paramètre était un seuil et non une période de
  retour, avec une correction sur `p0`. Fiches `rp-` renommées en
  conséquence.

Détail : `docs/dev/RENAMING.md` (2026-07-18).

## 2026-07-17

### Ajouté

- Le linter refuse les noms d'agrégation ambigus face aux valeurs
  manquantes : `sum` ou `mean` nus, qui ne disent pas ce qu'ils font
  d'une lacune, alors que le corpus dépend de cette réponse.

## 2026-07-16

### Ajouté

- Classification à facettes dans chaque fiche : bloc `classification`
  bilingue (`domain`, `phenomenon`, `aspect` aligné sur la typologie IHA,
  `season`, `output`, `purpose`), adossé au vocabulaire de contrôle
  `topics.yaml`, avec appariement français/anglais vérifié par le linter.
  L'arborescence `cards/<domain>/<output>/` doit refléter la
  classification, le linter l'impose. `list_cards` filtre par facette
  dans les deux langues.
- `inputs.yaml` : unités et définitions des variables d'entrée,
  invariants centralisés hors des fiches.
- `card.trend` : analyse de tendance consciente des fiches. Refuse
  explicitement les fiches qui ne sont pas `output: series`, traduit
  leurs métadonnées en `relative={variable: bool}` pour le moteur, et
  prend AR1 par défaut, les étiages étant autocorrélés.
- `card.extract(sampling_period="preferred"|"MM-DD")` : impose une
  fenêtre annuelle commune, pour comparer des stations entre elles. Les
  fenêtres partielles font partie de la définition d'une variable et ne
  sont jamais écrasées. La convention adaptative par phénomène (étiages
  `nanmax` et 01-01, crues `nanmin` et 09-01) devient un invariant
  vérifié par le linter.

### Retiré

- Les clés héritées `dataEX` et `metaEX` : `card.extract` renvoie
  `{"data", "meta"}`, et rien d'autre. La sortie d'une extraction est de
  la donnée comme une autre.
- Le champ `topic`, remplacé par la classification à facettes.

Détail : `docs/dev/TOPICS.md`.

## 2026-07-15

### Modifié

- Audit des métadonnées appliqué en quatre lots : `name`, `description`,
  `method` et `unit` alignés sur le bloc `process` réellement exécuté.
  Règle érigée à cette occasion : la fonction fait foi, une métadonnée ne
  ment jamais sur ce que calcule la fiche.
- Renommages de sorties, parité R rompue volontairement et fiches
  concernées passées en v2.0 : `STD` en `STD_ratio` (c'est le alpha du
  KGE, pas un écart-type), `Rc` en `QR_ratio` (le coefficient n'était pas
  adimensionnel), `median-finLF` en `median-endLF`.
- 48 champs `method` vides remplis, fiche `QJC10` réparée.

### Ajouté

- Guide de nommage écrit et arbitré (`docs/dev/NOMENCLATURE.md`) : le
  système du corpus consolidé par Oberlin, la grammaire des identifiants
  et sept règles de rédaction des métadonnées.
- 11 fiches comblant des manques évidents du catalogue (déclinaisons
  saisonnières des basses eaux, critère BFI-LH).

Détail : `docs/dev/archive/AUDIT_FICHES.md`, `docs/dev/NOMENCLATURE.md`,
`docs/dev/RENAMING.md`.

## 2026-07-12

Première version du paquet, port Python du paquet R
[CARD](https://github.com/lou-heraut/CARD).

### Ajouté

- 215 fiches YAML, les fonctions hydrologiques portées de R, le chargeur
  de fiches et l'extraction, cette dernière déléguée au moteur
  [stase](https://github.com/lou-heraut/stase).
- API pythonique : `card.extract`, `card.list_cards`, `card.info`,
  `card.copy_cards`. Les noms du R restent valides en alias.
- Linter sans dépendance (`python -m card.schema`), suite pytest adossée
  à des goldens figés depuis la validation R, catalogue généré
  (`docs/CARDS.md`) et page GitHub Pages.

### Modifié

- Résolution des fonctions par espace de noms (`card.functions` puis
  numpy) : les fiches appellent directement `nanmean`, `nanargmax`, le
  registre-table de R disparaît, comme le kwarg `{skipna: true}`.
- Renommage des fonctions hydro et des clés de fiche, table validée
  fonction par fonction (`get_deltaX` en `delta`, `get_Xn` en
  `return_level`, `to_normalise` en `relative`).
- Licence GPL-3 pour tout le dépôt, en-têtes de copyright repris des
  fichiers R d'origine.

Validation croisée : 552 comparaisons identiques à R sur le corpus
complet, tolérance 1e-6.

Détail : `docs/dev/archive/ROADMAP.md`, `docs/dev/RENAMING.md`,
`docs/dev/ORIGINE_R.md`.
