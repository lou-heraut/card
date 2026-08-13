---
hide:
  - toc
---

# `median-endBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-endBF              Inter-annual median of the end of base flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the dates when 90 % of the annual cumulative base flow is
     reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date when the sum of base flow (Wallingford) corresponds to
            │      90 % of the total sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           endBF
            ╷
            ├── circular_median(endBF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-endBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-endBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:73e4fb5e85f2c2d641b69675e23c5bc319df60a2</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-endBF    Médiane inter-annuelle de la fin des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des dates à laquelle 90 % du cumul annuel du débit de base sont
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
            │      correspond à 90 % de la somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           endBF
            ╷
            ├── circular_median(endBF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-endBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-endBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:73e4fb5e85f2c2d641b69675e23c5bc319df60a2</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-endBF"><code>median-endBF</code></a></dt><dd><span lang="en">Inter-annual median of the end of base flows</span><span lang="fr">Médiane inter-annuelle de la fin des écoulements lents</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/median-endBF.yaml) &middot; [back to the catalogue](../catalogue.md)
