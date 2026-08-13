---
hide:
  - toc
---

# `rp-QMNA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  rp-QMNA            Return period of the station's regulatory threshold  │
  │                   discharge in the distribution of the annual minima of  │
  │                                                           monthly flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Inverse of the return-level fiches (QMNA-5) - the log-normal law is
     fitted on the QMNA series and evaluated at the constant threshold
     discharge Q_lim given by regulatory texts (e.g. DOE, DCR); a threshold
     far below the fitted law gives an extrapolated return period, reported as
     is

     phenomenon ─ low flows
         season ─ by month
           form ─ scalar
           unit ─ year
         inputs ─ Q [m³·s⁻¹], Q_lim [m³·s⁻¹]

            ╷
            ├── QMA = nanmean(Q)
            │   └─ Mean of daily flows
            ├── QlimM = nanmean(Q_lim)
            │   └─ Mean of the Q_lim threshold
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QMA, QlimM
            ╷
            ├── QMNA = nanmin(QMA)
            │   └─ Minimum of QMA
            ├── Qlim = nanmean(QlimM)
            │   └─ Mean of the Q_lim threshold
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QMNA, Qlim
            ╷
            ├── return_period(QMNA)
            │   │  below Qlim, water_type=low
            │   └─ Return period of the Q_lim threshold with the log-normal
            │      distribution
            │    ◦ No temporal aggregation
            ▼
           rp-QMNA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/rp-QMNA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3b0b2f4e2124541c21d1ace3b99ee5cf7b81b6b7</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  rp-QMNA   Période de retour du débit seuil réglementaire de la station  │
  │                    dans la distribution des minimums annuels des débits  │
  │                                                                mensuels  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Inverse des fiches de niveau de retour (QMNA-5) - la loi log-normale est
     ajustée sur la série des QMNA puis évaluée au débit seuil constant Q_lim
     donné par les textes réglementaires (par exemple DOE, DCR) ; un seuil
     loin du corps de la loi donne une période de retour extrapolée, restituée
     telle quelle

      phénomène ─ basses eaux
         saison ─ par mois
          forme ─ scalaire
          unité ─ an
        entrées ─ Q [m³·s⁻¹], Q_lim [m³·s⁻¹]

            ╷
            ├── QMA = nanmean(Q)
            │   └─ Moyenne des débits journaliers
            ├── QlimM = nanmean(Q_lim)
            │   └─ Moyenne du seuil Q_lim
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QMA, QlimM
            ╷
            ├── QMNA = nanmin(QMA)
            │   └─ Minimum de QMA
            ├── Qlim = nanmean(QlimM)
            │   └─ Moyenne du seuil Q_lim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QMNA, Qlim
            ╷
            ├── return_period(QMNA)
            │   │  sous Qlim, water_type=low
            │   └─ Période de retour du seuil Q_lim avec la loi log-normale
            │    ◦ Aucune agrégation temporelle
            ▼
           rp-QMNA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/rp-QMNA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:3b0b2f4e2124541c21d1ace3b99ee5cf7b81b6b7</pre>

**Variables produced**  [`rp-QMNA`](../catalogue.md#rp-QMNA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/rp-QMNA.yaml) &middot; [back to the catalogue](../catalogue.md)
