---
hide:
  - toc
---

# `mean-TSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TSA_season                                              4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-TSA_DJF
       Inter-annual mean of winter mean temperatures (months of December,
       January and February)

     ◇ mean-TSA_MAM
       Inter-annual mean of spring mean temperatures (months of March, April
       and May)

     ◇ mean-TSA_JJA
       Inter-annual mean of summer mean temperatures (months of June, July and
       August)

     ◇ mean-TSA_SON
       Inter-annual mean of fall mean temperatures (months of September,
       October and November)

     phenomenon ─ mean temperatures
         season ─ by season
           form ─ scalar
           unit ─ °C
          input ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Average
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           TSA
            ╷
            ├── mean-TSA_DJF = nanmean(TSA_DJF)
            │   └─ Inter-annual mean
            ├── mean-TSA_MAM = nanmean(TSA_MAM)
            │   └─ Inter-annual mean
            ├── mean-TSA_JJA = nanmean(TSA_JJA)
            │   └─ Inter-annual mean
            ├── mean-TSA_SON = nanmean(TSA_SON)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-TSA_DJF, mean-TSA_MAM, mean-TSA_JJA, mean-TSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:461a9ace1d2521f074a791d7e60ab730e081578d</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TSA_season                                              4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-TSA_DJF (moyenne-TSA_DJF)
       Moyenne inter-annuelle des températures moyennes d'hiver
       Mois de décembre, janvier et février

     ◇ mean-TSA_MAM (moyenne-TSA_MAM)
       Moyenne inter-annuelle des températures moyennes de printemps
       Mois de mars, avril et mai

     ◇ mean-TSA_JJA (moyenne-TSA_JJA)
       Moyenne inter-annuelle des températures moyennes d'été
       Mois de juin, juillet et août

     ◇ mean-TSA_SON (moyenne-TSA_SON)
       Moyenne inter-annuelle des températures moyennes d'automne
       Mois de septembre, octobre et novembre

      phénomène ─ températures moyennes
         saison ─ par saison
          forme ─ scalaire
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
            ╷
            ├── mean-TSA_DJF = nanmean(TSA_DJF)
            │   └─ Moyenne inter-annuelle
            ├── mean-TSA_MAM = nanmean(TSA_MAM)
            │   └─ Moyenne inter-annuelle
            ├── mean-TSA_JJA = nanmean(TSA_JJA)
            │   └─ Moyenne inter-annuelle
            ├── mean-TSA_SON = nanmean(TSA_SON)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-TSA_DJF, mean-TSA_MAM, mean-TSA_JJA, mean-TSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:461a9ace1d2521f074a791d7e60ab730e081578d</pre>

**Variables produced**  [`mean-TSA_DJF`](../catalogue.md#mean-TSA_DJF) · [`mean-TSA_MAM`](../catalogue.md#mean-TSA_MAM) · [`mean-TSA_JJA`](../catalogue.md#mean-TSA_JJA) · [`mean-TSA_SON`](../catalogue.md#mean-TSA_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/scalar/mean-TSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
