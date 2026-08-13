---
hide:
  - toc
---

# `delta-QJXA-10_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QJXA-10_H     Change of annual maximum daily flow with a 10-year  │
  │                            return period between the target horizon and  │
  │                                                       historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

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
            ├── delta(QJXA, date)
            │   │  relative=True, water_type=high
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the 10-year return period flow with the
            │      Gumbel distribution on the historical period and in the
            │      target horizon then calculation of the average change
            │    ◦ No temporal aggregation
            ▼
           delta-QJXA-10

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/scalar/delta-QJXA-10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:415487a515a29072bb342ed2a34543caba7c8abf</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QJXA-10_H       Changement du débit journalier maximal annuel de  │
  │                    période de retour 10 ans entre l'horizon cible et la  │
  │                                                      période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

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
            ├── delta(QJXA, date)
            │   │  relative=True, water_type=high
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du débit de période de retour 10 ans avec la loi de
            │      Gumbel sur la période historique et en horizon cible puis
            │      calcul du changement moyen
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-QJXA-10

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/scalar/delta-QJXA-10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:415487a515a29072bb342ed2a34543caba7c8abf</pre>

**Variables produced**  [`delta-QJXA-10`](../catalogue.md#delta-QJXA-10)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/delta-QJXA-10_H.yaml) &middot; [back to the catalogue](../catalogue.md)
