# ROADMAP — refonte card / exstat (clarifiée avec l'utilisateur le 2026-07-11)

> **Phase A TERMINÉE (2026-07-11)** : packages `exstat` et `card` créés en
> repos séparés (git init, pas de commit initial), moteur remonté dans
> exstat (adaptatif, sorties vectorielles dynamiques, kwargs-colonnes,
> littéraux, keep-liste, colonnes creuses via DataFrame.attrs), corpus
> revalidé à l'identique (552 ok en mode parité rolling). Venvs
> `.python_env` créés dans les deux repos (pandas 3.0.3 / numpy 2.5.1,
> corpus validé sous ces versions).
>
> **Phase B TERMINÉE (2026-07-12)** : numpy natif appliqué (150 fiches,
> {skipna: true} disparu, registre supprimé — résolution par namespace
> card.functions → numpy) puis renommages customs validés par
> l'utilisateur et appliqués (get_deltaX→delta, get_Xn→return_level,
> compute_Biais→bias, BFS/dBFS→baseflow/quickflow, kwargs
> futur→future, to_normalise→relative, returnPeriod→return_period...).
> Table de correspondance : RENAMING.md. Corpus revalidé : 552 ok.
>
> **Phase C TERMINÉE (2026-07-12)** : suites pytest (`pytest` dans chaque
> repo — exstat 14 tests moteur, card 40 tests : goldens figés depuis la
> validation R, loader, intégration mini-jeu, lint, management) ;
> `card/schema.py` = linter sans dépendance (`python -m card.schema`),
> corpus 215 fiches valide, et le linter détecte bien le bug historique
> des fenêtres perdues (testé). Le harnais R croisé (tests/*.R,
> run_py_corpus.py) reste l'outil de validation lourde, hors pytest.
> Reste : phase D (doc finale, commits initiaux).

## Principes actés

- **Python natif d'abord** : chaque fonction R custom est remplacée par
  son équivalent numpy/scipy/pandas quand il existe et que le résultat
  est identique ou très proche. Pas de wrappers cosmétiques : le YAML
  référence directement le vrai nom Python (`nanmean`, `nanargmax`...).
  Le registre-table disparaît (résolution par namespace :
  card.functions puis numpy).
- **Corrections bienvenues** : franglais, doc, nomenclature des
  paramètres, noms de fonctions flous (ex. `get_Xn`) — Python a
  vocation à remplacer R, on en profite pour assainir.
- **Séparation nette ancien/nouveau** :
  - `EXstat_project/exstat/` = nouveau package Python (moteur de
    données/agrégation), à côté de l'ancien code R `EXstat_project/EXstat/`.
  - `CARD_project/card/` = nouveau package Python (fiches YAML +
    fonctions hydro + métadonnées), à côté de l'ancien repo R
    `CARD_project/CARD/`. Les CARD_yml déménagent dans `card/`.
- **Frontière** : card = au maximum la gestion des métadonnées et le
  chargement des fiches ; exstat = TOUTE la gestion de données et
  d'agrégation (y compris sampling adaptatif, transform, ragged,
  keep, colonnes creuses — actuellement hackés côté CARD_py).
- **Anciennes fiches R** : pas de réparation (utiles seulement pour la
  vérification croisée R↔Python, pas une fin en soi).

## Phase A — Squelette des deux packages

1. Créer `EXstat_project/exstat/` : pyproject, déplacement/adaptation de
   process_extraction.py + tools.py (depuis EXstat_Claude/EXstat_py),
   imports propres, smoke tests.
2. Remonter dans exstat les mécanismes moteur aujourd'hui dans CARD_py :
   sampling_period adaptatif par station, sorties transform
   (vectorielles) et ragged, keep=[colonnes], compaction des colonnes
   creuses. API à concevoir proprement, pas un copier-coller du hack.
3. Créer `CARD_project/card/` : pyproject (dépendance exstat), y
   déplacer le code de CARD_py + les fiches `CARD_yml/` (qui font
   partie du nouveau package) + les tests. L'ancien `CARD/CARD_py/`
   disparaît ; le repo CARD redevient purement R + fiches R.

## Phase B — Fonctions : Python natif d'abord

4. **Audit des ~50 fonctions** : pour chacune, équivalent natif ?
   Tableau livrable : nom R actuel → décision (natif direct / custom
   conservée / custom renommée) → écarts de comportement documentés.
   Premiers cas identifiés :
   - `which.minNA`/`which.maxNA` → `np.nanargmin`/`np.nanargmax`
     (0-based natif, déjà la convention du pipeline is_date)
   - `mean/min/max/median` + `{skipna: true}` → `nanmean/nanmin/
     nanmax/nanmedian` — le kwarg skipna disparaît des YAML
   - ⚠ `np.nansum(tout-NaN) = 0.0` ≠ `sumNA = NA` → décision explicite
   - `minNA/maxNA(div=)` : vérifier si `div` est réellement utilisé
     dans les fiches ; sinon natif direct
   - `compute_RAT_X` → scipy.stats.spearmanr (déjà fait), etc.
5. **Renommage des customs restantes** : anglais correct, noms
   explicites, paramètres nettoyés. À proposer en table complète AVANT
   application (ex. compute_Biais→compute_bias,
   compute_NSEracine→compute_NSE_sqrt, get_Xn→compute_return_level,
   compute_Qp→exceedance_quantile...). La table de correspondance
   R→Python est conservée dans la doc (traçabilité).
6. Mise à jour mécanique de tous les YAML (tuples funct) vers les
   nouveaux noms ; résolution par namespace, suppression du registre.

## Phase C — Non-régression et qualité

7. Re-exécution du harnais croisé complet (fiches R inchangées ↔
   card/exstat sur YAML renommés) : mêmes classes de résultats que la
   validation du 2026-07-11 attendues.
8. Suite pytest pérenne : golden values figées depuis la validation R,
   tests loader, intégration 5 fiches de référence ; harnais R en test
   optionnel.
9. Schéma de validation YAML (pydantic/jsonschema) + linter (aurait
   attrapé le bug des 29 sampling_period).

## Phase D — Finitions

10. README/doc des deux packages, exemples d'usage.
11. Commits de clôture côté repo CARD R (l'en-cours non commité).
12. Pas de réparation des fiches R cassées (CR, FDC, etc.) — documentées.

## Ordre

A (squelettes + frontière exstat) → B (audit puis renommage puis YAML)
→ C (non-régression) → D. La table d'audit/renommage de la phase B est
soumise à validation utilisateur avant application.
