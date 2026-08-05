> **Statut : registre vivant.** Ce fichier ne contient que des pistes
> **ouvertes**. Un chantier livré en sort et devient une entrée de
> `CHANGELOG.md`, à la racine du dépôt, qui renvoie au document
> expliquant le détail. Les sections portent des titres et non des
> numéros : le registre bouge, un numéro ne se cite pas durablement.

# CHANTIERS : pistes ouvertes (mise à jour 2026-08-04)

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

Des fiches plantent dans le paquet R lui-même, donc sans référence
croisée possible. Le signalement en amont est devenu actionnable le
2026-07-22, la cause étant diagnostiquée : **lesquelles, et pourquoi, se
lisent dans `ORIGINE_R.md`** (deux familles, dont l'une est un
`summarise` que dplyr a durci sous des fiches qui fonctionnaient).

Ce qui reste à faire, et qui n'est écrit qu'ici :

- correctif probable côté EXstat pour la première famille : basculer
  l'appel de `summarise` vers `reframe` quand la fonction rend un
  vecteur ; la seconde famille est à creuser séparément, sa cause n'est
  pas établie ;
- le diagnostic vaut pour la version de R installée ici : le rejouer sur
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

## Provenance logicielle : unifier card et card-api (état des lieux 2026-08-04)

**Le problème.** Trois niveaux de traçabilité sont annoncés (la
définition, le corpus, le moteur) mais un seul sort de `card` employé
seul :

| | `card.extract` en local | via `card-api` |
|---|---|---|
| la définition, quelle fiche | `swhid` + `version` | idem |
| le code qui a tourné | **rien** | `card_version` + `card_commit` |
| le moteur | **rien** | `stase_version` + `stase_commit` |

La colonne `functions` publie des noms, mais un nom sans version ne
désigne aucun code : `apply_threshold` de mars et celui d'aujourd'hui
portent le même. Un résultat calculé dans un carnet a donc une provenance
logicielle vide, alors que la même requête passée au service est
parfaitement tracée.

**Ce qui existe déjà, et qui est bon.** `card-api` a résolu la question
pour lui (`src/card_api/pipeline.py`, fonction `versions()`) :

- les numéros viennent de `importlib.metadata.version()`, avec repli sur
  `card-stase` tant que le nom PyPI n'est pas obtenu, et sur `"dev"` hors
  installation ;
- les commits sont résolus **à la construction de l'image** par
  `scripts/resolve_refs.py`, qui écrit `build_refs.json` ;
- le SWHID d'une révision est `swh:1:rev:<commit>`, calculable sans appel
  d'API.

Il n'y a donc **rien à inventer**, seulement à déplacer : la moitié
« numéros » ne doit rien à Docker ni au service, elle marche partout où
`card` est installé.

**La piste à creuser, PEP 610.** Un paquet installé par
`pip install git+https://…` porte un fichier `direct_url.json` normalisé
(PEP 610) qui contient le commit sous `vcs_info.commit_id`, lisible à
l'exécution par `importlib.metadata`. Or c'est exactement le mode
d'installation documenté de `card` tant que PyPI n'est pas obtenu. Si
cela se confirme, **`card` peut publier son propre commit sans aucune
machinerie de build**, et `build_refs.json` ne reste nécessaire que pour
une image construite depuis une copie de travail. Vérifié le 2026-08-04
sur cet environnement : l'installation y est éditable, donc
`direct_url.json` ne porte que `dir_info.editable`, sans commit. **À
retester sur une vraie installation depuis GitHub avant de conclure.**

**La difficulté qui reste, et elle est plus grave que je ne l'avais
écrite.** Le numéro de version ne ment pas parce qu'il serait figé, il
ment parce qu'il **retarde**, et parce que rien ne garantit qu'on lise le
bon.

Constaté le 2026-08-04, en trois points :

- le paquet est en **0.2.0**, tagué `v0.2.0` le 2026-07-22 au commit
  `677bd87`, et **plus de quatre-vingts commits** ont suivi. Publier
  « 0.2.0 » à côté d'un résultat calculé aujourd'hui désigne donc un état
  qui n'est pas celui qui a tourné ;
- `src/card/__init__.py` annonçait `0.1.0` quand les trois autres
  fichiers disaient `0.2.0`, parce que `tests/test_citation.py` ne
  regardait pas ce fichier. Corrigé le même jour, `set_version.py`
  l'écrit maintenant et le test refuse le désaccord ;
- pire pour la provenance : dans une installation ÉDITABLE,
  `importlib.metadata.version()` rend la valeur enregistrée au moment du
  `pip install -e`, donc `0.1.0` ici alors que le dépôt est en `0.2.0`.
  La source que `card-api` interroge peut donc être périmée sans que rien
  ne le signale.

**Conclusion : le numéro seul ne suffit jamais.** Il faut le commit, ou
rien. Et il reste à décider si card publie un numéro du tout dans ses
métadonnées, ou seulement un commit.

**Question de fond à trancher d'abord**, avant toute ligne de code : la
gestion des versions elle-même. Publier rarement et laisser le commit
tracer (doctrine actuelle) est cohérent, mais fabrique un numéro qui
retarde de quatre-vingts commits, et un `CITATION.cff` qui fait citer un
état vieux de deux semaines. À reprendre en session dédiée.

**Procédure unifiée proposée**, à valider avant d'écrire une ligne :

1. `card` expose une fonction publique de provenance qui rend les
   numéros de `card` et de `stase`, et leurs commits quand ils sont
   connaissables (PEP 610, variable d'environnement, ou fichier de
   build) ;
2. `card.extract` publie ces champs dans la table `meta`, à côté de
   `swhid` et `version`, de sorte qu'un résultat local dise avec quel
   logiciel il a été calculé ;
3. `card-api` **consomme** cette fonction au lieu de la réimplémenter, et
   n'ajoute que ce qui lui est propre : `api_version`, et les commits
   résolus au build quand PEP 610 ne peut pas répondre.

Le point 3 est l'enjeu réel : deux méthodes divergentes pour le même
fait finiraient par se contredire, et c'est déjà à moitié le cas.

## Deux réserves laissées dans des descriptions (2026-08-03)

Le chantier des descriptions est livré (cf. `CHANGELOG.md`). Deux points
n'ont pas pu être tranchés faute d'information :

- `CR` et `CRS_season` s'appellent « coefficient correctif » sans que la
  fiche ni le code ne disent comment appliquer la correction. Leur
  description s'arrête donc au fait, le rapport simulé sur observé.
- Celle d'`a-FDC` lit la pente comme une mesure de variabilité du régime,
  ce qui est la lecture usuelle mais reste une lecture.

## Si une moyenne de pluie devient une SORTIE (veille)

`RA-mean` règle trois colonnes intermédiaires, et c'est proportionné.
Mais Oberlin n'a pas de case pour la moyenne temporelle d'une pluie :
pour lui ce n'est pas une variate, la position 3 vide valant « totale »
(cf. `NOMENCLATURE.md`). Le jour où une telle moyenne devient une
sortie publiée, il faudra un jeton de position 3 plutôt qu'un suffixe de
variante, donc une extension du système et non un contournement.

## Deux fonctions circulaires sans usage

`circular_ratio` et `circular_difference` ne sont employées par aucune
fiche (mesuré le 2026-08-03). Ce sont des portages de R, donc la question
est une question de PARITÉ, pas de ménage : les retirer romprait la
correspondance avec `CARD`/`EXstat`, les garder laisse deux fonctions
qu'aucun test de fiche n'exerce. À trancher avec le sort du portage.

Leur voisine `difference_longest_run`, elle, a été retirée le 2026-08-03 :
créée par symétrie le 2026-07-31, aucune fiche ne l'a jamais employée
(cf. `RENAMING.md`).

## `meta.sampling_period` : prose d'un côté, littéral Python de l'autre

Une partie du corpus écrit une phrase (« Mois du maximum des débits
mensuels »), une autre un littéral brut (`['01-09', '31-08']`) que la
figure doit reformater pour le rendre lisible. Même famille de problème
que `method` avant sa refonte : un champ qui porte deux formes sans règle.
Repéré pendant le chantier `method`, pas traité.

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

## Unités machine-lisibles (UCUM) (différé)

Les unités sont des chaînes LaTeX-ish (`m^{3}.s^{-1}`, `hm^{3}`, `jour de
l'année`, `sans unité`). Lisibles pour un humain, mais pas
interopérables : un client ne peut pas convertir ni comparer sans parser.
Piste : ajouter un code **UCUM** (`m3/s`, `Cel`, `mm`…) à côté de chaque
unité, dans `inputs.yaml` pour les entrées et dans un registre pour les
sorties, exposé tel quel par card-api. Amélioration FAIR-Interopérabilité,
sans urgence (même famille que l'export SKOS). Noté depuis la revue FAIR
de card-api du 2026-07-24.

## Tendance des régimes mensuels et saisonniers (limite structurelle)

`card.trend` ne s'applique qu'aux fiches `output: series` (une valeur par
année). `QM` (régime mensuel, `curve`) et `QSA_season` (agrégat saisonnier)
ne sont donc pas tendançables, alors qu'une tendance du régime mensuel
aurait du sens. Ce n'est pas un bug : ces fiches collapsent ou indexent le
temps autrement que par année, ce que le modèle série-annuelle de stase ne
couvre pas. Piste future : une variante `output: series` par mois/saison
(le fan-out `_month`/`_season` existe déjà côté valeurs), ou un mode trend
qui accepte un axe sous-annuel. Noté à la revue card-api du 2026-07-24, à
ne pas traiter maintenant.

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

## Nettoyage docs et uniformisation (card, stase, card-api)

Campagne ouverte le 2026-07-21. Cloisonnement des trois paquets (ce qui
traite de card dans card, du moteur dans stase, du service dans
card-api), un rôle exclusif par fichier, et un `CHANGELOG.md` par paquet
pour que la trace des livraisons ne repose pas seulement sur git.

La procédure, ses phases et **l'état de chacune** vivent dans
`NETTOYAGE.md` : ce qui reste à faire se lit dans sa section « Campagne
en cours », et n'est redit nulle part ailleurs.

Deux points déjà appris, à ne pas reperdre :
- **un historique n'est pas supprimable tel quel** : ces documents sont
  référencés par des docs vivantes et portent du contenu à valeur. Il
  faut la carte des rôles d'abord, puis re-router les renvois, et
  archiver plutôt que supprimer ;
- **métadonnées à placeholder : cohérence vérifiée** le 2026-07-21, sans
  une anomalie. La forme générique par défaut (« the target horizon »,
  « l'horizon cible ») est **voulue** : c'est la métadonnée publique de
  `metadata_only`, que le suffixe vient clarifier avec le contexte.
  Reste l'avis de l'utilisateur sur ce terme générique, et la
  documentation de son usage.
