---
hide:
  - toc
---

# `RCXA1`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RCXA1                            Annual maximum of daily precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ heavy rain
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nanmax(R)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           RCXA1

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/heavy-rain/series/RCXA1.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc3d70748dfc3e1f1b1658d5890110fa93942c9e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RCXA1                   Maximum annuel des précipitations journalières  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ pluies fortes
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nanmax(R)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           RCXA1

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/heavy-rain/series/RCXA1.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cc3d70748dfc3e1f1b1658d5890110fa93942c9e</pre>

**Variables produced**  [`RCXA1`](../catalogue.md#RCXA1)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/RCXA1.yaml) &middot; [back to the catalogue](../catalogue.md)
