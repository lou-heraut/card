---
hide:
  - toc
---

# `TMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TMA_month                                                   12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ TMA_jan
       Average daily temperatures for each January

     ◇ TMA_feb
       Average daily temperatures for each February

     ◇ TMA_mar
       Average daily temperatures for each March

     ◇ TMA_apr
       Average daily temperatures for each April

     ◇ TMA_may
       Average daily temperatures for each May

     ◇ TMA_jun
       Average daily temperatures for each June

     ◇ TMA_jul
       Average daily temperatures for each July

     ◇ TMA_aug
       Average daily temperatures for each August

     ◇ TMA_sep
       Average daily temperatures for each September

     ◇ TMA_oct
       Average daily temperatures for each October

     ◇ TMA_nov
       Average daily temperatures for each November

     ◇ TMA_dec
       Average daily temperatures for each December

     phenomenon ─ mean temperatures
         season ─ by month
           form ─ series
           unit ─ °C
          input ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Mean
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           TMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e3c3cab5a5c2350be2912a2b9991027a839425ee</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TMA_month                                                   12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ TMA_jan (TMA_janv)
       Moyenne des températures journalières de chaque janvier

     ◇ TMA_feb (TMA_fevr)
       Moyenne des températures journalières de chaque février

     ◇ TMA_mar (TMA_mars)
       Moyenne des températures journalières de chaque mars

     ◇ TMA_apr (TMA_avril)
       Moyenne des températures journalières de chaque avril

     ◇ TMA_may (TMA_mai)
       Moyenne des températures journalières de chaque mai

     ◇ TMA_jun (TMA_juin)
       Moyenne des températures journalières de chaque juin

     ◇ TMA_jul (TMA_juil)
       Moyenne des températures journalières de chaque juillet

     ◇ TMA_aug (TMA_aout)
       Moyenne des températures journalières de chaque août

     ◇ TMA_sep (TMA_sept)
       Moyenne des températures journalières de chaque septembre

     ◇ TMA_oct
       Moyenne des températures journalières de chaque octobre

     ◇ TMA_nov
       Moyenne des températures journalières de chaque novembre

     ◇ TMA_dec
       Moyenne des températures journalières de chaque décembre

      phénomène ─ températures moyennes
         saison ─ par mois
          forme ─ série
          unité ─ °C
         entrée ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Moyenne
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           TMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e3c3cab5a5c2350be2912a2b9991027a839425ee</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#TMA_jan"><code>TMA_jan</code></a></dt><dd><span lang="en">Average daily temperatures for each January</span><span lang="fr">Moyenne des températures journalières de chaque janvier</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_feb"><code>TMA_feb</code></a></dt><dd><span lang="en">Average daily temperatures for each February</span><span lang="fr">Moyenne des températures journalières de chaque février</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_mar"><code>TMA_mar</code></a></dt><dd><span lang="en">Average daily temperatures for each March</span><span lang="fr">Moyenne des températures journalières de chaque mars</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_apr"><code>TMA_apr</code></a></dt><dd><span lang="en">Average daily temperatures for each April</span><span lang="fr">Moyenne des températures journalières de chaque avril</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_may"><code>TMA_may</code></a></dt><dd><span lang="en">Average daily temperatures for each May</span><span lang="fr">Moyenne des températures journalières de chaque mai</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_jun"><code>TMA_jun</code></a></dt><dd><span lang="en">Average daily temperatures for each June</span><span lang="fr">Moyenne des températures journalières de chaque juin</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_jul"><code>TMA_jul</code></a></dt><dd><span lang="en">Average daily temperatures for each July</span><span lang="fr">Moyenne des températures journalières de chaque juillet</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_aug"><code>TMA_aug</code></a></dt><dd><span lang="en">Average daily temperatures for each August</span><span lang="fr">Moyenne des températures journalières de chaque août</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_sep"><code>TMA_sep</code></a></dt><dd><span lang="en">Average daily temperatures for each September</span><span lang="fr">Moyenne des températures journalières de chaque septembre</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_oct"><code>TMA_oct</code></a></dt><dd><span lang="en">Average daily temperatures for each October</span><span lang="fr">Moyenne des températures journalières de chaque octobre</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_nov"><code>TMA_nov</code></a></dt><dd><span lang="en">Average daily temperatures for each November</span><span lang="fr">Moyenne des températures journalières de chaque novembre</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TMA_dec"><code>TMA_dec</code></a></dt><dd><span lang="en">Average daily temperatures for each December</span><span lang="fr">Moyenne des températures journalières de chaque décembre</span><span class="u">°C</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/series/TMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
