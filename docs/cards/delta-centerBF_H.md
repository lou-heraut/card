---
hide:
  - toc
---

# `delta-centerBF_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-centerBF_H     Average change of the center of low flows between  │
  │                                the target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date when 50 % of the annual cumulative baseflow is reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ day
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date when the baseflow (Wallingford) sum corresponds to 50
            │      % of the total sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           centerBF
            ╷
            ├── delta(centerBF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-centerBF

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/delta-centerBF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:da0af031a55ca8cfffdf637ce43931ca4a6094a5</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-centerBF_H      Changement moyen du centre des écoulements lents  │
  │                          entre l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date à laquelle 50 % du cumul annuel du débit de base sont atteints

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date à laquelle la somme du débit de base (Wallingford)
            │      correspond à 50 % de la somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           centerBF
            ╷
            ├── delta(centerBF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-centerBF

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/delta-centerBF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:da0af031a55ca8cfffdf637ce43931ca4a6094a5</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-centerBF"><code>delta-centerBF</code></a></dt><dd><span lang="en">Average change of the center of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du centre des écoulements lents entre l'horizon cible et la période historique</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/delta-centerBF_H.yaml) &middot; [back to the catalogue](../catalogue.md)
