---
hide:
  - toc
---

# `epsilon_R_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_R_season                                             4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ epsilon_R_DJF
       Winter flow elasticity to precipitation
       Months of December, January, and February

     ◇ epsilon_R_MAM
       Spring flow elasticity to precipitation
       Months of March, April, and May

     ◇ epsilon_R_JJA
       Summer flow elasticity to precipitation
       Months of June, July, and August

     ◇ epsilon_R_SON
       Autumn flow elasticity to precipitation
       Months of September, October, and November

         season ─ by season
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── QSA = nanmean(Q)
            │   └─ Mean flow
            ├── RSA-mean = nanmean(R)
            │   └─ Mean total precipitation
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QSA, RSA-mean
            ╷
            ├── epsilon_R_DJF = elasticity()
            │   │  Q=QSA_DJF, X=RSA-mean_DJF
            │   └─ Calculation of elasticity ε
            ├── epsilon_R_MAM = elasticity()
            │   │  Q=QSA_MAM, X=RSA-mean_MAM
            │   └─ Calculation of elasticity ε
            ├── epsilon_R_JJA = elasticity()
            │   │  Q=QSA_JJA, X=RSA-mean_JJA
            │   └─ Calculation of elasticity ε
            ├── epsilon_R_SON = elasticity()
            │   │  Q=QSA_SON, X=RSA-mean_SON
            │   └─ Calculation of elasticity ε
            │    ◦ No temporal aggregation
            ▼
           epsilon_R_DJF, epsilon_R_MAM, epsilon_R_JJA, epsilon_R_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_R_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:571ac3702c0b243b197e3f78842b44a0db79f430</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_R_season                                             4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ epsilon_R_DJF
       Élasticité hivernale du débit aux précipitations
       Mois de décembre, janvier et février

     ◇ epsilon_R_MAM
       Élasticité printanière du débit aux précipitations
       Mois de mars, avril et mai

     ◇ epsilon_R_JJA
       Élasticité estivale du débit aux précipitations
       Mois de juin, juillet et août

     ◇ epsilon_R_SON
       Élasticité automnale du débit aux précipitations
       Mois de septembre, octobre et novembre

         saison ─ par saison
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── QSA = nanmean(Q)
            │   └─ Débit moyen
            ├── RSA-mean = nanmean(R)
            │   └─ Précipitations totales moyennes
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QSA, RSA-mean
            ╷
            ├── epsilon_R_DJF = elasticity()
            │   │  Q=QSA_DJF, X=RSA-mean_DJF
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_R_MAM = elasticity()
            │   │  Q=QSA_MAM, X=RSA-mean_MAM
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_R_JJA = elasticity()
            │   │  Q=QSA_JJA, X=RSA-mean_JJA
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_R_SON = elasticity()
            │   │  Q=QSA_SON, X=RSA-mean_SON
            │   └─ Calcul de l'élasticité ε
            │    ◦ Aucune agrégation temporelle
            ▼
           epsilon_R_DJF, epsilon_R_MAM, epsilon_R_JJA, epsilon_R_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_R_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:571ac3702c0b243b197e3f78842b44a0db79f430</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#epsilon_R_DJF"><code>epsilon_R_DJF</code></a></dt><dd><span lang="en">Winter flow elasticity to precipitation</span><span lang="fr">Élasticité hivernale du débit aux précipitations</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_R_MAM"><code>epsilon_R_MAM</code></a></dt><dd><span lang="en">Spring flow elasticity to precipitation</span><span lang="fr">Élasticité printanière du débit aux précipitations</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_R_JJA"><code>epsilon_R_JJA</code></a></dt><dd><span lang="en">Summer flow elasticity to precipitation</span><span lang="fr">Élasticité estivale du débit aux précipitations</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_R_SON"><code>epsilon_R_SON</code></a></dt><dd><span lang="en">Autumn flow elasticity to precipitation</span><span lang="fr">Élasticité automnale du débit aux précipitations</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/epsilon_R_season.yaml) &middot; [back to the catalogue](../catalogue.md)
