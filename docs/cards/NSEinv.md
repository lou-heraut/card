---
hide:
  - toc
---

# `NSEinv`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSEinv            Nash-Sutcliffe Efficiency of the inverse of the data  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Identical to NSE, this score, however, gives strong emphasis on the
     reconstruction of low values of the examined variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE_inverse(Q_obs, Q_sim)
            │   └─ Inverse of daily data, then NSE
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           NSEinv

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSEinv.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8ce54d3d85a6f6b05d9195a5b77969474ea76ee6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSEinv     Coefficient d'efficience de Nash-Sutcliffe de l'inverse des  │
  │                                                                 données  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Identique au NSE, ce score donne cependant un poids fort à la
     reconstitution des valeurs faibles de la variable examinée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE_inverse(Q_obs, Q_sim)
            │   └─ Inverse des données journalières puis NSE
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           NSEinv

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSEinv.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8ce54d3d85a6f6b05d9195a5b77969474ea76ee6</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#NSEinv"><code>NSEinv</code></a></dt><dd><span lang="en">Nash-Sutcliffe Efficiency of the inverse of the data</span><span lang="fr">Coefficient d'efficience de Nash-Sutcliffe de l'inverse des données</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/NSEinv.yaml) &middot; [back to the catalogue](../catalogue.md)
