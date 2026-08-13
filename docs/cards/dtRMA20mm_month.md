---
hide:
  - toc
---

# `dtRMA20mm_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA20mm_month                                             12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA20mm_jan
       Number of heavy rain days for each January
       Number of days with at least 20 mm of precipitation for each January

     ◇ dtRMA20mm_feb
       Number of heavy rain days for each February
       Number of days with at least 20 mm of precipitation for each February

     ◇ dtRMA20mm_mar
       Number of heavy rain days for each March
       Number of days with at least 20 mm of precipitation for each March

     ◇ dtRMA20mm_apr
       Number of heavy rain days for each April
       Number of days with at least 20 mm of precipitation for each April

     ◇ dtRMA20mm_may
       Number of heavy rain days for each May
       Number of days with at least 20 mm of precipitation for each May

     ◇ dtRMA20mm_jun
       Number of heavy rain days for each June
       Number of days with at least 20 mm of precipitation for each June

     ◇ dtRMA20mm_jul
       Number of heavy rain days for each July
       Number of days with at least 20 mm of precipitation for each July

     ◇ dtRMA20mm_aug
       Number of heavy rain days for each August
       Number of days with at least 20 mm of precipitation for each August

     ◇ dtRMA20mm_sep
       Number of heavy rain days for each September
       Number of days with at least 20 mm of precipitation for each September

     ◇ dtRMA20mm_oct
       Number of heavy rain days for each October
       Number of days with at least 20 mm of precipitation for each October

     ◇ dtRMA20mm_nov
       Number of heavy rain days for each November
       Number of days with at least 20 mm of precipitation for each November

     ◇ dtRMA20mm_dec
       Number of heavy rain days for each December
       Number of days with at least 20 mm of precipitation for each December

     phenomenon ─ heavy rain
         season ─ by month
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 20 mm
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRMA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRMA20mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2d4041b040e20fee4111a8344f38ba6a5628b05e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA20mm_month                                             12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA20mm_jan (dtRMA20mm_janv)
       Nombre de jours de forte pluie de chaque janvier
       Nombre de jours avec au moins 20 mm de précipitations de chaque janvier

     ◇ dtRMA20mm_feb (dtRMA20mm_fevr)
       Nombre de jours de forte pluie de chaque février
       Nombre de jours avec au moins 20 mm de précipitations de chaque février

     ◇ dtRMA20mm_mar (dtRMA20mm_mars)
       Nombre de jours de forte pluie de chaque mars
       Nombre de jours avec au moins 20 mm de précipitations de chaque mars

     ◇ dtRMA20mm_apr (dtRMA20mm_avril)
       Nombre de jours de forte pluie de chaque avril
       Nombre de jours avec au moins 20 mm de précipitations de chaque avril

     ◇ dtRMA20mm_may (dtRMA20mm_mai)
       Nombre de jours de forte pluie de chaque mai
       Nombre de jours avec au moins 20 mm de précipitations de chaque mai

     ◇ dtRMA20mm_jun (dtRMA20mm_juin)
       Nombre de jours de forte pluie de chaque juin
       Nombre de jours avec au moins 20 mm de précipitations de chaque juin

     ◇ dtRMA20mm_jul (dtRMA20mm_juil)
       Nombre de jours de forte pluie de chaque juillet
       Nombre de jours avec au moins 20 mm de précipitations de chaque juillet

     ◇ dtRMA20mm_aug (dtRMA20mm_aout)
       Nombre de jours de forte pluie de chaque août
       Nombre de jours avec au moins 20 mm de précipitations de chaque août

     ◇ dtRMA20mm_sep (dtRMA20mm_sept)
       Nombre de jours de forte pluie de chaque septembre
       Nombre de jours avec au moins 20 mm de précipitations de chaque
       septembre

     ◇ dtRMA20mm_oct
       Nombre de jours de forte pluie de chaque octobre
       Nombre de jours avec au moins 20 mm de précipitations de chaque octobre

     ◇ dtRMA20mm_nov
       Nombre de jours de forte pluie de chaque novembre
       Nombre de jours avec au moins 20 mm de précipitations de chaque
       novembre

     ◇ dtRMA20mm_dec
       Nombre de jours de forte pluie de chaque décembre
       Nombre de jours avec au moins 20 mm de précipitations de chaque
       décembre

      phénomène ─ pluies fortes
         saison ─ par mois
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 20 mm
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRMA20mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRMA20mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2d4041b040e20fee4111a8344f38ba6a5628b05e</pre>

**Variables produced**  [`dtRMA20mm_jan`](../catalogue.md#dtRMA20mm_jan) · [`dtRMA20mm_feb`](../catalogue.md#dtRMA20mm_feb) · [`dtRMA20mm_mar`](../catalogue.md#dtRMA20mm_mar) · [`dtRMA20mm_apr`](../catalogue.md#dtRMA20mm_apr) · [`dtRMA20mm_may`](../catalogue.md#dtRMA20mm_may) · [`dtRMA20mm_jun`](../catalogue.md#dtRMA20mm_jun) · [`dtRMA20mm_jul`](../catalogue.md#dtRMA20mm_jul) · [`dtRMA20mm_aug`](../catalogue.md#dtRMA20mm_aug) · [`dtRMA20mm_sep`](../catalogue.md#dtRMA20mm_sep) · [`dtRMA20mm_oct`](../catalogue.md#dtRMA20mm_oct) · [`dtRMA20mm_nov`](../catalogue.md#dtRMA20mm_nov) · [`dtRMA20mm_dec`](../catalogue.md#dtRMA20mm_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/dtRMA20mm_month.yaml) &middot; [back to the catalogue](../catalogue.md)
