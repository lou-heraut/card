---
hide:
  - toc
---

# `epsilon_T_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_T_season                                             4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ epsilon_T_DJF
       Winter flow elasticity to air temperatures
       Months of December, January, and February

     ◇ epsilon_T_MAM
       Spring flow elasticity to air temperatures
       Months of March, April, and May

     ◇ epsilon_T_JJA
       Summer flow elasticity to air temperatures
       Months of June, July, and August

     ◇ epsilon_T_SON
       Autumn flow elasticity to air temperatures
       Months of September, October, and November

         season ─ by season
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], T [°C]

            ╷
            ├── QSA = nanmean(Q)
            │   └─ Mean flow
            ├── TSA = nanmean(T)
            │   └─ Mean temperatures
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QSA, TSA
            ╷
            ├── epsilon_T_DJF = elasticity()
            │   │  Q=QSA_DJF, X=TSA_DJF
            │   └─ Calculation of elasticity ε
            ├── epsilon_T_MAM = elasticity()
            │   │  Q=QSA_MAM, X=TSA_MAM
            │   └─ Calculation of elasticity ε
            ├── epsilon_T_JJA = elasticity()
            │   │  Q=QSA_JJA, X=TSA_JJA
            │   └─ Calculation of elasticity ε
            ├── epsilon_T_SON = elasticity()
            │   │  Q=QSA_SON, X=TSA_SON
            │   └─ Calculation of elasticity ε
            │    ◦ No temporal aggregation
            ▼
           epsilon_T_DJF, epsilon_T_MAM, epsilon_T_JJA, epsilon_T_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_T_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:9f4dacb18eb5b08dbfdb9d76f6630caaf4ae2aa8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_T_season                                             4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ epsilon_T_DJF
       Élasticité hivernale du débit aux températures de l'air
       Mois de décembre, janvier et février

     ◇ epsilon_T_MAM
       Élasticité printanière du débit aux températures de l'air
       Mois de mars, avril et mai

     ◇ epsilon_T_JJA
       Élasticité estivale du débit aux températures de l'air
       Mois de juin, juillet et août

     ◇ epsilon_T_SON
       Élasticité automnale du débit aux températures de l'air
       Mois de septembre, octobre et novembre

         saison ─ par saison
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], T [°C]

            ╷
            ├── QSA = nanmean(Q)
            │   └─ Débit moyen
            ├── TSA = nanmean(T)
            │   └─ Températures moyennes
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QSA, TSA
            ╷
            ├── epsilon_T_DJF = elasticity()
            │   │  Q=QSA_DJF, X=TSA_DJF
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_T_MAM = elasticity()
            │   │  Q=QSA_MAM, X=TSA_MAM
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_T_JJA = elasticity()
            │   │  Q=QSA_JJA, X=TSA_JJA
            │   └─ Calcul de l'élasticité ε
            ├── epsilon_T_SON = elasticity()
            │   │  Q=QSA_SON, X=TSA_SON
            │   └─ Calcul de l'élasticité ε
            │    ◦ Aucune agrégation temporelle
            ▼
           epsilon_T_DJF, epsilon_T_MAM, epsilon_T_JJA, epsilon_T_SON

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_T_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:9f4dacb18eb5b08dbfdb9d76f6630caaf4ae2aa8</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#epsilon_T_DJF"><code>epsilon_T_DJF</code></a></dt><dd><span lang="en">Winter flow elasticity to air temperatures</span><span lang="fr">Élasticité hivernale du débit aux températures de l'air</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_T_MAM"><code>epsilon_T_MAM</code></a></dt><dd><span lang="en">Spring flow elasticity to air temperatures</span><span lang="fr">Élasticité printanière du débit aux températures de l'air</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_T_JJA"><code>epsilon_T_JJA</code></a></dt><dd><span lang="en">Summer flow elasticity to air temperatures</span><span lang="fr">Élasticité estivale du débit aux températures de l'air</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#epsilon_T_SON"><code>epsilon_T_SON</code></a></dt><dd><span lang="en">Autumn flow elasticity to air temperatures</span><span lang="fr">Élasticité automnale du débit aux températures de l'air</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/epsilon_T_season.yaml) &middot; [back to the catalogue](../catalogue.md)
