---
hide:
  - toc
---

# `dtCWDSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDSA_season                                               4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCWDSA_DJF
       Maximum number of consecutive rainy days in winter
       Maximum number of consecutive days in winter with at least 1 mm of
       precipitation (months of December, January, and February)

     ◇ dtCWDSA_MAM
       Maximum number of consecutive rainy days in spring
       Maximum number of consecutive days in spring with at least 1 mm of
       precipitation (months of March, April, and May)

     ◇ dtCWDSA_JJA
       Maximum number of consecutive rainy days in summer
       Maximum number of consecutive days in summer with at least 1 mm of
       precipitation (months of June, July, and August)

     ◇ dtCWDSA_SON
       Maximum number of consecutive rainy days in autumn
       Maximum number of consecutive days in autumn with at least 1 mm of
       precipitation (months of September, October, and November)

     phenomenon ─ wet days
         season ─ by season
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  longest episode, duration
            │   └─ Length of the longest period with precipitation of at least
            │      1 mm
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtCWDSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:98075e32f5d2aeffd55a0f391aa029b59e0b8366</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDSA_season                                               4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCWDSA_DJF
       Nombre maximal de jours pluvieux consécutifs dans l'hiver
       Nombre maximal de jours consécutifs dans l'hiver avec au moins 1 mm de
       précipitation (mois de décembre, janvier et février)

     ◇ dtCWDSA_MAM
       Nombre maximal de jours pluvieux consécutifs au printemps
       Nombre maximal de jours consécutifs au printemps avec au moins 1 mm de
       précipitation (mois de mars, avril et mai)

     ◇ dtCWDSA_JJA
       Nombre maximal de jours pluvieux consécutifs en été
       Nombre maximal de jours consécutifs en été avec au moins 1 mm de
       précipitation (mois de juin, juillet et août)

     ◇ dtCWDSA_SON
       Nombre maximal de jours pluvieux consécutifs en automne
       Nombre maximal de jours consécutifs en automne avec au moins 1 mm de
       précipitation (mois de septembre, octobre et novembre)

      phénomène ─ jours pluvieux
         saison ─ par saison
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      d'au moins 1 mm
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtCWDSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:98075e32f5d2aeffd55a0f391aa029b59e0b8366</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#dtCWDSA_DJF"><code>dtCWDSA_DJF</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in winter</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs dans l'hiver</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDSA_MAM"><code>dtCWDSA_MAM</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in spring</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs au printemps</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDSA_JJA"><code>dtCWDSA_JJA</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in summer</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs en été</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDSA_SON"><code>dtCWDSA_SON</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in autumn</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs en automne</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtCWDSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
