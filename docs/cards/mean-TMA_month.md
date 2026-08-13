---
hide:
  - toc
---

# `mean-TMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TMA_month                                              12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-TMA_jan
       Inter-annual mean of January mean temperatures

     ◇ mean-TMA_feb
       Inter-annual mean of February mean temperatures

     ◇ mean-TMA_mar
       Inter-annual mean of March mean temperatures

     ◇ mean-TMA_apr
       Inter-annual mean of April mean temperatures

     ◇ mean-TMA_may
       Inter-annual mean of May mean temperatures

     ◇ mean-TMA_jun
       Inter-annual mean of June mean temperatures

     ◇ mean-TMA_jul
       Inter-annual mean of July mean temperatures

     ◇ mean-TMA_aug
       Inter-annual mean of August mean temperatures

     ◇ mean-TMA_sep
       Inter-annual mean of September mean temperatures

     ◇ mean-TMA_oct
       Inter-annual mean of October mean temperatures

     ◇ mean-TMA_nov
       Inter-annual mean of November mean temperatures

     ◇ mean-TMA_dec
       Inter-annual mean of December mean temperatures

     phenomenon ─ mean temperatures
         season ─ by month
           form ─ scalar
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
            ╷
            ├── mean-TMA_jan = nanmean(TMA_jan)
            │   └─ Inter-annual mean
            ├── mean-TMA_feb = nanmean(TMA_feb)
            │   └─ Inter-annual mean
            ├── mean-TMA_mar = nanmean(TMA_mar)
            │   └─ Inter-annual mean
            ├── mean-TMA_apr = nanmean(TMA_apr)
            │   └─ Inter-annual mean
            ├── mean-TMA_may = nanmean(TMA_may)
            │   └─ Inter-annual mean
            ├── mean-TMA_jun = nanmean(TMA_jun)
            │   └─ Inter-annual mean
            ├── mean-TMA_jul = nanmean(TMA_jul)
            │   └─ Inter-annual mean
            ├── mean-TMA_aug = nanmean(TMA_aug)
            │   └─ Inter-annual mean
            ├── mean-TMA_sep = nanmean(TMA_sep)
            │   └─ Inter-annual mean
            ├── mean-TMA_oct = nanmean(TMA_oct)
            │   └─ Inter-annual mean
            ├── mean-TMA_nov = nanmean(TMA_nov)
            │   └─ Inter-annual mean
            ├── mean-TMA_dec = nanmean(TMA_dec)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-TMA_jan, mean-TMA_feb, mean-TMA_mar, mean-TMA_apr,
           mean-TMA_may, mean-TMA_jun, mean-TMA_jul, mean-TMA_aug,
           mean-TMA_sep, mean-TMA_oct, mean-TMA_nov, mean-TMA_dec

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:044cf27aef228c8d2e9643fbc07d576cbf6e9fbe</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TMA_month                                              12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-TMA_jan (moyenne-TMA_janv)
       Moyenne inter-annuelle des températures moyennes de janvier

     ◇ mean-TMA_feb (moyenne-TMA_fevr)
       Moyenne inter-annuelle des températures moyennes de février

     ◇ mean-TMA_mar (moyenne-TMA_mars)
       Moyenne inter-annuelle des températures moyennes de mars

     ◇ mean-TMA_apr (moyenne-TMA_avril)
       Moyenne inter-annuelle des températures moyennes d'avril

     ◇ mean-TMA_may (moyenne-TMA_mai)
       Moyenne inter-annuelle des températures moyennes de mai

     ◇ mean-TMA_jun (moyenne-TMA_juin)
       Moyenne inter-annuelle des températures moyennes de juin

     ◇ mean-TMA_jul (moyenne-TMA_juil)
       Moyenne inter-annuelle des températures moyennes de juillet

     ◇ mean-TMA_aug (moyenne-TMA_aout)
       Moyenne inter-annuelle des températures moyennes d'août

     ◇ mean-TMA_sep (moyenne-TMA_sept)
       Moyenne inter-annuelle des températures moyennes de septembre

     ◇ mean-TMA_oct (moyenne-TMA_oct)
       Moyenne inter-annuelle des températures moyennes d'octobre

     ◇ mean-TMA_nov (moyenne-TMA_nov)
       Moyenne inter-annuelle des températures moyennes de novembre

     ◇ mean-TMA_dec (moyenne-TMA_dec)
       Moyenne inter-annuelle des températures moyennes de décembre

      phénomène ─ températures moyennes
         saison ─ par mois
          forme ─ scalaire
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
            ╷
            ├── mean-TMA_jan = nanmean(TMA_jan)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_feb = nanmean(TMA_feb)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_mar = nanmean(TMA_mar)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_apr = nanmean(TMA_apr)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_may = nanmean(TMA_may)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_jun = nanmean(TMA_jun)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_jul = nanmean(TMA_jul)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_aug = nanmean(TMA_aug)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_sep = nanmean(TMA_sep)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_oct = nanmean(TMA_oct)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_nov = nanmean(TMA_nov)
            │   └─ Moyenne inter-annuelle
            ├── mean-TMA_dec = nanmean(TMA_dec)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-TMA_jan, mean-TMA_feb, mean-TMA_mar, mean-TMA_apr,
           mean-TMA_may, mean-TMA_jun, mean-TMA_jul, mean-TMA_aug,
           mean-TMA_sep, mean-TMA_oct, mean-TMA_nov, mean-TMA_dec

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:044cf27aef228c8d2e9643fbc07d576cbf6e9fbe</pre>

**Variables produced**  [`mean-TMA_jan`](../catalogue.md#mean-TMA_jan) · [`mean-TMA_feb`](../catalogue.md#mean-TMA_feb) · [`mean-TMA_mar`](../catalogue.md#mean-TMA_mar) · [`mean-TMA_apr`](../catalogue.md#mean-TMA_apr) · [`mean-TMA_may`](../catalogue.md#mean-TMA_may) · [`mean-TMA_jun`](../catalogue.md#mean-TMA_jun) · [`mean-TMA_jul`](../catalogue.md#mean-TMA_jul) · [`mean-TMA_aug`](../catalogue.md#mean-TMA_aug) · [`mean-TMA_sep`](../catalogue.md#mean-TMA_sep) · [`mean-TMA_oct`](../catalogue.md#mean-TMA_oct) · [`mean-TMA_nov`](../catalogue.md#mean-TMA_nov) · [`mean-TMA_dec`](../catalogue.md#mean-TMA_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/scalar/mean-TMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
