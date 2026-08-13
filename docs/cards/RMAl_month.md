---
hide:
  - toc
---

# `RMAl_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMAl_month                                                  12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMAl_jan
       Cumulative daily liquid precipitation for each January

     ◇ RMAl_feb
       Cumulative daily liquid precipitation for each February

     ◇ RMAl_mar
       Cumulative daily liquid precipitation for each March

     ◇ RMAl_apr
       Cumulative daily liquid precipitation for each April

     ◇ RMAl_may
       Cumulative daily liquid precipitation for each May

     ◇ RMAl_jun
       Cumulative daily liquid precipitation for each June

     ◇ RMAl_jul
       Cumulative daily liquid precipitation for each July

     ◇ RMAl_aug
       Cumulative daily liquid precipitation for each August

     ◇ RMAl_sep
       Cumulative daily liquid precipitation for each September

     ◇ RMAl_oct
       Cumulative daily liquid precipitation for each October

     ◇ RMAl_nov
       Cumulative daily liquid precipitation for each November

     ◇ RMAl_dec
       Cumulative daily liquid precipitation for each December

     phenomenon ─ mean precipitation
         season ─ by month
           form ─ series
           unit ─ mm
          input ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Sum
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RMAl

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RMAl_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0073c96689a908a0892d4c609da4866b510eb4e7</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMAl_month                                                  12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMAl_jan (RMAl_janv)
       Cumul des précipitations liquides journalières de chaque janvier

     ◇ RMAl_feb (RMAl_fevr)
       Cumul des précipitations liquides journalières de chaque février

     ◇ RMAl_mar (RMAl_mars)
       Cumul des précipitations liquides journalières de chaque mars

     ◇ RMAl_apr (RMAl_avril)
       Cumul des précipitations liquides journalières de chaque avril

     ◇ RMAl_may (RMAl_mai)
       Cumul des précipitations liquides journalières de chaque mai

     ◇ RMAl_jun (RMAl_juin)
       Cumul des précipitations liquides journalières de chaque juin

     ◇ RMAl_jul (RMAl_juil)
       Cumul des précipitations liquides journalières de chaque juillet

     ◇ RMAl_aug (RMAl_aout)
       Cumul des précipitations liquides journalières de chaque août

     ◇ RMAl_sep (RMAl_sept)
       Cumul des précipitations liquides journalières de chaque septembre

     ◇ RMAl_oct
       Cumul des précipitations liquides journalières de chaque octobre

     ◇ RMAl_nov
       Cumul des précipitations liquides journalières de chaque novembre

     ◇ RMAl_dec
       Cumul des précipitations liquides journalières de chaque décembre

      phénomène ─ précipitations moyennes
         saison ─ par mois
          forme ─ série
          unité ─ mm
         entrée ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Somme
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RMAl

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RMAl_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0073c96689a908a0892d4c609da4866b510eb4e7</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RMAl_jan"><code>RMAl_jan</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each January</span><span lang="fr">Cumul des précipitations liquides journalières de chaque janvier</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_feb"><code>RMAl_feb</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each February</span><span lang="fr">Cumul des précipitations liquides journalières de chaque février</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_mar"><code>RMAl_mar</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each March</span><span lang="fr">Cumul des précipitations liquides journalières de chaque mars</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_apr"><code>RMAl_apr</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each April</span><span lang="fr">Cumul des précipitations liquides journalières de chaque avril</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_may"><code>RMAl_may</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each May</span><span lang="fr">Cumul des précipitations liquides journalières de chaque mai</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_jun"><code>RMAl_jun</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each June</span><span lang="fr">Cumul des précipitations liquides journalières de chaque juin</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_jul"><code>RMAl_jul</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each July</span><span lang="fr">Cumul des précipitations liquides journalières de chaque juillet</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_aug"><code>RMAl_aug</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each August</span><span lang="fr">Cumul des précipitations liquides journalières de chaque août</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_sep"><code>RMAl_sep</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each September</span><span lang="fr">Cumul des précipitations liquides journalières de chaque septembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_oct"><code>RMAl_oct</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each October</span><span lang="fr">Cumul des précipitations liquides journalières de chaque octobre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_nov"><code>RMAl_nov</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each November</span><span lang="fr">Cumul des précipitations liquides journalières de chaque novembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAl_dec"><code>RMAl_dec</code></a></dt><dd><span lang="en">Cumulative daily liquid precipitation for each December</span><span lang="fr">Cumul des précipitations liquides journalières de chaque décembre</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RMAl_month.yaml) &middot; [back to the catalogue](../catalogue.md)
