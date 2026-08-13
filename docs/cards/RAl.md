---
hide:
  - toc
---

# `RAl`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAl                                        Annual liquid precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean precipitation
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RAl

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/mean-precipitation/series/RAl.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc7653aa492e221fb5baedbb228d1264947589f7</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAl                           Cumul annuel des précipitations liquides  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ précipitations moyennes
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ Rl [mm]

            ╷
            ├── nansum_strict(Rl)
            │   └─ Somme
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RAl

  ──────────────────────────────────────────────────────────────────────────
  v1.2   precipitation/mean-precipitation/series/RAl.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc7653aa492e221fb5baedbb228d1264947589f7</pre>

**Variables produced**  [`RAl`](../catalogue.md#RAl)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RAl.yaml) &middot; [back to the catalogue](../catalogue.md)
