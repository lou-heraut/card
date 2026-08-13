---
hide:
  - toc
---

# `mean-RSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RSA_season                                              4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-RSA_DJF
       Inter-annual mean of winter total precipitation (months of December,
       January and February)

     ◇ mean-RSA_MAM
       Inter-annual mean of spring total precipitation (months of March, April
       and May)

     ◇ mean-RSA_JJA
       Inter-annual mean of summer total precipitation (months of June, July
       and August)

     ◇ mean-RSA_SON
       Inter-annual mean of fall total precipitation (months of September,
       October and November)

     phenomenon ─ mean precipitation
         season ─ by season
           form ─ scalar
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Average
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RSA
            ╷
            ├── mean-RSA_DJF = nanmean(RSA_DJF)
            │   └─ Inter-annual mean
            ├── mean-RSA_MAM = nanmean(RSA_MAM)
            │   └─ Inter-annual mean
            ├── mean-RSA_JJA = nanmean(RSA_JJA)
            │   └─ Inter-annual mean
            ├── mean-RSA_SON = nanmean(RSA_SON)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RSA_DJF, mean-RSA_MAM, mean-RSA_JJA, mean-RSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.1   precipitation/mean-precipitation/scalar/mean-RSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c22a5dfbe7bcab60e099dd249f0ced836463f3f8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RSA_season                                              4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-RSA_DJF (moyenne-RSA_DJF)
       Moyenne inter-annuelle des précipitations totales d'hiver
       Mois de décembre, janvier et février

     ◇ mean-RSA_MAM (moyenne-RSA_MAM)
       Moyenne inter-annuelle des précipitations totales de printemps
       Mois de mars, avril et mai

     ◇ mean-RSA_JJA (moyenne-RSA_JJA)
       Moyenne inter-annuelle des précipitations totales d'été
       Mois de juin, juillet et août

     ◇ mean-RSA_SON (moyenne-RSA_SON)
       Moyenne inter-annuelle des précipitations totales d'automne
       Mois de septembre, octobre et novembre

      phénomène ─ précipitations moyennes
         saison ─ par saison
          forme ─ scalaire
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Moyenne
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RSA
            ╷
            ├── mean-RSA_DJF = nanmean(RSA_DJF)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_MAM = nanmean(RSA_MAM)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_JJA = nanmean(RSA_JJA)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_SON = nanmean(RSA_SON)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RSA_DJF, mean-RSA_MAM, mean-RSA_JJA, mean-RSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.1   precipitation/mean-precipitation/scalar/mean-RSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c22a5dfbe7bcab60e099dd249f0ced836463f3f8</pre>

**Variables produced**  [`mean-RSA_DJF`](../catalogue.md#mean-RSA_DJF) · [`mean-RSA_MAM`](../catalogue.md#mean-RSA_MAM) · [`mean-RSA_JJA`](../catalogue.md#mean-RSA_JJA) · [`mean-RSA_SON`](../catalogue.md#mean-RSA_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/scalar/mean-RSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
