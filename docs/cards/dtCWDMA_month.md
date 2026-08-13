---
hide:
  - toc
---

# `dtCWDMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDMA_month                                               12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCWDMA_jan
       Maximum number of consecutive rainy days in each January
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each January

     ◇ dtCWDMA_feb
       Maximum number of consecutive rainy days in each February
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each February

     ◇ dtCWDMA_mar
       Maximum number of consecutive rainy days in each March
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each March

     ◇ dtCWDMA_apr
       Maximum number of consecutive rainy days in each April
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each April

     ◇ dtCWDMA_may
       Maximum number of consecutive rainy days in each May
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each May

     ◇ dtCWDMA_jun
       Maximum number of consecutive rainy days in each June
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each June

     ◇ dtCWDMA_jul
       Maximum number of consecutive rainy days in each July
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each July

     ◇ dtCWDMA_aug
       Maximum number of consecutive rainy days in each August
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each August

     ◇ dtCWDMA_sep
       Maximum number of consecutive rainy days in each September
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each September

     ◇ dtCWDMA_oct
       Maximum number of consecutive rainy days in each October
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each October

     ◇ dtCWDMA_nov
       Maximum number of consecutive rainy days in each November
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each November

     ◇ dtCWDMA_dec
       Maximum number of consecutive rainy days in each December
       Maximum number of consecutive days with at least 1 mm of precipitation
       for each December

     phenomenon ─ wet days
         season ─ by month
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  longest episode, duration
            │   └─ Length of the longest period with precipitation of at least
            │      1 mm
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtCWDMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:dbdb87c501523aeae51c4937adef3c17d7534baa</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDMA_month                                               12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCWDMA_jan (dtCWDMA_janv)
       Nombre maximal de jours pluvieux consécutifs de chaque janvier
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque janvier

     ◇ dtCWDMA_feb (dtCWDMA_fevr)
       Nombre maximal de jours pluvieux consécutifs de chaque février
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque février

     ◇ dtCWDMA_mar (dtCWDMA_mars)
       Nombre maximal de jours pluvieux consécutifs de chaque mars
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque mars

     ◇ dtCWDMA_apr (dtCWDMA_avril)
       Nombre maximal de jours pluvieux consécutifs de chaque avril
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque avril

     ◇ dtCWDMA_may (dtCWDMA_mai)
       Nombre maximal de jours pluvieux consécutifs de chaque mai
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque mai

     ◇ dtCWDMA_jun (dtCWDMA_juin)
       Nombre maximal de jours pluvieux consécutifs de chaque juin
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque juin

     ◇ dtCWDMA_jul (dtCWDMA_juil)
       Nombre maximal de jours pluvieux consécutifs de chaque juillet
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque juillet

     ◇ dtCWDMA_aug (dtCWDMA_aout)
       Nombre maximal de jours pluvieux consécutifs de chaque août
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque août

     ◇ dtCWDMA_sep (dtCWDMA_sept)
       Nombre maximal de jours pluvieux consécutifs de chaque septembre
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque septembre

     ◇ dtCWDMA_oct
       Nombre maximal de jours pluvieux consécutifs de chaque octobre
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque octobre

     ◇ dtCWDMA_nov
       Nombre maximal de jours pluvieux consécutifs de chaque novembre
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque novembre

     ◇ dtCWDMA_dec
       Nombre maximal de jours pluvieux consécutifs de chaque décembre
       Nombre maximal de jours consécutifs avec au moins 1 mm de précipitation
       de chaque décembre

      phénomène ─ jours pluvieux
         saison ─ par mois
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      d'au moins 1 mm
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtCWDMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:dbdb87c501523aeae51c4937adef3c17d7534baa</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#dtCWDMA_jan"><code>dtCWDMA_jan</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each January</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque janvier</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_feb"><code>dtCWDMA_feb</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each February</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque février</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_mar"><code>dtCWDMA_mar</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each March</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque mars</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_apr"><code>dtCWDMA_apr</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each April</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque avril</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_may"><code>dtCWDMA_may</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each May</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque mai</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_jun"><code>dtCWDMA_jun</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each June</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque juin</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_jul"><code>dtCWDMA_jul</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each July</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque juillet</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_aug"><code>dtCWDMA_aug</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each August</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque août</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_sep"><code>dtCWDMA_sep</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each September</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque septembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_oct"><code>dtCWDMA_oct</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each October</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque octobre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_nov"><code>dtCWDMA_nov</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each November</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque novembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCWDMA_dec"><code>dtCWDMA_dec</code></a></dt><dd><span lang="en">Maximum number of consecutive rainy days in each December</span><span lang="fr">Nombre maximal de jours pluvieux consécutifs de chaque décembre</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtCWDMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
