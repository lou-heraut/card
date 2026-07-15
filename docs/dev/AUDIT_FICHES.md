# AUDIT_FICHES — Noms et métadonnées des fiches (2026-07-13)

Audit des 215 fiches YAML : croisement de `name`, `description`,
`method` et `unit` (version fr) avec le bloc `process` réellement
exécuté. Les identifiants courts (ids) sont considérés comme stables ;
l'audit porte sur les métadonnées, sauf mention contraire. La version
en reflète la fr : toute correction est à faire dans les deux langues.

> **APPLIQUÉ le 2026-07-15** — tous les constats ci-dessous ont été
> arbitrés puis traités en 4 lots (commits b693fef, c3ccc94, 07a6931,
> c27fea9 ; règles : NOMENCLATURE.md ; renommages : RENAMING.md).
> Le document est conservé comme trace des constats et des décisions.

---

## Procédure d'arbitrage et d'application (fixée le 2026-07-15)

1. **Référence normative** : `NOMENCLATURE.md` (guide de nommage fondé
   sur le système du corpus consolidé par Oberlin 1992 — règles
   R1–R7). Chaque correction de métadonnée cite la règle qu'elle
   applique dans le récapitulatif de batch.
2. **Pré-arbitrages enregistrés** (note utilisateur du 2026-07-13,
   ex-note_tmp.txt) :
   - A1, A2, A4, A5 : acceptés.
   - A3, A6 : **la fonction fait foi** — les métadonnées décrivent le
     calcul réel, on ne « ment » jamais sur ce que fait le process
     (érigé en règle R6 du guide).
   - B1 : les delta de durées (dt*) en absolu → jour ; les delta de
     débits en relatif → % ; fréquences : cf. point ouvert B2.
   - B3 : delta de volumes en relatif → %.
   - C2 : multi-sorties ⇒ métadonnées en listes (le broadcast d'un
     scalaire est jugé trop piégeux). **Amendé le 2026-07-16** : ne
     vaut que pour de vraies variables distinctes ; les FDC* gardent
     un name unique (les colonnes p/Q sont les coordonnées d'une même
     courbe, expliquées en description) — cf. NOMENCLATURE.md §9.7.
   - C3 : renommage `median-finLF` → `median-endLF` accepté (à tracer
     dans RENAMING.md).
   - C4 : accepté, et **étendre le catalogue** : créer les fiches
     évidentes manquantes (ex. critère BFI-LH ; dérivés summer/winter
     des fiches basses eaux qui n'existent qu'en `all*`).
   - C5, C6, C7 : acceptés. C8 : compléter si utile et non ambigu.
   - D : `method` toujours remplissable → à remplir partout ;
     `description` seulement quand elle apporte plus que le `name`
     (règle R4 du guide).
3. **Arbitrages complets rendus le 2026-07-15** — plus aucun point
   ouvert, cf. NOMENCLATURE.md §9 (guide validé) :
   - C1 : listes explicites de 3 (pas de template `{horizon}`) ;
   - R2 : variante pédagogique (« inter-annuel » explicite) ;
   - QJC : « caractéristique » banni des name ; QJCd = régime
     journalier inter-annuel lissé sur d jours ;
   - R (précipitations) : assumé, standard climato ;
   - B2 : fQ*A = fraction sans unité (la fonction fait foi) ; fiches
     « durée cumulée de dépassement » (jours/an) à créer plus tard si
     besoin ;
   - A3 : id et sortie **STD → STD_ratio** (α du KGE) ;
   - A6 : id et sortie **Rc → QR_ratio** (calcul conservé) ; l'id Rc
     est réservé à une future fiche coefficient adimensionnel avec la
     surface en colonne d'entrée `S` (86,4 × ΣQ/ΣR / A(km²)).
4. **Application par lots**, après le retour complet :
   - lot 1 — métadonnées pures (risque nul) ;
   - lot 2 — arbitrages (unit/relative, renommages d'ids tracés dans
     RENAMING.md) ;
   - lot 3 — remplissage method (+ description sélective) ;
   - lot 4 — création des fiches manquantes (C4 étendu).
   Batchs de ~10 fiches, récapitulatif avec niveau de confiance,
   `pytest` + `python -m card.schema` après chaque lot ; le harnais R
   croisé n'est requis que si un calcul change (a priori aucun,
   cf. R6).

---

## A. `name` ou `method` contredisant le calcul

### A1. Famille « dépassé X années sur Y » (14 fiches)

`exceedance_quantile(Q, p)` calcule le quantile des débits
**journaliers** dépassé `p` % du temps (dans l'année pour les fiches
annuelles, sur toute la chronique pour `time_step: none`). Les noms
« Débit (annuel) dépassé X années sur Y » décrivent un tout autre
calcul (quantile inter-annuel de valeurs annuelles) :

| Fiche | name actuel | calcul réel |
|---|---|---|
| Q90, delta absent | « Débit dépassé 9 années sur 10 » | débit journalier dépassé 90 % du temps (chronique entière) |
| Q10 | « Débit dépassé 1 an sur 10 » | débit journalier dépassé 10 % du temps (chronique entière) |
| Q90A, delta-Q90A_H | « Débit annuel dépassé 9 années sur 10 » | débit journalier dépassé 90 % du temps, par année |
| Q95A, delta-Q95A_H | « … 19 années sur 20 » | idem, 95 % |
| Q99A, delta-Q99A_H | « … 99 années sur 100 » | idem, 99 % |
| Q01A, delta-Q01A_H | « … 1 année sur 100 » | idem, 1 % |
| Q05A, delta-Q05A_H | « … 1 année sur 20 » | idem, 5 % |
| Q10A, delta-Q10A_H | « … 1 année sur 10 » | idem, 10 % |

Les fiches fQ01A/fQ05A/fQ10A décrivent correctement le même objet
(« Q01 est le débit dépassé 1 % du temps, extrait de la courbe des
débits classés ») : reprendre cette formulation.

Dans la même veine, Q25A/Q50A/Q75A (+ deltas) : « Premier quartile /
Médiane / Troisième quartile **des débits annuels** » — ce sont des
quantiles des débits **journaliers** de chaque année (« quartile
annuel des débits journaliers »), pas des quantiles de la série des
débits annuels.

### A2. n-VCN10-5_H : sens du seuil inversé

`name` : « Nombre d'années … où le VCN10 est **supérieur** au
VCN10-5 » ; le process compte avec `where: '<='` les années où le
VCN10 est **inférieur ou égal** au VCN10-5 historique (ce qui est le
comptage hydrologiquement pertinent en étiage). Le nom dit l'inverse
du calcul — probable copier-coller de n-QJXA-10_H (où `>=` et
« supérieur » concordent). Corriger le nom, pas le calcul.

### A3. STD : ce n'est pas un écart-type

`name` « Écart-type des données journalières », `unit` m³/s ; la
fonction `std_ratio` retourne le **rapport** sd(sim)/sd(obs), sans
unité. Le nom, la desc (qui parle de « capacité des modèles à
reproduire la variabilité » — cohérente avec un ratio) et l'unité
sont à réaligner sur « Rapport des écarts-types simulé/référence »,
sans unité. L'id `STD` lui-même est trompeur (STD_ratio ?) — à
arbitrer car il touche aux sorties.

### A4. QJC10 : nom faux ET fiche cassée

- `name` « Débit moyen **mensuel** moyenné sur 10 jours » : le
  process agrège par **jour de l'année** (`time_step: yearday`) puis
  lisse sur 10 jours — c'est le régime journalier inter-annuel lissé,
  pas du mensuel.
- Bug fonctionnel : `input_vars: Q` mais P1 référence `Q_obs`
  (`QJ: [nanmean, "Q_obs"]`). La fiche ne peut pas tourner avec
  l'entrée déclarée. À corriger (probablement `"Q"`), avec test.

### A5. `method` erronés (copier-coller)

- RA, RAl, RAs et l'étape 1 de mean-RA : method dit « moyenne »
  alors que le calcul est une **somme** (`nansum_strict`).
- RAT_ET0 et RAT_R : method dit « Qref − Qsim et **températures**
  moyennes », copié de RAT_T ; remplacer par ET0 / précipitations.
  Au passage `bias` est un écart relatif, pas « Qref − Qsim ».
- alpha-QJXA / alpha-VCN10 : method ne mentionne que la pente de Sen
  alors que la fiche produit aussi le test (hyp-alpha-*) ; alpha-QA
  le mentionne. Harmoniser.

### A6. Rc : « coefficient » non adimensionnel

`runoff_coefficient` fait sum(Q)/sum(R) sans conversion d'unités ni
surface de bassin → unité affichée m³·s⁻¹·mm⁻¹. Un « coefficient de
ruissellement » est normalement sans unité (lame écoulée / lame
précipitée). Soit renommer (« rapport débit/précipitations », en
assumant l'unité hybride), soit prévoir la conversion avec surface —
décision à prendre, le calcul est peut-être voulu tel quel.

---

## B. Incohérences `relative` (delta) vs `unit`

`delta` avec `relative: True` produit un changement en %, avec
`relative: False` une différence dans l'unité de la variable. Cas
discordants :

| Fiche | relative | unit affichée | attendu |
|---|---|---|---|
| delta-dtBF_H | True | jour | % (ou passer relative=False) |
| delta-dtFlood_H | True | jour | % (ou relative=False) |
| delta-QNA_H | False | % | m³/s (ou relative=True) |
| delta-QNA_summer_H | False | % | idem |
| delta-QNA_winter_H | False | % | idem |
| delta-fQ01A/05A/10A_H | False | jour.an⁻¹ | sans unité (cf. B2) |

Référence interne cohérente : delta-dtLF_H (False + jour),
delta-vBF_H (True + %).

**B2 — unité des fréquences fQ*A** : `exceedance_frequency` retourne
n/N, une fraction sans unité (la method le dit : « rapport du nombre
de jours … par le nombre de jours dans l'année »). L'unité affichée
« jour.an⁻¹ » supposerait une multiplication par 365 qui n'existe
pas. Corriger l'unité (série et deltas), ou le calcul si c'est un
nombre de jours qui était voulu.

**B3 — delta-vLF_H : deux calculs différents sous le même nom de
sortie.** La fiche individuelle delta-vLF_H utilise
`relative: True` ; la fiche groupée delta-allLF_H calcule les mêmes
sorties `delta-vLF_H1/2/3` avec `relative: False` (tout en affichant
l'unité %). Selon la fiche exécutée, la même colonne de sortie change
de sémantique. Les versions summer/winter (groupées uniquement) sont
en False avec unité %. À trancher : True partout (et unité %) semble
l'intention, vu l'unité déclarée.

---

## C. Incohérences de convention (sans erreur de calcul)

1. **Deux styles de nommage des fiches _H** : 63 fiches avec `name`
   en liste de 3 (« l'horizon proche/moyen/lointain ») ; 13 avec un
   template `{horizon}` en chaîne unique (n-VCN10-5_H et toutes les
   summer/winter). Choisir un style ; le template est plus léger mais
   il faut que les outils de rendu (catalogue, CARD_info) le
   substituent.
2. **`name` scalaire pour fiches multi-sorties** (23 fiches) :
   alpha-* (2 sorties : pente + test), FDC* (p + Q), RA_all (3),
   RA_ratio (2), n-VCN10-5_H (3) — aligner `name`/`desc`/`unit` en
   listes sur les sorties, comme le font QMA_month, QSA_season, etc.
   Pour alpha-*, l'unité m³·s⁻¹·an⁻¹ ne vaut que pour la pente, pas
   pour le booléen du test.
3. **median-finLF** : id en français (« fin ») mais la sortie
   s'appelle `median-endLF` ; toutes les variables sœurs sont en
   anglais (startLF/endLF). Renommer l'id `median-endLF`
   (attention : renommage d'id = impact utilisateur, cf. RENAMING.md).
4. **BFI-Wal** : name « Indice de débit de base » sans préciser
   « (Wallingford) », alors que les fiches delta-BFI-Wal_H et
   delta-BFI-LH_H le précisent. Il n'existe d'ailleurs pas de fiche
   critère BFI-LH (asymétrie du catalogue). Les noms delta-BFI-*
   disent « Changement de » là où tous les autres disent « Changement
   moyen de ».
5. **mean-* ambigus** : mean-TSA_season « Moyenne des températures de
   chaque hiver » et mean-RSA_season se lisent exactement comme les
   séries annuelles correspondantes (TSA_season, RSA_season). Dire
   « Moyenne **inter-annuelle** … » (mean-QA est explicite, s'en
   inspirer). TSA_season a de plus un style à part
   (« Températures hivernales annuelles » vs « Moyenne des débits
   journaliers de chaque hiver » pour QSA_season).
6. **ETPA** : « Cumul des évapotranspirations annuelles » → « Cumul
   annuel de l'évapotranspiration potentielle » (l'entrée est ETP ;
   le nom actuel n'indique pas « potentielle » et la syntaxe met
   « annuelles » sur le mauvais mot). Même remarque grammaticale pour
   RA/RAl/RAs (« Cumul des précipitations totales annuelles »).
7. **QSA_JJASO** : name « Moyenne saisonnière annuelle du débit
   journalier » ne dit pas la saison (juin–octobre) — la seule info
   distinctive de la fiche.
8. **QMNA/VCN et sampling adaptatif** : les fiches série QNA, QMNA,
   VCN* documentent bien « Mois du maximum des débits mensuels » dans
   sampling_period(fr) mais QNA et QNA_summer/winter ont `method`
   vide — la seule fiche de la famille sans méthode.

---

## D. Champs vides et coquilles

- `description` vide : **110/215** fiches.
- `method` vide : **53/215** fiches — ETPA, QNA (+summer/winter,
  + leurs deltas), delta-QMA_month_H, QJC10, QM, QMA_month, QM_H0-H3,
  median-QJ (+H0-H3), CR, CRS_season, RA_all, RA_ratio, RAl_ratio,
  RAs_ratio, RCXA1, RCXA5, RMA*_month, RSA*_season, dtCDD*, dtCWD*,
  dtR*mm*, Rc, TA, TMA_month, TSA_season.
- Coquilles : « Somme des écarts entre **de** la moyenne » (vLF,
  allLF, delta-allLF_H) ; « agrégation annuelle **saisonnalisé** »
  (delta-QSA_season_H, mean-RSA_season, mean-TSA_season — ailleurs
  « saisonnalisée ») ; desc de délta-BFI-* décrit le BFI, pas le
  changement (convention assumée ? à trancher, la plupart des deltas
  font pareil).

---

## E. Vers une convention de nommage écrite

→ **Fait le 2026-07-15 : voir `NOMENCLATURE.md`** (guide complet,
brouillon à valider). La grammaire du corpus y est documentée et
consolidée par le système d'Oberlin (1992, transcription
`Oberlin_1994ITCEMAGREF_1-8_edit.md`) : quatre positions hiérarchisées
grandeur / pas de temps / représentativité / saison, préfixes-opérateurs
CARD (soudés = dérivation intra-annuelle, à tiret = opérateur
inter-annuel), suffixes (-k retour, _H horizons, saisons, fan-out),
règles de rédaction R1–R7 (dont « moyenne » réservé à l'inter-annuel et
« la fonction fait foi »), ancrages SANDRE / ETCCDI / OMM, et points
ouverts §9 soumis à arbitrage.

---

## Proposition de lots

→ Remplacée par la « Procédure d'arbitrage et d'application » en tête
de document (lots 1–4, pré-arbitrages enregistrés, points ouverts).
