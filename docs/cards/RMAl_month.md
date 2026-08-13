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

**Variables produced**  [`RMAl_jan`](../catalogue.md#RMAl_jan) · [`RMAl_feb`](../catalogue.md#RMAl_feb) · [`RMAl_mar`](../catalogue.md#RMAl_mar) · [`RMAl_apr`](../catalogue.md#RMAl_apr) · [`RMAl_may`](../catalogue.md#RMAl_may) · [`RMAl_jun`](../catalogue.md#RMAl_jun) · [`RMAl_jul`](../catalogue.md#RMAl_jul) · [`RMAl_aug`](../catalogue.md#RMAl_aug) · [`RMAl_sep`](../catalogue.md#RMAl_sep) · [`RMAl_oct`](../catalogue.md#RMAl_oct) · [`RMAl_nov`](../catalogue.md#RMAl_nov) · [`RMAl_dec`](../catalogue.md#RMAl_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RMAl_month.yaml) &middot; [back to the catalogue](../catalogue.md)
