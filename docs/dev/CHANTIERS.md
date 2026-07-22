> **Statut : registre vivant.** Ce fichier ne contient que des pistes
> **ouvertes**. Un chantier livré en sort et devient une entrée de
> `CHANGELOG.md`, à la racine du dépôt, qui renvoie au document
> expliquant le détail. Les sections portent des titres et non des
> numéros : le registre bouge, un numéro ne se cite pas durablement.

# CHANTIERS : pistes ouvertes (mise à jour 2026-07-22)

## Nom PyPI de card (PEP 541)

Le nom `card` sur PyPI est un squat manifeste : release unique 0.0.1 du
2019-08-23, résumé « card », page d'accueil github.com/pipname/card.
Plan validé le 2026-07-12, en attente d'action de l'utilisateur :

1. déposer une demande PEP 541 (transfert de nom pour squatting) sur
   github.com/pypi/support, depuis le compte PyPI de l'utilisateur ;
2. ne rien publier sur PyPI en attendant (installation depuis GitHub),
   pour pouvoir publier directement sous `card` si la demande aboutit ;
3. `card-stase` reste le nom de repli dans `pyproject.toml`, l'import
   étant `card` dans tous les cas.

## Signalement amont des fiches R cassées

11 fiches plantent dans le paquet R lui-même. Le signalement est
désormais actionnable, la cause ayant été diagnostiquée le 2026-07-22
(R 4.x, dplyr 1.2.1) en deux familles :

- **retour vectoriel** (FDC, FDC_H0..H3, QJC10, RAl_ratio, RAs_ratio) :
  la fonction rend plus d'une valeur par groupe, et `dplyr::summarise`
  exige une taille 1 depuis dplyr 1.1, qui renvoie vers `reframe()`. Ces
  fiches **fonctionnaient** avec les versions antérieures de dplyr : ce
  n'est pas une erreur d'écriture, c'est le moteur R qui a vieilli sous
  elles. Correctif probable côté EXstat : basculer l'appel concerné de
  `summarise` vers `reframe` quand la fonction rend un vecteur ;
- **`get()` sur un premier argument incorrect** (CR, CRS_season,
  RA_ratio), dans la résolution des arguments du moteur R. À creuser
  séparément, cause non établie.

Le diagnostic vaut pour la version installée ici ; le vérifier sur
l'environnement de l'utilisateur avant d'ouvrir le signalement.

## Références bibliographiques externes dans les fiches

Ancrer les fiches standardisées sur leurs références : identifiants
climdex/ETCCDI (RCXA1 ↔ RX1day, RCXA5 ↔ RX5day, dtCDDA ↔ CDD,
dtCWDA ↔ CWD...), libellés SANDRE/eaufrance (QMNA, VCNd, module).
**À retravailler avec le système de biblio scientifique existant de
l'utilisateur** (ne pas inventer un format de citation avant d'avoir
vu le sien).

## Lint temps réel sous Emacs

Objectif : valider les YAML pendant l'édition. Deux voies :
- générer un **JSON Schema** des fiches (depuis schema.py) et brancher
  `yaml-language-server` (paquet Emacs `lsp-mode` ou `eglot`), la voie
  standard, autocomplétion incluse ;
- ou un checker flycheck maison qui appelle
  `python -m card.schema <fichier>` (déjà supporté en CLI, plus simple
  mais sans autocomplétion).

## Revue de code du package (lisibilité, dé-boîte-noire)

Crainte utilisateur : code trop compliqué ou alambiqué par endroits.
À son initiative, mais aides possibles : un `ARCHITECTURE.md` qui
explique le pipeline en langage simple (loader, stase, compactage), et
une passe de simplification ciblée sur `extraction.py`, qui concentre la
complexité (kwargs-colonnes, colonnes creuses, fan-out).

## Documentation utilisateur étendue

- README : section « développer sa fiche » faite (copy_cards puis
  extract(path=...) puis `python -m card.schema`) ; à étoffer d'un
  exemple complet de fiche commentée ligne à ligne ?
- Pages : tutoriel pas-à-pas avec données réelles.

## Convertir les 12 fiches à horizon figé au modèle suffixe

Ouvert le 2026-07-22, demandé par l'utilisateur. Douze fiches figent leur
période **dans le fichier**, alors que le chantier du 2026-07-21 a sorti
ces bornes des 59 autres. Une famille par type, déclinée quatre fois :

| famille | fiches | ce que fait le process |
|---|---|---|
| `QM_H0..H3` | 4 | `nanmean(Q)`, `time_step: month` |
| `FDC_H0..H3` | 4 | `fdc_probabilities` / `fdc_quantiles`, `time_step: none` |
| `median-QJ_H0..H3` | 4 | `nanmedian(Q)`, `time_step: yearday` |

**Cible** : trois fiches, `QM_H`, `FDC_H` et `median-QJ_H`, recevant
leurs bornes en colonnes d'entrée et se déclinant par suffixe, comme les
fiches delta. L'appelant choisit ses horizons, autant qu'il veut, sans
qu'aucune date ne vive dans le corpus.

**Le principe est déjà en place**, et c'est ce qui rend le chantier
simple : la période ne doit pas être portée par le champ `period` du
process, qui est un filtre global du moteur, mais par la **fonction**,
comme le font déjà `return_level` et `apply_threshold` depuis le
2026-07-21 :

```yaml
[return_level, "VCN10", {dates: "date", period_start: "ref_start",
                         period_end: "ref_end", ...}]
```

Rien à changer dans stase, donc. Il s'agit de donner le même traitement
aux fonctions employées par ces douze fiches.

### Conception : trois voies, dont une écartée par la mesure

**Écartée : masquer puis agréger.** L'idée la plus élégante était une
fonction `mask_period` rendant la série avec des NaN hors fenêtre, suivie
des agrégations habituelles inchangées, vecteur vers vecteur comme
`rollmean_center`. Elle marche, mais les NaN du masque **sont comptés
comme des lacunes** : mesuré le 2026-07-22, une agrégation mensuelle
avec `max_na_pct=3` sur une série masquée à 20 ans sur 51 rend **0 mois
sur 12** au lieu de 12. Les douze fiches actuelles n'utilisent pas ce
seuil et n'en souffriraient pas, mais toute fiche future en hériterait
en silence. Fondation trop piégeuse, on n'y revient pas.

**Retenue : restreindre DANS la fonction d'agrégation.** C'est déjà le
motif de `return_level` et `apply_threshold`, la restriction restant
invisible au comptage des lacunes. Deux formes possibles :

- une fonction générique `over_period(X, dates, func, period_start,
  period_end, **kw)` qui restreint puis délègue à `func`. Elle couvre les
  trois familles d'un coup, et surtout les deux qui appellent `nanmean`
  et `nanmedian` : ce sont des fonctions **numpy**, on ne peut pas leur
  ajouter de kwargs, il faut de toute façon passer par une fonction card.
  Vérifié le 2026-07-22 : un kwarg dont la valeur est une chaîne ne
  devient une référence de colonne que si la colonne existe, sinon il est
  passé en littéral ; `{func: nanmean}` arrive donc bien comme le nom à
  résoudre.
- ou les kwargs de période ajoutés à `fdc_quantiles` comme ils l'ont été
  à `return_level`, la générique ne servant qu'aux deux agrégations numpy.

Points à régler dans les deux cas : les kwargs de la fonction enveloppée
partagent le même dictionnaire plat que ceux de l'enveloppe (`n`,
`norm_spacing` pour `fdc_quantiles`), donc réserver et documenter les
noms de l'enveloppe ; et `fdc_probabilities` ne lit aucune donnée, il
n'a pas besoin de période, seul `fdc_quantiles` en veut une.

**Coût annexe** : douze identifiants disparaissent au profit de trois.
Changement de sorties, donc trace dans RENAMING.md, bump majeur, et le
catalogue comme le service en sont affectés. Prévoir aussi la valeur par
défaut à recommander pour la période de référence, aujourd'hui écrite
dans les fiches H0 (`1976-01-01` à `2005-08-31`, un début calendaire
pour une fin hydrologique).

## Entrées optionnelles, et le sort des trois fiches de période

Ouvert le 2026-07-22. `QM_H`, `FDC_H` et `median-QJ_H` calculent la même
chose que `QM`, `FDC` et `median-QJ`, restreinte à une période. Or
`over_period` traite déjà une borne absente comme un côté ouvert : sans
bornes, il calcule sur toute la chronique. Les trois fiches restreintes
et les trois fiches entières pourraient donc n'en faire que **trois**,
la période devenant une entrée facultative.

Ce qui manque : card exige toutes les `input_vars` déclarées, sans
notion d'entrée facultative (vérifié le 2026-07-22, aucun mécanisme). Il
faudrait pouvoir écrire quelque chose comme
`input_vars: "Q, period_start?, period_end?"`, ou un champ séparé, et
que la vérification amont ne réclame que les obligatoires.

**Question de nomenclature liée, à trancher par l'utilisateur.** Le
suffixe `_H` de ces trois fiches signifie « horizons de projection »
(NOMENCLATURE.md), or elles acceptent désormais n'importe quelle période,
observée comprise, et leur métadonnée dit « période » depuis le
2026-07-22. Trois voies : garder `_H` malgré l'inexactitude, choisir un
autre suffixe, ou faire disparaître la question en fusionnant avec les
fiches de base comme ci-dessus. La troisième est la plus propre, elle
suppose seulement les entrées facultatives.

## Export SKOS / thésaurus (différé de longue date)

La classification (`TOPICS.md`) fournit désormais les concepts et les
paires français/anglais : chaque facette devient un concept scheme.
Réévaluer quand le besoin Skosmos se concrétise.

Le SKOS n'est pas un service : c'est un artefact de publication de la
classification, dont la source de vérité est ici (`src/card/topics.yaml`
et les blocs classification des fiches).

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

## Fiches futures

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

## Palettes : questions ouvertes (2026-07-18)

État : les fiches à grandeur non ambiguë sont toutes équipées (héritage
de la fiche mère ; voir RENAMING.md 2026-07-18 pour l'orientation ETP).
Quatre palettes sémantiques en usage : marron vers vert (quantités
d'eau), bleu vers rouge (température), violet vers orange (dates et
durées de crue), vert vers marron (durées et volumes d'étiage, ETP :
assèchement).

- **Scores de performance et indices sans unité** (KGE, NSE et
  variantes, Bias, STD_ratio, epsilon_R/T, RAT_*, QR_ratio, RA_ratio,
  BFI-LH/Wal et leurs deltas, BFM, a-FDC) : laissés sans palette
  volontairement. Si on les équipe un jour, il faudra une palette
  divergente centrée sur la valeur de référence (1 pour KGE/NSE, 0 pour
  les deltas de BFI), décision non prise.
- **dtFlood** : partage la palette violet vers orange avec les dates, et
  non la palette d'assèchement de dtLF/dtBF. Examiné le 2026-07-18 et
  conservé : une durée de crue représente un risque (dégâts), pas un
  assèchement, et une crue plus longue n'est pas « plus d'eau » ; la
  dynamique diffère de celle des étiages. Si on veut un jour distinguer
  le risque de crue des dates par une palette dédiée, c'est une
  décision à part.

## Grand nettoyage docs et uniformisation (card, stase, card-api)

Ouvert le 2026-07-21, plan exécutable dans `PLAN_nettoyage.md`.
Cloisonnement des trois paquets (ce qui traite de card dans card, du
moteur dans stase, du service dans card-api), un rôle exclusif par
fichier, et un `CHANGELOG.md` par paquet pour que la trace des
livraisons ne repose pas seulement sur git.

**Fait pour card le 2026-07-22** : carte des rôles, CHANGELOG, archive
badgée, ORIGINE_R renommé, ce registre purgé. **Reste** : la même passe
sur stase et sur card-api, puis la relecture des métadonnées à
placeholder (phase 4 du plan) et les README (phase 3).

Deux points déjà appris, à ne pas reperdre :
- **un historique n'est pas supprimable tel quel** : ces documents sont
  référencés par des docs vivantes et portent du contenu à valeur. Il
  faut la carte des rôles d'abord, puis re-router les renvois, et
  archiver plutôt que supprimer ;
- **métadonnées à placeholder : cohérence vérifiée** (62 fiches, 0
  anomalie). La forme générique par défaut (« the target horizon »,
  « l'horizon cible ») est **voulue** : c'est la métadonnée publique de
  `metadata_only`, que le suffixe vient clarifier avec le contexte.
  Reste l'avis de l'utilisateur sur ce terme générique, et la
  documentation de son usage.
