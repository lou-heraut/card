> **Statut : norme en vigueur.** Deux rôles : la table de correspondance
> des noms R vers Python (elle fait foi, tout nouveau renommage passe par
> l'utilisateur), et le journal daté des changements de **sorties** de
> fiches, c'est-à-dire des ruptures assumées de parité avec R. Le journal
> des livraisons du paquet est `CHANGELOG.md`, à la racine.

# Table de correspondance R → Python : APPLIQUÉE le 2026-07-12

Phase B de la refonte (`archive/ROADMAP.md`). La partie « numpy natif »
est déjà appliquée
(2026-07-11, pré-validée) : `mean/median/sum/minNA/maxNA/which.*NA` →
`nanmean/nanmedian/nansum/nanmin/nanmax/nanargmin/nanargmax`, le kwarg
`{skipna: true}` a disparu des fiches, le registre est supprimé
(résolution par namespace card.functions → numpy).

Reste ci-dessous : les fonctions hydro custom. Règle de nommage proposée :
**nom de la quantité calculée, snake_case, acronymes hydrologiques en
majuscules, pas de préfixe verbal (compute_/get_)**.

## A. Renommages proposés (usage = nb d'occurrences dans les fiches)

| Actuel | Usage | Proposition | Renommage des paramètres |
|---|---|---|---|
| get_deltaX | 249 | **delta** (validé utilisateur : direct et non ambigu, cohérent avec les variables delta-*) | futur→future, to_normalise→relative |
| apply_threshold | 63 | apply_threshold (inchangé) |  |
| rollmean_center | 61 | rollmean_center (inchangé) | isCyclical→cyclical |
| compute_Qp | 27 | **exceedance_quantile** | p (inchangé, proba de dépassement) |
| sumNA | 25 | **nansum_strict** | (NaN si tout-NaN, ≠ nansum) |
| divided | 12 | **ratio** | first (inchangé) |
| circular_median | 10 | circular_median (inchangé) |  |
| compute_VolDef | 10 | **deficit_volume** | upLim→threshold ; kwarg fantôme `select` supprimé des fiches |
| compute_elasticity | 10 | elasticity | Q, X (inchangés) |
| compute_tVolSnowmelt | 9 | **snowmelt_timing** | p→fraction |
| get_Xn | 6 | **return_level** (terme hydrologique standard) | returnPeriod→return_period, waterType→water_type |
| compute_fAp | 6 | **exceedance_frequency** | lowLim→threshold |
| BFS | 5 | **baseflow** (retourne la série de débit de base) | method (inchangé) |
| compute_FDC_p | 5 | **fdc_probabilities** | isNormLaw→norm_spacing |
| compute_FDC_Q | 5 | **fdc_quantiles** | idem |
| compute_Biais | 5 | **bias** | sim_minus_obs (inchangé) |
| dBFS | 3 | **quickflow** (Q − débit de base) |  |
| compute_tSnowmelt | 3 | **snowmelt_duration** | p1/p2→fraction1/fraction2 |
| compute_VolSnowmelt | 3 | **snowmelt_volume** |  |
| get_MKalpha | 3 | **mannkendall_slope** (pente de Sen) | level (inchangé) |
| get_MKH | 3 | **mannkendall_test** | idem |
| compute_RAT_X | 3 | **RAT** | thresh (inchangé) |
| compute_NSE | 1 | **NSE** |  |
| compute_NSElog | 1 | **NSE_log** |  |
| compute_NSEi | 1 | **NSE_inverse** |  |
| compute_NSEracine | 1 | **NSE_sqrt** |  |
| compute_KGE | 1 | **KGE** | method (inchangé) |
| compute_KGEracine | 1 | **KGE_sqrt** |  |
| compute_STD | 1 | **std_ratio** (c'est sd(sim)/sd(obs)) |  |
| compute_Rc | 1 | **runoff_coefficient** |  |
| get_BFI | 1 | **BFI** |  |
| get_BFM | 1 | **BFM** |  |
| fdc_slope | 1 | fdc_slope (inchangé) | p (inchangé) |
| rollsum_center | 1 | rollsum_center (inchangé) |  |

## B. Non utilisées dans les fiches (bibliothèque, renommées par cohérence)

| Actuel | Proposition |
|---|---|
| minus | difference |
| circular_minus | circular_difference |
| circular_divided | circular_ratio |
| get_MKp | mannkendall_pvalue |
| compute_GumbelParams/Law, compute_LogNormal | internes à return_level (préfixe _) |

## C. Statut

Appliquée intégralement le 2026-07-12 (143 fiches YAML + modules
card/functions) avec deux extensions cohérentes : le kwarg/paramètre
`Date` → `dates` aussi dans apply_threshold (aligné avec return_level),
et le kwarg fantôme `select: longest` supprimé des fiches deficit_volume.
Les noms de variables internes aux fiches (upLim, lowLim comme sorties
de processus) sont conservés. Validation croisée R↔Python relancée
après application : corpus identique (552 ok en mode parité rolling).
Cette table est conservée pour la traçabilité R↔Python.


# Renommages Python (2026-07-12)

Nettoyage validé par l'utilisateur : renommage sec des paramètres et des
clés YAML ; fonctions R conservées en alias. Côté stase :
voir stase/docs/dev/RENAMING_PY.md.

## Fonctions (alias R conservés)

| R / historique | Python canonique |
|---|---|
| CARD_extraction (param CARD_name accepté) | card.extract(data, cards=[...]) |
| CARD_list_all | card.list_cards |
| CARD_info | card.info |
| CARD_management | card.copy_cards |

## Paramètres (renommage sec)

| Ancien | Nouveau |
|---|---|
| CARD_path (extract, list_cards, info) | path |
| period_default | default_period |
| cancel_lim | ignore_na_limits |
| extract_only_metadata | metadata_only |
| info(CARD_name) | info(name) |
| copy_cards : CARD_name / CARD_path / CARD_source / add_id | cards / dest / source / numbered |

## Clés de retour de card.extract

`{"data": ..., "meta": ...}`. Les clés héritées `dataEX` / `metaEX` ont
été acceptées en transition, puis purgées de tout l'écosystème le
2026-07-16 : la sortie d'une extraction est de la donnée comme une autre.

## Clés des fiches YAML (215 fiches réécrites)

| Ancien | Nouveau |
|---|---|
| funct (process et sampling adaptatif) | func |
| NApct_lim | max_na_pct |
| NAyear_lim | max_na_years |
| Seasons | seasons |
| to_normalise (meta global) | relative |

La colonne de métadonnées correspondante s'appelle aussi `relative`.
C'est `card.trend` qui la traduit pour le moteur, sous la forme
`relative={variable: bool}` (le paramètre `meta=` de `stase.trend`, qui
lisait directement la table de métadonnées, a été retiré en stase 0.4.0 ;
voir l'entrée du 2026-07-20 plus bas).

## Note de validation

Le corpus R↔Python a été régénéré avant/après renommage : aucun statut
ne change sur les vraies variables ; seules disparaissent 11 lignes
« ok » triviales où les colonnes structurelles R (Month, Yearday)
étaient comparées à elles-mêmes par coïncidence de nom (les colonnes
Python sont désormais en snake_case).

## Renommages de fiches, audit 2026-07-15 (archive/AUDIT_FICHES.md, NOMENCLATURE.md)

Ids et sorties, validés par l'utilisateur :

| Ancien id | Nouveau id | Sorties | Motif |
|---|---|---|---|
| STD | STD_ratio | STD → STD_ratio | la fonction retourne sd(sim)/sd(obs), sans unité (composante α du KGE), audit A3 |
| Rc | QR_ratio | Rc → QR_ratio | ΣQ/ΣR n'est pas un coefficient de ruissellement (unité m³·s⁻¹·mm⁻¹) ; l'id Rc est réservé à la future fiche adimensionnelle avec surface en entrée `S`, audit A6 |
| median-finLF | median-endLF | inchangées (median-endLF) | id franglais, sorties déjà en anglais, audit C3 |

Changements de **valeurs** de sorties (bascules du kwarg `relative` de
`delta`, décisions B1/B3 ; la parité avec le R historique
est volontairement rompue pour ces sorties) :

| Fiche | Sorties | relative | Avant | Après |
|---|---|---|---|---|
| delta-dtBF_H | delta-dtBF_H1..H3 | true → false | % implicite | jours (cohérent avec l'unité) |
| delta-dtFlood_H | delta-dtFlood_H1..H3 | true → false | % implicite | jours |
| delta-QNA_H (+ _summer, _winter) | delta-QNA*_H1..H3 | false → true | m³/s | % (cohérent avec l'unité) |
| delta-allLF_H (+ _summer, _winter) | delta-vLF*_H1..H3 uniquement | false → true | m³ | %, aligne les bundles sur la fiche individuelle delta-vLF_H |

Correction fonctionnelle : QJC10 P1 lisait la colonne `Q_obs`
inexistante (`input_vars: Q`), corrigé en `Q`, la fiche est
exécutable (audit A4).

## Corrections de cohérence : 2026-07-18

Sorties renommées (validé utilisateur : lever l'ambiguïté S/M avant
distribution publique ; la parité R est rompue sur le NOM seulement,
les valeurs sont identiques) :

| Fiche | Sorties avant | Sorties après | Motif |
|---|---|---|---|
| mean-RSA_season (v2.0) | mean-RA_DJF..SON (fr moyenne-RA_*) | mean-RSA_DJF..SON (fr moyenne-RSA_*) | le stem doit refléter l'agrégation saisonnière, comme mean-TSA_season et mean-QSA_season |

Corrections fonctionnelles sans changement de valeurs :

- **ETPA (v1.1), ETPSA_season, ETPMA_month** : `nansum` → `nansum_strict`.
  np.nansum vaut 0.0 sur une fenêtre entièrement vide (cumul nul faux) ;
  nansum_strict y vaut NaN, comme toutes les autres fiches de cumul (R).
  Avec `max_na_pct: 3`, les fenêtres vides étaient déjà filtrées en NaN
  par stase : les sorties sont inchangées en pratique, c'est une défense
  si le garde-fou est retiré d'une copie de fiche.
- **Palette ETP** (les 3 fiches) : marron→vert (convention « plus d'eau =
  vert » des cumuls de pluie et débits) remplacée par la palette
  vert→marron des durées de sécheresse (dtLF, vLF) : une ETP forte
  traduit un assèchement, pas un apport d'eau.

## Correction de la loi log-normale des basses eaux : 2026-07-18

Changement de **valeurs** (validé utilisateur, rupture volontaire avec
le R historique, à signaler en amont comme les 11 fiches cassées) :
le quantile et la CDF de la loi mixte des minima traitent désormais
les années à débit nul par l'approche des probabilités conditionnelles
standard (Jennings & Benson 1969) : F(x) = p0 + (1 - p0) x F_pos(x).
Le R omettait la division par (1 - p0), ce qui biaisait les quantiles
vers le bas (étiages annoncés plus sévères, jusqu'à -13 % mesurés pour
p0 = 30 %) et pouvait produire des « probabilités » au-delà de 100 %.
Identique quand p0 = 0 : seules les stations avec au moins une année
à sec changent. Fiches concernées : VCN10-5, VCN30-2, QMNA-5,
delta-VCN10-5_H, n-VCN10-5_H, rp-VCN10, rp-VCN30, rp-QMNA.
Corrigé aussi (parité R conservée) : au bord exact p0 = 1/T, le port
Python levait une exception là où R renvoie silencieusement 0 ;
le Python renvoie maintenant 0.

Nouvelle fonction : **return_period** (inverse exacte de return_level,
même module ; seuil -> période de retour, lois log-normale et Gumbel).
## Suffixes de scénario et métadonnées évolutives : 2026-07-20

Ajout de capacité, sans rupture de sortie : conception complète dans
`CHANTIERS.md` §9.

`card.extract` gagne **suffix=** et **suffix_delimiter=** (mêmes noms
qu'en R et que dans `stase.trend`, une seule grammaire) : une même fiche
s'applique à plusieurs variantes d'une entrée en un appel, plusieurs
seuils réglementaires (`Q_lim_DOE`, `Q_lim_DCR`) ou obs/sim. Le fan-out
des valeurs est celui de stase, au niveau colonne : les séries partagées
ne sont lues qu'une fois, et une fiche dont aucune référence ne varie
n'est calculée qu'une fois et sort sans suffixe.

**Forme de retour modifiée** : `extract(...)["meta"]` porte une colonne
supplémentaire **suffix** (vide pour les lignes non suffixées). Ajout de
colonne, donc compatible avec les lecteurs existants (dont card-api),
mais c'est un changement de schéma à connaître. Les lignes de méta sont
désormais construites APRÈS le run, d'après les colonnes réellement
sorties : une variable suffixée est une autre variable, donc une autre
ligne.

**Grammaire des fiches** : les champs texte de `meta.<lang>` acceptent
les placeholders `{suffix}` (= `{suffix.short}`) et `{suffix.<champ>}`,
résolus depuis `meta.<lang>.suffixes` (ensemble fermé), depuis l'appel
(l'appelant gagne champ par champ), ou depuis `meta.<lang>.suffix_default`
en l'absence de suffixe. Le linter refuse un placeholder sans défaut et
un vocabulaire de suffixes que rien n'utilise, ce qui garantit qu'aucune
accolade ne sort jamais non résolue et rend impossible le cas
`horizon_labels` (champ déclaré dans 55 fiches et lu par personne).

Fiches modifiées (version 1.0 -> 1.1, méta seulement) : **rp-VCN10,
rp-VCN30, rp-QMNA**. Sans suffixe, leur `name` est inchangé au caractère
près ; leur `method` passe de « return period of the threshold Q_lim » à
« return period of the Q_lim threshold » (« période de retour du seuil
Q_lim » inchangé en français). Aucune valeur numérique modifiée.

## card.trend : suffixes et unités de la sortie de tendance : 2026-07-20

Suite du chantier suffixes, côté tendance. Nécessite **stase 0.4.0**.

`card.trend` ne passe plus la table `meta` à stase (le paramètre `meta=`
y a été retiré : il faisait dépendre stase du format de card et
court-circuitait une validation). Il traduit désormais les fiches vers
la forme générique `relative={variable: bool}`. Rien ne change pour
l'utilisateur : le caractère relatif vient toujours de
`meta.global.relative` des fiches, card fait la traduction.

`card.trend` dérive aussi `suffix=` de la colonne `suffix` de la table
`meta` : une extraction suffixée (`QA_obs`, `QA_sim`) est suivie sans
avoir à répéter les suffixes, et la sortie porte `variable_no_suffix`.

Nouveau paramètre **extremes_pool_suffixes** (défaut False, même nom
qu'en stase) : met les bornes de quantiles en commun entre les variantes
d'une même variable de base, ce qui rend `QA_obs` et `QA_sim`
comparables sur la même échelle.

**Sorties de tendance modifiées** (rupture de parité R volontaire,
détail dans stase `docs/dev/ORIGINE_R.md`) : `a` et `change` portent
toujours la valeur absolue, `a_relative` et `change_relative` toujours
le pourcentage et valent NaN quand la variable n'est pas relative. Le R
recopiait la valeur absolue dans la colonne relative, si bien que deux
variables d'une même sortie pouvaient être dans des unités différentes
sous le même nom de colonne. Nouvelles colonnes `a_min`/`a_max` et
`change_min`/`change_max` (bornes de quantiles dans l'unité de la
variable), `change_relative` et ses bornes. `mean_period` est désormais
toujours calculée.

## Horizons en colonnes d'entrée (2026-07-21)

Les 59 fiches `_H` (57 delta + n-VCN10-5_H, n-QJXA-10_H) reçoivent leurs
dates d'horizon comme colonnes d'ENTRÉE fournies par l'appelant (comme
Q_lim pour rp-*), et non plus écrites en dur via `$H`. Les SORTIES ne
changent pas : nouveau == ancien vérifié à l'exact sur le corpus des 59
(255 comparaisons), parité R inchangée, ce n'est donc pas une rupture.
Changements :

- `delta(X, dates, ref_start, ref_end, horizon_start, horizon_end,
  relative, return_period=None, water_type="low", Q_for_BFI=None)` :
  les deux paires `past`/`future` deviennent quatre bornes scalaires,
  extraites d'une colonne constante par série si besoin ; filtrage sur
  de vraies dates.
- `return_level` et `apply_threshold` gagnent `period_start`/`period_end`
  (rétrocompatibles avec `period`), pour porter la période en colonnes
  (fiches n-count par horizon).
- `inputs.yaml` : nouvelles entrées `ref_start`/`ref_end`/`horizon_start`/
  `horizon_end` avec une clé `type: date`. `type` distingue les
  paramètres-dates (routés comme covariables, ni axe ni mesure) des
  mesures numériques ; défaut `numeric` implicite.
- Fiches collapsées : P2 à une entrée + suffixe d'horizon (la fiche ne
  fige plus 3 horizons, leur nombre et identité viennent de `suffix=`),
  variable de base + `suffix_default`, `{horizon}` → `{suffix.name}`.
- `$H`, `meta.global.horizons` et `_substitute_horizons` retirés du loader.
- Moteur : stase gagne `param_cols` (colonnes de paramètre constantes par
  série, portées et CONSERVÉES à travers les process, hors canal
  numérique, détection de l'axe par élimination). Détail dans le
  docstring de `stase/src/stase/extraction.py`.

## Fiches à horizon fixe converties au modèle suffixe (2026-07-22)

Douze fiches figeaient leur période dans le fichier. Elles deviennent
trois, dont l'appelant choisit l'horizon, comme les fiches delta depuis
le 2026-07-21.

| Retirées | Remplacées par | Variable produite |
|---|---|---|
| QM_H0, QM_H1, QM_H2, QM_H3 | `QM_H` | `QM`, suffixée par horizon |
| FDC_H0..H3 | `FDC_H` | `FDC_p` et `FDC_Q` |
| median-QJ_H0..H3 | `median-QJ_H` | `median-QJ` |

Les bornes arrivent en colonnes `horizon_start` et `horizon_end`, et une
déclinaison `suffix=["H1", "H3"]` reproduit exactement les anciens noms
de sortie (`QM_H1`, `QM_H3`). Vérifié valeur par valeur sur les trois
familles : à période égale, le résultat est identique à l'ancien.

Les dates figées disparaissent du corpus. Celles qui y étaient, pour
mémoire : H0 du 1976-01-01 au 2005-08-31, puis 2021-2050, 2041-2070 et
2070-2099. La fenêtre H0 mélangeait un début calendaire et une fin
hydrologique, incohérence qui sort du corpus avec elle.

Mécanisme : `over_period(X, func, dates, period_start, period_end)`,
qui restreint puis délègue. La restriction se fait dans la fonction et
non par un masque en amont, un masque étant compté comme des lacunes
(mesuré : `max_na_pct=3` sur une série masquée ne rend plus aucun mois).

Corrigé au passage : `fdc_probabilities` ne déclare aucune colonne, or le
moteur affecte d'office la première colonne numérique à une fonction qui
n'en déclare pas. La valeur se liait au paramètre `n` et faisait échouer
l'appel. **Les cinq fiches FDC plantaient donc depuis l'origine du
portage**, trois d'entre elles masquant le défaut par une période sans
données. Aucun test ne les couvrait, et le corpus de validation les
excluait puisqu'elles plantent aussi dans le paquet R.

**Complément du 2026-07-22, famille FDC.** Les deux fiches déclaraient
une variable unique (`FDC`) pour deux colonnes de sortie (`FDC_p` et
`FDC_Q`). Une seule ligne de métadonnées décrivait donc la courbe
entière, et sous suffixe elle ne pouvait plus rattacher `FDC_Q_H1` à son
horizon : la métadonnée retombait sur la forme générique. Les variables
sont désormais déclarées distinctes (`[FDC_p, FDC_Q]`), le `name` restant
unique comme le veut la règle des coordonnées d'un même objet. L'unité
suit : sans unité pour les probabilités, m³/s pour les quantiles, là où
les deux héritaient du débit. Sous suffixe, `FDC_p` est émis une seule
fois, l'axe des probabilités étant le même pour tous les horizons.
