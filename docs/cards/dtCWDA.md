---
hide:
  - toc
---

# `dtCWDA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDA            Maximum number of consecutive rainy days in the year  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Maximum number of consecutive days in the year with at least 1 mm of
     precipitation

     phenomenon ─ wet days
         season ─ annual
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  longest episode, duration
            │   └─ Length of the longest period with precipitation of at least
            │      1 mm
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtCWDA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f47be4c438c458c5827279d912d2fb69674265ee</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCWDA       Nombre maximal de jours pluvieux consécutifs dans l'année  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Nombre maximal de jours consécutifs dans l'année avec au moins 1 mm de
     précipitation

      phénomène ─ jours pluvieux
         saison ─ annuelle
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      d'au moins 1 mm
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtCWDA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/wet-days/series/dtCWDA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f47be4c438c458c5827279d912d2fb69674265ee</pre>

**Variables produced**  [`dtCWDA`](../catalogue.md#dtCWDA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/wet-days/series/dtCWDA.yaml) &middot; [back to the catalogue](../catalogue.md)
