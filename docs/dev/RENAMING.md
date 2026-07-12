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
