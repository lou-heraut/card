# API — architecture de l'écosystème et ébauche du service

> Réflexion du 2026-07-16, à arbitrer. L'aspect commercial est écarté
> (décision utilisateur : les statistiques d'usage valent plus, comme
> preuve d'impact pour les financements, que des recettes de niche) —
> le service sera ouvert, avec clés et quotas pour la robustesse et
> les statistiques, pas pour la facturation.

## 1. Où ranger quoi — la carte de l'écosystème

Principe : **card reste une bibliothèque de calcul pure** (installable,
légère, sans dépendance service). Tout ce qui est *service* (réseau,
cache, clés, déploiement) vit dans un repo séparé, comme stase et card
sont déjà séparés par nature (moteur / fiches).

```
stase        moteur d'extraction/stationnarité         (repo existant)
  ▲
card         fiches + classification + fonctions hydro (repo existant)
  │            ├─ scripts/generate_catalog.py → docs/CARDS.md   (Pages)
  │            └─ scripts/generate_skos.py    → docs/card.ttl   (Pages, chantier §4)
  ▼
card-api     service web FastAPI                       (NOUVEAU repo, VM)
               ├─ hubeau.py    client Hub'Eau + cache des chroniques
               ├─ main.py      endpoints v1
               ├─ auth/quotas  clés d'API (statistiques d'usage)
               └─ Dockerfile / systemd (déploiement VM)

Skosmos      navigateur de thésaurus (VM, optionnel)   lit docs/card.ttl
```

Pourquoi un repo séparé (`card-api`, nom de travail) :
- cycles de vie différents (une fiche corrigée ≠ un redéploiement ;
  une évolution d'endpoint ≠ une release card) ;
- dépendances contenues : card garde numpy/pandas/yaml ; l'API ajoute
  fastapi/uvicorn/httpx sans alourdir les utilisateurs de la
  bibliothèque ;
- le déploiement (Docker, secrets, logs) ne pollue pas le package
  scientifique ;
- même logique de frontière que stase/card : la donnée nationale et le
  réseau sont un métier, le calcul en est un autre.

## 2. Ébauche de l'API v1

Toutes les réponses JSON portent `card_version`, `stase_version` et la
`version` de chaque fiche utilisée (discipline de versions en place).
Préfixe `/v1` dès le départ.

### Découverte

- `GET /v1/cards` — le catalogue (metaEX). Filtres = les facettes de
  la classification, dans les deux langues, identiques à
  `card.list_cards()` : `?phenomenon=basses eaux&output=série`,
  `&operator=delta`, `&function=baseflow`, `&search=étiage`, `&lang=`.
- `GET /v1/cards/{id}` — détail d'une fiche (info + lien vers le YAML
  source sur GitHub).
- `GET /v1/stations?dept=07&river=Ardèche&bbox=...` — recherche de
  stations (proxy du référentiel Hub'Eau) pour ne pas obliger à
  connaître les codes à l'avance.

### Calcul

- `GET /v1/extract?station=H5920010&cards=QA,VCN10&start=1970&end=2020`
  — télécharge la chronique journalière Hub'Eau
  (`hydrometrie/obs_elab`, QmnJ), exécute card, renvoie
  `{meta, metaEX, dataEX}` ; `&format=csv` possible.
- `POST /v1/extract` (corps = CSV/JSON d'une chronique fournie par
  l'utilisateur, taille plafonnée) — même calcul sur des données
  privées, rien n'est conservé côté serveur.
- `GET /v1/trend?station=...&cards=QA,VCN10&mk=INDE` — enchaîne
  extraction + `stase.trend` (Mann-Kendall/Sen) : le service rend le
  diagnostic de stationnarité complet, à la MAKAHO.

### Infrastructure

- **Clés d'API** gratuites (auto-service ou sur demande), quota par
  clé (protège la VM et Hub'Eau), en-tête `X-API-Key`.
- **Journal d'usage** : (clé, endpoint, station, fiches, date) →
  la matière première des bilans d'impact pour les dossiers de
  financement.
- **Cache à deux étages** : chroniques par station (TTL quotidien —
  les séries validées bougent peu) ; résultats d'extraction par
  (station, fiche, version de fiche) — l'invalidation est offerte par
  la discipline de versions.
- Respecter la politique de débit Hub'Eau (taille de page, pauses) ;
  bannière de provenance des données (Licence Ouverte, eaufrance).

## 3. Étapes proposées

1. Squelette card-api : FastAPI + `GET /v1/cards` (zéro réseau, juste
   card) — déployable immédiatement, valide la chaîne VM.
2. Client Hub'Eau + cache + `GET /v1/extract` sur quelques fiches.
3. Clés/quotas/journal, puis `POST /v1/extract` et `/v1/trend`.
4. Page de doc auto (OpenAPI/Swagger, gratuite avec FastAPI) liée
   depuis les Pages card.

## 4. Articulation avec l'export SKOS

Le SKOS n'est **pas** un service : c'est un artefact de publication de
la classification, qui vit dans card (source de vérité :
`src/card/topics.yaml` + les blocs classification).

- `scripts/generate_skos.py` (chantier) : chaque facette devient un
  `skos:ConceptScheme` (domain, phenomenon, aspect, season, output,
  purpose) ; chaque valeur un `skos:Concept` avec `prefLabel` fr/en
  (les paires sont déjà dans topics.yaml) et `exactMatch`/`closeMatch`
  vers l'existant (aspect ↔ typologie IHA ; fiches climat ↔ ETCCDI) ;
  chaque fiche devient un concept rattaché à ses facettes
  (`dcterms:subject`).
- Publication statique : `docs/card.ttl` servi par GitHub Pages —
  aucun serveur nécessaire pour être moissonnable.
- URIs stables : demander un préfixe **w3id.org** (ex.
  `https://w3id.org/card-hydro/...`) qui redirige vers les Pages —
  gratuit, pérenne, indépendant de l'hébergement.
- Skosmos sur la VM = optionnel et purement cosmétique (navigation
  humaine dans le thésaurus) ; il lit le même `card.ttl`.
- L'API peut exposer `GET /v1/concepts` en renvoyant vers ces URIs —
  mais la vérité reste dans card.

## 5. À arbitrer

1. Nom du repo service : `card-api` (nom de travail) — autre idée ?
2. `POST /v1/extract` (données utilisateur) en v1 ou plus tard ?
3. `/v1/trend` en v1 (c'est la valeur MAKAHO) ou v1.1 ?
4. Clés d'API : auto-service (formulaire) ou attribution manuelle au
   début (plus simple, suffisant pour démarrer) ?
5. w3id.org pour les URIs SKOS : ok pour déposer la demande le moment
   venu ?
