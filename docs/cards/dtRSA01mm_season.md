---
hide:
  - toc
---

# `dtRSA01mm_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA01mm_season                                             4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA01mm_DJF
       Number of rainy days in winter
       number of days with at least 1 mm of precipitation (months of December,
       January, and February)

     ◇ dtRSA01mm_MAM
       Number of rainy days in spring
       number of days with at least 1 mm of precipitation (months of March,
       April, and May)

     ◇ dtRSA01mm_JJA
       Number of rainy days in summer
       number of days with at least 1 mm of precipitation (months of June,
       July, and August)

     ◇ dtRSA01mm_SON
       Number of rainy days in autumn
       number of days with at least 1 mm of precipitation (months of
       September, October, and November)

     phenomenon ─ wet days
         season ─ by season
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 1 mm
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRSA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRSA01mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3cc3516ebe43958ba3f2154e1673fd04dccaf580</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA01mm_season                                             4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA01mm_DJF
       Nombre de jours pluvieux en hiver
       Nombre de jours dans l'hiver avec au moins 1 mm de précipitations (mois
       de décembre, janvier et février)

     ◇ dtRSA01mm_MAM
       Nombre de jours pluvieux au printemps
       Nombre de jours au printemps avec au moins 1 mm de précipitations (mois
       de mars, avril et mai)

     ◇ dtRSA01mm_JJA
       Nombre de jours pluvieux en été
       Nombre de jours en été avec au moins 1 mm de précipitations (mois de
       juin, juillet et août)

     ◇ dtRSA01mm_SON
       Nombre de jours pluvieux en automne
       Nombre de jours en automne avec au moins 1 mm de précipitations (mois
       de septembre, octobre et novembre)

      phénomène ─ jours pluvieux
         saison ─ par saison
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 1 mm
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRSA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRSA01mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3cc3516ebe43958ba3f2154e1673fd04dccaf580</pre>

**Variables produced**  [`dtRSA01mm_DJF`](../catalogue.md#dtRSA01mm_DJF) · [`dtRSA01mm_MAM`](../catalogue.md#dtRSA01mm_MAM) · [`dtRSA01mm_JJA`](../catalogue.md#dtRSA01mm_JJA) · [`dtRSA01mm_SON`](../catalogue.md#dtRSA01mm_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtRSA01mm_season.yaml) &middot; [back to the catalogue](../catalogue.md)
