---
hide:
  - toc
---

# `dtRSA20mm_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA20mm_season                                             4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA20mm_DJF
       Number of heavy rain days in winter
       number of days with at least 20 mm of precipitation (months of
       December, January, and February)

     ◇ dtRSA20mm_MAM
       Number of heavy rain days in spring
       number of days with at least 20 mm of precipitation (months of March,
       April, and May)

     ◇ dtRSA20mm_JJA
       Number of heavy rain days in summer
       number of days with at least 20 mm of precipitation (months of June,
       July, and August)

     ◇ dtRSA20mm_SON
       Number of heavy rain days in autumn
       number of days with at least 20 mm of precipitation (months of
       September, October, and November)

     phenomenon ─ heavy rain
         season ─ by season
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 20 mm
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRSA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRSA20mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0b9f5977cc5b981d2fe620c056ec8b17390ef5d6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA20mm_season                                             4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA20mm_DJF
       Nombre de jours de forte pluie en hiver
       Nombre de jours dans l'hiver avec au moins 20 mm de précipitations
       (mois de décembre, janvier et février)

     ◇ dtRSA20mm_MAM
       Nombre de jours de forte pluie au printemps
       Nombre de jours au printemps avec au moins 20 mm de précipitations
       (mois de mars, avril et mai)

     ◇ dtRSA20mm_JJA
       Nombre de jours de forte pluie en été
       Nombre de jours en été avec au moins 20 mm de précipitations (mois de
       juin, juillet et août)

     ◇ dtRSA20mm_SON
       Nombre de jours de forte pluie en automne
       Nombre de jours en automne avec au moins 20 mm de précipitations (mois
       de septembre, octobre et novembre)

      phénomène ─ pluies fortes
         saison ─ par saison
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 20 mm
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRSA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRSA20mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0b9f5977cc5b981d2fe620c056ec8b17390ef5d6</pre>

**Variables produced**  [`dtRSA20mm_DJF`](../catalogue.md#dtRSA20mm_DJF) · [`dtRSA20mm_MAM`](../catalogue.md#dtRSA20mm_MAM) · [`dtRSA20mm_JJA`](../catalogue.md#dtRSA20mm_JJA) · [`dtRSA20mm_SON`](../catalogue.md#dtRSA20mm_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/dtRSA20mm_season.yaml) &middot; [back to the catalogue](../catalogue.md)
