---
hide:
  - toc
---

# `dtRA01mm`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRA01mm                              Number of rainy days in the year  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Number of days with at least 1 mm of precipitation

     phenomenon ─ wet days
         season ─ annual
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 1 mm
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtRA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRA01mm.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d1e9b90fd5838bb7489217fda2dd77b317a7ea2</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRA01mm                         Nombre de jours pluvieux dans l'année  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Nombre de jours avec au moins 1 mm de précipitations

      phénomène ─ jours pluvieux
         saison ─ annuelle
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 1 mm
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtRA01mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtRA01mm.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d1e9b90fd5838bb7489217fda2dd77b317a7ea2</pre>

**Variables produced**  [`dtRA01mm`](../catalogue.md#dtRA01mm)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtRA01mm.yaml) &middot; [back to the catalogue](../catalogue.md)
