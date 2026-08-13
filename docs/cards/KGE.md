---
hide:
  - toc
---

# `KGE`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  KGE                                Kling-Gupta Performance Coefficient  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     It measures the proximity between reference and simulated data series
     based on three sub-criteria (r, alpha, and beta) with equal weights. The
     coefficient gives strong weight to the reconstruction of high values of
     the examined variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── KGE(Q_obs, Q_sim)
            │   └─ Calculation of KGE
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           KGE

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/KGE.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7c0dea0d42c2a2c9ebebf2de0dcc8fa559d6c4e0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  KGE                          Coefficient de performance de Kling-Gupta  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Il mesure la proximité entre les séries de données de référence et celles
     simulées, sur la base de trois sous-critères (r, alpha et beta) aux
     pondérations identiques. Le coefficient donne un poids fort à la
     reconstitution des valeurs fortes de la variable examinée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── KGE(Q_obs, Q_sim)
            │   └─ Calcul du KGE
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           KGE

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/KGE.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7c0dea0d42c2a2c9ebebf2de0dcc8fa559d6c4e0</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#KGE"><code>KGE</code></a></dt><dd><span lang="en">Kling-Gupta Performance Coefficient</span><span lang="fr">Coefficient de performance de Kling-Gupta</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/KGE.yaml) &middot; [back to the catalogue](../catalogue.md)
