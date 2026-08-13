---
hide:
  - toc
---

# `tVCN10_summer`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10_summer          Date of the summer minimum of 10-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Months from May to November

     phenomenon ─ low flows
         season ─ summer
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
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           tVCN10_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/tVCN10_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:70989038eb9804a507e21f3f913dc6af41a16b34</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10_summer   Date du minimum estival des débits moyens sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Mois de mai à novembre

      phénomène ─ basses eaux
         saison ─ estivale
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
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           tVCN10_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/tVCN10_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:70989038eb9804a507e21f3f913dc6af41a16b34</pre>

**Variables produced**  [`tVCN10_summer`](../catalogue.md#tVCN10_summer)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/tVCN10_summer.yaml) &middot; [back to the catalogue](../catalogue.md)
