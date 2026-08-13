---
hide:
  - toc
---

# `Bias`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  Bias                                                              Bias  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Relative difference between simulated and reference data. It measures the
     mean deviation over the entire series.

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── bias(Q_obs, Q_sim)
            │   └─ Bias calculation
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           Bias

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/Bias.yaml
  https://archive.softwareheritage.org/swh:1:cnt:143ab1ee5db271c6034aef4bd948e9b2b0a1fcc8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  Bias                                                             Biais  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Différence relative entre les données simulées et de référence. Il mesure
     l'écart moyen sur l'ensemble de la série.

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── bias(Q_obs, Q_sim)
            │   └─ Calcul du Biais
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           Bias

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/model-performance/scalar/Bias.yaml
  https://archive.softwareheritage.org/swh:1:cnt:143ab1ee5db271c6034aef4bd948e9b2b0a1fcc8</pre>

**Variables produced**  [`Bias`](../catalogue.md#Bias)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/Bias.yaml) &middot; [back to the catalogue](../catalogue.md)
