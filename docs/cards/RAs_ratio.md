---
hide:
  - toc
---

# `RAs_ratio`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAs_ratio          Ratio of annual solid precipitation to total annual  │
  │                                                           precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ snow
         season ─ annual
           form ─ series
           unit ─ without unit
         inputs ─ R [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Sum of total precipitation
            ├── RAs = nansum_strict(Rs)
            │   └─ Sum of solid precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA, RAs
            ╷
            ├── ratio(RAs, RA)
            │   └─ Solid/total ratio
            │    ◦ One value per year
            ▼
           RAs_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/series/RAs_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0b44e1c2151b9fade0ac4787d332b6755c0ff72c</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAs_ratio           Ratio des précipitations annuelles solides sur les  │
  │                                        précipitations annuelles totales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ neige
         saison ─ annuelle
          forme ─ série
          unité ─ sans unité
        entrées ─ R [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Somme des précipitations totales
            ├── RAs = nansum_strict(Rs)
            │   └─ Somme des précipitations solides
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA, RAs
            ╷
            ├── ratio(RAs, RA)
            │   └─ Rapport solide/total
            │    ◦ Une valeur par année
            ▼
           RAs_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/series/RAs_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0b44e1c2151b9fade0ac4787d332b6755c0ff72c</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RAs_ratio"><code>RAs_ratio</code></a></dt><dd><span lang="en">Ratio of annual solid precipitation to total annual precipitation</span><span lang="fr">Ratio des précipitations annuelles solides sur les précipitations annuelles totales</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/series/RAs_ratio.yaml) &middot; [back to the catalogue](../catalogue.md)
