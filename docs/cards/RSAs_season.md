---
hide:
  - toc
---

# `RSAs_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSAs_season                                                  4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSAs_DJF
       Cumulative daily solid precipitation of each winter
       Months of December, January, and February

     ◇ RSAs_MAM
       Cumulative daily solid precipitation of each spring
       Months of March, April, and May

     ◇ RSAs_JJA
       Cumulative daily solid precipitation of each summer
       Months of June, July, and August

     ◇ RSAs_SON
       Cumulative daily solid precipitation of each autumn
       Months of September, October, and November

     phenomenon ─ snow
         season ─ by season
           form ─ series
           unit ─ mm
          input ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Sum
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RSAs

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/snow/series/RSAs_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a6eeb7b29d28d26e1df3d885e4753a633021f9cb</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSAs_season                                                  4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSAs_DJF
       Cumul des précipitations solides journalières de chaque hiver
       Mois de décembre, janvier et février

     ◇ RSAs_MAM
       Cumul des précipitations solides journalières de chaque printemps
       Mois de mars, avril et mai

     ◇ RSAs_JJA
       Cumul des précipitations solides journalières de chaque été
       Mois de juin, juillet et août

     ◇ RSAs_SON
       Cumul des précipitations solides journalières de chaque automne
       Mois de septembre, octobre et novembre

      phénomène ─ neige
         saison ─ par saison
          forme ─ série
          unité ─ mm
         entrée ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Somme
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RSAs

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/snow/series/RSAs_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a6eeb7b29d28d26e1df3d885e4753a633021f9cb</pre>

**Variables produced**  [`RSAs_DJF`](../catalogue.md#RSAs_DJF) · [`RSAs_MAM`](../catalogue.md#RSAs_MAM) · [`RSAs_JJA`](../catalogue.md#RSAs_JJA) · [`RSAs_SON`](../catalogue.md#RSAs_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/series/RSAs_season.yaml) &middot; [back to the catalogue](../catalogue.md)
