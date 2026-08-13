---
hide:
  - toc
---

# `RMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMA_month                                                   12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMA_jan
       Cumulative daily precipitation for each January

     ◇ RMA_feb
       Cumulative daily precipitation for each February

     ◇ RMA_mar
       Cumulative daily precipitation for each March

     ◇ RMA_apr
       Cumulative daily precipitation for each April

     ◇ RMA_may
       Cumulative daily precipitation for each May

     ◇ RMA_jun
       Cumulative daily precipitation for each June

     ◇ RMA_jul
       Cumulative daily precipitation for each July

     ◇ RMA_aug
       Cumulative daily precipitation for each August

     ◇ RMA_sep
       Cumulative daily precipitation for each September

     ◇ RMA_oct
       Cumulative daily precipitation for each October

     ◇ RMA_nov
       Cumulative daily precipitation for each November

     ◇ RMA_dec
       Cumulative daily precipitation for each December

     phenomenon ─ mean precipitation
         season ─ by month
           form ─ series
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

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:99917040f1c13155c2f8c73f54bfcc92d6aa2542</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RMA_month                                                   12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RMA_jan (RMA_janv)
       Cumul des précipitations journalières de chaque janvier

     ◇ RMA_feb (RMA_fevr)
       Cumul des précipitations journalières de chaque février

     ◇ RMA_mar (RMA_mars)
       Cumul des précipitations journalières de chaque mars

     ◇ RMA_apr (RMA_avril)
       Cumul des précipitations journalières de chaque avril

     ◇ RMA_may (RMA_mai)
       Cumul des précipitations journalières de chaque mai

     ◇ RMA_jun (RMA_juin)
       Cumul des précipitations journalières de chaque juin

     ◇ RMA_jul (RMA_juil)
       Cumul des précipitations journalières de chaque juillet

     ◇ RMA_aug (RMA_aout)
       Cumul des précipitations journalières de chaque août

     ◇ RMA_sep (RMA_sept)
       Cumul des précipitations journalières de chaque septembre

     ◇ RMA_oct
       Cumul des précipitations journalières de chaque octobre

     ◇ RMA_nov
       Cumul des précipitations journalières de chaque novembre

     ◇ RMA_dec
       Cumul des précipitations journalières de chaque décembre

      phénomène ─ précipitations moyennes
         saison ─ par mois
          forme ─ série
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

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   precipitation/mean-precipitation/series/RMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:99917040f1c13155c2f8c73f54bfcc92d6aa2542</pre>

**Variables produced**  [`RMA_jan`](../catalogue.md#RMA_jan) · [`RMA_feb`](../catalogue.md#RMA_feb) · [`RMA_mar`](../catalogue.md#RMA_mar) · [`RMA_apr`](../catalogue.md#RMA_apr) · [`RMA_may`](../catalogue.md#RMA_may) · [`RMA_jun`](../catalogue.md#RMA_jun) · [`RMA_jul`](../catalogue.md#RMA_jul) · [`RMA_aug`](../catalogue.md#RMA_aug) · [`RMA_sep`](../catalogue.md#RMA_sep) · [`RMA_oct`](../catalogue.md#RMA_oct) · [`RMA_nov`](../catalogue.md#RMA_nov) · [`RMA_dec`](../catalogue.md#RMA_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
