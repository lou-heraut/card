---
hide:
  - toc
---

# `NSE`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSE                                          Nash-Sutcliffe Efficiency  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     It measures the proximity between the reference data series and the
     simulated ones, based on the square deviation. The coefficient gives
     strong emphasis on the reconstruction of high values of the examined
     variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE(Q_obs, Q_sim)
            │   └─ NSE calculation
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           NSE

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSE.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3c3ad249978bc283aa485f57904c092e2e184a8f</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSE                         Coefficient d'efficience de Nash-Sutcliffe  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Il mesure la proximité entre les séries de données de référence et celles
     simulées, sur la base de l'écart quadratique. Le coefficient donne un
     poids fort à la reconstitution des valeurs fortes de la variable
     examinée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE(Q_obs, Q_sim)
            │   └─ Calcul du NSE
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           NSE

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSE.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3c3ad249978bc283aa485f57904c092e2e184a8f</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#NSE"><code>NSE</code></a></dt><dd><span lang="en">Nash-Sutcliffe Efficiency</span><span lang="fr">Coefficient d'efficience de Nash-Sutcliffe</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/NSE.yaml) &middot; [back to the catalogue](../catalogue.md)
