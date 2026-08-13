---
hide:
  - toc
---

# `dtCDDA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDA              Maximum number of consecutive dry days in the year  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Maximum number of consecutive days in the year with less than 1 mm of
     precipitation

     phenomenon ─ dry spells
         season ─ annual
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, longest episode, duration
            │   └─ Length of the longest period with precipitation below 1 mm
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtCDDA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f4309f5104c49ecf32c40a261bd6aadcef4a8de3</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDA           Nombre maximal de jours secs consécutifs dans l'année  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Nombre maximal de jours consécutifs dans l'année avec moins de 1 mm de
     précipitation

      phénomène ─ périodes sèches
         saison ─ annuelle
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      inférieures à 1 mm
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtCDDA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f4309f5104c49ecf32c40a261bd6aadcef4a8de3</pre>

**Variables produced**  [`dtCDDA`](../catalogue.md#dtCDDA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/dry-spells/series/dtCDDA.yaml) &middot; [back to the catalogue](../catalogue.md)
