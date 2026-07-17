# CHANTIERS — pistes ouvertes (mise à jour 2026-07-17)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

## 1. card-api : suivi des jobs, identité et RGPD

Le service est réalisé et **déployé** (VM de l'utilisateur, derrière
l'Apache existant, 2026-07-17 ; conception : [API.md](API.md)).
Questions ouvertes issues du premier usage réel, à arbitrer :

- **Lister « mes jobs »**. Pas de liste publique des jobs (volontaire :
  sans comptes, une liste serait celle de tout le monde, tickets et
  résultats compris ; et les paramètres d'un job sont de l'activité de
  recherche d'autrui). Mais les porteurs de clé de priorité ONT une
  identité : un `GET /v1/jobs?key=...` listant les jobs déposés avec
  cette clé serait cohérent et petit. À faire si le besoin se confirme.
- **Reprise anonyme par ticket : risque réel ?** Quiconque a le ticket
  peut lire le résultat. Les données dérivées sont publiques
  (Hub'Eau) : l'enjeu n'est pas la donnée mais l'activité (qui étudie
  quoi). Ticket = `secrets.token_hex(4)`, 32 bits : énumération
  impraticable sous quota, mais passer à `token_hex(8)` ne coûterait
  rien si on veut fermer le sujet. Verdict provisoire : risque faible,
  à re-trancher explicitement.
- **RGPD des clés nominatives.** `keys.json` stocke nom/labo ; le
  journal enregistre le NOM de la clé à chaque requête : c'est un
  suivi d'activité nominatif, contrairement au public (IP hachées
  salées). À traiter avant d'attribuer des clés à des tiers :
  mention d'information dans le template d'issue (finalité, durée),
  durée de rétention du journal, pseudonymisation possible
  (journaliser le préfixe du jeton plutôt que le nom), effacement à
  la révocation. `make stats` (télémétrie d'exploitation agrégée)
  reste côté admin, c'est sa place.

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
