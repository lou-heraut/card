---
hide:
  - toc
---

# `RA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA                                          Annual total precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean precipitation
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/series/RA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a07f07aff5cbf35dcf6947dde24e4a6989960076</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA                             Cumul annuel des précipitations totales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ précipitations moyennes
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Somme
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/series/RA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a07f07aff5cbf35dcf6947dde24e4a6989960076</pre>

**Variables produced**  [`RA`](../catalogue.md#RA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/series/RA.yaml) &middot; [back to the catalogue](../catalogue.md)
