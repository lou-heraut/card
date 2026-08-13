---
hide:
  - toc
---

# `RSAl_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSAl_season                                                  4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSAl_DJF
       Cumulative daily liquid precipitation of each winter
       Months of December, January, and February

     ◇ RSAl_MAM
       Cumulative daily liquid precipitation of each spring
       Months of March, April, and May

     ◇ RSAl_JJA
       Cumulative daily liquid precipitation of each summer
       Months of June, July, and August

     ◇ RSAl_SON
       Cumulative daily liquid precipitation of each autumn
       Months of September, October, and November

     phenomenon ─ mean precipitation
         season ─ by season
           form ─ series
           unit ─ mm
          input ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Sum
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RSAl

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RSAl_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:1a75a039b973ecc4596453c7d22f8c22746a303b</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RSAl_season                                                  4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RSAl_DJF
       Cumul des précipitations liquides journalières de chaque hiver
       Mois de décembre, janvier et février

     ◇ RSAl_MAM
       Cumul des précipitations liquides journalières de chaque printemps
       Mois de mars, avril et mai

     ◇ RSAl_JJA
       Cumul des précipitations liquides journalières de chaque été
       Mois de juin, juillet et août

     ◇ RSAl_SON
       Cumul des précipitations liquides journalières de chaque automne
       Mois de septembre, octobre et novembre

      phénomène ─ précipitations moyennes
         saison ─ par saison
          forme ─ série
          unité ─ mm
         entrée ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Somme
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RSAl

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RSAl_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:1a75a039b973ecc4596453c7d22f8c22746a303b</pre>

**Variables produced**  [`RSAl_DJF`](../catalogue.md#RSAl_DJF) · [`RSAl_MAM`](../catalogue.md#RSAl_MAM) · [`RSAl_JJA`](../catalogue.md#RSAl_JJA) · [`RSAl_SON`](../catalogue.md#RSAl_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RSAl_season.yaml) &middot; [back to the catalogue](../catalogue.md)
