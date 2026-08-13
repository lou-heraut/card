---
hide:
  - toc
---

# `dtRSA50mm_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA50mm_season                                             4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA50mm_DJF
       Number of extreme rain days in winter
       Number of days with at least 50 mm of precipitation (months of
       December, January, and February)

     ◇ dtRSA50mm_MAM
       Number of extreme rain days in spring
       Number of days with at least 50 mm of precipitation (months of March,
       April, and May)

     ◇ dtRSA50mm_JJA
       Number of extreme rain days in summer
       Number of days with at least 50 mm of precipitation (months of June,
       July, and August)

     ◇ dtRSA50mm_SON
       Number of extreme rain days in autumn
       Number of days with at least 50 mm of precipitation (months of
       September, October, and November)

     phenomenon ─ heavy rain
         season ─ by season
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 50 mm
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRSA50mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRSA50mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:793dd6403de543691a7ef7f7d38a008e0a9753f0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRSA50mm_season                                             4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRSA50mm_DJF
       Nombre de jours de pluie extrême en hiver
       Nombre de jours dans l'hiver avec au moins 50 mm de précipitations
       (mois de décembre, janvier et février)

     ◇ dtRSA50mm_MAM
       Nombre de jours de pluie extrême au printemps
       Nombre de jours au printemps avec au moins 50 mm de précipitations
       (mois de mars, avril et mai)

     ◇ dtRSA50mm_JJA
       Nombre de jours de pluie extrême en été
       Nombre de jours en été avec au moins 50 mm de précipitations (mois de
       juin, juillet et août)

     ◇ dtRSA50mm_SON
       Nombre de jours de pluie extrême en automne
       Nombre de jours en automne avec au moins 50 mm de précipitations (mois
       de septembre, octobre et novembre)

      phénomène ─ pluies fortes
         saison ─ par saison
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 50 mm
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRSA50mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRSA50mm_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:793dd6403de543691a7ef7f7d38a008e0a9753f0</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#dtRSA50mm_DJF"><code>dtRSA50mm_DJF</code></a></dt><dd><span lang="en">Number of extreme rain days in winter</span><span lang="fr">Nombre de jours de pluie extrême en hiver</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRSA50mm_MAM"><code>dtRSA50mm_MAM</code></a></dt><dd><span lang="en">Number of extreme rain days in spring</span><span lang="fr">Nombre de jours de pluie extrême au printemps</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRSA50mm_JJA"><code>dtRSA50mm_JJA</code></a></dt><dd><span lang="en">Number of extreme rain days in summer</span><span lang="fr">Nombre de jours de pluie extrême en été</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRSA50mm_SON"><code>dtRSA50mm_SON</code></a></dt><dd><span lang="en">Number of extreme rain days in autumn</span><span lang="fr">Nombre de jours de pluie extrême en automne</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/dtRSA50mm_season.yaml) &middot; [back to the catalogue](../catalogue.md)
