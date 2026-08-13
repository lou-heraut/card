---
hide:
  - toc
---

# `QMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMA_month                                                   12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QMA_jan
       Average daily discharge for each January

     ◇ QMA_feb
       Average daily discharge for each February

     ◇ QMA_mar
       Average daily discharge for each March

     ◇ QMA_apr
       Average daily discharge for each April

     ◇ QMA_may
       Average daily discharge for each May

     ◇ QMA_jun
       Average daily discharge for each June

     ◇ QMA_jul
       Average daily discharge for each July

     ◇ QMA_aug
       Average daily discharge for each August

     ◇ QMA_sep
       Average daily discharge for each September

     ◇ QMA_oct
       Average daily discharge for each October

     ◇ QMA_nov
       Average daily discharge for each November

     ◇ QMA_dec
       Average daily discharge for each December

     phenomenon ─ mean flows
         season ─ by month
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:12859c9e0bb9417db8645687d7489db36f1e8ff0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMA_month                                                   12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QMA_jan (QMA_janv)
       Moyenne des débits journaliers de chaque janvier

     ◇ QMA_feb (QMA_fevr)
       Moyenne des débits journaliers de chaque février

     ◇ QMA_mar (QMA_mars)
       Moyenne des débits journaliers de chaque mars

     ◇ QMA_apr (QMA_avril)
       Moyenne des débits journaliers de chaque avril

     ◇ QMA_may (QMA_mai)
       Moyenne des débits journaliers de chaque mai

     ◇ QMA_jun (QMA_juin)
       Moyenne des débits journaliers de chaque juin

     ◇ QMA_jul (QMA_juil)
       Moyenne des débits journaliers de chaque juillet

     ◇ QMA_aug (QMA_aout)
       Moyenne des débits journaliers de chaque août

     ◇ QMA_sep (QMA_sept)
       Moyenne des débits journaliers de chaque septembre

     ◇ QMA_oct
       Moyenne des débits journaliers de chaque octobre

     ◇ QMA_nov
       Moyenne des débits journaliers de chaque novembre

     ◇ QMA_dec
       Moyenne des débits journaliers de chaque décembre

      phénomène ─ moyennes eaux
         saison ─ par mois
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:12859c9e0bb9417db8645687d7489db36f1e8ff0</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QMA_jan"><code>QMA_jan</code></a></dt><dd><span lang="en">Average daily discharge for each January</span><span lang="fr">Moyenne des débits journaliers de chaque janvier</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_feb"><code>QMA_feb</code></a></dt><dd><span lang="en">Average daily discharge for each February</span><span lang="fr">Moyenne des débits journaliers de chaque février</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_mar"><code>QMA_mar</code></a></dt><dd><span lang="en">Average daily discharge for each March</span><span lang="fr">Moyenne des débits journaliers de chaque mars</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_apr"><code>QMA_apr</code></a></dt><dd><span lang="en">Average daily discharge for each April</span><span lang="fr">Moyenne des débits journaliers de chaque avril</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_may"><code>QMA_may</code></a></dt><dd><span lang="en">Average daily discharge for each May</span><span lang="fr">Moyenne des débits journaliers de chaque mai</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_jun"><code>QMA_jun</code></a></dt><dd><span lang="en">Average daily discharge for each June</span><span lang="fr">Moyenne des débits journaliers de chaque juin</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_jul"><code>QMA_jul</code></a></dt><dd><span lang="en">Average daily discharge for each July</span><span lang="fr">Moyenne des débits journaliers de chaque juillet</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_aug"><code>QMA_aug</code></a></dt><dd><span lang="en">Average daily discharge for each August</span><span lang="fr">Moyenne des débits journaliers de chaque août</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_sep"><code>QMA_sep</code></a></dt><dd><span lang="en">Average daily discharge for each September</span><span lang="fr">Moyenne des débits journaliers de chaque septembre</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_oct"><code>QMA_oct</code></a></dt><dd><span lang="en">Average daily discharge for each October</span><span lang="fr">Moyenne des débits journaliers de chaque octobre</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_nov"><code>QMA_nov</code></a></dt><dd><span lang="en">Average daily discharge for each November</span><span lang="fr">Moyenne des débits journaliers de chaque novembre</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QMA_dec"><code>QMA_dec</code></a></dt><dd><span lang="en">Average daily discharge for each December</span><span lang="fr">Moyenne des débits journaliers de chaque décembre</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/series/QMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
