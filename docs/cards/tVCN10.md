---
hide:
  - toc
---

# `tVCN10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10                 Date of the annual minimum of 10-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ series
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

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

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/tVCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bc6035182ce7038e603eb1378d1bc1041be58641</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10           Date du minimum annuel des débits moyens sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ série
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

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

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/tVCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bc6035182ce7038e603eb1378d1bc1041be58641</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#tVCN10"><code>tVCN10</code></a></dt><dd><span lang="en">Date of the annual minimum of 10-day mean flows</span><span lang="fr">Date du minimum annuel des débits moyens sur 10 jours</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/tVCN10.yaml) &middot; [back to the catalogue](../catalogue.md)
