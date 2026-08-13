---
hide:
  - toc
---

# `centerBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  centerBF                                           Center of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date when 50 % of the annual cumulative baseflow is reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ series
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

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

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/baseflow/series/centerBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:eed5768a439caebb80361beb85ca1acfc9f4410e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  centerBF                                  Centre des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date à laquelle 50 % du cumul annuel du débit de base sont atteints

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ série
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

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/baseflow/series/centerBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:eed5768a439caebb80361beb85ca1acfc9f4410e</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#centerBF"><code>centerBF</code></a></dt><dd><span lang="en">Center of low flows</span><span lang="fr">Centre des écoulements lents</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/series/centerBF.yaml) &middot; [back to the catalogue](../catalogue.md)
