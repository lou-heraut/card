# CLAUDE.md : card

## Contexte

`card` est le package Python du recueil de fiches hydroclimatiques
CARD : chaque fiche YAML décrit comment extraire une variable (débit,
précipitation, température...) de séries journalières. Exécution par le
moteur [`stase`](../../EXstat_project/stase/). Ports Python des
packages R `CARD`/`EXstat` ; les repos R (`../CARD-R/`,
`EXstat_project/EXstat/`) sont en maintenance, référence de validation
uniquement, sans fichiers IA. Port validé R↔Python sur corpus complet
(552 comparaisons, tol 1e-6).

Où lire quoi. Un rôle par fichier, chacun l'annonce dans un bandeau de
statut en tête ; ne jamais recopier d'un fichier à l'autre, renvoyer.
- `CHANGELOG.md` (racine) : ce qui a changé, quand, et où lire le détail.
- docs/dev/, normes en vigueur : `NOMENCLATURE.md` (nommage, règles
  R1-R7, Oberlin), `TOPICS.md` (classification à facettes),
  `RENAMING.md` (noms R vers Python, et sorties modifiées
  volontairement), `ORIGINE_R.md` (origine, validation croisée,
  divergences assumées).
- docs/dev/`CHANTIERS.md` : pistes ouvertes seulement.
- docs/dev/archive/ : documents d'époque, non maintenus (`ROADMAP.md`,
  `AUDIT_FICHES.md`).

## Structure

```
src/card/
  cards/<domain>/<output>/   # 237 fiches : flow|precipitation|temperature|
                             #   evapotranspiration / series|scalar|curve ;
                             #   le linter impose chemin == classification
  functions/     # fonctions hydro portées de R
  loader.py      # YAML -> processus ($Hx, tuples func, défauts)
  extraction.py  # card.extract -> {data, meta} (chaîne P1..Pn via stase)
  suffix.py      # suffixes de scénario : vocabulaire {clé: enregistrement},
                 #   placeholders {suffix.<champ>}, défauts de fiche
  trend.py       # card.trend : stase.trend fiche-conscient (refus explicite
                 #   des fiches non `output: series` ; traduit les fiches en
                 #   relative={variable: bool}, dérive suffix= de meta)
  management.py  # list_cards (filtres par facette), info, copy_cards
  schema.py      # linter : python -m card.schema
  topics.yaml    # vocabulaire de contrôle de la classification (en/fr)
  inputs.yaml    # unités/définitions des variables d'entrée (invariants)
tests/           # pytest 76 tests (goldens R, loader, lint, suffixes, UX)
scripts/generate_catalog.py   # docs/CARDS.md, relancer après toute modif
```

Env : venv `.python_env/` ; `tests/conftest.py` rend card+stase
importables. Vérifs après toute modif de fiche : `pytest`,
`python -m card.schema`, régénérer le catalogue.

## Format d'une fiche

```yaml
id: QA                      # = nom de fichier ; grammaire NOMENCLATURE.md
version: "2.0"              # bump majeur si les SORTIES changent,
                            # mineur si method/description, patch sinon
authors: ["Louis Héraut (INRAE, UR RiverLy)"]
date: "2026-04-30"

meta:
  en:
    variable: QA            # listes si plusieurs sorties distinctes
    unit: "m^{3}.s^{-1}"
    name: Annual mean daily discharge
    description: ""         # remplir seulement si + d'info que le name
    method: "1. annual aggregation [09-01, 08-31] - mean"
    sampling_period: ["09-01", "08-31"]     # MM-DD en en, DD-MM en fr
    classification:         # labels MINUSCULES, validés contre topics.yaml
      domain: flow          #   (liste si plusieurs grandeurs)
      phenomenon: mean flows  # scalaire/liste/absent, jamais forcé
      aspect: magnitude     # IHA ; interdit si purpose présent
      season: annual        # annual|summer|winter|by season|by month|record
      output: series        # series|scalar|curve, doit matcher le dossier
      # purpose: model performance | climate sensitivity (optionnel)
  fr:
    ...                     # mêmes champs, labels français appariés
  global:                   # zone neutre non traduite
    input_vars: Q           # doit exister dans inputs.yaml
    preferred_sampling_period: "09-01"
    palette: [...]

process:
  P1:
    func:
      QA: [nanmean, "Q"]    # [fonction, *colonnes, kwargs?, is_date?]
    sampling_period: "09-01"
    max_na_pct: 3
    max_na_years: 10
```

Règles clés (détail : NOMENCLATURE.md) :
- **func** : résolution card.functions puis numpy (nanmean, nanargmax,
  delta, return_level, apply_threshold...) ; kwarg dont la valeur est
  une variable amont ({lim: upLim}) résolu dynamiquement ; littéraux
  positionnels permis ; `true` final = is_date.
- **sampling_period adaptatif** : `{type: adaptive, func: [nanmax, "Q"]}`.
  Convention PAR PHÉNOMÈNE (linter) : low flows = nanmax + preferred
  01-01 ; high flows = nanmin + preferred 09-01 ; toute fiche adaptative
  doit déclarer un preferred_sampling_period. À l'exécution,
  `card.extract(..., sampling_period="preferred"|"MM-DD")` écrase les
  fenêtres ANNUELLES (protocole MAKAHO = "preferred") ; les fenêtres
  partielles [début, fin] font partie de la définition, jamais écrasées.
- **horizons** : déclarés dans meta.global.horizons, référencés `$H0..$H3`.
- **défauts à omettre** : dans meta.global, is_date false, relative true,
  is_experimental false, source/palette/preferred null, input_vars "X" ;
  dans process, time_step "year", sampling_period/period/max_na_* null,
  seasons [DJF,MAM,JJA,SON], keep null, compress/expand false. Exception :
  un kwarg explicite dans la source reste explicite.
- **multi-sorties** : métadonnées en listes si les sorties sont des
  variables distinctes ; name UNIQUE si ce sont les coordonnées d'un même
  objet (FDC_p/FDC_Q = une courbe).
- La moyenne intra-pas-de-temps est implicite ; « inter-annuel(le) »
  toujours explicite pour mean-/median-. Quantiles temporels : « dépassé
  p % du temps », jamais « X années sur Y ».

> ## À NE JAMAIS FAIRE
>
> - **`note.txt` (et tout fichier de notes de l'utilisateur) : NE PAS
>   L'OUVRIR.** Ni Read, ni `cat`, ni `grep`, ni au détour d'un `git add`.
>   C'est son brouillon personnel : pas de lecture, pas de résumé, pas de
>   « au passage j'ai vu que ». Il n'entre dans aucune tâche sans une
>   demande explicite de sa part, fichier par fichier. Un en-tête qui dit
>   de ne pas lire est un ordre, pas une mise en garde à évaluer.
> - **Pas de `git add -A` ni de `git add .`** : stager nommément les
>   fichiers que l'on a soi-même modifiés. Ce qui traîne dans l'arbre de
>   travail appartient à l'utilisateur.

## Règles de travail

- Lire la fiche complète avant modification ; la fonction fait foi (les
  métadonnées décrivent le calcul réel).
- Modifications de masse par batch (~10), récap avec niveau de confiance,
  attendre le go. Corrections auto uniquement à confiance élevée
  (grammaire, casse, cohérence) ; réécriture scientifique = validation.
- Noms de fonctions/paramètres : RENAMING.md fait foi, tout nouveau
  renommage validé par l'utilisateur.
- **Deux versions à ne pas confondre.**
  - Celle d'une **fiche** (champ `version:` de son YAML) : majeur si ses
    SORTIES changent (+ trace RENAMING.md, parité R rompue documentée,
    goldens re-figés), mineur pour method/description, patch sinon. Elle
    part dans les métadonnées de sortie : un résultat dit avec quelle
    définition il a été calculé.
  - Celle du **paquet** (`pyproject.toml`) : on n'y touche pas au
    quotidien, elle ne sert qu'à publier. Le service suit `main` et
    identifie ce qu'il exécute par le commit, pas par ce numéro.
  **Le seul geste à ne pas oublier** : écrire l'entrée `## Non publié`
  du CHANGELOG quand un changement mérite d'être retenu. Le proposer
  soi-même, l'utilisateur ne le demandera pas.
- Pas de PDF ni de `*~` sous git.
- Pas de tiret quadratin (—) dans la prose (docs, messages, commentaires,
  réponses) : reformuler (deux points, parenthèses, phrases séparées).
  Perçu comme un marqueur de texte IA, rebute des utilisateurices.

## État (2026-07-22)

Tout est commité et poussé sur card et sur `../../EXstat_project/stase/`,
qui va de pair. Corpus = 237 fiches, 482 variables, 76 tests verts.

Ce qui a été livré et quand se lit dans `CHANGELOG.md`, ce qui reste
ouvert dans `docs/dev/CHANTIERS.md`. Ces deux fichiers font foi : ne pas
les paraphraser ici, cette section ne doit pas regonfler à chaque
chantier.

Deux acquis récents à ne pas reperdre, parce qu'ils changent la façon
d'écrire une fiche :
- **suffixes de scénario** : le fan-out des valeurs est fait par stase au
  niveau colonne, card n'ajoute que les métadonnées, donc aucun
  placeholder ne peut changer un calcul. Une variable suffixée est une
  autre variable, donc une autre ligne de `meta` et une colonne
  `suffix`. Conception : docstring de `src/card/suffix.py`.
- **paramètres externes en colonnes d'entrée** : seuils réglementaires et
  bornes d'horizon arrivent comme des colonnes (rôle `param_cols` côté
  stase), une fiche ne fige plus ni un seuil ni une date. Conception :
  docstring de l'extraction de stase.

Écosystème : le service web vit dans le dépôt séparé `../card-api/`, qui
a son propre CLAUDE.md, ses chantiers et son état de déploiement. Ne rien
en consigner ici, et réciproquement.

En attente de l'utilisateur, côté card seulement : demande PEP 541 pour
le nom PyPI, et signalement amont des 11 fiches cassées du paquet R
(détail des deux dans CHANTIERS).
