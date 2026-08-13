---
hide:
  - toc
---

# `RAl_ratio`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAl_ratio         Ratio of annual liquid precipitation to total annual  │
  │                                                           precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ snow
         season ─ annual
           form ─ series
           unit ─ without unit
         inputs ─ R [mm], Rl [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Sum of total precipitation
            ├── RAl = nansum_strict(Rl)
            │   └─ Sum of liquid precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA, RAl
            ╷
            ├── ratio(RAl, RA)
            │   └─ Liquid/total ratio
            │    ◦ One value per year
            ▼
           RAl_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/series/RAl_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c79995bc79b0d171a2150057d5986e56e37fe7a3</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAl_ratio          Ratio des précipitations annuelles liquides sur les  │
  │                                        précipitations annuelles totales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ neige
         saison ─ annuelle
          forme ─ série
          unité ─ sans unité
        entrées ─ R [mm], Rl [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Somme des précipitations totales
            ├── RAl = nansum_strict(Rl)
            │   └─ Somme des précipitations liquides
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA, RAl
            ╷
            ├── ratio(RAl, RA)
            │   └─ Rapport liquide/total
            │    ◦ Une valeur par année
            ▼
           RAl_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/series/RAl_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c79995bc79b0d171a2150057d5986e56e37fe7a3</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RAl_ratio"><code>RAl_ratio</code></a></dt><dd><span lang="en">Ratio of annual liquid precipitation to total annual precipitation</span><span lang="fr">Ratio des précipitations annuelles liquides sur les précipitations annuelles totales</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/series/RAl_ratio.yaml) &middot; [back to the catalogue](../catalogue.md)
