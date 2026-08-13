---
hide:
  - toc
---

# `delta-fQ05A_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-fQ05A_H      Average change of the annual frequency of exceeding  │
  │                    Q05 between the target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual frequency of exceeding Q &gt; Q05, where Q05 is the flow exceeded 5 %
     of the time, extracted from the ranked flow curve

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile at the 5 % exceedance probability, taken as the
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
           fQ05A
            ╷
            ├── delta(fQ05A, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-fQ05A

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/high-flows/scalar/delta-fQ05A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:314595107d882a768557b87041e3b96505196d47</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-fQ05A_H             Changement moyen de la fréquence annuelle de  │
  │                  dépassement du Q05 entre l'horizon cible et la période  │
  │                                                              historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Fréquence annuelle de dépassement de Q &gt; Q05, Q05 est le débit dépassé 5
     % du temps, extrait de la courbe des débits classés

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile à la probabilité de dépassement de 5 %, pris comme
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
           fQ05A
            ╷
            ├── delta(fQ05A, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-fQ05A

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/high-flows/scalar/delta-fQ05A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:314595107d882a768557b87041e3b96505196d47</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-fQ05A"><code>delta-fQ05A</code></a></dt><dd><span lang="en">Average change of the annual frequency of exceeding Q05 between the target horizon and historical period</span><span lang="fr">Changement moyen de la fréquence annuelle de dépassement du Q05 entre l'horizon cible et la période historique</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/delta-fQ05A_H.yaml) &middot; [back to the catalogue](../catalogue.md)
