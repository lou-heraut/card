---
hide:
  - toc
---

# `rp-VCN30`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  rp-VCN30           Return period of the station's regulatory threshold  │
  │                   discharge in the distribution of the annual minima of  │
  │                                                       30-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Inverse of the return-level fiches (VCN30-2) - the log-normal law is
     fitted on the VCN30 series and evaluated at the constant threshold
     discharge Q_lim given by regulatory texts (e.g. DOE, DCR); a threshold
     far below the fitted law gives an extrapolated return period, reported as
     is

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ year
         inputs ─ Q [m³·s⁻¹], Q_lim [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 30-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC30
            ╷
            ├── VCN30 = nanmin(VC30)
            │   └─ Minimum of VC30
            ├── Qlim = nanmean(Q_lim)
            │   └─ Mean of the Q_lim threshold
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN30, Qlim
            ╷
            ├── return_period(VCN30)
            │   │  below Qlim, water_type=low
            │   └─ Return period of the Q_lim threshold with the log-normal
            │      distribution
            │    ◦ No temporal aggregation
            ▼
           rp-VCN30

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/rp-VCN30.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f0af635092b1b1a939fb76d2f95138073a4b1d25</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  rp-VCN30          Période de retour du débit seuil réglementaire de la  │
  │                   station dans la distribution des minimums annuels des  │
  │                                              débits moyens sur 30 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Inverse des fiches de niveau de retour (VCN30-2) - la loi log-normale est
     ajustée sur la série des VCN30 puis évaluée au débit seuil constant Q_lim
     donné par les textes réglementaires (par exemple DOE, DCR) ; un seuil
     loin du corps de la loi donne une période de retour extrapolée, restituée
     telle quelle

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ an
        entrées ─ Q [m³·s⁻¹], Q_lim [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 30 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC30
            ╷
            ├── VCN30 = nanmin(VC30)
            │   └─ Minimum de VC30
            ├── Qlim = nanmean(Q_lim)
            │   └─ Moyenne du seuil Q_lim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN30, Qlim
            ╷
            ├── return_period(VCN30)
            │   │  sous Qlim, water_type=low
            │   └─ Période de retour du seuil Q_lim avec la loi log-normale
            │    ◦ Aucune agrégation temporelle
            ▼
           rp-VCN30

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/rp-VCN30.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f0af635092b1b1a939fb76d2f95138073a4b1d25</pre>

**Variables produced**  [`rp-VCN30`](../catalogue.md#rp-VCN30)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/rp-VCN30.yaml) &middot; [back to the catalogue](../catalogue.md)
