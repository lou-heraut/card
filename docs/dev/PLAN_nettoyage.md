# Plan de nettoyage / uniformisation — card, stase, card-api

Grand nettoyage transverse aux 3 packages : docs de dev, docs
d'utilisation (README), pages web, métadonnées à placeholder, et surtout
**cloisonnement** (chaque info à un seul endroit) pour réduire le coût
token du re-chargement de contexte des futurs Claude.

Établi le 2026-07-21. Plan pour une session future ; à supprimer une fois
exécuté (historique dans git). Aucune exécution encore faite.

## Principes directeurs

1. **Une info, un seul endroit (source de vérité).** Les autres fichiers
   RENVOIENT, ne recopient pas. Toute duplication est un futur mensonge.
2. **Budget token.** Ce qui est chargé chaque session (les 3 CLAUDE.md,
   MEMORY.md) doit être concis, factuel, non dérivable du code, et
   pointer vers les docs détaillées plutôt que les inclure.
3. **Historique = git.** Un doc périmé/terminé s'archive ou se supprime ;
   on ne le garde pas « au cas où » dans l'arbre courant.
4. **Sobre et exécuté.** Docs utilisateur : parcours clair, exemples
   RÉELLEMENT exécutés, Python puis R en parallèle (cf. feedback style).

## État des lieux (survol 2026-07-21, à confirmer/compléter en Phase 0)

Docs de dev, tailles en lignes :
- card : RENAMING 288, AUDIT_FICHES 271, NOMENCLATURE 250, TOPICS 233,
  CHANTIERS 218, ROADMAP 133, VALIDATION_R 56, Oberlin_1994...edit 688
  (référence scientifique OCR), CARDS 282 (catalogue généré).
- stase : CONVERSION_R 508, PLAN 349, ORIGINE_R 106, RENAMING_PY 64.
- card-api : README 235, API 173, INSTALL 168, CLAUDE 102, CHANTIERS 67.
- CLAUDE.md : card 177, stase 116, card-api 102.

Problèmes repérés :
- **Périmé/historique (~990 lignes)** : stase CONVERSION_R (« archive,
  non maintenu »), stase PLAN (audit terminé), card ROADMAP (phases A-D
  terminées). Candidats archivage/suppression.
- **Divergences R↔Python éparpillées** : card RENAMING (changements de
  SORTIES de fiches), stase ORIGINE_R (divergences du MOTEUR), stase
  RENAMING_PY (renommages de paramètres), card VALIDATION_R (origine).
  Frontières à clarifier, renvois croisés à poser.
- **Métadonnées génériques par défaut (VOULU, pas un trou)** : sans
  suffixe, les fiches rendent « the target horizon » (défaut générique) =
  la métadonnée publique de `metadata_only`, volontairement générale ; le
  suffixe la clarifie avec le contexte. Cf. Phase 4 : vérifier la
  cohérence, pas figer du contexte.

## Phase 0 — Inventaire et carte des redondances

- Compléter la carte ci-dessus (rôle d'UNE phrase par fichier de doc des
  3 repos). Marquer : source de vérité | renvoi | périmé | à fusionner.
- Repérer toute info présente à ≥2 endroits (grep de termes clés :
  divergences R, quotas API, format de fiche, protocole MAKAHO...).
- Livrable : un tableau « fichier -> rôle exclusif » validé.

## Phase 1 — Élaguer l'historique (PROPREMENT, pas grossièrement)

Constat 2026-07-21 (survol) : les 3 candidats NE SONT PAS supprimables
tels quels. Piège important à retenir.
- Ils sont RÉFÉRENCÉS par des docs vivantes : card ROADMAP <- README (l.
  164), CLAUDE.md (l. 18), VALIDATION_R (l. 8), RENAMING (l. 3) ; stase
  PLAN <- README (l. 107), CLAUDE.md (l. 43/53, « suivi à jour », liens
  de tests) ; stase CONVERSION_R <- ORIGINE_R (l. 15), CLAUDE.md (l.
  22/115, « historique complet de la conversion »).
- Ils portent du contenu à valeur : ROADMAP a « Principes actés », PLAN
  a le rationnel + les liens vers les tests d'équivalence, CONVERSION_R
  est LA trace référencée de la conversion.

Donc Phase 0 (carte source-de-vérité) OBLIGATOIRE d'abord. Puis, par
doc, deux options PROPRES :
- le GARDER comme trace historique assumée (déjà marqué archive/terminé),
  simplement pas chargé en session ; ou
- le RETIRER seulement après avoir RE-ROUTÉ chaque référence vers la
  source de vérité actuelle et vérifié qu'aucune info unique n'est perdue.
Ne jamais supprimer un doc encore référencé sans corriger les renvois.

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
- [ ] carte « fichier -> rôle exclusif » des 3 repos, redondances repérées.

Phase 1 :
- [ ] archiver/supprimer CONVERSION_R, PLAN (stase), ROADMAP (card) ;
      corriger les renvois.

Phase 2 :
- [ ] CLAUDE.md × 3 élagués, uniformisés, État réduit à un pointeur.
- [ ] mémoire élaguée (project-state.md à jour ou remplacé).

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

0 (carte) -> 1 (élaguer, gain token immédiat) -> 4 (métadonnées, lié au
chantier qu'on vient de livrer) -> 3 (README) -> 2 (CLAUDE/mémoire) ->
5 -> 6. La Phase 4 peut se faire tôt tant que le chantier horizon est
frais.
