---
hide:
  - toc
---

# `RMAs_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMAs_month                                                  12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMAs_jan
       Cumulative daily solid precipitation for each January

     ◇ RMAs_feb
       Cumulative daily solid precipitation for each February

     ◇ RMAs_mar
       Cumulative daily solid precipitation for each March

     ◇ RMAs_apr
       Cumulative daily solid precipitation for each April

     ◇ RMAs_may
       Cumulative daily solid precipitation for each May

     ◇ RMAs_jun
       Cumulative daily solid precipitation for each June

     ◇ RMAs_jul
       Cumulative daily solid precipitation for each July

     ◇ RMAs_aug
       Cumulative daily solid precipitation for each August

     ◇ RMAs_sep
       Cumulative daily solid precipitation for each September

     ◇ RMAs_oct
       Cumulative daily solid precipitation for each October

     ◇ RMAs_nov
       Cumulative daily solid precipitation for each November

     ◇ RMAs_dec
       Cumulative daily solid precipitation for each December

     phenomenon ─ snow
         season ─ by month
           form ─ series
           unit ─ mm
          input ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Sum
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RMAs

  ──────────────────────────────────────────────────────────────────────────
  v2.0   precipitation/snow/series/RMAs_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:622a5382fedaccdab3e3d267c25b061bfa2807a0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMAs_month                                                  12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMAs_jan (RMAs_janv)
       Cumul des précipitations solides journalières de chaque janvier

     ◇ RMAs_feb (RMAs_fevr)
       Cumul des précipitations solides journalières de chaque février

     ◇ RMAs_mar (RMAs_mars)
       Cumul des précipitations solides journalières de chaque mars

     ◇ RMAs_apr (RMAs_avril)
       Cumul des précipitations solides journalières de chaque avril

     ◇ RMAs_may (RMAs_mai)
       Cumul des précipitations solides journalières de chaque mai

     ◇ RMAs_jun (RMAs_juin)
       Cumul des précipitations solides journalières de chaque juin

     ◇ RMAs_jul (RMAs_juil)
       Cumul des précipitations solides journalières de chaque juillet

     ◇ RMAs_aug (RMAs_aout)
       Cumul des précipitations solides journalières de chaque août

     ◇ RMAs_sep (RMAs_sept)
       Cumul des précipitations solides journalières de chaque septembre

     ◇ RMAs_oct
       Cumul des précipitations solides journalières de chaque octobre

     ◇ RMAs_nov
       Cumul des précipitations solides journalières de chaque novembre

     ◇ RMAs_dec
       Cumul des précipitations solides journalières de chaque décembre

      phénomène ─ neige
         saison ─ par mois
          forme ─ série
          unité ─ mm
         entrée ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Somme
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RMAs

  ──────────────────────────────────────────────────────────────────────────
  v2.0   precipitation/snow/series/RMAs_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:622a5382fedaccdab3e3d267c25b061bfa2807a0</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RMAs_jan"><code>RMAs_jan</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each January</span><span lang="fr">Cumul des précipitations solides journalières de chaque janvier</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_feb"><code>RMAs_feb</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each February</span><span lang="fr">Cumul des précipitations solides journalières de chaque février</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_mar"><code>RMAs_mar</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each March</span><span lang="fr">Cumul des précipitations solides journalières de chaque mars</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_apr"><code>RMAs_apr</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each April</span><span lang="fr">Cumul des précipitations solides journalières de chaque avril</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_may"><code>RMAs_may</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each May</span><span lang="fr">Cumul des précipitations solides journalières de chaque mai</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_jun"><code>RMAs_jun</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each June</span><span lang="fr">Cumul des précipitations solides journalières de chaque juin</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_jul"><code>RMAs_jul</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each July</span><span lang="fr">Cumul des précipitations solides journalières de chaque juillet</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_aug"><code>RMAs_aug</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each August</span><span lang="fr">Cumul des précipitations solides journalières de chaque août</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_sep"><code>RMAs_sep</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each September</span><span lang="fr">Cumul des précipitations solides journalières de chaque septembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_oct"><code>RMAs_oct</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each October</span><span lang="fr">Cumul des précipitations solides journalières de chaque octobre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_nov"><code>RMAs_nov</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each November</span><span lang="fr">Cumul des précipitations solides journalières de chaque novembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RMAs_dec"><code>RMAs_dec</code></a></dt><dd><span lang="en">Cumulative daily solid precipitation for each December</span><span lang="fr">Cumul des précipitations solides journalières de chaque décembre</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/series/RMAs_month.yaml) &middot; [back to the catalogue](../catalogue.md)
