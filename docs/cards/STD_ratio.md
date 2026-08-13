---
hide:
  - toc
---

# `STD_ratio`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  STD_ratio           Ratio of simulated to observed standard deviations  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio sd(sim)/sd(obs) of the daily data: the α component of the KGE
     (Gupta et al. 2009). Measures the ability of models to reproduce the
     variability of the examined variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── std_ratio(Q_obs, Q_sim)
            │   └─ Ratio of standard deviations sd(sim)/sd(obs)
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           STD_ratio

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/model-performance/scalar/STD_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2a6ac53aec6f847b8c814bfe06af14dd97692b50</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  STD_ratio                      Rapport des écarts-types simulé/observé  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport sd(sim)/sd(obs) des données journalières : la composante α du KGE
     (Gupta et al. 2009). Mesure la capacité des modèles à reproduire la
     variabilité de la variable examinée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── std_ratio(Q_obs, Q_sim)
            │   └─ Rapport des écarts-types sd(sim)/sd(obs)
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           STD_ratio

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/model-performance/scalar/STD_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2a6ac53aec6f847b8c814bfe06af14dd97692b50</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#STD_ratio"><code>STD_ratio</code></a></dt><dd><span lang="en">Ratio of simulated to observed standard deviations</span><span lang="fr">Rapport des écarts-types simulé/observé</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/STD_ratio.yaml) &middot; [back to the catalogue](../catalogue.md)
