# CHANTIERS — pistes ouvertes (mise à jour 2026-07-20)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

Sorti le 2026-07-20 : « Multi-seuils réglementaires et métadonnées
évolutives » (suffix= dans card.extract et card.trend, vocabulaire de
suffixes, placeholders, colonne suffix de meta, règle de lint, fiches
rp-* ; retrait de meta= de stase). Trace : RENAMING.md 2026-07-20 et
stase docs/dev/ORIGINE_R.md.

Sorti le 2026-07-18 : « card-api : suivi des jobs, identité et RGPD »
(jetons hachés affichés une fois, préfixe pseudonyme dans le journal
et sur les jobs, GET /v1/jobs par clé, tickets 64 bits, mention RGPD
dans le template d'issue ; clés conservées tant qu'actives, effacées
à la révocation).

## 2. Références bibliographiques externes dans les fiches

Ancrer les fiches standardisées sur leurs références : identifiants
climdex/ETCCDI (RCXA1 ↔ RX1day, RCXA5 ↔ RX5day, dtCDDA ↔ CDD,
dtCWDA ↔ CWD...), libellés SANDRE/eaufrance (QMNA, VCNd, module).
**À retravailler avec le système de biblio scientifique existant de
l'utilisateur** (ne pas inventer un format de citation avant d'avoir
vu le sien).

## 3. Lint temps réel sous Emacs

Objectif : valider les YAML pendant l'édition. Deux voies :
- générer un **JSON Schema** des fiches (depuis schema.py) et brancher
  `yaml-language-server` (paquet Emacs `lsp-mode` ou `eglot`) — la voie
  standard, autocomplétion incluse ;
- ou un checker flycheck maison qui appelle
  `python -m card.schema <fichier>` (déjà supporté en CLI, plus simple
  mais sans autocomplétion).

## 4. Revue de code du package (lisibilité, dé-boîte-noire)

Crainte utilisateur : code trop compliqué/alambiqué par endroits.
À son initiative, mais aides possibles : un `docs/dev/ARCHITECTURE.md`
qui explique le pipeline en langage simple (loader → stase →
compactage), et une passe de simplification ciblée (/simplify) sur
extraction.py qui concentre la complexité (kwargs-colonnes, sparse,
fan-out).

## 5. Documentation utilisateur étendue

- README : section « développer sa fiche » faite (copy_cards →
  extract(path=...) → python -m card.schema) ; à étoffer d'un exemple
  complet de fiche commentée ligne à ligne ?
- Pages : tutoriel pas-à-pas avec données réelles (lié au chantier 1 ?).

## 6. Export SKOS / thésaurus (différé de longue date)

La classification (docs/dev/TOPICS.md) fournit désormais les concepts
et les paires en/fr — chaque facette devient un concept scheme.
Réévaluer quand le besoin Skosmos se concrétise.

## 7. Fiches futures

- **Rc** (vrai coefficient de ruissellement adimensionnel) :
  86,4 × ΣQ/ΣR / S, avec la surface S en colonne constante d'entrée
  (déjà au registre inputs.yaml) ;
- **durées cumulées de dépassement** (jours/an, famille DC d'Oberlin,
  préfixe dt) si le besoin se confirme ;
- fiches personnelles de l'utilisateur (en local via copy_cards puis
  contribution).

### Complétion de symétrie restante (inventaire 2026-07-18)

Trous relevés lors de l'inventaire familles x déclinaisons, non créés
pour l'instant (décision : se limiter au lot climatologique
mean-QSA_season, mean-TMA_month, mean-RMA_month, ETPSA_season,
ETPMA_month et aux cases isolées median-centerLF, median-tVCX3,
median-tVCX10, faits le 2026-07-18). À reprendre si le besoin se
confirme :

- **delta saisonniers des caractéristiques d'étiage** (10 fiches) :
  delta-{dtLF, vLF, centerLF, startLF, endLF}\_{summer, winter}\_H,
  modèle direct delta-allLF_summer_H / delta-allLF_winter_H (les
  séries saisonnières correspondantes existent déjà) ;
- **compagnons de niveaux de retour** (4 fiches) : delta-VCN30-2_H et
  delta-QMNA-5_H (modèle delta-VCN10-5_H), n-VCN30-2_H et n-QMNA-5_H
  (modèle n-VCN10-5_H) ;
- **maxima saisonniers de précipitations** : RCXSA1_season,
  RCXSA5_season (modèle RSA_season + RCXA1/RCXA5) ;
- **coefficient d'écoulement mensuel** : CRM_month (modèle CRS_season) ;
- **miroirs basses eaux des fréquences fQ** : fQ90A, fQ95A, fQ99A
  (temps passé sous le quantile) + deltas ; opérateur inversé par
  rapport à fQ01A, pas une pure déclinaison ;
- absences uniformes assumées, à rediscuter seulement si un usage les
  demande : aucun median- saisonnier, aucune variante saisonnière côté
  hautes eaux (VCX*_summer...), ratios annuels uniquement, famille
  alpha- limitée au trio MAKAHO (QA, QJXA, VCN10).

## 8. Palettes : questions ouvertes (2026-07-18)

État : les fiches à grandeur non ambiguë sont toutes équipées (héritage
de la fiche mère ; voir RENAMING.md 2026-07-18 pour l'orientation ETP).
Quatre palettes sémantiques en usage : marron→vert (quantités d'eau),
bleu→rouge (température), violet→orange (dates et durées de crue),
vert→marron (durées/volumes d'étiage, ETP : assèchement).

- **Scores de performance et indices sans unité** (KGE, NSE et
  variantes, Bias, STD_ratio, epsilon_R/T, RAT_*, QR_ratio, RA_ratio,
  BFI-LH/Wal et leurs deltas, BFM, a-FDC) : laissés sans palette
  volontairement. Si on les équipe un jour, il faudra une palette
  divergente centrée sur la valeur de référence (1 pour KGE/NSE, 0 pour
  les deltas de BFI), décision non prise.
- **dtFlood** : partage la palette violet→orange avec les dates, et non
  la palette d'assèchement de dtLF/dtBF. Examiné le 2026-07-18 et
  conservé : une durée de crue représente un risque (dégâts), pas un
  assèchement, et une crue plus longue n'est pas « plus d'eau » ; la
  dynamique diffère de celle des étiages. Si on veut un jour distinguer
  le risque de crue des dates par une palette dédiée, c'est une
  décision à part.

## 9. Fiches delta par horizon : paramètres de fonction en colonnes

Le gros chantier suivant. Il rend enfin utile la couche de métadonnées
évolutives livrée le 2026-07-20 (suffixes et placeholders, cf. la
section « Suffixes de scénario » de RENAMING.md et le docstring de
`src/card/suffix.py`), et il débloque les horizons par degré de
réchauffement.

### Le problème

Les 55 fiches `delta-*_H` énumèrent leurs horizons À LA MAIN. Le P2 de
`delta-QNA_summer_H` contient trois entrées `func` qui ne diffèrent que
par des dates littérales, substituées au chargement par `$Hx` :

```yaml
P2:
  func:
    delta-QNA_summer_H1: [delta, "QNA_summer", "date", {past: $H0, future: $H1, ...}]
    delta-QNA_summer_H2: [delta, "QNA_summer", "date", {past: $H0, future: $H2, ...}]
    delta-QNA_summer_H3: [delta, "QNA_summer", "date", {past: $H0, future: $H3, ...}]
```

Trois conséquences : trois `name` écrits à la main dans chaque langue,
un `{horizon}` jamais substitué qui traîne dans 110 blocs `method`, et
surtout des dates d'horizon IDENTIQUES pour toutes les séries.

### La cible

Passer les dates en colonnes des données. Les fiches `delta` deviennent
structurellement identiques aux fiches de seuil `rp-*` : une colonne
constante par série, éclatée par le suffixe stase. Le P2 tombe à UNE
entrée `func`, les noms de sortie restent `delta-QNA_summer_H1` (base
plus suffixe, à l'identique), les trois phrases deviennent une seule
phrase à placeholder, et les **horizons par degré de réchauffement**
deviennent exprimables : chaque chaîne de modèles atteint +2 °C à une
date différente, ce qui est le cas Explore2, pas un cas d'école.

### Deux blocages, vérifiés dans le code le 2026-07-20

- `delta(X, dates, past, future, relative, ...)` prend des PAIRES
  (`functions/seasonal.py:33`, usage `past[0]`, `past[1]`). Une colonne
  donne une valeur par ligne, pas une paire. Il faut donc deux colonnes
  par période et une signature à quatre scalaires : changement de
  signature, donc trace RENAMING.md et 59 fiches à reprendre.
- stase ne résout en référence que les kwargs dont la valeur est une
  chaîne UNIQUE (`extraction.py:936`, `isinstance(v, str)`). Un
  `{past: ["H0_start", "H0_end"]}` repartirait en littéral. Soit quatre
  kwargs scalaires, soit apprendre à stase à résoudre une liste de
  références (code moteur, profite à tout le monde, élargit la
  grammaire des kwargs).

C'est l'arbitrage d'entrée du chantier, et il revient à l'utilisateur.

### Ce qui est déjà ouvert, vérifié

- Une sortie de process devient une colonne disponible au process
  suivant, et un kwarg nommant une colonne est résolu dynamiquement.
  Des dates CALCULÉES par un process amont et consommées en aval sont
  donc possibles sans code nouveau côté stase.
- La couche métadonnées ne bouge pas : `suffixes`, `suffix_default`,
  les placeholders `{suffix.<champ>}` et la colonne `suffix` de `meta`
  fonctionnent à l'identique que les horizons restent des littéraux ou
  deviennent des colonnes. `horizon_labels` (champ mort dans 55 fiches)
  devient `suffixes`, et `{horizon}` devient `{suffix.name}`.
- `card.trend` suit déjà les suffixes tout seul.

### Coût annexe

Quatre colonnes de dates constantes répétées sur chaque ligne
journalière. Le précédent existe : `Q_lim` est déjà exactement ça.
Perte apparente de l'autodocumentation des horizons de référence dans
la fiche, qui se rattrape : la fiche garde son `meta.global.horizons`
et `card.extract` matérialise ces dates en colonnes constantes quand
l'appelant n'en fournit pas. Défaut inchangé, override par série
possible.

### Migration des métadonnées

Indépendante du reste et faisable seule : remplacer dans les 55 fiches
les trois `name` par une phrase à `{suffix.name}`, `horizon_labels` par
`suffixes`, et `{horizon}` par `{suffix.name}` dans les `method`.
Aucune valeur numérique modifiée, donc bump de version mineur. À faire
en batch séparé du changement de mécanisme.
