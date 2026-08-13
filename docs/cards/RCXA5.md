---
hide:
  - toc
---

# `RCXA5`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RCXA5           Annual maximum of 5-day cumulative daily precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ heavy rain
         season ─ annual
           form ─ series
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── rollsum_center(R)
            │   └─ 5-day centered moving sum
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           RC5
            ╷
            ├── nanmax(RC5)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           RCXA5

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/heavy-rain/series/RCXA5.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f156ccaf05436ff5fa40e03cd8ace2212f1c3a29</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RCXA5           Maximum annuel du cumul sur 5 jours des précipitations  │
  │                                                            journalières  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ pluies fortes
         saison ─ annuelle
          forme ─ série
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── rollsum_center(R)
            │   └─ Somme mobile centrée sur 5 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           RC5
            ╷
            ├── nanmax(RC5)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           RCXA5

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/heavy-rain/series/RCXA5.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f156ccaf05436ff5fa40e03cd8ace2212f1c3a29</pre>

**Variables produced**  [`RCXA5`](../catalogue.md#RCXA5)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/RCXA5.yaml) &middot; [back to the catalogue](../catalogue.md)
