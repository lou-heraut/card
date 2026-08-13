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

**Variables produced**  [`TMA_jan`](../catalogue.md#TMA_jan) · [`TMA_feb`](../catalogue.md#TMA_feb) · [`TMA_mar`](../catalogue.md#TMA_mar) · [`TMA_apr`](../catalogue.md#TMA_apr) · [`TMA_may`](../catalogue.md#TMA_may) · [`TMA_jun`](../catalogue.md#TMA_jun) · [`TMA_jul`](../catalogue.md#TMA_jul) · [`TMA_aug`](../catalogue.md#TMA_aug) · [`TMA_sep`](../catalogue.md#TMA_sep) · [`TMA_oct`](../catalogue.md#TMA_oct) · [`TMA_nov`](../catalogue.md#TMA_nov) · [`TMA_dec`](../catalogue.md#TMA_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/series/TMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
