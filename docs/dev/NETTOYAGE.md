> **Statut : procédure en vigueur.** Le mode d'emploi d'un coup de
> nettoyage documentaire sur les dépôts de l'écosystème : ce qu'on
> vérifie, dans quel ordre, et à quoi on reconnaît que c'est fini. Il ne
> se périme pas, il se rejoue. Seule la section « Campagne en cours » en
> fin de document porte un état, et elle seule.

# Nettoyage et uniformisation : card, stase, card4r, card-api

Nettoyage transverse aux paquets de l'écosystème : docs de dev, docs
d'utilisation (README), pages web, métadonnées à placeholder, et surtout
**cloisonnement** (chaque info à un seul endroit) pour réduire le coût
token du re-chargement de contexte des futurs Claude.

Écrit le 2026-07-21 pour la première campagne, gardé comme procédure.
Les phases ci-dessous décrivent le travail à faire et ne disent jamais
où il en est : cet état vit dans la campagne en cours, et nulle part
ailleurs. Une campagne close laisse une entrée de `CHANGELOG.md` ; la
suivante rouvre les phases dont elle a besoin.

## Principes directeurs

1. **Une VALEUR, un seul endroit (source de vérité).** Un nombre, un
   décompte, une affirmation vérifiable : les autres fichiers RENVOIENT,
   ne recopient pas, sinon l'un des deux finira faux. En revanche un
   **rappel de procédure** gagne à être répété là où on travaille
   (arbitrage utilisateur du 2026-07-22) : il ne peut pas mentir, et sa
   redondance est précisément ce qui évite l'oubli. Doubler une consigne,
   oui ; doubler un numéro de version, jamais.
2. **Budget token.** Ce qui est chargé chaque session (les 3 CLAUDE.md,
   MEMORY.md) doit être concis, factuel, non dérivable du code, et
   pointer vers les docs détaillées plutôt que les inclure.
3. **Git ne suffit pas** (arbitrage utilisateur du 2026-07-22, après
   s'être fait piéger sur la divergence de rolling, retrouvée à la main
   faute d'être écrite quelque part). Un document terminé s'**archive**
   avec un bandeau de statut, il ne se supprime pas, et chaque paquet
   tient un `CHANGELOG.md` qui dit ce qui a changé, quand, et où lire le
   détail.
4. **Pas de nom maison** (même arbitrage). On utilise les noms attendus à
   la racine d'un dépôt (README, LICENSE, AUTHORS, CHANGELOG,
   CITATION.cff) plutôt que d'inventer HISTORIQUE ou JOURNAL, qui
   obligent à deviner. Un bandeau de statut en tête de chaque document
   dit son rôle et sa validité, dans l'esprit des ADR.
5. **Sobre et exécuté.** Docs utilisateur : parcours clair, exemples
   RÉELLEMENT exécutés, Python puis R en parallèle (cf. feedback style).

## Structure cible, identique dans tous les dépôts

```
README.md          vitrine et usage
CHANGELOG.md       journal daté, une section par version
CLAUDE.md          contexte de session
docs/dev/
  CHANTIERS.md     ce qui est ouvert, rien d'autre
  archive/         documents d'époque, bandeau de statut en tête
  <normatives>     card : NOMENCLATURE, TOPICS, RENAMING, ORIGINE_R
                   stase : ORIGINE_R, RENAMING_PY
                   card-api : API
```

## Carte « fichier -> rôle exclusif »

Statuts : **SOURCE** (seul endroit qui définit l'info), **RENVOI** (ne
fait que pointer), **GÉNÉRÉ** (produit par un script, ne pas éditer),
**HISTORIQUE** (trace datée, non maintenue), **RÉFÉRENCE** (document
externe), **TEMPORAIRE** (disparaît une fois exécuté).

Un document créé dans `docs/dev/` s'inscrit ici en même temps qu'il est
écrit : une carte qui ne couvre pas tout le dossier n'est plus un
inventaire, et ne garantit donc plus le « un rôle par fichier ».

### card

Aucune valeur dérivée dans ces tableaux, en particulier pas de colonne
« lignes » : celle qu'ils portaient avait dérivé sur chacune de ses
lignes en deux semaines (constaté le 2026-08-04). `wc -l` la donne quand
elle sert.

| fichier | rôle exclusif | statut |
|---|---|---|
| README.md | vitrine et parcours d'usage : installer, extraire, suffixes, tendance, écrire sa fiche | SOURCE |
| CLAUDE.md | contexte de session : format d'une fiche, règles de travail, état court | SOURCE |
| CHANGELOG.md | journal daté des livraisons, une section par jalon | SOURCE |
| docs/index.md | landing Pages : renvoi vers catalogue et dépôt | RENVOI |
| docs/CARDS.md | catalogue, une ligne par fiche | GÉNÉRÉ |
| docs/dev/NOMENCLATURE.md | grammaire des noms de variables et rédaction des métadonnées (R1 à R7, Oberlin) | SOURCE |
| docs/dev/TOPICS.md | classification à facettes : modèle, vocabulaire, arbitrages | SOURCE |
| docs/dev/RENAMING.md | journal daté des renommages et des changements de SORTIES (parité R rompue) | SOURCE |
| docs/dev/CHANTIERS.md | registre des pistes ouvertes du corpus | SOURCE |
| docs/dev/ORIGINE_R.md | origine R du corpus, validation croisée, divergences propres aux FICHES | SOURCE |
| docs/dev/NETTOYAGE.md | ce document : procédure de nettoyage documentaire de l'écosystème | SOURCE |
| docs/dev/PLAN_R.md | décisions sur l'accès R au corpus et le sort des paquets R | TEMPORAIRE |
| docs/dev/Oberlin_1994...edit.md | source scientifique du système de nommage (OCR) | RÉFÉRENCE |
| docs/dev/archive/AUDIT_FICHES.md | constats et décisions de l'audit appliqué le 2026-07-15 | HISTORIQUE |
| docs/dev/archive/ROADMAP.md | phases A à D de la refonte R vers Python | HISTORIQUE |
| docs/dev/archive/PLAN_METHOD.md | conception de la refonte du champ `method`, août 2026 | HISTORIQUE |

### stase

| fichier | rôle exclusif | statut |
|---|---|---|
| README.md | vitrine et usage du moteur | SOURCE |
| CLAUDE.md | contexte de session : structure, règles (tools.py gelé, détection par type), API | SOURCE |
| CHANGELOG.md | journal daté des livraisons du moteur | SOURCE |
| docs/dev/CHANTIERS.md | registre des pistes ouvertes du moteur | SOURCE |
| docs/dev/ORIGINE_R.md | origine R du moteur, validation, divergences intentionnelles du MOTEUR | SOURCE |
| docs/dev/RENAMING_PY.md | renommages de paramètres et de colonnes de sortie de stase | SOURCE |
| docs/dev/archive/CONVERSION_R.md | ancien CLAUDE.md d'EXstat_Claude, trace de la conversion | HISTORIQUE |
| docs/dev/archive/PLAN.md | audit du 2026-07-12 et son plan, clôturé | HISTORIQUE |
| docs/dev/archive/harnais_R/ | harnais de comparaison R, figé | HISTORIQUE |

### card4r

Quatrième dépôt depuis le 2026-08-05, front R du corpus. Il suit les
mêmes conventions, avec les noms attendus d'un paquet R là où ils
diffèrent (`DESCRIPTION`, `man/`).

| fichier | rôle exclusif | statut |
|---|---|---|
| README.md | vitrine et usage : installer, extraire, tendance, ce que le paquet ne fera pas | SOURCE |
| CHANGELOG.md | journal daté, et la règle de coupe propre au paquet | SOURCE |
| CITATION.cff | métadonnées de citation ; accord avec DESCRIPTION tenu par un test | SOURCE |
| DESCRIPTION | identité du paquet R, version, dépendances | SOURCE |
| R/zzz.R | le pont : provisionnement Python et refs épinglées de card et stase | SOURCE |
| R/card.R | l'API R, et le traitement des dates | SOURCE |
| man/ | pages d'aide | GÉNÉRÉ (roxygen2) |

### card-api

| fichier | rôle exclusif | statut |
|---|---|---|
| README.md | vitrine du service : endpoints, cas d'usage Python puis R, quotas | SOURCE |
| INSTALL.md | développement et déploiement (Docker, Apache, variables d'env) | SOURCE |
| CLAUDE.md | contexte de session | SOURCE |
| CHANGELOG.md | journal daté des livraisons du service | SOURCE |
| docs/dev/API.md | conception du service, et §1 = carte de l'écosystème à trois repos | SOURCE |
| docs/dev/CHANTIERS.md | registre des pistes ouvertes du service | SOURCE |
| docs/dev/PLAN_FAIR.md | revue FAIR du 2026-07-24 et son plan | SOURCE |
| docs/dev/THEME_DOCS.md | thème de la documentation servie | SOURCE |

## Phase 0 : inventaire et carte des redondances

Tenir la carte ci-dessus à jour, puis chercher les redondances et les
affirmations périmées. Toute trouvaille se vérifie **dans le code** avant
d'être écrite : une redondance supposée est souvent une explication
légitime à deux niveaux de détail.

Les sept trouvées le 2026-07-22, toutes corrigées depuis, disent les
formes que ça prend, et c'est cette liste qu'on rejoue :

1. une API donnée pour vivante alors qu'elle est purgée (les clés
   `dataEX`/`metaEX`, le `meta=` de `process_trend`) ;
2. une valeur dérivée recopiée dans des docs vivantes (le nombre de
   fiches, alors qu'un script le génère) ;
3. la même explication écrite deux fois (les alias R, la divergence du
   rolling à fenêtre paire) ;
4. un registre qui garde ce qu'il déclare ne pas garder (CHANTIERS et
   ses chantiers livrés) ;
5. un renvoi vers un document déplacé, archivé ou renommé.

Trois questions suffisent à trancher : qui **définit** cette
information ? qui la **recopie** ? est-elle encore **vraie** ?

## Phase 1 : ranger l'historique

Recette établie sur card le 2026-07-22, à rejouer telle quelle dans
chaque dépôt :

1. écrire le `CHANGELOG.md` du paquet à partir de `git log --reverse`,
   une section par jalon daté, 3 à 6 lignes par entrée, avec un renvoi
   vers le document qui explique le détail (jamais de recopie) ;
2. `git mv` des documents terminés vers `docs/dev/archive/`, avec un
   bandeau de statut en tête qui dit ce qu'ils sont, pourquoi ils sont
   là, et où lire l'état courant ;
3. ré-héberger d'abord ce qui reste vivant à l'intérieur (pour card :
   les principes de conversion vers ORIGINE_R, le plan PEP 541 vers
   CHANTIERS) ;
4. re-router TOUS les renvois avant de bouger quoi que ce soit
   (`grep -rn` sur le nom du fichier dans les trois dépôts, les renvois
   croisés inter-dépôts compris) ;
5. purger CHANTIERS de ce qui est livré, poser un bandeau de statut sur
   chaque document restant.

Exemple, première campagne sur card : `ROADMAP.md` et `AUDIT_FICHES.md`
archivés, `VALIDATION_R.md` renommé `ORIGINE_R.md` (même rôle que dans
stase), CHANTIERS ramené aux pistes ouvertes et numéros de section
abandonnés (un numéro ne se cite pas durablement dans un registre qui
bouge).

## Phase 2 : CLAUDE.md et mémoire (budget token)

- Les 3 CLAUDE.md : garder l'essentiel non dérivable (format, règles de
  travail, état COURT). Sortir tout ce qui est détaillé dans docs/dev en
  RENVOI. La section « État » de card CLAUDE gonfle à chaque chantier :
  la réduire à un pointeur (dernier chantier + lien CHANTIERS/git).
- Uniformiser la structure des 3 CLAUDE.md (mêmes sections : Contexte,
  Structure, Règles, État, renvois).
- Mémoire (`~/.claude/.../memory/`) : élaguer les entrées obsolètes. Une
  entrée dit ce qui était vrai le jour où elle a été écrite ; la
  confronter au code avant de s'y fier.

## Phase 3 : README utilisateur (donner envie)

Pour chacun des 3 README, parcours « pourquoi -> quoi -> comment », UN
exemple exécuté par capacité :
- **card** : extract (une fiche), plusieurs fiches, suffix (multi-seuils
  DOE/DCR et obs/sim), horizons en colonnes, trend, dev de sa propre
  fiche (copy_cards -> schema).
- **stase** : process_extraction (agrégation), sampling adaptatif,
  param_cols (covariables), process_trend.
- **card-api** : table des endpoints, exemples curl/Python/R, jobs, clé
  de priorité.
- Vérifier chaque exemple par EXÉCUTION (motif scratchpad apitest déjà
  utilisé pour card-api).

## Phase 4 : Métadonnées à placeholder (cohérence, PAS un « trou »)

Cadrage (précisé par l'utilisateur le 2026-07-21) : la forme PAR DÉFAUT
(sans suffixe, placeholders résolus par `suffix_default`) est VOULUE
générique. C'est la métadonnée publique exportée par
`card.extract(metadata_only=True)` : une fiche générique, volontairement
non spécifique. Le mécanisme de suffixe est précisément ce qui CLARIFIE
les placeholders avec le contexte, quand l'appelant fournit ses données
de paramétrage externes (et donc, potentiellement, des enregistrements
de métadonnée en plus, selon le contexte). C'est le but même des fiches
qui exigent un paramétrage externe. Donc « target horizon » par défaut
n'est PAS un bug : c'est la forme générique assumée.

Mesure du 2026-07-21 : exemples rendus sur delta-QA_H (générique
« the target/cible horizon » cohérent ; clés nues « the H1 horizon » un
peu sèches mais valides ; records riches « the near-future (2021-2050)
horizon » informatifs), et scan des fiches à placeholder sans une seule
anomalie (aucune accolade résiduelle, aucun mot double).

Le travail n'est donc pas de figer du contexte dans la fiche, mais de
VÉRIFIER la cohérence :
- Fournir à l'utilisateur des EXEMPLES rendus (forme générique par défaut
  vs avec records riches near/2021-2050) pour qu'il juge : il ne les a
  pas encore lus. Un éventuel `suffixes:` par défaut ne se déciderait que
  SI les exemples montraient le générique incohérent, pas par principe.
- Vérifier que CHAQUE `{suffix.X}` forme une phrase cohérente EN et FR,
  autant en générique qu'avec records (script : rendre les métadonnées
  de toutes les fiches à placeholder, relire).
- Vérifier que `suffix_default` (short/name) donne un générique qui se
  LIT bien (« target/cible » convient-il, ou un terme plus naturel ?).
- Documenter côté utilisateur : comment et quand fournir des records
  riches (horizons fixes DRIAS vs par degré de réchauffement).

## Phase 5 : Pages web / publication

- card `docs/index.md` (stub) : décider son rôle (landing ?
  renvoi vers CARDS.md + README + SKOS). Étoffer ou assumer minimal.
- SKOS/thésaurus (CHANTIERS §6) : lien depuis la landing si concrétisé.
- card-api : vérifier que la doc API (README + API.md) reflète l'état
  déployé.

## Phase 6 : Uniformisation inter-packages

- Conventions communes aux 3 repos : structure `docs/dev/`, format
  CLAUDE.md, structure README, style des renvois croisés
  (card <-> stase <-> card-api), en-têtes de licence.
- Un « index » léger par repo : quel fichier pour quelle question.

## Campagne en cours (ouverte le 2026-07-21)

**Seul état d'avancement** : ce qui est coché est fait, le reste est
ouvert. Aucun autre document ne redit cet état, tous renvoient ici.

Phase 0 :
- [x] carte « fichier -> rôle exclusif » des 3 repos, redondances
      repérées, puis toutes corrigées (2026-07-22, re-vérifiées le
      2026-08-05).

Phase 1 (recette établie le 2026-07-22) :
- [x] **card** : CHANGELOG écrit, ROADMAP et AUDIT_FICHES archivés,
      VALIDATION_R renommé ORIGINE_R, CHANTIERS purgé, bandeaux de
      statut posés, renvois re-routés.
- [x] **stase** : CHANGELOG écrit, PLAN et harnais R archivés, renvois
      de CLAUDE.md corrigés.
- [x] **card-api** : CHANGELOG écrit, API.md trié (état d'avancement et
      étapes retirés), renvois corrigés.

Phase 2 :
- [x] card CLAUDE.md : État réduit à un pointeur vers CHANGELOG et
      CHANTIERS, déploiement de card-api renvoyé chez lui.
- [x] stase et card-api CLAUDE.md élagués et uniformisés (même section
      « où lire quoi », même bloc « versions et citation »).
- [x] mémoire élaguée (project-state réécrit, feedback-private-files
      ajouté).

Phase 3 :
- [x] **card** : un exemple exécuté par capacité (extract, trend,
      sampling_period, seuils et suffixes, horizons et périodes en
      colonnes, provenance d'un résultat, list_cards, info, copy_cards
      puis schema). Tous rejoués le 2026-08-04, sorties conformes ; la
      figure de « Lire une fiche » est régénérée à la même date.
- [x] **stase** : quick start, stationnarité, enchaînement, fenêtre
      adaptative, `param_cols`, tous avec leur sortie. Fait le
      2026-07-28, jamais coché ici.
- [x] **card-api** : endpoints, curl, Python, R, jobs, clé de priorité.
      Fait le 2026-07-29, jamais coché ici.

Phase 4 :
- [ ] exemples rendus (générique vs records) fournis à l'utilisateur.
- [ ] toutes les phrases `{suffix.X}` cohérentes EN/FR (vérif scriptée).
- [ ] `suffix_default` relu (le générique se lit bien).

Phase 5 :
- [ ] rôle de docs/index.md tranché.
- [x] doc API à jour : provenance documentée dans le README de card-api,
      liens yaml et archive dans /v1/cards/{id}.

Phase 6 :
- [x] conventions communes et renvois croisés (2026-08-05) : bloc
      « écosystème » identique dans les six README, About alignés,
      bandeaux `superseded` sur les deux paquets historiques, liens
      croisés réparés, carte des rôles étendue au quatrième dépôt.
- [x] langue tranchée : anglais pour les paquets (card, stase, card4r,
      et les deux historiques qui l'étaient déjà), **français assumé
      pour card-api**, dont les utilisateurs, les données et les
      mentions légales le sont.
