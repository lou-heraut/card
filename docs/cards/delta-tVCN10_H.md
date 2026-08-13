---
hide:
  - toc
---

# `delta-tVCN10_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-tVCN10_H     Average change of the date of the annual minimum of  │
  │                        10-day mean flows between the target horizon and  │
  │                                                       historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ day
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            ▼
           VC10
            ╷
            ├── nanargmin(VC10)
            │   └─ Date of the minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           tVCN10
            ╷
            ├── delta(tVCN10, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-tVCN10

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/low-flows/scalar/delta-tVCN10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2fde723a15b755c3235b46ed301fe5e910400248</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-tVCN10_H       Changement moyen de la date du minimum annuel des  │
  │                     débits moyens sur 10 jours entre l'horizon cible et  │
  │                                                   la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            ▼
           VC10
            ╷
            ├── nanargmin(VC10)
            │   └─ Date du minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           tVCN10
            ╷
            ├── delta(tVCN10, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-tVCN10

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/low-flows/scalar/delta-tVCN10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2fde723a15b755c3235b46ed301fe5e910400248</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-tVCN10"><code>delta-tVCN10</code></a></dt><dd><span lang="en">Average change of the date of the annual minimum of 10-day mean flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la date du minimum annuel des débits moyens sur 10 jours entre l'horizon cible et la période historique</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-tVCN10_H.yaml) &middot; [back to the catalogue](../catalogue.md)
