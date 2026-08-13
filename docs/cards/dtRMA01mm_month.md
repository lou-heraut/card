---
hide:
  - toc
---

# `dtRMA01mm_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA01mm_month                                             12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA01mm_jan
       Number of rainy days of each January
       Number of days with at least 1 mm of precipitation of each January

     ◇ dtRMA01mm_feb
       Number of rainy days of each February
       Number of days with at least 1 mm of precipitation of each February

     ◇ dtRMA01mm_mar
       Number of rainy days of each March
       Number of days with at least 1 mm of precipitation of each March

     ◇ dtRMA01mm_apr
       Number of rainy days of each April
       Number of days with at least 1 mm of precipitation of each April

     ◇ dtRMA01mm_may
       Number of rainy days of each May
       Number of days with at least 1 mm of precipitation of each May

     ◇ dtRMA01mm_jun
       Number of rainy days of each June
       Number of days with at least 1 mm of precipitation of each June

     ◇ dtRMA01mm_jul
       Number of rainy days of each July
       Number of days with at least 1 mm of precipitation of each July

     ◇ dtRMA01mm_aug
       Number of rainy days of each August
       Number of days with at least 1 mm of precipitation of each August

     ◇ dtRMA01mm_sep
       Number of rainy days of each September
       Number of days with at least 1 mm of precipitation of each September

     ◇ dtRMA01mm_oct
       Number of rainy days of each October
       Number of days with at least 1 mm of precipitation of each October

     ◇ dtRMA01mm_nov
       Number of rainy days of each November
       Number of days with at least 1 mm of precipitation of each November

     ◇ dtRMA01mm_dec
       Number of rainy days of each December
       Number of days with at least 1 mm of precipitation of each December

     phenomenon ─ wet days
         season ─ by month
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 1 mm
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRMA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRMA01mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:19fe02ff4014300fc83ec3a3056b7fdab0f58f73</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA01mm_month                                             12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA01mm_jan (dtRMA01mm_janv)
       Nombre de jours pluvieux de chaque janvier
       Nombre de jours avec au moins 1 mm de précipitations de chaque janvier

     ◇ dtRMA01mm_feb (dtRMA01mm_fevr)
       Nombre de jours pluvieux de chaque février
       Nombre de jours avec au moins 1 mm de précipitations de chaque février

     ◇ dtRMA01mm_mar (dtRMA01mm_mars)
       Nombre de jours pluvieux de chaque mars
       Nombre de jours avec au moins 1 mm de précipitations de chaque mars

     ◇ dtRMA01mm_apr (dtRMA01mm_avril)
       Nombre de jours pluvieux de chaque avril
       Nombre de jours avec au moins 1 mm de précipitations de chaque avril

     ◇ dtRMA01mm_may (dtRMA01mm_mai)
       Nombre de jours pluvieux de chaque mai
       Nombre de jours avec au moins 1 mm de précipitations de chaque mai

     ◇ dtRMA01mm_jun (dtRMA01mm_juin)
       Nombre de jours pluvieux de chaque juin
       Nombre de jours avec au moins 1 mm de précipitations de chaque juin

     ◇ dtRMA01mm_jul (dtRMA01mm_juil)
       Nombre de jours pluvieux de chaque juillet
       Nombre de jours avec au moins 1 mm de précipitations de chaque juillet

     ◇ dtRMA01mm_aug (dtRMA01mm_aout)
       Nombre de jours pluvieux de chaque août
       Nombre de jours avec au moins 1 mm de précipitations de chaque août

     ◇ dtRMA01mm_sep (dtRMA01mm_sept)
       Nombre de jours pluvieux de chaque septembre
       Nombre de jours avec au moins 1 mm de précipitations de chaque
       septembre

     ◇ dtRMA01mm_oct
       Nombre de jours pluvieux de chaque octobre
       Nombre de jours avec au moins 1 mm de précipitations de chaque octobre

     ◇ dtRMA01mm_nov
       Nombre de jours pluvieux de chaque novembre
       Nombre de jours avec au moins 1 mm de précipitations de chaque novembre

     ◇ dtRMA01mm_dec
       Nombre de jours pluvieux de chaque décembre
       Nombre de jours avec au moins 1 mm de précipitations de chaque décembre

      phénomène ─ jours pluvieux
         saison ─ par mois
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 1 mm
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRMA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRMA01mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:19fe02ff4014300fc83ec3a3056b7fdab0f58f73</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#dtRMA01mm_jan"><code>dtRMA01mm_jan</code></a></dt><dd><span lang="en">Number of rainy days of each January</span><span lang="fr">Nombre de jours pluvieux de chaque janvier</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_feb"><code>dtRMA01mm_feb</code></a></dt><dd><span lang="en">Number of rainy days of each February</span><span lang="fr">Nombre de jours pluvieux de chaque février</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_mar"><code>dtRMA01mm_mar</code></a></dt><dd><span lang="en">Number of rainy days of each March</span><span lang="fr">Nombre de jours pluvieux de chaque mars</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_apr"><code>dtRMA01mm_apr</code></a></dt><dd><span lang="en">Number of rainy days of each April</span><span lang="fr">Nombre de jours pluvieux de chaque avril</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_may"><code>dtRMA01mm_may</code></a></dt><dd><span lang="en">Number of rainy days of each May</span><span lang="fr">Nombre de jours pluvieux de chaque mai</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_jun"><code>dtRMA01mm_jun</code></a></dt><dd><span lang="en">Number of rainy days of each June</span><span lang="fr">Nombre de jours pluvieux de chaque juin</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_jul"><code>dtRMA01mm_jul</code></a></dt><dd><span lang="en">Number of rainy days of each July</span><span lang="fr">Nombre de jours pluvieux de chaque juillet</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_aug"><code>dtRMA01mm_aug</code></a></dt><dd><span lang="en">Number of rainy days of each August</span><span lang="fr">Nombre de jours pluvieux de chaque août</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_sep"><code>dtRMA01mm_sep</code></a></dt><dd><span lang="en">Number of rainy days of each September</span><span lang="fr">Nombre de jours pluvieux de chaque septembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_oct"><code>dtRMA01mm_oct</code></a></dt><dd><span lang="en">Number of rainy days of each October</span><span lang="fr">Nombre de jours pluvieux de chaque octobre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_nov"><code>dtRMA01mm_nov</code></a></dt><dd><span lang="en">Number of rainy days of each November</span><span lang="fr">Nombre de jours pluvieux de chaque novembre</span><span class="u">day</span></dd><dt><a href="../../catalogue/#dtRMA01mm_dec"><code>dtRMA01mm_dec</code></a></dt><dd><span lang="en">Number of rainy days of each December</span><span lang="fr">Nombre de jours pluvieux de chaque décembre</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtRMA01mm_month.yaml) &middot; [back to the catalogue](../catalogue.md)
