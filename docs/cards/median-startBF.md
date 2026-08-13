---
hide:
  - toc
---

# `median-startBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-startBF            Inter-annual median of the start of baseflow  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the dates at which 10 % of the annual cumulative baseflow is
     reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date when the baseflow (Wallingford) sum corresponds to 10
            │      % of the total sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           startBF
            ╷
            ├── circular_median(startBF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-startBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-startBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bedf30207b4230270594a9222356db4d3689853f</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-startBF   Médiane inter-annuelle du début des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des dates à laquelle 10 % du cumul annuel du débit de base sont
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
            │      correspond à 10 % de la somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           startBF
            ╷
            ├── circular_median(startBF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-startBF

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/median-startBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bedf30207b4230270594a9222356db4d3689853f</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-startBF"><code>median-startBF</code></a></dt><dd><span lang="en">Inter-annual median of the start of baseflow</span><span lang="fr">Médiane inter-annuelle du début des écoulements lents</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/median-startBF.yaml) &middot; [back to the catalogue](../catalogue.md)
