# Table de correspondance R → Python — APPLIQUÉE le 2026-07-12

Phase B de la ROADMAP. La partie « numpy natif » est déjà appliquée
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
| apply_threshold | 63 | apply_threshold (inchangé) | — |
| rollmean_center | 61 | rollmean_center (inchangé) | isCyclical→cyclical |
| compute_Qp | 27 | **exceedance_quantile** | p (inchangé, proba de dépassement) |
| sumNA | 25 | **nansum_strict** | (NaN si tout-NaN, ≠ nansum) |
| divided | 12 | **ratio** | first (inchangé) |
| circular_median | 10 | circular_median (inchangé) | — |
| compute_VolDef | 10 | **deficit_volume** | upLim→threshold ; kwarg fantôme `select` supprimé des fiches |
| compute_elasticity | 10 | elasticity | Q, X (inchangés) |
| compute_tVolSnowmelt | 9 | **snowmelt_timing** | p→fraction |
| get_Xn | 6 | **return_level** (terme hydrologique standard) | returnPeriod→return_period, waterType→water_type |
| compute_fAp | 6 | **exceedance_frequency** | lowLim→threshold |
| BFS | 5 | **baseflow** (retourne la série de débit de base) | method (inchangé) |
| compute_FDC_p | 5 | **fdc_probabilities** | isNormLaw→norm_spacing |
| compute_FDC_Q | 5 | **fdc_quantiles** | idem |
| compute_Biais | 5 | **bias** | sim_minus_obs (inchangé) |
| dBFS | 3 | **quickflow** (Q − débit de base) | — |
| compute_tSnowmelt | 3 | **snowmelt_duration** | p1/p2→fraction1/fraction2 |
| compute_VolSnowmelt | 3 | **snowmelt_volume** | — |
| get_MKalpha | 3 | **mannkendall_slope** (pente de Sen) | level (inchangé) |
| get_MKH | 3 | **mannkendall_test** | idem |
| compute_RAT_X | 3 | **RAT** | thresh (inchangé) |
| compute_NSE | 1 | **NSE** | — |
| compute_NSElog | 1 | **NSE_log** | — |
| compute_NSEi | 1 | **NSE_inverse** | — |
| compute_NSEracine | 1 | **NSE_sqrt** | — |
| compute_KGE | 1 | **KGE** | method (inchangé) |
| compute_KGEracine | 1 | **KGE_sqrt** | — |
| compute_STD | 1 | **std_ratio** (c'est sd(sim)/sd(obs)) | — |
| compute_Rc | 1 | **runoff_coefficient** | — |
| get_BFI | 1 | **BFI** | — |
| get_BFM | 1 | **BFM** | — |
| fdc_slope | 1 | fdc_slope (inchangé) | p (inchangé) |
| rollsum_center | 1 | rollsum_center (inchangé) | — |

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

`{"data": ..., "meta": ...}` ; les clés héritées `dataEX` / `metaEX`
pointent vers les mêmes objets (transition, retrait possible plus tard).

## Clés des fiches YAML (215 fiches réécrites)

| Ancien | Nouveau |
|---|---|
| funct (process et sampling adaptatif) | func |
| NApct_lim | max_na_pct |
| NAyear_lim | max_na_years |
| Seasons | seasons |
| to_normalise (meta global) | relative |

La colonne metaEX correspondante s'appelle aussi `relative`
(consommée par stase.trend via meta=).

## Note de validation

Le corpus R↔Python a été régénéré avant/après renommage : aucun statut
ne change sur les vraies variables ; seules disparaissent 11 lignes
« ok » triviales où les colonnes structurelles R (Month, Yearday)
étaient comparées à elles-mêmes par coïncidence de nom (les colonnes
Python sont désormais en snake_case).

## Renommages de fiches — audit 2026-07-15 (AUDIT_FICHES.md, NOMENCLATURE.md)

Ids et sorties, validés par l'utilisateur :

| Ancien id | Nouveau id | Sorties | Motif |
|---|---|---|---|
| STD | STD_ratio | STD → STD_ratio | la fonction retourne sd(sim)/sd(obs), sans unité (composante α du KGE) — audit A3 |
| Rc | QR_ratio | Rc → QR_ratio | ΣQ/ΣR n'est pas un coefficient de ruissellement (unité m³·s⁻¹·mm⁻¹) ; l'id Rc est réservé à la future fiche adimensionnelle avec surface en entrée `S` — audit A6 |
| median-finLF | median-endLF | inchangées (median-endLF) | id franglais, sorties déjà en anglais — audit C3 |

Changements de **valeurs** de sorties (bascules du kwarg `relative` de
`delta`, décisions B1/B3 — la parité avec le R historique est
volontairement rompue pour ces sorties) :

| Fiche | Sorties | relative | Avant | Après |
|---|---|---|---|---|
| delta-dtBF_H | delta-dtBF_H1..H3 | true → false | % implicite | jours (cohérent avec l'unité) |
| delta-dtFlood_H | delta-dtFlood_H1..H3 | true → false | % implicite | jours |
| delta-QNA_H (+ _summer, _winter) | delta-QNA*_H1..H3 | false → true | m³/s | % (cohérent avec l'unité) |
| delta-allLF_H (+ _summer, _winter) | delta-vLF*_H1..H3 uniquement | false → true | m³ | % — aligne les bundles sur la fiche individuelle delta-vLF_H |

Correction fonctionnelle : QJC10 P1 lisait la colonne `Q_obs`
inexistante (`input_vars: Q`) — corrigé en `Q`, la fiche est
exécutable (audit A4).

## Corrections de cohérence — 2026-07-18

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

## Correction de la loi log-normale des basses eaux — 2026-07-18

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