---
hide:
  - toc
---

# `dtCDDMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDMA_month                                               12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCDDMA_jan
       Maximum number of consecutive dry days in each January
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each January

     ◇ dtCDDMA_feb
       Maximum number of consecutive dry days in each February
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each February

     ◇ dtCDDMA_mar
       Maximum number of consecutive dry days in each March
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each March

     ◇ dtCDDMA_apr
       Maximum number of consecutive dry days in each April
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each April

     ◇ dtCDDMA_may
       Maximum number of consecutive dry days in each May
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each May

     ◇ dtCDDMA_jun
       Maximum number of consecutive dry days in each June
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each June

     ◇ dtCDDMA_jul
       Maximum number of consecutive dry days in each July
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each July

     ◇ dtCDDMA_aug
       Maximum number of consecutive dry days in each August
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each August

     ◇ dtCDDMA_sep
       Maximum number of consecutive dry days in each September
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each September

     ◇ dtCDDMA_oct
       Maximum number of consecutive dry days in each October
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each October

     ◇ dtCDDMA_nov
       Maximum number of consecutive dry days in each November
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each November

     ◇ dtCDDMA_dec
       Maximum number of consecutive dry days in each December
       Maximum number of consecutive days with less than 1 mm of precipitation
       in each December

     phenomenon ─ dry spells
         season ─ by month
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, longest episode, duration
            │   └─ Length of the longest period with precipitation below 1 mm
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtCDDMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c2ce56ba41a5b3ffb58142d93c81eed3f13bc984</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDMA_month                                               12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCDDMA_jan (dtCDDMA_janv)
       Nombre maximal de jours secs consécutifs de chaque janvier
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque janvier

     ◇ dtCDDMA_feb (dtCDDMA_fevr)
       Nombre maximal de jours secs consécutifs de chaque février
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque février

     ◇ dtCDDMA_mar (dtCDDMA_mars)
       Nombre maximal de jours secs consécutifs de chaque mars
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque mars

     ◇ dtCDDMA_apr (dtCDDMA_avril)
       Nombre maximal de jours secs consécutifs de chaque avril
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque avril

     ◇ dtCDDMA_may (dtCDDMA_mai)
       Nombre maximal de jours secs consécutifs de chaque mai
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque mai

     ◇ dtCDDMA_jun (dtCDDMA_juin)
       Nombre maximal de jours secs consécutifs de chaque juin
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque juin

     ◇ dtCDDMA_jul (dtCDDMA_juil)
       Nombre maximal de jours secs consécutifs de chaque juillet
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque juillet

     ◇ dtCDDMA_aug (dtCDDMA_aout)
       Nombre maximal de jours secs consécutifs de chaque août
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque août

     ◇ dtCDDMA_sep (dtCDDMA_sept)
       Nombre maximal de jours secs consécutifs de chaque septembre
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque septembre

     ◇ dtCDDMA_oct
       Nombre maximal de jours secs consécutifs de chaque octobre
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque octobre

     ◇ dtCDDMA_nov
       Nombre maximal de jours secs consécutifs de chaque novembre
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque novembre

     ◇ dtCDDMA_dec
       Nombre maximal de jours secs consécutifs de chaque décembre
       Nombre maximal de jours consécutifs avec moins de 1 mm de précipitation
       de chaque décembre

      phénomène ─ périodes sèches
         saison ─ par mois
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      inférieures à 1 mm
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtCDDMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c2ce56ba41a5b3ffb58142d93c81eed3f13bc984</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#dtCDDMA_jan"><code>dtCDDMA_jan</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each January</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque janvier</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_feb"><code>dtCDDMA_feb</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each February</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque février</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_mar"><code>dtCDDMA_mar</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each March</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque mars</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_apr"><code>dtCDDMA_apr</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each April</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque avril</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_may"><code>dtCDDMA_may</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each May</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque mai</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_jun"><code>dtCDDMA_jun</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each June</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque juin</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_jul"><code>dtCDDMA_jul</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each July</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque juillet</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_aug"><code>dtCDDMA_aug</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each August</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque août</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_sep"><code>dtCDDMA_sep</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each September</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque septembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_oct"><code>dtCDDMA_oct</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each October</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque octobre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_nov"><code>dtCDDMA_nov</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each November</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque novembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtCDDMA_dec"><code>dtCDDMA_dec</code></a></dt><dd><span lang="en">Maximum number of consecutive dry days in each December</span><span lang="fr">Nombre maximal de jours secs consécutifs de chaque décembre</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/dry-spells/series/dtCDDMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
