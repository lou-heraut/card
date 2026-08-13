---
hide:
  - toc
---

# `QR_ratio`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QR_ratio          Ratio of cumulative flow to cumulative precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio between the sum of flows and the sum of precipitation. Proportional
     to the runoff coefficient through the basin area (dimensionless
     coefficient = 86.4 × ratio / area in km²): suited to temporal monitoring
     of a station, not to comparison between basins

         season ─ record
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ m³·s⁻¹·mm⁻¹
         inputs ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── runoff_coefficient(Q, R)
            │   └─ Sum of flows divided by sum of precipitation
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           QR_ratio

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/QR_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:56ef1880488c2a748757c32c1bd2d0edf29792f9</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QR_ratio                   Rapport des cumuls débit sur précipitations  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport entre la somme des débits et la somme des précipitations.
     Proportionnel au coefficient de ruissellement via la surface du bassin
     (coefficient adimensionnel = 86,4 × rapport / surface en km²) : adapté au
     suivi temporel d'une station, pas à la comparaison entre bassins

         saison ─ chronique
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ m³·s⁻¹·mm⁻¹
        entrées ─ Q [m³·s⁻¹], R [mm]

            ╷
            ├── runoff_coefficient(Q, R)
            │   └─ Somme des débits divisée par la somme des précipitations
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QR_ratio

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/QR_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:56ef1880488c2a748757c32c1bd2d0edf29792f9</pre>

**Variables produced**  [`QR_ratio`](../catalogue.md#QR_ratio)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/QR_ratio.yaml) &middot; [back to the catalogue](../catalogue.md)
