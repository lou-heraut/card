---
hide:
  - toc
---

# `delta-fQ01A_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-fQ01A_H      Average change of the annual frequency of exceeding  │
  │                    Q01 between the target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual frequency of exceeding Q &gt; Q01, where Q01 is the flow exceeded 1 %
     of the time, extracted from the ranked flow curve

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile at the 1 % exceedance probability, taken as the
            │      threshold
            │    ◦ A single value, repeated over the whole record
            │    ◦ Cut beyond 10 missing years
            ▼
           lowLim
            ╷
            ├── exceedance_frequency(Q)
            │   │  below lowLim
            │   └─ Ratio of the number of days with flow exceeding lowLim to
            │      the number of days in the year
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           fQ01A
            ╷
            ├── delta(fQ01A, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-fQ01A

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/high-flows/scalar/delta-fQ01A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cec1f62fa61666420ea12ab24f9f409fefe14f8f</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-fQ01A_H             Changement moyen de la fréquence annuelle de  │
  │                  dépassement du Q01 entre l'horizon cible et la période  │
  │                                                              historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Fréquence annuelle de dépassement de Q &gt; Q01, Q01 est le débit dépassé 1
     % du temps, extrait de la courbe des débits classés

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile à la probabilité de dépassement de 1 %, pris comme
            │      seuil
            │    ◦ Une seule valeur, répétée sur toute la chronique
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           lowLim
            ╷
            ├── exceedance_frequency(Q)
            │   │  sous lowLim
            │   └─ Rapport du nombre de jours où le débit dépasse lowLim par
            │      le nombre de jours dans l'année
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           fQ01A
            ╷
            ├── delta(fQ01A, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-fQ01A

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/high-flows/scalar/delta-fQ01A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cec1f62fa61666420ea12ab24f9f409fefe14f8f</pre>

**Variables produced**  [`delta-fQ01A`](../catalogue.md#delta-fQ01A)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/delta-fQ01A_H.yaml) &middot; [back to the catalogue](../catalogue.md)
