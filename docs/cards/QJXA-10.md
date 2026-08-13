---
hide:
  - toc
---

# `QJXA-10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJXA-10         Annual maximum daily flow with a 10-year return period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QJXA
            ╷
            ├── return_level(QJXA)
            │   │  water_type=high
            │   └─ Calculation of the flow with a 10-year return period using
            │      the Gumbel distribution
            │    ◦ No temporal aggregation
            ▼
           QJXA-10

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/high-flows/scalar/QJXA-10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f0a70abfca019af68bf5d7e3c3689ebdb4b16406</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJXA-10    Débit journalier maximal annuel de période de retour 10 ans  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QJXA
            ╷
            ├── return_level(QJXA)
            │   │  water_type=high
            │   └─ Calcul du débit de période de retour 10 ans avec la loi de
            │      Gumbel
            │    ◦ Aucune agrégation temporelle
            ▼
           QJXA-10

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/high-flows/scalar/QJXA-10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f0a70abfca019af68bf5d7e3c3689ebdb4b16406</pre>

**Variables produced**  [`QJXA-10`](../catalogue.md#QJXA-10)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/QJXA-10.yaml) &middot; [back to the catalogue](../catalogue.md)
