---
hide:
  - toc
---

# `RAs`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAs                                         Annual solid precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ snow
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RAs

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/snow/series/RAs.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c473a316c168b020055501984f2c9720b0e621bd</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAs                            Cumul annuel des précipitations solides  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ neige
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ Rs [mm]

            ╷
            ├── nansum_strict(Rs)
            │   └─ Somme
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RAs

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/snow/series/RAs.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c473a316c168b020055501984f2c9720b0e621bd</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RAs"><code>RAs</code></a></dt><dd><span lang="en">Annual solid precipitation</span><span lang="fr">Cumul annuel des précipitations solides</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/series/RAs.yaml) &middot; [back to the catalogue](../catalogue.md)
