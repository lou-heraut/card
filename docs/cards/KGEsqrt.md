---
hide:
  - toc
---

# `KGEsqrt`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  KGEsqrt              Kling-Gupta Efficiency of the square root of data  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Similar to KGE, this score gives equivalent weight across the entire
     range of the evaluated variable.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── KGE_sqrt(Q_obs, Q_sim)
            │   └─ Square root of simulated and reference data, then KGE
            │      calculation
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           KGEsqrt

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/KGEsqrt.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3c1799ea755ff7ace9744a25d1250ee216a697f5</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  KGEsqrt    Coefficient d'efficience de Kling-Gupta de la racine carrée  │
  │                                                             des données  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Identique au KGE, ce score donne cependant un poids équivalent sur
     l'ensemble de la plage de variation de la variable évaluée.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── KGE_sqrt(Q_obs, Q_sim)
            │   └─ Racine carrée des données simulées et de référence puis KGE
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           KGEsqrt

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/KGEsqrt.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3c1799ea755ff7ace9744a25d1250ee216a697f5</pre>

**Variables produced**  [`KGEsqrt`](../catalogue.md#KGEsqrt)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/KGEsqrt.yaml) &middot; [back to the catalogue](../catalogue.md)
