---
hide:
  - toc
---

# `ETPMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPMA_month                                                 12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ ETPMA_jan
       Cumulative potential evapotranspiration for each January

     ◇ ETPMA_feb
       Cumulative potential evapotranspiration for each February

     ◇ ETPMA_mar
       Cumulative potential evapotranspiration for each March

     ◇ ETPMA_apr
       Cumulative potential evapotranspiration for each April

     ◇ ETPMA_may
       Cumulative potential evapotranspiration for each May

     ◇ ETPMA_jun
       Cumulative potential evapotranspiration for each June

     ◇ ETPMA_jul
       Cumulative potential evapotranspiration for each July

     ◇ ETPMA_aug
       Cumulative potential evapotranspiration for each August

     ◇ ETPMA_sep
       Cumulative potential evapotranspiration for each September

     ◇ ETPMA_oct
       Cumulative potential evapotranspiration for each October

     ◇ ETPMA_nov
       Cumulative potential evapotranspiration for each November

     ◇ ETPMA_dec
       Cumulative potential evapotranspiration for each December

     phenomenon ─ evaporative demand
         season ─ by month
           form ─ series
           unit ─ mm
          input ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Sum
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           ETPMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   evapotranspiration/evaporative-demand/series/ETPMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:1bc39e958c68abac9c658b85a66e27a2da556b16</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPMA_month                                                 12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ ETPMA_jan (ETPMA_janv)
       Cumul de l'évapotranspiration potentielle de chaque janvier

     ◇ ETPMA_feb (ETPMA_fevr)
       Cumul de l'évapotranspiration potentielle de chaque février

     ◇ ETPMA_mar (ETPMA_mars)
       Cumul de l'évapotranspiration potentielle de chaque mars

     ◇ ETPMA_apr (ETPMA_avril)
       Cumul de l'évapotranspiration potentielle de chaque avril

     ◇ ETPMA_may (ETPMA_mai)
       Cumul de l'évapotranspiration potentielle de chaque mai

     ◇ ETPMA_jun (ETPMA_juin)
       Cumul de l'évapotranspiration potentielle de chaque juin

     ◇ ETPMA_jul (ETPMA_juil)
       Cumul de l'évapotranspiration potentielle de chaque juillet

     ◇ ETPMA_aug (ETPMA_aout)
       Cumul de l'évapotranspiration potentielle de chaque août

     ◇ ETPMA_sep (ETPMA_sept)
       Cumul de l'évapotranspiration potentielle de chaque septembre

     ◇ ETPMA_oct
       Cumul de l'évapotranspiration potentielle de chaque octobre

     ◇ ETPMA_nov
       Cumul de l'évapotranspiration potentielle de chaque novembre

     ◇ ETPMA_dec
       Cumul de l'évapotranspiration potentielle de chaque décembre

      phénomène ─ demande évaporative
         saison ─ par mois
          forme ─ série
          unité ─ mm
         entrée ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Somme
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           ETPMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   evapotranspiration/evaporative-demand/series/ETPMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:1bc39e958c68abac9c658b85a66e27a2da556b16</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#ETPMA_jan"><code>ETPMA_jan</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each January</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque janvier</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_feb"><code>ETPMA_feb</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each February</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque février</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_mar"><code>ETPMA_mar</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each March</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque mars</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_apr"><code>ETPMA_apr</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each April</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque avril</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_may"><code>ETPMA_may</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each May</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque mai</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_jun"><code>ETPMA_jun</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each June</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque juin</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_jul"><code>ETPMA_jul</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each July</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque juillet</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_aug"><code>ETPMA_aug</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each August</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque août</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_sep"><code>ETPMA_sep</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each September</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque septembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_oct"><code>ETPMA_oct</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each October</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque octobre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_nov"><code>ETPMA_nov</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each November</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque novembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPMA_dec"><code>ETPMA_dec</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration for each December</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque décembre</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/evapotranspiration/evaporative-demand/series/ETPMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
