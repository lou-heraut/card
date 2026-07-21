# CHANTIERS — pistes ouvertes (mise à jour 2026-07-20)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

Sorti le 2026-07-21 : « Fiches delta par horizon » (dates d'horizon en
colonnes d'entrée fournies par l'appelant, 59 fiches _H collapsées avec
suffixe d'horizon, `delta` à quatre bornes, `return_level`/
`apply_threshold` avec `period_start`/`period_end`, rôle `param_cols`
dans stase, `inputs.yaml type: date`, `$H` retiré). Nouveau == ancien
vérifié à l'exact sur les 59 fiches. Trace : RENAMING.md 2026-07-21.
Reste ouvert : §10 (goldens injouables des fiches divergentes de R).

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

Le SKOS n'est pas un service : c'est un artefact de publication de la
classification, dont la source de vérité est ici (`src/card/topics.yaml`
et les blocs classification des fiches). Conception rapatriée le
2026-07-20 depuis l'ancien docs/dev/API.md, parti dans card-api.

- `scripts/generate_skos.py` (à écrire) : chaque facette devient un
  `skos:ConceptScheme` (domain, phenomenon, aspect, season, output,
  purpose) ; chaque valeur un `skos:Concept` avec `prefLabel` fr/en
  (les paires sont déjà dans topics.yaml) et `exactMatch`/`closeMatch`
  vers l'existant (aspect ↔ typologie IHA, fiches climat ↔ ETCCDI) ;
  chaque fiche devient un concept rattaché à ses facettes
  (`dcterms:subject`).
- Publication statique : `docs/card.ttl` servi par GitHub Pages, aucun
  serveur nécessaire pour être moissonnable.
- URIs stables : demander un préfixe **w3id.org** (ex.
  `https://w3id.org/card-hydro/...`) qui redirige vers les Pages,
  gratuit, pérenne, indépendant de l'hébergement. Arbitrage du
  2026-07-16 : à confirmer le moment venu, non bloquant.
- Skosmos sur la VM : optionnel et purement cosmétique (navigation
  humaine), il lit le même `card.ttl`.
- Côté service, card-api pourrait exposer un `GET /v1/concepts` qui
  renvoie vers ces URIs. C'est un renvoi, pas une source : la vérité
  reste ici.

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

## 10. Goldens injouables des fiches volontairement divergentes de R

Question soulevée le 2026-07-21 par l'utilisateur pendant le chantier horizons (sorti le 2026-07-21),
à traiter APRÈS lui. À quoi servent des tests qui ne peuvent jamais
passer (diff permanent) parce que la sortie Python a volontairement
divergé de R ? Faut-il les garder, à quelle condition pour être non
ambigu, ou les jeter ?

### Constat mesuré (ancien code, corpus contre R, 59 fiches `_H`)

48 fiches passent (ok, == R), 12 divergent (diff permanent) :
- 8 divergences DOCUMENTÉES (bascule `relative` B1/B3, RENAMING.md,
  parité R rompue volontairement pour aligner la valeur sur l'unité
  « % ») : delta-QNA_H/_summer/_winter, delta-allLF_H/_summer/_winter,
  delta-dtBF_H, delta-dtFlood_H. Cause racine côté R : la fiche R
  déclare unit « % » mais `to_normalise = FALSE`, donc R sort de
  l'absolu mal étiqueté ; Python a corrigé (relatif).
- 4 divergences NON documentées, à comprendre AVANT toute décision :
  delta-VCN10_summer_H, delta-VCN30_summer_H, delta-VCN3_winter_H,
  delta-tVCN10_summer_H.

### Le vrai problème (analyse)

Le corpus mélange deux rôles dans une seule comparaison :
1. **parité R** : Python reproduit-il R ? (pertinent pour les 48 qui
   VEULENT la parité) ;
2. **non-régression** : Python produit-il encore ce qu'il produisait
   hier ? (pertinent pour TOUTES, y compris les divergentes).

Pour une fiche qui diverge de R par décision, le rôle 1 est mort (diff
par design), mais le rôle 2 reste précieux. Or le corpus ne fait que le
rôle 1 (comparer à R), d'où le « diff » permanent, sans distinguer
« diff attendu » d'une « nouvelle régression ». Et le CLAUDE.md impose
déjà « goldens re-figés » sur changement de sorties : ça n'a pas été
appliqué à ces 12 fiches, d'où le trou.

### Pistes de résolution

- **A (recommandée)** : figer un golden « Python attendu » pour les
  fiches divergentes (applique la règle existante). La fiche est jugée
  contre CE golden (== exact), plus contre R. Chaque test redevient
  jouable ; R reste la référence de parité là où la parité est voulue.
  Coût : générer + maintenir ces goldens Python.
- **B** : un manifeste des divergences attendues (max_diff ou valeurs
  par fiche) ; le test passe si le diff est INCHANGÉ (pas si diff==0).
  Plus léger, moins précis.
- **C** : signaler en amont le bug des fiches R (unit vs to_normalise)
  et régénérer les goldens une fois R corrigé, dans le sillage de la
  tâche « signalement amont des 11 fiches R cassées ». Lent, externe, R
  est en maintenance/référence seule.
- **D (préalable)** : comprendre les 4 divergences VCN non documentées
  (bug Python ? bug R ? ok_approx basculé ?) avant de choisir leur
  golden.

Recommandation : D d'abord, puis A. B en repli si A trop coûteux.
