---
hide:
  - toc
---

# `delta-Q10A_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-Q10A_H     Average change of the daily flow exceeded 10 % of the  │
  │                     time within the year between the target horizon and  │
  │                                                       historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual flow with an exceedance probability of 10 % (90th percentile)

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile at the exceedance probability of 10 %
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 01-01 to 12-31
            ▼
           Q10A
            ╷
            ├── delta(Q10A, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-Q10A

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/scalar/delta-Q10A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:55f23748238f6db2268dcfaaa2d3f75be7b16bc3</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-Q10A_H      Changement moyen du débit journalier dépassé 10 % du  │
  │                    temps de l'année entre l'horizon cible et la période  │
  │                                                              historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit annuel avec une probabilité de dépassement de 10 % (centile 90 %)

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile à la probabilité de dépassement de 10 %
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-01 au 31-12
            ▼
           Q10A
            ╷
            ├── delta(Q10A, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-Q10A

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/scalar/delta-Q10A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:55f23748238f6db2268dcfaaa2d3f75be7b16bc3</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-Q10A"><code>delta-Q10A</code></a></dt><dd><span lang="en">Average change of the daily flow exceeded 10 % of the time within the year between the target horizon and historical period</span><span lang="fr">Changement moyen du débit journalier dépassé 10 % du temps de l'année entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/delta-Q10A_H.yaml) &middot; [back to the catalogue](../catalogue.md)
