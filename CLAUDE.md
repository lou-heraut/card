# CLAUDE.md — card

## Contexte

`card` est le package Python du recueil de fiches hydroclimatiques CARD :
chaque fiche YAML décrit comment extraire une variable (débit,
précipitation, température...) à partir de séries journalières. Les
fiches sont exécutées par le moteur générique
[`stase`](../../EXstat_project/stase/) (STatistical Aggregation &
Stationarity Evaluation), lui aussi en Python.

Les deux packages sont issus de la refonte (2026-07) des packages R
`CARD` et `EXstat` :

- les fiches YAML de `src/card/cards/` sont la **source de vérité** ;
- l'ancien repo R (`../CARD-R/`, fiches dans `inst/__all__/`) est en
  maintenance et sert uniquement de référence de validation croisée —
  aucun développement IA n'y a lieu ;
- le port a été validé par comparaison croisée R↔Python sur le corpus
  complet (552 comparaisons identiques, tol 1e-6, mode parité rolling).

Historique et décisions : `docs/dev/ROADMAP.md` (phases A–D de la
refonte, toutes terminées), `docs/dev/RENAMING.md` (table R→Python des
noms de fonctions et de paramètres, validée par l'utilisateur),
`docs/dev/VALIDATION_R.md` (protocole et résultats de la validation
croisée), `docs/dev/AUDIT_FICHES.md` (audit 2026-07-13 des métadonnées,
constats **à arbitrer avant modification**). Le registre détaillé des
anomalies R corrigées pendant la conversion est conservé dans
l'historique git du CLAUDE.md de `../CARD-R/`.

## Structure

```
src/card/
  cards/           # 215 fiches YAML, organisées par thème
    Flow/{Baseflow,High_Flows,Low_Flows,...}/{serie,criteria}/
    Evapotranspiration/  Precipitations/  Temperature/
    Sensitivity_to_Climate_Variability/
  functions/       # fonctions hydro portées de R (baseflow, return_level...)
  loader.py        # YAML → processus (défauts, $Hx, tuples func)
  extraction.py    # card.extract : chaîne P1..Pn via stase
  schema.py        # linter sans dépendance : python -m card.schema
  management.py    # découverte/copie des fiches
tests/             # pytest (~40 tests : goldens R, loader, lint, intégration)
tests/*.R, run_py_corpus.py   # harnais R croisé (validation lourde, hors pytest)
docs/dev/          # ROADMAP, RENAMING, AUDIT_FICHES, VALIDATION_R
```

Environnement : venv `.python_env/` (pandas ≥3, numpy ≥2.5) ;
`tests/conftest.py` rend `card` et `stase` importables sans installation
(sinon `pip install -e ../../EXstat_project/stase -e .`). Vérifications :
`pytest` puis `python -m card.schema`.

---

## Format YAML — Règles de rédaction

> Le format a été assaini en phase B : noms Python natifs (`nanmean`,
> `nanargmax`...), plus de `{skipna: true}`, kwargs renommés
> (cf. RENAMING.md), clés `func` / `max_na_pct` / `max_na_years`.
> Ne pas réintroduire les anciens noms R.

### Structure générale

```yaml
id: QA
version: "1.0"
authors: []
date: "2026-04-30"

meta:
  en:
    variable: QA
    unit: "m^{3}.s^{-1}"
    name: Annual mean daily discharge
    description: ""
    method: "1. annual aggregation [09-01, 08-31] - mean"
    sampling_period: ["09-01", "08-31"]
    topic: "Flow, Mean Flows, Intensity"

  fr:
    variable: QA
    unit: "m^{3}.s^{-1}"
    name: Moyenne annuelle du débit journalier
    description: ""
    method: "1. agrégation annuelle [01-09, 31-08] - moyenne"
    sampling_period: ["01-09", "31-08"]
    topic: "Débit, Moyennes Eaux, Intensité"

  global:
    input_vars: Q
    preferred_sampling_period: "09-01"
    palette: ["#452C1A", "#7F4A23", "#B3762A", "#D4B86A", "#EFE0B0",
              "#BCE6DB", "#7ACEB9", "#449C93", "#2A6863", "#193830"]

process:
  P1:
    func:
      QA: [nanmean, "Q"]
    sampling_period: "09-01"
    max_na_pct: 3
    max_na_years: 10
```

### Règle 1 — func (le plus important)

Chaque variable de sortie est une clé dans `func`. La valeur est un
tuple `[fonction, *colonnes, kwargs?, is_date?]` :

- 1er élément : nom de la fonction en string — résolution par namespace
  `card.functions` puis numpy (pas de registre) ;
- éléments string suivants : noms des colonnes d'entrée (certaines
  fonctions n'en prennent pas, ex. `fdc_probabilities`) ;
- avant-dernier (si dict) : kwargs ;
- dernier (si booléen) : `is_date: true` — omis si false.

```yaml
func:
  QA:    [nanmean,         "Q"]
  tQJXA: [nanargmax,       "Q",     true]
  VC10:  [rollmean_center, "Q",     {k: 10}]
  VCN10: [nanmin,          "VC10"]
  upLim: [nanmax,          "VCN10"]
  dtLF:  [apply_threshold, "VC10",  {lim: upLim, where: "<=", what: length, select: longest}]
  endLF: [apply_threshold, "VC10",  {lim: upLim, where: "<=", what: last, select: longest}, true]
```

Un kwarg dont la valeur (sans guillemets) est le nom d'une variable
calculée en amont (`{lim: upLim}`) est résolu dynamiquement ; les
littéraux positionnels sont permis (`[ratio, "dQXA", 2, {first: true}]`).

### Règle 2 — sampling_period adaptatif

Quand la fenêtre annuelle est calculée depuis les données, même
formalisme tuple que `func` :

```yaml
sampling_period:
  type: adaptive
  func: [nanmax, "Q"]
```

### Règle 3 — sampling_period : liste vs string (meta.en / meta.fr)

- **Fenêtre [début, fin]** → liste de deux strings, format MM-DD en
  `en`, DD-MM en `fr` :
  `["09-01", "08-31"]` (en) / `["01-09", "31-08"]` (fr)
- **Date unique** ou **texte adaptatif** → string :
  `"09-01"` ou `Month of maximum monthly flows`

Dans `process.Px`, `sampling_period` est toujours une string (date de
début), une liste `[début, fin]`, ou un bloc `type: adaptive`.

### Règle 4 — Variables multiples (horizons, bundles)

Quand une fiche produit plusieurs variables (H1/H2/H3, bundles),
`variable`, `name`, `method` (et si besoin `palette`, `is_date`,
`relative` dans `global`) deviennent des listes. Les horizons sont
déclarés dans `meta.global.horizons` et référencés `$H0`, `$H1`... dans
les kwargs — le loader substitue :

```yaml
meta:
  en:
    horizon_labels: {H1: near, H2: middle, H3: distant}
  global:
    horizons:
      H0: ["1976-01-01", "2005-08-31"]
      H1: ["2021-01-01", "2050-12-31"]
      H2: ["2041-01-01", "2070-12-31"]
      H3: ["2070-01-01", "2099-12-31"]

process:
  P5:
    func:
      delta-endLF_H1: [delta, "endLF", "date", {past: $H0, future: $H1, relative: false}]
      delta-endLF_H2: [delta, "endLF", "date", {past: $H0, future: $H2, relative: false}]
      delta-endLF_H3: [delta, "endLF", "date", {past: $H0, future: $H3, relative: false}]
    time_step: none
```

### Règle 5 — Champs à omettre (valeurs par défaut du loader)

Ne pas écrire un champ si sa valeur est identique au défaut :

| Champ | Défaut (ne pas écrire) |
|-------|------------------------|
| `meta.global.is_date` | `false` |
| `meta.global.relative` | `true` |
| `meta.global.is_experimental` | `false` |
| `meta.global.source` | `null` |
| `meta.global.palette` | `null` |
| `meta.global.preferred_sampling_period` | `null` |
| `meta.global.input_vars` | `"X"` (écrire si `"Q"` ou autre) |
| `Px.time_step` | `"year"` |
| `Px.sampling_period` | `null` |
| `Px.period` | `null` |
| `Px.max_na_pct` | `null` |
| `Px.max_na_years` | `null` |
| `Px.seasons` | `[DJF, MAM, JJA, SON]` |
| `Px.keep` | `null` |
| `Px.compress` | `false` |
| `Px.expand` | `false` |

Exception validée : un kwarg explicite dans le R source (ex.
`relative: true` dans un `delta`) reste explicite dans le tuple, même
s'il égale le défaut global.

---

## Règles de travail

- **Lire avant de modifier** : toute modification de fiche part de la
  lecture complète de la fiche (et de la fiche R source dans
  `../CARD-R/inst/__all__/` si l'on vérifie une conversion).
- **Noms de fonctions et de paramètres** : la nomenclature est celle de
  RENAMING.md, validée par l'utilisateur. Tout nouveau renommage doit
  être validé par lui avant application.
- **Corrections automatiques** : corriger sans demander toute
  incohérence à confiance élevée — grammaire (accords, pluriels),
  orthographe, casse (Title Case → sentence case), mot dans la mauvaise
  langue, incohérence de structure entre fiches. Seule une réécriture
  scientifique de fond d'une métadonnée nécessite validation
  (cf. AUDIT_FICHES.md : constats en attente d'arbitrage).
- **Batches + récapitulatif** : pour les modifications de masse,
  procéder par batch (~10 fiches), récapituler avec niveau de confiance
  par fiche (high / medium / low), attendre le "go".
- **Revalider après modification** : `pytest`, `python -m card.schema`,
  et le harnais R croisé pour tout changement touchant les calculs.

## État et reprise (2026-07-15)

- Refonte terminée (phases A–D), corpus validé, repos poussés sur
  github.com/lou-heraut (Pages actives, CI).
- **En attente** : arbitrage utilisateur des constats AUDIT_FICHES.md ;
  demande PEP 541 pour le nom PyPI `card` (squatté — repli
  `card-stase` dans pyproject) ; signalement en amont des 11 fiches qui
  crashent dans le package R lui-même (CR, CRS_season, FDC×5, QJC10,
  RA_ratio, RAl/RAs_ratio — les versions Python fonctionnent).
