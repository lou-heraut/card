---
hide:
  - toc
---

# `epsilon_T`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_T                   Annual flow elasticity to air temperatures  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Relative change in flow for a 1 % relative change in air temperature,
     estimated as the median of the inter-annual departures scaled by their
     means

         season ─ annual
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], T [°C]

            ╷
            ├── QA = nanmean(Q)
            │   └─ Mean flow
            ├── TA = nanmean(T)
            │   └─ Mean temperatures
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QA, TA
            ╷
            ├── elasticity()
            │   │  from QA, TA
            │   └─ Calculation of elasticity ε
            │    ◦ No temporal aggregation
            ▼
           epsilon_T

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_T.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0fe16e6cd032458941bd8bbf32a71413d017131a</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_T       Élasticité annuelle du débit aux températures de l'air  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Variation relative du débit pour une variation relative de 1 % de la
     température de l'air, estimée par la médiane des écarts inter-annuels
     rapportés à leurs moyennes

         saison ─ annuelle
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], T [°C]

            ╷
            ├── QA = nanmean(Q)
            │   └─ Débit moyen
            ├── TA = nanmean(T)
            │   └─ Températures moyennes
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QA, TA
            ╷
            ├── elasticity()
            │   │  d'après QA, TA
            │   └─ Calcul de l'élasticité ε
            │    ◦ Aucune agrégation temporelle
            ▼
           epsilon_T

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_T.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0fe16e6cd032458941bd8bbf32a71413d017131a</pre>

**Variables produced**  [`epsilon_T`](../catalogue.md#epsilon_T)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/epsilon_T.yaml) &middot; [back to the catalogue](../catalogue.md)
