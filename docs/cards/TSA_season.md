---
hide:
  - toc
---

# `TSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TSA_season                                                   4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ TSA_DJF
       Annual winter temperatures
       Months of December, January, and February

     ◇ TSA_MAM
       Annual spring temperatures
       Months of March, April, and May

     ◇ TSA_JJA
       Annual summer temperatures
       Months of June, July, and August

     ◇ TSA_SON
       Annual autumn temperatures
       Months of September, October, and November

     phenomenon ─ mean temperatures
         season ─ by season
           form ─ series
           unit ─ °C
          input ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Mean
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           TSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0f9c9445c3284a464c82876fcb0626f4f99ea262</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TSA_season                                                   4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ TSA_DJF
       Températures hivernales annuelles
       Mois de décembre, janvier et février

     ◇ TSA_MAM
       Températures printanières annuelles
       Mois de mars, avril et mai

     ◇ TSA_JJA
       Températures estivales annuelles
       Mois de juin, juillet et août

     ◇ TSA_SON
       Températures automnales annuelles
       Mois de septembre, octobre et novembre

      phénomène ─ températures moyennes
         saison ─ par saison
          forme ─ série
          unité ─ °C
         entrée ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Moyenne
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           TSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0f9c9445c3284a464c82876fcb0626f4f99ea262</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#TSA_DJF"><code>TSA_DJF</code></a></dt><dd><span lang="en">Annual winter temperatures</span><span lang="fr">Températures hivernales annuelles</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TSA_MAM"><code>TSA_MAM</code></a></dt><dd><span lang="en">Annual spring temperatures</span><span lang="fr">Températures printanières annuelles</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TSA_JJA"><code>TSA_JJA</code></a></dt><dd><span lang="en">Annual summer temperatures</span><span lang="fr">Températures estivales annuelles</span><span class="u">°C</span></dd><dt><a href="../../catalogue/#TSA_SON"><code>TSA_SON</code></a></dt><dd><span lang="en">Annual autumn temperatures</span><span lang="fr">Températures automnales annuelles</span><span class="u">°C</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/series/TSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
