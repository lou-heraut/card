---
hide:
  - toc
---

# `delta-VCN10-5_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN10-5_H          Change of annual minimum of 10-day mean daily  │
  │                       discharge with a return period of 5 years between  │
  │                                the target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN10
            ╷
            ├── delta(VCN10, date)
            │   │  relative=True, water_type=low
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the 5-year return period flow with the
            │      log-normal distribution on the historical period and in the
            │      target horizon then calculation of the average change
            │    ◦ No temporal aggregation
            ▼
           delta-VCN10-5

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/low-flows/scalar/delta-VCN10-5_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:54bb2a011529ac92cb86d91f75b32698278c27ea</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN10-5_H      Changement du minimum annuel de la moyenne sur 10  │
  │                    jours du débit journalier VCN10 de période de retour  │
  │                    5 ans entre l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN10
            ╷
            ├── delta(VCN10, date)
            │   │  relative=True, water_type=low
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du débit de période de retour 5 ans avec la loi
            │      log-normal sur la période historique et en horizon cible
            │      puis calcul du changement moyen
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-VCN10-5

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/low-flows/scalar/delta-VCN10-5_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:54bb2a011529ac92cb86d91f75b32698278c27ea</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-VCN10-5"><code>delta-VCN10-5</code></a></dt><dd><span lang="en">Change of annual minimum of 10-day mean daily discharge with a return period of 5 years between the target horizon and historical period</span><span lang="fr">Changement du minimum annuel de la moyenne sur 10 jours du débit journalier VCN10 de période de retour 5 ans entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-VCN10-5_H.yaml) &middot; [back to the catalogue](../catalogue.md)
