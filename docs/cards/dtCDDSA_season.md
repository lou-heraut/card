---
hide:
  - toc
---

# `dtCDDSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDSA_season                                               4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCDDSA_DJF
       Maximum number of consecutive dry days in winter
       Maximum number of consecutive days in winter with less than 1 mm of
       precipitation (months of December, January, and February)

     ◇ dtCDDSA_MAM
       Maximum number of consecutive dry days in spring
       Maximum number of consecutive days in spring with less than 1 mm of
       precipitation (months of March, April, and May)

     ◇ dtCDDSA_JJA
       Maximum number of consecutive dry days in summer
       Maximum number of consecutive days in summer with less than 1 mm of
       precipitation (months of June, July, and August)

     ◇ dtCDDSA_SON
       Maximum number of consecutive dry days in autumn
       Maximum number of consecutive days in autumn with less than 1 mm of
       precipitation (months of September, October, and November)

     phenomenon ─ dry spells
         season ─ by season
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, longest episode, duration
            │   └─ Length of the longest period with precipitation below 1 mm
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtCDDSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:00b1d47f7e927d2479dbf83d1119d3b57b663d31</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtCDDSA_season                                               4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtCDDSA_DJF
       Nombre maximal de jours secs consécutifs dans l'hiver
       Nombre maximal de jours consécutifs dans l'hiver avec moins de 1 mm de
       précipitation (mois de décembre, janvier et février)

     ◇ dtCDDSA_MAM
       Nombre maximal de jours secs consécutifs au printemps
       Nombre maximal de jours consécutifs au printemps avec moins de 1 mm de
       précipitation (mois de mars, avril et mai)

     ◇ dtCDDSA_JJA
       Nombre maximal de jours secs consécutifs en été
       Nombre maximal de jours consécutifs en été avec moins de 1 mm de
       précipitation (mois de juin, juillet et août)

     ◇ dtCDDSA_SON
       Nombre maximal de jours secs consécutifs en automne
       Nombre maximal de jours consécutifs en automne avec moins de 1 mm de
       précipitation (mois de septembre, octobre et novembre)

      phénomène ─ périodes sèches
         saison ─ par saison
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  R &lt; 1, plus long épisode, durée
            │   └─ Durée de la plus longue période avec des précipitations
            │      inférieures à 1 mm
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtCDDSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/dry-spells/series/dtCDDSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:00b1d47f7e927d2479dbf83d1119d3b57b663d31</pre>

**Variables produced**  [`dtCDDSA_DJF`](../catalogue.md#dtCDDSA_DJF) · [`dtCDDSA_MAM`](../catalogue.md#dtCDDSA_MAM) · [`dtCDDSA_JJA`](../catalogue.md#dtCDDSA_JJA) · [`dtCDDSA_SON`](../catalogue.md#dtCDDSA_SON)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/dry-spells/series/dtCDDSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
