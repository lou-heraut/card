---
hide:
  - toc
---

# `delta-dtBF_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-dtBF_H   Average change of the duration of low flows between the  │
  │                                    target horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Duration between the start and end of low flows

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ day
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── snowmelt_duration(Q)
            │   │  method=Wal
            │   └─ Number of days between the dates when the baseflow
            │      (Wallingford) sum corresponds to 10 % and 90 % of the total
            │      sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtBF
            ╷
            ├── delta(dtBF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-dtBF

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/baseflow/scalar/delta-dtBF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:41993975e8c9b51db0e2b2e2bb9e1aff04660c7e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-dtBF_H        Changement moyen de la durée des écoulements lents  │
  │                          entre l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Durée entre le début et la fin des écoulements lents

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── snowmelt_duration(Q)
            │   │  method=Wal
            │   └─ Nombre de jours entre les dates auxquelles la somme du
            │      débit de base (Wallingford) correspond à 10 % et 90 % de la
            │      somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtBF
            ╷
            ├── delta(dtBF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-dtBF

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/baseflow/scalar/delta-dtBF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:41993975e8c9b51db0e2b2e2bb9e1aff04660c7e</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-dtBF"><code>delta-dtBF</code></a></dt><dd><span lang="en">Average change of the duration of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la durée des écoulements lents entre l'horizon cible et la période historique</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/delta-dtBF_H.yaml) &middot; [back to the catalogue](../catalogue.md)
