# CLAUDE.md — card

## Contexte

`card` est le package Python du recueil de fiches hydroclimatiques
CARD : chaque fiche YAML décrit comment extraire une variable (débit,
précipitation, température...) de séries journalières. Exécution par le
moteur [`stase`](../../EXstat_project/stase/). Ports Python des
packages R `CARD`/`EXstat` ; les repos R (`../CARD-R/`,
`EXstat_project/EXstat/`) sont en maintenance, référence de validation
uniquement, sans fichiers IA. Port validé R↔Python sur corpus complet
(552 comparaisons, tol 1e-6).

Docs de référence (docs/dev/) : `NOMENCLATURE.md` (nommage, règles
R1–R7, Oberlin), `TOPICS.md` (classification à facettes), `RENAMING.md`
(renommages R→Python + sorties modifiées volontairement),
`AUDIT_FICHES.md` (audit 2026-07 appliqué), `VALIDATION_R.md`,
`ROADMAP.md` (historique), `CHANTIERS.md` (pistes ouvertes).

## Structure

```
src/card/
  cards/<domain>/<output>/   # 237 fiches — flow|precipitation|temperature|
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
tests/           # pytest 78 tests (goldens R, loader, lint, suffixes, UX)
scripts/generate_catalog.py   # docs/CARDS.md — relancer après toute modif
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
      phenomenon: mean flows  # scalaire/liste/absent — jamais forcé
      aspect: magnitude     # IHA ; interdit si purpose présent
      season: annual        # annual|summer|winter|by season|by month|record
      output: series        # series|scalar|curve — doit matcher le dossier
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
- **défauts à omettre** : meta.global — is_date false, relative true,
  is_experimental false, source/palette/preferred null, input_vars "X" ;
  process — time_step "year", sampling_period/period/max_na_* null,
  seasons [DJF,MAM,JJA,SON], keep null, compress/expand false. Exception :
  un kwarg explicite dans la source reste explicite.
- **multi-sorties** : métadonnées en listes si les sorties sont des
  variables distinctes ; name UNIQUE si ce sont les coordonnées d'un même
  objet (FDC_p/FDC_Q = une courbe).
- La moyenne intra-pas-de-temps est implicite ; « inter-annuel(le) »
  toujours explicite pour mean-/median-. Quantiles temporels : « dépassé
  p % du temps », jamais « X années sur Y ».

## Règles de travail

- Lire la fiche complète avant modification ; la fonction fait foi (les
  métadonnées décrivent le calcul réel).
- Modifications de masse par batch (~10), récap avec niveau de confiance,
  attendre le go. Corrections auto uniquement à confiance élevée
  (grammaire, casse, cohérence) ; réécriture scientifique = validation.
- Noms de fonctions/paramètres : RENAMING.md fait foi, tout nouveau
  renommage validé par l'utilisateur.
- Changement de sorties = bump version majeur + trace RENAMING.md
  (parité R rompue documentée) + goldens re-figés.
- Pas de PDF ni de `*~` sous git.
- Pas de tiret quadratin (—) dans la prose (docs, messages, commentaires,
  réponses) : reformuler (deux points, parenthèses, phrases séparées).
  Perçu comme un marqueur de texte IA, rebute des utilisateurices.

## État (2026-07-21)

Tout est commité et poussé sur les deux dépôts (card et
`../../EXstat_project/stase/`, qui va de pair). Corpus = 237 fiches.

**Chantier du 2026-07-20 : suffixes de scénario et métadonnées
évolutives.** Une même fiche s'applique à plusieurs variantes d'une
entrée en un appel, `card.extract(..., suffix=["DOE","DCR"])` sur des
colonnes `Q_lim_DOE`/`Q_lim_DCR`, ou `obs`/`sim` sur n'importe quelle
fiche. Le fan-out des valeurs est fait par stase au niveau colonne ;
card n'ajoute que les métadonnées, si bien qu'aucun placeholder ne peut
changer un calcul. Une variable suffixée est une autre variable, donc
une autre ligne de `meta`, plus une colonne `suffix`. `card.trend` suit
les suffixes tout seul en lisant cette colonne. Détail utilisateur dans
RENAMING.md (deux entrées du 2026-07-20), conception dans le docstring
de `src/card/suffix.py`, divergences R dans stase
`docs/dev/ORIGINE_R.md`.

Au passage, stase 0.4.0 est redevenu agnostique de card (retrait du
paramètre `meta=` de `process_trend`) et ses colonnes de tendance ne
sont plus ambiguës : `a`/`change` toujours en absolu, `a_relative`/
`change_relative` toujours en pourcentage et NaN sinon.

**Dernier chantier livré (2026-07-21) : fiches delta par horizon.** Les
59 fiches `_H` reçoivent leurs dates d'horizon comme colonnes d'entrée
(comme Q_lim), au lieu de `$H` écrit en dur. `delta` prend quatre bornes
(`ref_start/ref_end/horizon_start/horizon_end`), `return_level`/
`apply_threshold` gagnent `period_start`/`period_end`, stase gagne le
rôle `param_cols` (colonnes de paramètre constantes par série, portées
et CONSERVÉES à travers les process, hors canal numérique, axe détecté
par élimination), `inputs.yaml` gagne `type: date`. Fiches collapsées
(P2 à une entrée + suffixe d'horizon, la fiche ne fige plus 3 horizons).
Sorties inchangées (nouveau == ancien vérifié à l'exact sur les 59),
`$H`/`_substitute_horizons` retirés du loader. Trace RENAMING.md
2026-07-21, conception dans le docstring de `stase` extraction.py.
Débloque les horizons par degré de réchauffement (bornes variables par
série). Reste ouvert (CHANTIERS §10) : les goldens injouables des fiches
volontairement divergentes de R, dont comprendre 4 divergences VCN non
documentées.

**Écosystème** : le service web vit dans le repo séparé `../card-api/`
(FastAPI + Hub'Eau + quotas + journal, conception et chantiers dans
`../card-api/docs/dev/`, son propre CLAUDE.md), DÉPLOYÉ depuis le
2026-07-17 sur la VM de
l'utilisateur derrière son Apache (make apache, port local 8001,
DOMAIN=IP donc HTTP en attendant un nom de domaine). En attente
utilisateur : PEP 541 (nom PyPI `card`, repli card-stase), signalement
amont des 11 fiches cassées dans le package R, nom de domaine +
certbot. Reste aussi une passe anti-quadratin sur les docs (demandée,
non faite).
