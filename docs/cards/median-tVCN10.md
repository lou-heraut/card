---
hide:
  - toc
---

# `median-tVCN10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tVCN10   Inter-annual median of the dates of the annual minimum  │
  │                                                    of 10-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanargmin(VC10)
            │   └─ Date of the minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           tVCN10
            ╷
            ├── circular_median(tVCN10)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-tVCN10

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/low-flows/scalar/median-tVCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0cdf7ad135147e50c7f5e416e8c105b9b4168987</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tVCN10   Médiane inter-annuelle des dates du minimum annuel des  │
  │                                              débits moyens sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanargmin(VC10)
            │   └─ Date du minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           tVCN10
            ╷
            ├── circular_median(tVCN10)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-tVCN10

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/low-flows/scalar/median-tVCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0cdf7ad135147e50c7f5e416e8c105b9b4168987</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-tVCN10"><code>median-tVCN10</code></a></dt><dd><span lang="en">Inter-annual median of the dates of the annual minimum of 10-day mean flows</span><span lang="fr">Médiane inter-annuelle des dates du minimum annuel des débits moyens sur 10 jours</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/median-tVCN10.yaml) &middot; [back to the catalogue](../catalogue.md)
