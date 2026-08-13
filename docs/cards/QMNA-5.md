---
hide:
  - toc
---

# `QMNA-5`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMNA-5       Annual minimum of monthly flows with a return period of 5  │
  │                                                                   years  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ by month
           form ─ scalar
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QMA
            ╷
            ├── nanmin(QMA)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QMNA
            ╷
            ├── return_level(QMNA)
            │   │  water_type=low
            │   └─ Calculation of the 5-year return period flow with the
            │      log-normal distribution
            │    ◦ No temporal aggregation
            ▼
           QMNA-5

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/low-flows/scalar/QMNA-5.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cf7945b0290b6540274e8f330bb6da215c30a091</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMNA-5   Minimum annuel des débits mensuels de période de retour 5 ans  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ par mois
          forme ─ scalaire
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QMA
            ╷
            ├── nanmin(QMA)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QMNA
            ╷
            ├── return_level(QMNA)
            │   │  water_type=low
            │   └─ Calcul du débit de période de retour 5 ans avec la loi
            │      log-normale
            │    ◦ Aucune agrégation temporelle
            ▼
           QMNA-5

  ──────────────────────────────────────────────────────────────────────────
  v1.3   flow/low-flows/scalar/QMNA-5.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cf7945b0290b6540274e8f330bb6da215c30a091</pre>

**Variables produced**  [`QMNA-5`](../catalogue.md#QMNA-5)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/QMNA-5.yaml) &middot; [back to the catalogue](../catalogue.md)
