---
hide:
  - toc
---

# `delta-Q50A_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-Q50A_H        Average change of the annual median of daily flows  │
  │                        between the target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual flow with an exceedance probability of 50 % (50th percentile)

     phenomenon ─ mean flows
         season ─ annual
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   │  p=0.5
            │   └─ Median
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 01-01 to 12-31
            ▼
           Q50A
            ╷
            ├── delta(Q50A, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-Q50A

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-Q50A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:343bfa8a897651d6be627bb990ee85b64cc4f2ce</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-Q50A_H        Changement moyen de la médiane annuelle des débits  │
  │                         journaliers entre l'horizon cible et la période  │
  │                                                              historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit annuel avec une probabilité de dépassement de 50 % (centile 50 %)

      phénomène ─ moyennes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── exceedance_quantile(Q)
            │   │  p=0.5
            │   └─ Médiane
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-01 au 31-12
            ▼
           Q50A
            ╷
            ├── delta(Q50A, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-Q50A

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-Q50A_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:343bfa8a897651d6be627bb990ee85b64cc4f2ce</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-Q50A"><code>delta-Q50A</code></a></dt><dd><span lang="en">Average change of the annual median of daily flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la médiane annuelle des débits journaliers entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/delta-Q50A_H.yaml) &middot; [back to the catalogue](../catalogue.md)
