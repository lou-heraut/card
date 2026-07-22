# Plan de nettoyage / uniformisation : card, stase, card-api

Grand nettoyage transverse aux 3 packages : docs de dev, docs
d'utilisation (README), pages web, métadonnées à placeholder, et surtout
**cloisonnement** (chaque info à un seul endroit) pour réduire le coût
token du re-chargement de contexte des futurs Claude.

Établi le 2026-07-21, **appliqué à card le 2026-07-22** (phases 0 et 1).
À supprimer une fois déroulé sur les trois dépôts.

## Principes directeurs

1. **Une info, un seul endroit (source de vérité).** Les autres fichiers
   RENVOIENT, ne recopient pas. Toute duplication est un futur mensonge.
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

## Structure cible, identique dans les trois dépôts

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

## Carte « fichier -> rôle exclusif » (Phase 0 faite le 2026-07-22)

Statuts : **SOURCE** (seul endroit qui définit l'info), **RENVOI** (ne
fait que pointer), **GÉNÉRÉ** (produit par un script, ne pas éditer),
**HISTORIQUE** (trace datée, non maintenue), **RÉFÉRENCE** (document
externe), **TEMPORAIRE** (disparaît une fois exécuté).

### card

| fichier | lignes | rôle exclusif | statut |
|---|---|---|---|
| README.md | 165 | vitrine et parcours d'usage : installer, extraire, suffixes, tendance, écrire sa fiche | SOURCE |
| CLAUDE.md | 177 | contexte de session : format d'une fiche, règles de travail, état court | SOURCE |
| docs/index.md | 15 | landing Pages : renvoi vers catalogue et dépôt | RENVOI |
| docs/CARDS.md | 282 | catalogue, une ligne par fiche | GÉNÉRÉ |
| docs/dev/NOMENCLATURE.md | 250 | grammaire des noms de variables et rédaction des métadonnées (R1 à R7, Oberlin) | SOURCE |
| docs/dev/TOPICS.md | 233 | classification à facettes : modèle, vocabulaire, arbitrages | SOURCE |
| docs/dev/RENAMING.md | 288 | journal daté des renommages et des changements de SORTIES (parité R rompue) | SOURCE |
| docs/dev/CHANTIERS.md | 243 | registre des pistes ouvertes du corpus | SOURCE |
| docs/dev/VALIDATION_R.md | 56 | origine R du corpus, validation croisée, divergences propres aux FICHES | SOURCE (mal nommé, cf. Phase 6) |
| docs/dev/AUDIT_FICHES.md | 271 | constats et décisions de l'audit appliqué le 2026-07-15 | HISTORIQUE |
| docs/dev/ROADMAP.md | 133 | phases A à D de la refonte, plus deux blocs vivants (« Principes actés », plan PEP 541) | HISTORIQUE + à ré-héberger |
| docs/dev/PLAN_nettoyage.md | 183 | ce plan | TEMPORAIRE |
| docs/dev/Oberlin_1994...edit.md | 688 | source scientifique du système de nommage (OCR) | RÉFÉRENCE |

### stase

| fichier | lignes | rôle exclusif | statut |
|---|---|---|---|
| README.md | 107 | vitrine et usage du moteur | SOURCE |
| CLAUDE.md | 116 | contexte de session : structure, règles (tools.py gelé, détection par type), API | SOURCE |
| docs/dev/ORIGINE_R.md | 106 | origine R du moteur, validation, divergences intentionnelles du MOTEUR | SOURCE |
| docs/dev/RENAMING_PY.md | 64 | renommages de paramètres et de colonnes de sortie de stase | SOURCE |
| docs/dev/CONVERSION_R.md | 508 | ancien CLAUDE.md d'EXstat_Claude, trace de la conversion | HISTORIQUE |
| docs/dev/PLAN.md | 349 | audit du 2026-07-12 et son plan, clôturé | HISTORIQUE |

### card-api

| fichier | lignes | rôle exclusif | statut |
|---|---|---|---|
| README.md | 235 | vitrine du service : endpoints, cas d'usage Python puis R, quotas | SOURCE |
| INSTALL.md | 168 | développement et déploiement (Docker, Apache, variables d'env) | SOURCE |
| CLAUDE.md | 102 | contexte de session | SOURCE |
| docs/dev/API.md | 173 | conception du service, et §1 = carte de l'écosystème à trois repos | SOURCE |
| docs/dev/CHANTIERS.md | 67 | registre des pistes ouvertes du service | SOURCE |

### Redondances et affirmations périmées (vérifiées dans le code le 2026-07-22)

1. **`dataEX`/`metaEX` présentés comme alias vivants** (card RENAMING
   « Clés de retour », stase RENAMING_PY, card-api API.md §2) alors
   qu'ils ont été purgés : `card.extract` ne renvoie que `data`/`meta`.
2. **`meta=` de `process_trend` présenté comme le canal du caractère
   relatif** (card RENAMING, stase RENAMING_PY) alors qu'il a été retiré
   en stase 0.4.0 au profit de `relative={variable: bool}`.
3. **Le nombre de fiches est recopié dans trois docs vivantes**
   (card docs/index.md « 226 fiches, 588 variables », card-api README
   « 226 fiches », stase README « 226 fiches ») alors que la source est
   le catalogue généré (237 fiches, 482 variables).
4. **Alias R de l'API card documentés deux fois** : card RENAMING
   « Fonctions (alias R conservés) » et VALIDATION_R « Noms hérités ».
5. **Divergence du rolling à fenêtre paire** expliquée dans VALIDATION_R
   puis redémontrée au long dans CHANTIERS §10 (résolu).
6. **CHANTIERS (card) contredit sa propre règle d'en-tête** (« un
   chantier terminé sort de ce fichier ») : trois blocs « Sorti le... »
   et un §10 RÉSOLU de 70 lignes.
7. **Renvoi croisé vers un doc candidat au retrait** : stase CLAUDE.md
   pointe card `docs/dev/ROADMAP.md` pour « la refonte commune ».

Rappel de cadrage, **métadonnées génériques par défaut (VOULU, pas un
trou)** : sans suffixe, les fiches rendent « the target horizon »
(défaut générique), métadonnée publique de `metadata_only`,
volontairement générale ; le suffixe la clarifie avec le contexte.
Cf. Phase 4 : vérifier la cohérence, pas figer du contexte.

## Phase 0 : inventaire et carte des redondances (FAITE le 2026-07-22)

Carte ci-dessus, 24 fichiers, 7 redondances relevées et vérifiées dans le
code. À refaire à l'identique pour stase et card-api si la carte y est
jugée insuffisante (elle a été établie sur les 3 dépôts d'un coup).

## Phase 1 : ranger l'historique (FAITE pour card le 2026-07-22)

Recette appliquée, à rejouer telle quelle sur stase et card-api :

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

Pour card : `ROADMAP.md` et `AUDIT_FICHES.md` archivés, `VALIDATION_R.md`
renommé `ORIGINE_R.md` (même rôle que dans stase), CHANTIERS ramené aux
pistes ouvertes et numéros de section abandonnés (un numéro ne se cite
pas durablement dans un registre qui bouge).

Restent à traiter : stase (`CONVERSION_R.md` reste en archive, il est
déjà badgé ; `PLAN.md` à archiver, et corriger stase CLAUDE.md l. 43 qui
le dit « suivi à jour » alors qu'il est clôturé, et l. 53 qui s'appuie
dessus pour justifier les exceptions au gel de `tools.py` : renvoyer aux
tests d'équivalence) et card-api.

## Phase 2 — CLAUDE.md et mémoire (budget token)

- Les 3 CLAUDE.md : garder l'essentiel non dérivable (format, règles de
  travail, état COURT). Sortir tout ce qui est détaillé dans docs/dev en
  RENVOI. La section « État » de card CLAUDE gonfle à chaque chantier :
  la réduire à un pointeur (dernier chantier + lien CHANTIERS/git).
- Uniformiser la structure des 3 CLAUDE.md (mêmes sections : Contexte,
  Structure, Règles, État, renvois).
- Mémoire (`~/.claude/.../memory/`) : élaguer les entrées obsolètes
  (project-state.md date du 2026-07-16, très en retard sur le code).

## Phase 3 — README utilisateur (donner envie)

Pour chacun des 3 README, parcours « pourquoi -> quoi -> comment », UN
exemple exécuté par capacité :
- **card** : extract (une fiche), plusieurs fiches, suffix (multi-seuils
  DOE/DCR et obs/sim), horizons en colonnes (le nouveau), trend, dev de
  sa propre fiche (copy_cards -> schema).
- **stase** : process_extraction (agrégation), sampling adaptatif,
  param_cols (covariables), process_trend.
- **card-api** : table des endpoints, exemples curl/Python/R, jobs, clé
  de priorité.
- Vérifier chaque exemple par EXÉCUTION (motif scratchpad apitest déjà
  utilisé pour card-api).

## Phase 4 — Métadonnées à placeholder (cohérence, PAS un « trou »)

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

Statut 2026-07-21 : cohérence déjà VÉRIFIÉE. Exemples rendus sur
delta-QA_H (générique « the target/cible horizon » cohérent ; clés nues
« the H1 horizon » un peu sèches mais valides ; records riches
« the near-future (2021-2050) horizon » informatifs). Scan des 62 fiches
à placeholder = 0 anomalie (aucune accolade résiduelle, aucun mot
double). Reste surtout l'avis utilisateur sur le terme générique et la
doc d'usage.

Le travail n'est donc pas de figer du contexte dans la fiche, mais de
VÉRIFIER la cohérence :
- Fournir à l'utilisateur des EXEMPLES rendus (forme générique par défaut
  vs avec records riches near/2021-2050) pour qu'il juge — il ne les a
  pas encore lus. Un éventuel `suffixes:` par défaut ne se déciderait que
  SI les exemples montraient le générique incohérent, pas par principe.
- Vérifier que CHAQUE `{suffix.X}` forme une phrase cohérente EN et FR,
  autant en générique qu'avec records (script : rendre les métadonnées
  de toutes les fiches à placeholder, relire).
- Vérifier que `suffix_default` (short/name) donne un générique qui se
  LIT bien (« target/cible » convient-il, ou un terme plus naturel ?).
- Documenter côté utilisateur : comment et quand fournir des records
  riches (horizons fixes DRIAS vs par degré de réchauffement).

## Phase 5 — Pages web / publication

- card `docs/index.md` (15 lignes, stub) : décider son rôle (landing ?
  renvoi vers CARDS.md + README + SKOS). Étoffer ou assumer minimal.
- SKOS/thésaurus (CHANTIERS §6) : lien depuis la landing si concrétisé.
- card-api : vérifier que la doc API (README + API.md) reflète l'état
  déployé.

## Phase 6 — Uniformisation inter-packages

- Conventions communes aux 3 repos : structure `docs/dev/`, format
  CLAUDE.md, structure README, style des renvois croisés
  (card <-> stase <-> card-api), en-têtes de licence.
- Un « index » léger par repo : quel fichier pour quelle question.

## Checklist

Phase 0 :
- [x] carte « fichier -> rôle exclusif » des 3 repos, redondances repérées.

Phase 1 :
- [x] **card** : CHANGELOG écrit, ROADMAP et AUDIT_FICHES archivés,
      VALIDATION_R renommé ORIGINE_R, CHANTIERS purgé, bandeaux de
      statut posés, renvois re-routés.
- [ ] **stase** : CHANGELOG (0.1 à 0.4.0, jamais écrit), PLAN archivé,
      CONVERSION_R laissé en archive, renvois de CLAUDE.md corrigés.
- [ ] **card-api** : CHANGELOG, tri de API.md (conception durable contre
      ébauche datée), renvois.

Phase 2 :
- [x] card CLAUDE.md : État réduit à un pointeur vers CHANGELOG et
      CHANTIERS, déploiement de card-api renvoyé chez lui.
- [ ] stase et card-api CLAUDE.md élagués et uniformisés.
- [ ] mémoire élaguée (project-state.md date du 2026-07-16, très en
      retard sur le code).

Phase 3 :
- [ ] README card/stase/card-api : un exemple exécuté par capacité.

Phase 4 :
- [ ] exemples rendus (générique vs records) fournis à l'utilisateur.
- [ ] toutes les phrases `{suffix.X}` cohérentes EN/FR (vérif scriptée).
- [ ] `suffix_default` relu (le générique se lit bien).

Phase 5 :
- [ ] rôle de docs/index.md tranché ; doc API à jour.

Phase 6 :
- [ ] conventions communes appliquées ; renvois croisés cohérents.

## Ordre conseillé

0 (carte) puis 1 (ranger l'historique) sur les trois dépôts, puis 4
(métadonnées, tant que le chantier horizon est frais), puis 3 (README),
2 (CLAUDE et mémoire), 5, 6.
