---
hide:
  - toc
---

# `Bias_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  Bias_season                                                  4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ Bias_DJF
       Winter Bias
       Relative difference between simulated and reference winter data.
       Similar to Bias, this score measures the mean deviation only over
       winter months (December, January, and February).

     ◇ Bias_MAM
       Spring Bias
       Relative difference between simulated and reference spring data.
       Similar to Bias, this score measures the mean deviation only over
       spring months (March, April, and May).

     ◇ Bias_JJA
       Summer Bias
       Relative difference between simulated and reference summer data.
       Similar to Bias, this score measures the mean deviation only over
       summer months (June, July, and August).

     ◇ Bias_SON
       Autumn Bias
       Relative difference between simulated and reference autumn data.
       Similar to Bias, this score measures the mean deviation only over
       autumn months (September, October, and November).

         season ─ record
           form ─ scalar
        purpose ─ model performance
           unit ─ without unit
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── bias(Q_obs, Q_sim)
            │   └─ Bias calculation
            │    ◦ One value per season
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           Bias

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/model-performance/scalar/Bias_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0802d419aef8b1dc32a78a4275e4a9e5233a7c71</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  Bias_season                                                  4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ Bias_DJF (Biais_DJF)
       Biais hivernal
       Différence relative entre les données d'hiver simulées et de référence.
       Identique au Biais, ce score mesure l'écart moyen uniquement sur les
       mois d'hiver (mois de décembre, janvier et février).

     ◇ Bias_MAM (Biais_MAM)
       Biais printanier
       Différence relative entre les données de printemps simulées et de
       référence. Identique au Biais, ce score mesure l'écart moyen uniquement
       sur les mois de printemps (mois de mars, avril et mai).

     ◇ Bias_JJA (Biais_JJA)
       Biais estival
       Différence relative entre les données d'été simulées et de référence.
       Identique au Biais, ce score mesure l'écart moyen uniquement sur les
       mois d'été (mois de juin, juillet et août).

     ◇ Bias_SON (Biais_SON)
       Biais automnal
       Différence relative entre les données d'automne simulées et de
       référence. Identique au Biais, ce score mesure l'écart moyen uniquement
       sur les mois d'automne (mois de septembre, octobre et novembre).

         saison ─ chronique
          forme ─ scalaire
       finalité ─ performance de modèle
          unité ─ sans unité
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹]

            ╷
            ├── bias(Q_obs, Q_sim)
            │   └─ Calcul du Biais
            │    ◦ Une valeur par saison
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           Bias

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/model-performance/scalar/Bias_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0802d419aef8b1dc32a78a4275e4a9e5233a7c71</pre>

**Variables produced**  [`Bias_DJF`](../catalogue.md#Bias_DJF) · [`Bias_MAM`](../catalogue.md#Bias_MAM) · [`Bias_JJA`](../catalogue.md#Bias_JJA) · [`Bias_SON`](../catalogue.md#Bias_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/model-performance/scalar/Bias_season.yaml) &middot; [back to the catalogue](../catalogue.md)
