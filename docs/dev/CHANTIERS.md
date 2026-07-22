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

11 fiches plantent dans le paquet R lui-même (CR, CRS_season, FDC x5,
QJC10, RA_ratio, RAl_ratio, RAs_ratio) : leurs versions Python
fonctionnent, aucune référence de validation croisée n'est possible. À
signaler en amont, le paquet R étant en maintenance. Liste et contexte :
`ORIGINE_R.md`.

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

## Donner une fiche à LIRE : rendu ASCII de la chaîne de calcul

Ouvert le 2026-07-22. Demande de fond de l'utilisateur, la même que
celle du chantier card-api sur la lisibilité du catalogue, mais prise
par le bon bout : la matière est dans les fiches, donc le rendu se fait
ici, et le service ne fait que le relayer.

**Le problème.** Une fiche contient tout ce qu'il faut pour comprendre
ce qu'elle calcule : colonne d'entrée, fonction et ses paramètres, pas
de temps, fenêtre d'échantillonnage, seuils de lacunes, et le chaînage
(une variable produite par P1 est consommée par P2). `card.info()`
aplatit tout ça en une liste de champs, et `method` en une phrase
numérotée. On peut le lire, mais on ne le VOIT pas, et l'ambiguïté reste
possible sur ce que fait exactement chaque étape.

**Ce qu'on veut.** Un rendu texte qui montre la chaîne, ses étapes, ce
qui entre et ce qui sort de chacune, et la fenêtre annuelle sur douze
mois. Lisible dans un terminal, dans un notebook, et relayable par
l'API. Sans dépendance graphique.

**Première esquisse, à retravailler** (VCN10, deux étapes, fenêtre
adaptative) :

```
VCN10   Minimum annuel de la moyenne sur 10 jours du débit journalier
        m³·s⁻¹  ·  série  ·  annuelle  ·  basses eaux

   Q   débit journalier moyen [m³·s⁻¹]
   │
   P1  rollmean_center(Q, k=10)        moyenne mobile centrée sur 10 jours
   │   pas de temps : aucun, la série journalière est conservée
   │   écarte une série trouée de plus de 10 années consécutives
   │
   VC10
   │
   P2  nanmin(VC10)                    minimum
   │   pas de temps : année
   │   fenêtre : adaptative, départ au mois du maximum des débits mensuels
   │   écarte une année à plus de 3 % de lacunes
   │
   VCN10

   fenêtre           J  F  M  A  M  J  J  A  S  O  N  D
   annuelle          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
   (QNA_summer)            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

**Questions à trancher avant d'écrire.**

- Où vit le rendu : `card.info(..., render=True)` ? une fonction
  dédiée `card.show()` ? Le retour dict actuel de `info()` ne doit pas
  changer de forme, du code en dépend.
- Comment le relayer par l'API sans alourdir : un champ `render` dans
  `/v1/cards/{id}` ? un `format=txt` ? Décider une fois le rendu stable,
  pas avant.
- Que faire des fiches à fan-out (12 mois, 4 saisons) et des courbes
  (FDC), dont la sortie n'est pas une série annuelle.
- Jusqu'où décrire une fonction : `rollmean_center` mérite une glose,
  `nanmin` non. La source serait les docstrings de `card.functions`,
  qui existent déjà.
- Unicode ou ASCII strict : les barres et flèches passent mal dans
  certains terminaux Windows. Prévoir un repli.

**Prendre le temps.** L'utilisateur demande explicitement une phase de
réflexion et de recherche de forme sur ce chantier, pas une première
version expédiée : c'est de la communication scientifique, l'objet doit
être juste ET agréable. Référence de goût maison : le tableau de bord
`make stats` de card-api (sparklines, heatmap façon contributions).

## Convertir les 12 fiches à horizon figé au modèle suffixe

Ouvert le 2026-07-22, demandé par l'utilisateur. Douze fiches figent
encore leurs dates d'horizon **dans le fichier**, alors que le chantier
du 2026-07-21 a sorti ces bornes des 59 autres :

| famille | fiches | période figée |
|---|---|---|
| `QM_H0..H3` | 4 | H0 1976-01-01 à 2005-08-31, puis DRIAS 2021-2050, 2041-2070, 2070-2099 |
| `FDC_H0..H3` | 4 | idem |
| `median-QJ_H0..H3` | 4 | idem |

Conséquence mesurée : sur des observations 1970-2020, `QM_H1` rend zéro
ligne et un avertissement. Ces fiches ne servent qu'à des projections
DRIAS, et à celles-là seulement, ce que rien n'annonce.

**Cible** : trois fiches, `QM_H`, `FDC_H` et `median-QJ_H`, recevant
`horizon_start` et `horizon_end` en colonnes d'entrée, avec
`{suffix.name}` dans les métadonnées. Exactement le modèle des 45 fiches
delta, et ce qui débloque les horizons par degré de réchauffement.

**Verrou technique, à lever d'abord dans stase.** Ces fiches restreignent
la période avec le champ `period` d'un process, et le `period` de
`process_extraction` est un filtre **global** à dates littérales,
identique pour toutes les séries : il n'accepte pas de nom de colonne et
ne peut pas varier d'une série à l'autre (extraction.py, bloc « Filtre
period »). Les fiches delta, elles, passent leurs bornes en **kwargs de
fonction**, ce qui marche déjà. Il faut donc soit étendre `period` aux
colonnes de paramètre, soit un mécanisme dédié. Chantier ouvert côté
stase, à faire avant la conversion.

**À arbitrer au passage** : la fenêtre H0 vaut `1976-01-01` à
`2005-08-31`, une date de début calendaire pour une date de fin
hydrologique (30 années hydrologiques auraient commencé au 1975-09-01).
Les trois autres horizons finissent en 12-31. Une fois les bornes
fournies par l'appelant la question sort des fiches, mais la valeur
recommandée pour DRIAS mérite d'être écrite quelque part.

**Coût annexe** : 12 identifiants disparaissent au profit de 3. C'est un
changement de sorties, donc trace dans RENAMING.md, bump majeur, et le
catalogue comme le service en sont affectés.

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
