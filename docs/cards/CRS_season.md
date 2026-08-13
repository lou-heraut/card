---
hide:
  - toc
---

# `CRS_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  CRS_season                                                   4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ CRS_DJF
       Winter precipitation correction coefficient
       Ratio between the simulated and the observed precipitation totals over
       December, January and February, both averaged over the record

     ◇ CRS_MAM
       Spring precipitation correction coefficient
       Ratio between the simulated and the observed precipitation totals over
       March, April and May, both averaged over the record

     ◇ CRS_JJA
       Summer precipitation correction coefficient
       Ratio between the simulated and the observed precipitation totals over
       June, July and August, both averaged over the record

     ◇ CRS_SON
       Autumn precipitation correction coefficient
       Ratio between the simulated and the observed precipitation totals over
       September, October and November, both averaged over the record

         season ─ by season
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ R_obs [mm], R_sim [mm]

            ╷
            ├── RSA_obs = nansum_strict(R_obs)
            │   └─ Sum of observed precipitation
            ├── RSA_sim = nansum_strict(R_sim)
            │   └─ Sum of simulated precipitation
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           RSA_obs, RSA_sim
            ╷
            ├── mean-RSA_obs_DJF = nanmean(RSA_obs_DJF)
            │   └─ Inter-annual mean
            ├── mean-RSA_obs_MAM = nanmean(RSA_obs_MAM)
            │   └─ Inter-annual mean
            ├── mean-RSA_obs_JJA = nanmean(RSA_obs_JJA)
            │   └─ Inter-annual mean
            ├── mean-RSA_obs_SON = nanmean(RSA_obs_SON)
            │   └─ Inter-annual mean
            ├── mean-RSA_sim_DJF = nanmean(RSA_sim_DJF)
            │   └─ Inter-annual mean
            ├── mean-RSA_sim_MAM = nanmean(RSA_sim_MAM)
            │   └─ Inter-annual mean
            ├── mean-RSA_sim_JJA = nanmean(RSA_sim_JJA)
            │   └─ Inter-annual mean
            ├── mean-RSA_sim_SON = nanmean(RSA_sim_SON)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RSA_obs_DJF, mean-RSA_obs_MAM, mean-RSA_obs_JJA,
           mean-RSA_obs_SON, mean-RSA_sim_DJF, mean-RSA_sim_MAM,
           mean-RSA_sim_JJA, mean-RSA_sim_SON
            ╷
            ├── CRS_DJF = ratio(mean-RSA_sim_DJF, mean-RSA_obs_DJF)
            │   └─ Simulated/observed ratio for each season
            ├── CRS_MAM = ratio(mean-RSA_sim_MAM, mean-RSA_obs_MAM)
            │   └─ Simulated/observed ratio for each season
            ├── CRS_JJA = ratio(mean-RSA_sim_JJA, mean-RSA_obs_JJA)
            │   └─ Simulated/observed ratio for each season
            ├── CRS_SON = ratio(mean-RSA_sim_SON, mean-RSA_obs_SON)
            │   └─ Simulated/observed ratio for each season
            │    ◦ No temporal aggregation
            ▼
           CRS_DJF, CRS_MAM, CRS_JJA, CRS_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/model-performance/scalar/CRS_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d533c9113afab11612ac4ede5c1283141eac1db</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  CRS_season                                                   4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ CRS_DJF
       Coefficient correctif des précipitations hivernales
       Rapport entre le cumul de précipitations simulé et le cumul observé sur
       les mois de décembre, janvier et février, tous deux moyennés sur la
       chronique

     ◇ CRS_MAM
       Coefficient correctif des précipitations printanières
       Rapport entre le cumul de précipitations simulé et le cumul observé sur
       les mois de mars, avril et mai, tous deux moyennés sur la chronique

     ◇ CRS_JJA
       Coefficient correctif des précipitations estivales
       Rapport entre le cumul de précipitations simulé et le cumul observé sur
       les mois de juin, juillet et août, tous deux moyennés sur la chronique

     ◇ CRS_SON
       Coefficient correctif des précipitations automnales
       Rapport entre le cumul de précipitations simulé et le cumul observé sur
       les mois de septembre, octobre et novembre, tous deux moyennés sur la
       chronique

         saison ─ par saison
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ R_obs [mm], R_sim [mm]

            ╷
            ├── RSA_obs = nansum_strict(R_obs)
            │   └─ Somme des précipitations observées
            ├── RSA_sim = nansum_strict(R_sim)
            │   └─ Somme des précipitations simulées
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RSA_obs, RSA_sim
            ╷
            ├── mean-RSA_obs_DJF = nanmean(RSA_obs_DJF)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_obs_MAM = nanmean(RSA_obs_MAM)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_obs_JJA = nanmean(RSA_obs_JJA)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_obs_SON = nanmean(RSA_obs_SON)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_sim_DJF = nanmean(RSA_sim_DJF)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_sim_MAM = nanmean(RSA_sim_MAM)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_sim_JJA = nanmean(RSA_sim_JJA)
            │   └─ Moyenne inter-annuelle
            ├── mean-RSA_sim_SON = nanmean(RSA_sim_SON)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RSA_obs_DJF, mean-RSA_obs_MAM, mean-RSA_obs_JJA,
           mean-RSA_obs_SON, mean-RSA_sim_DJF, mean-RSA_sim_MAM,
           mean-RSA_sim_JJA, mean-RSA_sim_SON
            ╷
            ├── CRS_DJF = ratio(mean-RSA_sim_DJF, mean-RSA_obs_DJF)
            │   └─ Rapport simulé/observé pour chaque saison
            ├── CRS_MAM = ratio(mean-RSA_sim_MAM, mean-RSA_obs_MAM)
            │   └─ Rapport simulé/observé pour chaque saison
            ├── CRS_JJA = ratio(mean-RSA_sim_JJA, mean-RSA_obs_JJA)
            │   └─ Rapport simulé/observé pour chaque saison
            ├── CRS_SON = ratio(mean-RSA_sim_SON, mean-RSA_obs_SON)
            │   └─ Rapport simulé/observé pour chaque saison
            │    ◦ Aucune agrégation temporelle
            ▼
           CRS_DJF, CRS_MAM, CRS_JJA, CRS_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/model-performance/scalar/CRS_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d533c9113afab11612ac4ede5c1283141eac1db</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#CRS_DJF"><code>CRS_DJF</code></a></dt><dd><span lang="en">Winter precipitation correction coefficient</span><span lang="fr">Coefficient correctif des précipitations hivernales</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#CRS_MAM"><code>CRS_MAM</code></a></dt><dd><span lang="en">Spring precipitation correction coefficient</span><span lang="fr">Coefficient correctif des précipitations printanières</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#CRS_JJA"><code>CRS_JJA</code></a></dt><dd><span lang="en">Summer precipitation correction coefficient</span><span lang="fr">Coefficient correctif des précipitations estivales</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#CRS_SON"><code>CRS_SON</code></a></dt><dd><span lang="en">Autumn precipitation correction coefficient</span><span lang="fr">Coefficient correctif des précipitations automnales</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/model-performance/scalar/CRS_season.yaml) &middot; [back to the catalogue](../catalogue.md)
