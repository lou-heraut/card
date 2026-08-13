---
hide:
  - toc
---

# `RA_all`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA_all                                                       3 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RA
       Annual total precipitation

     ◇ RAl
       Annual liquid precipitation

     ◇ RAs
       Annual solid precipitation

     phenomenon ─ mean precipitation
         season ─ annual
           form ─ series
           unit ─ mm
         inputs ─ R [mm], Rl [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Sum of total precipitation
            ├── RAl = nansum_strict(Rl)
            │   └─ Sum of liquid precipitation
            ├── RAs = nansum_strict(Rs)
            │   └─ Sum of solid precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA, RAl, RAs

  ──────────────────────────────────────────────────────────────────────────
  v2.0   precipitation/mean-precipitation/series/RA_all.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2df25743a4ba39aff31d9bfca76999e66405369c</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA_all                                                       3 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ RA
       Cumul annuel des précipitations totales

     ◇ RAl
       Cumul annuel des précipitations liquides

     ◇ RAs
       Cumul annuel des précipitations solides

      phénomène ─ précipitations moyennes
         saison ─ annuelle
          forme ─ série
          unité ─ mm
        entrées ─ R [mm], Rl [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Somme des précipitations totales
            ├── RAl = nansum_strict(Rl)
            │   └─ Somme des précipitations liquides
            ├── RAs = nansum_strict(Rs)
            │   └─ Somme des précipitations solides
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA, RAl, RAs

  ──────────────────────────────────────────────────────────────────────────
  v2.0   precipitation/mean-precipitation/series/RA_all.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2df25743a4ba39aff31d9bfca76999e66405369c</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RA"><code>RA</code></a></dt><dd><span lang="en">Annual total precipitation</span><span lang="fr">Cumul annuel des précipitations totales</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RAl"><code>RAl</code></a></dt><dd><span lang="en">Annual liquid precipitation</span><span lang="fr">Cumul annuel des précipitations liquides</span><span class="u">mm</span></dd><dt><a href="../../catalogue/#RAs"><code>RAs</code></a></dt><dd><span lang="en">Annual solid precipitation</span><span lang="fr">Cumul annuel des précipitations solides</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RA_all.yaml) &middot; [back to the catalogue](../catalogue.md)
