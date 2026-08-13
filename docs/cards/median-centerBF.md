---
hide:
  - toc
---

# `median-centerBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-centerBF          Inter-annual median of the center of baseflow  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the dates at which 50 % of the annual cumulative baseflow is
     reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date at which the baseflow (Wallingford) sum Qb corresponds
            │      to 50 % of the total sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           centerBF
            ╷
            ├── circular_median(centerBF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-centerBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-centerBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5fe544355dfbf6e9c2e132038034e39e25a676b6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-centerBF       Médiane inter-annuelle du centre des écoulements  │
  │                                                                   lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des dates à laquelle 50 % du cumul annuel du débit de base sont
     atteints

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

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
            ├── circular_median(centerBF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-centerBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-centerBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5fe544355dfbf6e9c2e132038034e39e25a676b6</pre>

**Variables produced**  [`median-centerBF`](../catalogue.md#median-centerBF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/median-centerBF.yaml) &middot; [back to the catalogue](../catalogue.md)
