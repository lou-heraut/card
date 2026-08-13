---
hide:
  - toc
---

# `CR`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  CR                            Correction coefficient for precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio between the simulated and the observed annual precipitation totals,
     both averaged over the record

         season ─ annual
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ R_obs [mm], R_sim [mm]

            ╷
            ├── RA_obs = nansum_strict(R_obs)
            │   └─ Sum of observed precipitation
            ├── RA_sim = nansum_strict(R_sim)
            │   └─ Sum of simulated precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA_obs, RA_sim
            ╷
            ├── mean-RA_obs = nanmean(RA_obs)
            │   └─ Inter-annual mean
            ├── mean-RA_sim = nanmean(RA_sim)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RA_obs, mean-RA_sim
            ╷
            ├── ratio(mean-RA_sim, mean-RA_obs)
            │   └─ Simulated/observed ratio
            │    ◦ No temporal aggregation
            ▼
           CR

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/model-performance/scalar/CR.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e6c6567283641687716fff1bde3c6bb00df23e57</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  CR                            Coefficient correctif des précipitations  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport entre le cumul annuel de précipitations simulé et le cumul
     observé, tous deux moyennés sur la chronique

         saison ─ annuelle
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ R_obs [mm], R_sim [mm]

            ╷
            ├── RA_obs = nansum_strict(R_obs)
            │   └─ Somme des précipitations observées
            ├── RA_sim = nansum_strict(R_sim)
            │   └─ Somme des précipitations simulées
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA_obs, RA_sim
            ╷
            ├── mean-RA_obs = nanmean(RA_obs)
            │   └─ Moyenne inter-annuelle
            ├── mean-RA_sim = nanmean(RA_sim)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RA_obs, mean-RA_sim
            ╷
            ├── ratio(mean-RA_sim, mean-RA_obs)
            │   └─ Rapport simulé/observé
            │    ◦ Aucune agrégation temporelle
            ▼
           CR

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/model-performance/scalar/CR.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e6c6567283641687716fff1bde3c6bb00df23e57</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#CR"><code>CR</code></a></dt><dd><span lang="en">Correction coefficient for precipitation</span><span lang="fr">Coefficient correctif des précipitations</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/model-performance/scalar/CR.yaml) &middot; [back to the catalogue](../catalogue.md)
