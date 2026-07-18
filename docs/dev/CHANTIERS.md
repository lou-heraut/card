# CHANTIERS — pistes ouvertes (mise à jour 2026-07-18)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

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
