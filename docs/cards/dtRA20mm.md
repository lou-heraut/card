---
hide:
  - toc
---

# `dtRA20mm`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRA20mm                         Number of heavy rain days in the year  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Number of days with at least 20 mm of precipitation

     phenomenon ─ heavy rain
         season ─ annual
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 20 mm
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtRA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRA20mm.yaml
  https://archive.softwareheritage.org/swh:1:cnt:04e749ebdff634aecd9a92e5ed316347332b3cf9</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRA20mm                   Nombre de jours de forte pluie dans l'année  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Nombre de jours avec au moins 20 mm de précipitations

      phénomène ─ pluies fortes
         saison ─ annuelle
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 20 mm
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtRA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRA20mm.yaml
  https://archive.softwareheritage.org/swh:1:cnt:04e749ebdff634aecd9a92e5ed316347332b3cf9</pre>

**Variables produced**  [`dtRA20mm`](../catalogue.md#dtRA20mm)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/dtRA20mm.yaml) &middot; [back to the catalogue](../catalogue.md)
