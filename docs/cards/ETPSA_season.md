---
hide:
  - toc
---

# `ETPSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPSA_season                                                 4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ ETPSA_DJF
       Cumulative potential evapotranspiration of each winter
       Months of December, January, and February

     ◇ ETPSA_MAM
       Cumulative potential evapotranspiration of each spring
       Months of March, April, and May

     ◇ ETPSA_JJA
       Cumulative potential evapotranspiration of each summer
       Months of June, July, and August

     ◇ ETPSA_SON
       Cumulative potential evapotranspiration of each autumn
       Months of September, October, and November

     phenomenon ─ evaporative demand
         season ─ by season
           form ─ series
           unit ─ mm
          input ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Sum
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           ETPSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   evapotranspiration/evaporative-demand/series/ETPSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3b012aa1c680a0b3139909d81ab442199e68f4b5</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPSA_season                                                 4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ ETPSA_DJF
       Cumul de l'évapotranspiration potentielle de chaque hiver
       Mois de décembre, janvier et février

     ◇ ETPSA_MAM
       Cumul de l'évapotranspiration potentielle de chaque printemps
       Mois de mars, avril et mai

     ◇ ETPSA_JJA
       Cumul de l'évapotranspiration potentielle de chaque été
       Mois de juin, juillet et août

     ◇ ETPSA_SON
       Cumul de l'évapotranspiration potentielle de chaque automne
       Mois de septembre, octobre et novembre

      phénomène ─ demande évaporative
         saison ─ par saison
          forme ─ série
          unité ─ mm
         entrée ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Somme
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           ETPSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   evapotranspiration/evaporative-demand/series/ETPSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3b012aa1c680a0b3139909d81ab442199e68f4b5</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#ETPSA_DJF"><code>ETPSA_DJF</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration of each winter</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque hiver</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPSA_MAM"><code>ETPSA_MAM</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration of each spring</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque printemps</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPSA_JJA"><code>ETPSA_JJA</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration of each summer</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque été</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#ETPSA_SON"><code>ETPSA_SON</code></a></dt><dd><span lang="en">Cumulative potential evapotranspiration of each autumn</span><span lang="fr">Cumul de l'évapotranspiration potentielle de chaque automne</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/evapotranspiration/evaporative-demand/series/ETPSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
