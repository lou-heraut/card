---
hide:
  - toc
---

# `ETPA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPA                    Annual cumulative potential evapotranspiration  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ evaporative demand
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           ETPA

  ──────────────────────────────────────────────────────────────────────────
  v1.1.1   evapotranspiration/evaporative-demand/series/ETPA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b1336d286c80c8d34c8a2d3713370cb6994cd3c3</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  ETPA                  Cumul annuel de l'évapotranspiration potentielle  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ demande évaporative
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ ETP [mm]

            ╷
            ├── nansum_strict(ETP)
            │   └─ Somme
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           ETPA

  ──────────────────────────────────────────────────────────────────────────
  v1.1.1   evapotranspiration/evaporative-demand/series/ETPA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b1336d286c80c8d34c8a2d3713370cb6994cd3c3</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#ETPA"><code>ETPA</code></a></dt><dd><span lang="en">Annual cumulative potential evapotranspiration</span><span lang="fr">Cumul annuel de l'évapotranspiration potentielle</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/evapotranspiration/evaporative-demand/series/ETPA.yaml) &middot; [back to the catalogue](../catalogue.md)
