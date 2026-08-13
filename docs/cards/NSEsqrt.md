---
hide:
  - toc
---

# `NSEsqrt`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSEsqrt       Nash-Sutcliffe Efficiency of the square root of the data  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Identical to NSE, this score, however, gives equal weight across the
     entire range of the evaluated variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE_sqrt(Q_obs, Q_sim)
            │   └─ Square root of simulated and reference data, then NSE
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           NSEsqrt

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSEsqrt.yaml
  https://archive.softwareheritage.org/swh:1:cnt:97545ccc3c650912d12467e1942f3e910969081e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  NSEsqrt        Coefficient d'efficience de Nash-Sutcliffe de la racine  │
  │                                                      carrée des données  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Identique au NSE, ce score donne cependant un poids équivalent sur
     l'ensemble de la plage de variation de la variable évaluée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── NSE_sqrt(Q_obs, Q_sim)
            │   └─ Racine carrée des données simulées et de référence puis NSE
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           NSEsqrt

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/NSEsqrt.yaml
  https://archive.softwareheritage.org/swh:1:cnt:97545ccc3c650912d12467e1942f3e910969081e</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#NSEsqrt"><code>NSEsqrt</code></a></dt><dd><span lang="en">Nash-Sutcliffe Efficiency of the square root of the data</span><span lang="fr">Coefficient d'efficience de Nash-Sutcliffe de la racine carrée des données</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/NSEsqrt.yaml) &middot; [back to the catalogue](../catalogue.md)
