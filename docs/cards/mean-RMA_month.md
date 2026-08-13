---
hide:
  - toc
---

# `mean-RMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RMA_month                                              12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-RMA_jan
       Inter-annual mean of January total precipitation

     ◇ mean-RMA_feb
       Inter-annual mean of February total precipitation

     ◇ mean-RMA_mar
       Inter-annual mean of March total precipitation

     ◇ mean-RMA_apr
       Inter-annual mean of April total precipitation

     ◇ mean-RMA_may
       Inter-annual mean of May total precipitation

     ◇ mean-RMA_jun
       Inter-annual mean of June total precipitation

     ◇ mean-RMA_jul
       Inter-annual mean of July total precipitation

     ◇ mean-RMA_aug
       Inter-annual mean of August total precipitation

     ◇ mean-RMA_sep
       Inter-annual mean of September total precipitation

     ◇ mean-RMA_oct
       Inter-annual mean of October total precipitation

     ◇ mean-RMA_nov
       Inter-annual mean of November total precipitation

     ◇ mean-RMA_dec
       Inter-annual mean of December total precipitation

     phenomenon ─ mean precipitation
         season ─ by month
           form ─ scalar
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Sum
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RMA
            ╷
            ├── mean-RMA_jan = nanmean(RMA_jan)
            │   └─ Inter-annual mean
            ├── mean-RMA_feb = nanmean(RMA_feb)
            │   └─ Inter-annual mean
            ├── mean-RMA_mar = nanmean(RMA_mar)
            │   └─ Inter-annual mean
            ├── mean-RMA_apr = nanmean(RMA_apr)
            │   └─ Inter-annual mean
            ├── mean-RMA_may = nanmean(RMA_may)
            │   └─ Inter-annual mean
            ├── mean-RMA_jun = nanmean(RMA_jun)
            │   └─ Inter-annual mean
            ├── mean-RMA_jul = nanmean(RMA_jul)
            │   └─ Inter-annual mean
            ├── mean-RMA_aug = nanmean(RMA_aug)
            │   └─ Inter-annual mean
            ├── mean-RMA_sep = nanmean(RMA_sep)
            │   └─ Inter-annual mean
            ├── mean-RMA_oct = nanmean(RMA_oct)
            │   └─ Inter-annual mean
            ├── mean-RMA_nov = nanmean(RMA_nov)
            │   └─ Inter-annual mean
            ├── mean-RMA_dec = nanmean(RMA_dec)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RMA_jan, mean-RMA_feb, mean-RMA_mar, mean-RMA_apr,
           mean-RMA_may, mean-RMA_jun, mean-RMA_jul, mean-RMA_aug,
           mean-RMA_sep, mean-RMA_oct, mean-RMA_nov, mean-RMA_dec

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/scalar/mean-RMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc29d57b5319e51f71ff51f7f6dfcf54b6e9da01</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RMA_month                                              12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-RMA_jan (moyenne-RMA_janv)
       Moyenne inter-annuelle des précipitations totales de janvier

     ◇ mean-RMA_feb (moyenne-RMA_fevr)
       Moyenne inter-annuelle des précipitations totales de février

     ◇ mean-RMA_mar (moyenne-RMA_mars)
       Moyenne inter-annuelle des précipitations totales de mars

     ◇ mean-RMA_apr (moyenne-RMA_avril)
       Moyenne inter-annuelle des précipitations totales d'avril

     ◇ mean-RMA_may (moyenne-RMA_mai)
       Moyenne inter-annuelle des précipitations totales de mai

     ◇ mean-RMA_jun (moyenne-RMA_juin)
       Moyenne inter-annuelle des précipitations totales de juin

     ◇ mean-RMA_jul (moyenne-RMA_juil)
       Moyenne inter-annuelle des précipitations totales de juillet

     ◇ mean-RMA_aug (moyenne-RMA_aout)
       Moyenne inter-annuelle des précipitations totales d'août

     ◇ mean-RMA_sep (moyenne-RMA_sept)
       Moyenne inter-annuelle des précipitations totales de septembre

     ◇ mean-RMA_oct (moyenne-RMA_oct)
       Moyenne inter-annuelle des précipitations totales d'octobre

     ◇ mean-RMA_nov (moyenne-RMA_nov)
       Moyenne inter-annuelle des précipitations totales de novembre

     ◇ mean-RMA_dec (moyenne-RMA_dec)
       Moyenne inter-annuelle des précipitations totales de décembre

      phénomène ─ précipitations moyennes
         saison ─ par mois
          forme ─ scalaire
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Somme
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RMA
            ╷
            ├── mean-RMA_jan = nanmean(RMA_jan)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_feb = nanmean(RMA_feb)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_mar = nanmean(RMA_mar)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_apr = nanmean(RMA_apr)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_may = nanmean(RMA_may)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_jun = nanmean(RMA_jun)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_jul = nanmean(RMA_jul)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_aug = nanmean(RMA_aug)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_sep = nanmean(RMA_sep)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_oct = nanmean(RMA_oct)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_nov = nanmean(RMA_nov)
            │   └─ Moyenne inter-annuelle
            ├── mean-RMA_dec = nanmean(RMA_dec)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RMA_jan, mean-RMA_feb, mean-RMA_mar, mean-RMA_apr,
           mean-RMA_may, mean-RMA_jun, mean-RMA_jul, mean-RMA_aug,
           mean-RMA_sep, mean-RMA_oct, mean-RMA_nov, mean-RMA_dec

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/scalar/mean-RMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc29d57b5319e51f71ff51f7f6dfcf54b6e9da01</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#mean-RMA_jan"><code>mean-RMA_jan</code></a></dt><dd><span lang="en">Inter-annual mean of January total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de janvier</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_feb"><code>mean-RMA_feb</code></a></dt><dd><span lang="en">Inter-annual mean of February total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de février</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_mar"><code>mean-RMA_mar</code></a></dt><dd><span lang="en">Inter-annual mean of March total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de mars</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_apr"><code>mean-RMA_apr</code></a></dt><dd><span lang="en">Inter-annual mean of April total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales d'avril</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_may"><code>mean-RMA_may</code></a></dt><dd><span lang="en">Inter-annual mean of May total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de mai</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_jun"><code>mean-RMA_jun</code></a></dt><dd><span lang="en">Inter-annual mean of June total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de juin</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_jul"><code>mean-RMA_jul</code></a></dt><dd><span lang="en">Inter-annual mean of July total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de juillet</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_aug"><code>mean-RMA_aug</code></a></dt><dd><span lang="en">Inter-annual mean of August total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales d'août</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_sep"><code>mean-RMA_sep</code></a></dt><dd><span lang="en">Inter-annual mean of September total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de septembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_oct"><code>mean-RMA_oct</code></a></dt><dd><span lang="en">Inter-annual mean of October total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales d'octobre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_nov"><code>mean-RMA_nov</code></a></dt><dd><span lang="en">Inter-annual mean of November total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de novembre</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#mean-RMA_dec"><code>mean-RMA_dec</code></a></dt><dd><span lang="en">Inter-annual mean of December total precipitation</span><span lang="fr">Moyenne inter-annuelle des précipitations totales de décembre</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/scalar/mean-RMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
