# Aligner les quatre dépôts sur une même hygiène de projet

> **Statut : terminé le 2026-11-06.** Plan de campagne commun à card,
> stase, card4r et card-api, ouvert et mené le même jour. L'état de
> chaque dépôt est dans le tableau ci-dessous ; le bilan et ce qui reste à
> observer, en fin de document. Il a succédé à `docs/dev/NETTOYAGE.md`,
> devenu `dev/plans/2026-07-21_cleanup.md`. Il reste en place, et ses
> tables de correspondance permettent de résoudre un ancien chemin cité
> par un document figé.

| ordre | dépôt    | état                                                |
|------:|----------|-----------------------------------------------------|
|     1 | card-api | **fait le 2026-11-06** (commits 35df446 à 90a1cc3)  |
|     2 | stase    | **fait le 2026-11-06** (commits cfcf771 à dda86cf)  |
|     3 | card4r   | **fait le 2026-11-06**, après card (commit 016be69) |
|     4 | card     | **fait le 2026-11-06** (commits 6c154ba à 3d2fbe5)  |
|     5 | ensemble | **fait le 2026-11-06**, cf. « Bilan »               |

## Pourquoi

Deux organisations coexistent. Les dépôts suivent encore celle du ménage de
juillet (`docs/dev/CHANTIERS.md`, `docs/dev/archive/`, la procédure
`NETTOYAGE.md`), alors que l'utilisateur travaille désormais avec des
règles de projet communes à tous ses dépôts, qui en décrivent une autre.
Tant que les deux coexistent, chaque reprise demande de se souvenir
laquelle s'applique où, et c'est ce qui fait perdre le fil. Décidé le
2026-11-06 avec l'utilisateur : aligner les quatre dépôts sur la seconde.

Le but n'est pas de déplacer des fichiers, c'est qu'un prochain lecteur,
humain ou Claude, retrouve chaque information à un seul endroit en lisant
peu, **sans qu'aucune information importante ne se perde en route**. D'où
les garde-fous, et une phase de prise de recul avant chaque déplacement.

## La structure cible

```
README.md                        à quoi ça sert, comment s'en servir
ROADMAP.md                       ce qui reste à faire
CHANGELOG.md                     ce qui a été fait, version par version
CLAUDE.md                        comment on travaille ici, ce qu'il ne faut pas casser
CITATION.cff, codemeta.json      qui a fait quoi, comment citer
docs/                            la documentation publiée, s'il y en a une
dev/decisions.md                 les repères du projet, avec leur raison
dev/references.md                les sources lues, avec les passages utiles
dev/plans/AAAA-MM-JJ_sujet.md    le fichier de travail d'un point devenu trop lourd
dev/audits/AAAA-MM-JJ_sujet.md   un état des lieux daté, et ce qu'il appelle
```

La racine porte ce qu'on trouve dans tout dépôt ; `docs/` s'adresse aux
utilisateurs, `dev/` à qui développe. Un fichier n'est créé que s'il a
quelque chose à porter, et répond à une seule question. Ce qui se tape
(noms de fichiers et de dossiers) est en anglais, ce qui se lit (le
contenu) reste en français.

Trois règles qui en découlent et changent des habitudes de juillet :

- **une information qui évolue vit à un seul endroit** (version, état,
  reste à faire), les autres fichiers y renvoient ;
- **un plan porte son état en tête** (en cours, terminé le …) **et reste
  en place une fois terminé** : il n'y a plus de dossier `archive/`, la
  date dans le nom range les plans dans l'ordre ;
- **un audit ne change plus une fois écrit** : ses tâches partent dans
  `ROADMAP.md`.

Les choix du projet qui se construisent au fil du travail s'écrivent dans
`dev/decisions.md`, avec leur date et leur raison, pour qu'un prochain
Claude ne les défasse pas. Le `CLAUDE.md` garde la règle en une ligne et
renvoie à la raison.

## Les décisions de la campagne

Prises avec l'utilisateur le 2026-11-06 :

1. **Les textes normatifs restent des fichiers à part** dans `dev/`
   (nomenclature, classification, renommages, origine R) : chacun répond à
   sa propre question, et les fondre dans `decisions.md` le rendrait
   illisible.
2. **Les noms de fichiers passent en anglais**, conformément à la règle :
   `nomenclature.md`, `r-origin.md`… On renomme de toute façon.
3. **`NETTOYAGE.md` prend sa retraite** à la fin de la campagne. La
   structure est désormais dans les règles communes et la passe de
   nettoyage dans `/kit-clean`. Ce qu'il est seul à porter est reporté
   avant (section « Ce que NETTOYAGE.md porte encore »).
4. **Un dépôt par session**, parce que chaque session charge le
   `CLAUDE.md` de son dépôt. card-api d'abord (sa version 0.9.0 se fera
   ensuite dans la nouvelle structure), puis stase, card4r et card, qui
   ne sont pas sur le chemin de MAKAHO.
5. **Ce plan vit dans card**, là où vivait l'état des campagnes communes.
   Chaque dépôt a une ligne dans son registre qui y renvoie.

Proposées par ce plan, à confirmer au début de la session concernée :

6. **Les documents figés gardent leurs chemins** (audits, anciennes
   archives, consignes de passation de MAKAHO-next) : ils décrivent leur
   date. La table de correspondance plus bas permet de résoudre un ancien
   chemin. **Les entrées du CHANGELOG, elles, sont re-routées** : leur
   « où lire le détail » est un outil de navigation, et un renvoi qui ne
   mène nulle part perd l'information qu'il annonce.
7. **Les liens publics qui cassent sont acceptés, pas contournés.** Les
   README de card et de stase pointent vers `docs/dev/…` sur GitHub, et
   une page PyPI publiée garde le README de sa version. Laisser des
   fichiers relais aux anciens chemins réencombrerait ce qu'on range ;
   on corrige les README courants, et l'information reste dans le dépôt.
   À l'avenir, un lien public vers un document de `dev/` pointe vers un
   tag plutôt que vers `main`.

## Les garde-fous : ne rien perdre

1. **Déplacer avec `git mv`, dans un commit qui ne fait que déplacer.**
   Aucune modification de contenu dans ce commit : git suit alors les
   renommages (`git log --follow`), et le diff des commits suivants montre
   exactement ce qui a changé dans le texte.
2. **Avant de raccourcir, fusionner ou retirer un texte, lister ce qu'il
   est seul à porter** : mesures datées, arbitrages de l'utilisateur avec
   leur raison, choses à ne pas faire, erreurs déjà commises. Chacune
   reçoit une destination avant que le texte bouge. Rien ne disparaît qui
   ne soit porté ailleurs ou démenti par un fait vérifié dans le code.
3. **Vérifier dans le code avant de déclarer une redondance** : une
   redondance supposée est souvent la même chose dite à deux niveaux de
   détail, ce qui est légitime (les trois champs humains d'une fiche en
   sont l'exemple, cf. `CLAUDE.md` de card).
4. **Re-router tous les renvois**, dans les quatre dépôts et dans
   MAKAHO-next, y compris les commentaires de code, les tests, les
   workflows de CI et `mkdocs.yml`. Commande de départ, à lancer depuis
   `projects/` :
   `git -C <dépôt> grep -n -E 'docs/dev|NETTOYAGE|CHANTIERS'`.
   Relevé du 2026-11-06 : une centaine de renvois dans card, une
   soixantaine dans card-api, une vingtaine dans stase, deux dans card4r,
   une douzaine dans MAKAHO-next (dont ses consignes de passation, figées).
5. **Ce qui n'est pas suivi par git n'entre pas dans la campagne** : on ne
   le déplace pas, on ne le lit pas, on ne le liste pas. On stage
   nommément ce qu'on a soi-même modifié, jamais `git add -A`.
6. **Vérifier après chaque phase**, avec les commandes du dépôt : tests
   et lint partout, `make check` et `mkdocs build` pour card, `R CMD
   check` pour card4r si un fichier du paquet bouge.

## La méthode, dépôt par dépôt

**Phase A, prise de recul (lecture seule).** Lire en entier le
`CLAUDE.md`, le README, l'en-tête du CHANGELOG et chaque document de
développement. Remplir la section du dépôt dans ce plan : pour chaque
fichier, sa destination et ce qu'il est seul à porter. Relever les
contradictions, les doublons et ce qui est périmé, sous les cinq formes
que la campagne de juillet a appris à reconnaître :

- une API donnée pour vivante alors qu'elle est purgée ;
- une valeur dérivée recopiée dans un document vivant ;
- la même explication écrite deux fois ;
- un registre qui garde ce qu'il déclare ne pas garder ;
- un renvoi vers un document déplacé, archivé ou renommé.

Trois questions tranchent chaque cas : qui **définit** cette information ?
qui la **recopie** ? est-elle encore **vraie** ? Exposer à l'utilisateur,
en prose, ce qui n'est pas évident, avant de déplacer quoi que ce soit.

**Phase B, déplacer.** `git mv` seulement, un commit.

**Phase C, re-router.** Tous les renvois, un commit. À la fin, l'ancien
chemin ne doit plus apparaître que dans les documents figés (décision 6).

**Phase D, réécrire.** `ROADMAP.md` à partir du registre, réduit à ce qui
est ouvert ; `dev/decisions.md` à partir des arbitrages éparpillés ;
`CLAUDE.md` allégé, chaque ligne apportant ce qu'on ne peut pas déduire du
code, ni état du projet ni pratique générale. Le bloc « À NE JAMAIS
FAIRE » se garde tel quel. Un état en tête de chaque plan.

**Phase E, vérifier et consigner.** Les vérifications du garde-fou 6 ;
une relecture du `CLAUDE.md` à froid (un Claude qui ne connaît rien
sait-il où chercher ?) ; une entrée `## Non publié` du CHANGELOG ; l'état
du dépôt mis à jour dans le tableau de tête.

**Phase F, la prise de recul globale**, une fois les quatre faits. Poser
les quatre dépôts côte à côte : même squelette, mêmes noms, mêmes sections
de `CLAUDE.md`, renvois croisés justes (card, stase, card4r, card-api,
MAKAHO-next). Deux questions à trancher à ce moment-là :

- les règles recopiées dans les quatre `CLAUDE.md` (tiret cadratin, pas
  de fenêtre de choix, fichiers de notes, doctrine des versions) : les
  garder, puisqu'un dépôt public sert aussi des sessions qui n'ont pas les
  règles communes, ou les retirer ? L'arbitrage du 2026-07-22 (« doubler
  une consigne, oui ; doubler une valeur, jamais ») penche pour garder ;
- ce qui de `NETTOYAGE.md` n'a pas encore trouvé sa place, puis sa
  retraite.

## Ce que NETTOYAGE.md porte encore

À reporter avant sa retraite, chaque ligne vers sa destination :

- **Les principes de juillet**, arbitrés par l'utilisateur le 2026-07-22 :
  une valeur à un seul endroit mais un rappel de procédure peut se
  répéter ; git ne suffit pas, un document terminé garde un bandeau et le
  CHANGELOG dit où lire le détail ; pas de nom maison à la racine ; un
  bandeau de statut en tête de chaque document. Ils sont repris dans ce
  plan, et vont dans le `dev/decisions.md` de card.
- **Aucune valeur dérivée dans un tableau d'inventaire** (constaté le
  2026-08-04 : une colonne « lignes » avait dérivé sur chacune de ses
  lignes en deux semaines). Repris ici ; va dans `dev/decisions.md` de
  card.
- **Le cadrage des métadonnées à placeholder** (phase 4, précisé par
  l'utilisateur le 2026-07-21) : la forme par défaut est voulue
  générique, le suffixe est ce qui la précise, et « target horizon » n'est
  pas un bug. C'est une décision de fond du corpus : va dans le
  `dev/decisions.md` de card.
- **Les exemples de README exécutés, jamais seulement écrits**, et le
  parcours « pourquoi, quoi, comment » : va dans le `dev/decisions.md` de
  chaque dépôt qui a un README d'usage.

## Les correspondances

Proposées ; la phase A de chaque dépôt les confirme ou les corrige. La date
d'un plan est celle de la création du fichier
(`git log --follow --diff-filter=A`), relevée le 2026-11-06.

### card-api

```
docs/dev/CHANTIERS.md                        ROADMAP.md
docs/dev/API.md                              dev/decisions.md
docs/dev/PLAN_CACHE.md                       dev/plans/2026-09-18_cache.md            terminé
docs/dev/PLAN_CACHE_SUITE.md                 dev/plans/2026-09-19_cache-followup.md   en cours (B3)
docs/dev/PLAN_FAIR.md                        dev/plans/2026-07-24_fair.md             terminé ; phase 4 au ROADMAP
docs/dev/THEME_DOCS.md                       dev/docs-theme.md
docs/dev/audits/2026-10-11_…complexity.md    dev/audits/ (même nom)
INSTALL.md                                   reste à la racine
CLAUDE.md, bloc « Structure »                allégé ; ses arbitrages vers dev/decisions.md
```

Le `CLAUDE.md` de card-api pèse le plus lourd des quatre et raconte
encore l'histoire dans son bloc « Structure ». Son allègement est la suite
« Alléger la prose » de l'audit du 2026-10-11, faite dans la phase D.

**Phase A, faite le 2026-11-06.** Ce que chaque fichier est seul à porter :

- `API.md` : les arbitrages datés de la conception (accès en trois
  étages, une représentation par URL, provenance et nom du CSV, nom des
  colonnes, chronique servie, station muette, fraîcheur, chronique
  entière). Devient `dev/decisions.md`, qui reçoit aussi ce que le
  `CLAUDE.md` est seul à dire (plus bas).
- Les trois plans, l'audit et `THEME_DOCS.md` : se déplacent intacts.
- `CHANTIERS.md` : ses pistes ouvertes vont au ROADMAP. Son paragraphe
  « ce qui a quitté ce fichier le 2026-07-29 » est de l'histoire, sauf une
  décision : **le déploiement depuis le CI est écarté** (`make update`
  reste un geste conscient). Le paragraphe la dit « consignée dans
  `CLAUDE.md` », **elle n'y est pas, ni nulle part ailleurs** : elle va
  dans `dev/decisions.md`.
- `CLAUDE.md` : son bloc « Structure » redit, vérifié point par point, les
  docstrings de module de `cache.py`, `pool.py`, `pipeline.py`, `keys.py`,
  `usage.py` et `jobs.py`, les commentaires de `stats.py`, de `conftest.py`
  et du `Makefile`, et `API.md`. Il est seul, ou seul avec le CHANGELOG,
  à porter : la sauvegarde du volume écartée (nulle part ailleurs) ;
  l'absence de dépôt Zenodo, choix de l'utilisateur ; le durcissement des
  clés non rétroactif ; l'engagement des versions à partir de la première
  clé (`FINGERPRINT_VERSION`, renommage de colonne) ; la validation des
  mentions légales par INRAE, qui est une tâche ouverte ; et ses sections
  de règles (service, versions, « À NE JAMAIS FAIRE »).

Périmé ou contradictoire, à corriger en phase D :

1. `API.md`, section fraîcheur : une demande mal routée « bloquait tous
   ceux qui attendaient derrière le sémaphore ». Faux : depuis
   `pipeline.py` (2026-07-29) les téléchargements se font avant de le
   prendre. Même phrase dans `PLAN_CACHE.md` (A1) et dans une docstring
   de `tests/test_jobs.py`.
2. `API.md`, déploiement : « card et stase à révision épinglée, API x.y =
   card @tag + stase @tag ». Contredit par la règle en vigueur : la
   production suit `main`, et c'est le commit résolu qui trace.
3. `API.md`, carte de l'écosystème du 2026-07-16 : trois dépôts (card4r
   manque), « NOUVEAU repo », systemd, Skosmos, « chantier §4 ».
4. `API.md`, arbitrage 4 : « quota IP bas », démenti par sa propre revue
   du 2026-07-29.
5. `main.py`, docstring de module : « Conception : docs/dev/API.md du
   repo card ». C'est celui de card-api.
6. `CLAUDE.md` : « 343 fiches sur 472 », deux décomptes qui dérivent.

**Fait le 2026-11-06**, choix de l'utilisateur : allègement franc du
`CLAUDE.md` (une ligne par module, règles intactes, 27 à 9 Ko) ;
`THEME_DOCS.md` gardé à part ; la note sur les clés non rétroactives va
dans `dev/decisions.md` avec la condition qui la rend sans objet ;
décisions 6 et 7 appliquées. Les six points ci-dessus sont corrigés, et
un septième trouvé en route : `cache.py` portait aussi la phrase du
sémaphore. `docs/` a disparu, il ne contenait que `dev/`.

**Laissé pour la migration de card**, qui doit re-router ces renvois
depuis card-api : `src/card_api/main.py` cite `docs/dev/TOPICS.md` de
card, `dev/plans/2026-09-18_cache.md` cite son `docs/dev/ORIGINE_R.md`, et
`dev/plans/2026-07-24_fair.md` son registre de chantiers.

### stase

```
docs/dev/CHANTIERS.md                        ROADMAP.md
docs/dev/ORIGINE_R.md                        dev/r-origin.md
docs/dev/RENAMING_PY.md                      dev/renaming.md
docs/dev/archive/PLAN.md                     dev/plans/2026-07-12_audit-and-fixes.md  terminé
docs/dev/archive/CONVERSION_R.md             dev/plans/2026-07-15_r-conversion.md     terminé
docs/dev/archive/harnais_R/                  dev/r-harness/
docs/img/                                    reste (figures du README)
```

### stase, fait le 2026-11-06

Correspondances appliquées telles que proposées. En plus : un
`dev/decisions.md` est créé pour les cinq règles du 2026-07-12 et la
séparation d'avec les dépôts R, que le `CLAUDE.md` portait avec leurs
raisons ; il n'en garde qu'une ligne par règle (10,6 à 8 Ko). Retirés du
`CLAUDE.md` : les versions de pandas et de numpy du venv (recopiées, elles
dérivent) et la règle de remontée de `stase>=` dite deux fois. Le corps
du plan d'audit du 2026-07-12 garde les chemins de son époque, comme son
bandeau l'annonce. Les deux renvois de `docs/dev/RENAMING.md` de card vers
stase sont corrigés. Le bloc « À NE JAMAIS FAIRE » de stase n'a pas la
règle des fichiers non suivis que portent card et card-api : question
pour la phase F.

### card4r

Pas de document de développement. Deux renvois à corriger : son
`CLAUDE.md` cite `../card/docs/dev/PLAN_R.md`, qui est en réalité dans
`archive/` (renvoi déjà cassé le 2026-11-06), et la procédure
`NETTOYAGE.md`. Tous deux visent des documents de card : card4r passe
donc après card, dont la phase C les re-route. Un `ROADMAP.md` seulement si quelque chose est ouvert.
`docs/` est le site pkgdown généré, il ne bouge pas.

### card

`docs/` est le site publié (mkdocs) ; `docs/dev/` en est exclu par
`exclude_docs`, entrée qui disparaît une fois le dossier sorti.

```
docs/dev/CHANTIERS.md                        ROADMAP.md (gros : ce qui est lourd part en plan)
docs/dev/NOMENCLATURE.md                     dev/nomenclature.md
docs/dev/TOPICS.md                           dev/topics.md
docs/dev/RENAMING.md                         dev/renaming.md
docs/dev/ORIGINE_R.md                        dev/r-origin.md
docs/dev/Oberlin_1994ITCEMAGREF_1-8_edit.md  dev/references/oberlin-1994.md, cité par dev/references.md
docs/dev/PLAN_PYPI.md                        dev/plans/2026-08-06_pypi-name.md        en cours (PEP 541)
docs/dev/PLAN_SITE_SKOS.md                   dev/plans/2026-08-11_site-skos.md        construit, publication en attente
docs/dev/PLAN_THESAURUS.md                   dev/plans/2026-08-14_thesaurus.md        forme close, publication en attente
docs/dev/PLAN_AUTOPORTANCE.md                dev/plans/2026-08-14_self-sufficiency.md arrêté, à implémenter
docs/dev/QUESTIONS_THEIA.md                  dev/theia-questions.md                   brouillon de courrier
docs/dev/RETOURS_SCHAPI.md                   dev/schapi-feedback.md                   brouillon de courrier
docs/dev/NETTOYAGE.md                        retraite en fin de campagne (décision 3)
docs/dev/archive/ROADMAP.md                  dev/plans/2026-07-12_r-to-python.md      terminé
docs/dev/archive/AUDIT_FICHES.md             dev/audits/2026-07-15_card-metadata.md
docs/dev/archive/PLAN_METHOD.md              dev/plans/2026-08-03_method-field.md     terminé
docs/dev/archive/PLAN_R.md                   dev/plans/2026-08-05_r-ecosystem.md      terminé
CLAUDE.md, règles datées                     la règle reste, la raison va dans dev/decisions.md
```

Déjà relevé pour la phase A : `tests/run_py_corpus.py` et
`tests/test_suffix.py` citent « CHANTIERS §10 » et « §9 », alors que le
registre a abandonné ses numéros de section en juillet. Ces renvois ne
mènent plus nulle part.

`PLAN_SITE_SKOS.md` est de loin le plus gros document des quatre dépôts.
Il porte seul l'audit des vocabulaires : la phase A de card doit décider
s'il reste un plan ou si cet audit devient un fichier à part.

### MAKAHO-next

Hors campagne : ce n'est pas encore un dépôt git. Il adoptera la structure
au chantier M1, en mettant à jour les renvois de son `CLAUDE.md` et de son
`PLAN.md`. Ses consignes de passation sont figées (décision 6).

## Bilan, phase F faite le 2026-11-06

**card, ce qui a différé de la table proposée.** `NETTOYAGE.md` n'a pas
été supprimé mais rangé comme plan terminé de la campagne de juillet
(`dev/plans/2026-07-21_cleanup.md`) : c'est la règle des plans terminés,
et rien ne s'y perd ; ce qu'il était seul à porter (principes du
2026-07-22, inventaires sans valeur dérivée, cadrage des placeholders,
README exécutés) est dans le nouveau `dev/decisions.md` de card.
`dev/references.md` n'a pas été créé : il n'aurait porté qu'une ligne, la
publication d'Oberlin, que `dev/nomenclature.md` cite déjà depuis
`dev/references/`. `PLAN_SITE_SKOS.md` est resté un seul plan : en sortir
l'audit des vocabulaires demandait de le relire en entier, pour un gain
de rangement seulement. Le `CLAUDE.md` de card n'a été allégé que de sa
carte des documents (28 à 26 Ko) : le reste est le format d'une fiche et
les règles de rédaction, de vraies consignes de travail. L'exclusion
`dev/` de `mkdocs.yml` est gardée, par prudence pour un dossier local.

**Les quatre côte à côte.** Même squelette partout où il a de quoi
porter : `README`, `ROADMAP` (card, stase, card-api ; card4r n'a rien
d'ouvert), `CHANGELOG`, `CLAUDE.md`, `CITATION.cff`, `dev/decisions.md`
et `dev/plans/` (card, stase, card-api), `dev/audits/` (card, card-api).
Aucun ancien chemin ne subsiste hors des documents figés, des entrées
historiques des CHANGELOG et des consignes de passation de MAKAHO-next ;
aucun lien Markdown relatif n'est cassé dans les quatre dépôts ; tests,
lint et construction du site passent.

**Les deux questions de la phase F, tranchées.** Les règles recopiées
dans les `CLAUDE.md` sont gardées, selon l'arbitrage du 2026-07-22 ; le
bloc « À NE JAMAIS FAIRE » est donc complété dans stase (la règle des
fichiers non suivis) et ajouté à card4r, et `bac/` y est ignoré comme
dans card et card-api. `NETTOYAGE.md` a pris sa retraite comme plan
terminé. card-api et stase renvoient désormais aux principes communs,
dans `dev/decisions.md` de card.

**Laissé à observer, hors campagne :**

- card4r n'a pas de `codemeta.json`, que les trois autres portent ;
- MAKAHO-next cite encore les anciens chemins dans son `CLAUDE.md`, son
  `PLAN.md` et `scripts/mesure_sampling.py` : à mettre à jour au chantier
  M1, avec le reste de son `PLAN.md` ;
- le bloc « Structure » du `CLAUDE.md` de card décrit longuement ses
  scripts, dont certains portent déjà leur raison dans leur docstring :
  un allègement possible, à juger à l'usage ;
- les pages PyPI déjà publiées de stase pointent vers l'ancien chemin de
  `ORIGINE_R.md` (décision 7).

