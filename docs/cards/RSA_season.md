---
hide:
  - toc
---

# `RSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSA_season                                                   4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSA_DJF
       Cumulative daily precipitation of each winter
       Months of December, January, and February

     ◇ RSA_MAM
       Cumulative daily precipitation of each spring
       Months of March, April, and May

     ◇ RSA_JJA
       Cumulative daily precipitation of each summer
       Months of June, July, and August

     ◇ RSA_SON
       Cumulative daily precipitation of each autumn
       Months of September, October, and November

     phenomenon ─ mean precipitation
         season ─ by season
           form ─ series
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Sum
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c389b9401ad980c768cff5ab8017e8b6bcd858b7</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSA_season                                                   4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSA_DJF
       Cumul des précipitations journalières de chaque hiver
       Mois de décembre, janvier et février

     ◇ RSA_MAM
       Cumul des précipitations journalières de chaque printemps
       Mois de mars, avril et mai

     ◇ RSA_JJA
       Cumul des précipitations journalières de chaque été
       Mois de juin, juillet et août

     ◇ RSA_SON
       Cumul des précipitations journalières de chaque automne
       Mois de septembre, octobre et novembre

      phénomène ─ précipitations moyennes
         saison ─ par saison
          forme ─ série
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Somme
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c389b9401ad980c768cff5ab8017e8b6bcd858b7</pre>

**Variables produced**  [`RSA_DJF`](../catalogue.md#RSA_DJF) · [`RSA_MAM`](../catalogue.md#RSA_MAM) · [`RSA_JJA`](../catalogue.md#RSA_JJA) · [`RSA_SON`](../catalogue.md#RSA_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
