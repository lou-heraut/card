---
hide:
  - toc
---

# `epsilon_R`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_R                      Annual flow elasticity to precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Relative change in flow for a 1 % relative change in precipitation,
     estimated as the median of the inter-annual departures scaled by their
     means

         season ─ annual
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── QA = nanmean(Q)
            │   └─ Mean flow
            ├── RA-mean = nanmean(R)
            │   └─ Mean total precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QA, RA-mean
            ╷
            ├── elasticity()
            │   │  from QA, RA-mean
            │   └─ Calculation of elasticity ε
            │    ◦ No temporal aggregation
            │    ◦ At most 3 % missing
            ▼
           epsilon_R

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_R.yaml
  https://archive.softwareheritage.org/swh:1:cnt:70778227882c250facc76c14a2eb25b3db0ee7fe</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  epsilon_R              Élasticité annuelle du débit aux précipitations  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Variation relative du débit pour une variation relative de 1 % des
     précipitations, estimée par la médiane des écarts inter-annuels rapportés
     à leurs moyennes

         saison ─ annuelle
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── QA = nanmean(Q)
            │   └─ Débit moyen
            ├── RA-mean = nanmean(R)
            │   └─ Précipitations totales moyennes
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QA, RA-mean
            ╷
            ├── elasticity()
            │   │  d'après QA, RA-mean
            │   └─ Calcul de l'élasticité ε
            │    ◦ Aucune agrégation temporelle
            │    ◦ Au plus 3 % de lacunes
            ▼
           epsilon_R

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/epsilon_R.yaml
  https://archive.softwareheritage.org/swh:1:cnt:70778227882c250facc76c14a2eb25b3db0ee7fe</pre>

**Variables produced**  [`epsilon_R`](../catalogue.md#epsilon_R)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/epsilon_R.yaml) &middot; [back to the catalogue](../catalogue.md)
