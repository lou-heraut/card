---
hide:
  - toc
---

# `dtRMA50mm_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA50mm_month                                             12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA50mm_jan
       Number of extreme rain days for each January
       Number of days with at least 50 mm of precipitation for each January

     ◇ dtRMA50mm_feb
       Number of extreme rain days for each February
       Number of days with at least 50 mm of precipitation for each February

     ◇ dtRMA50mm_mar
       Number of extreme rain days for each March
       Number of days with at least 50 mm of precipitation for each March

     ◇ dtRMA50mm_apr
       Number of extreme rain days for each April
       Number of days with at least 50 mm of precipitation for each April

     ◇ dtRMA50mm_may
       Number of extreme rain days for each May
       Number of days with at least 50 mm of precipitation for each May

     ◇ dtRMA50mm_jun
       Number of extreme rain days for each June
       Number of days with at least 50 mm of precipitation for each June

     ◇ dtRMA50mm_jul
       Number of extreme rain days for each July
       Number of days with at least 50 mm of precipitation for each July

     ◇ dtRMA50mm_aug
       Number of extreme rain days for each August
       Number of days with at least 50 mm of precipitation for each August

     ◇ dtRMA50mm_sep
       Number of extreme rain days for each September
       Number of days with at least 50 mm of precipitation for each September

     ◇ dtRMA50mm_oct
       Number of extreme rain days for each October
       Number of days with at least 50 mm of precipitation for each October

     ◇ dtRMA50mm_nov
       Number of extreme rain days for each November
       Number of days with at least 50 mm of precipitation for each November

     ◇ dtRMA50mm_dec
       Number of extreme rain days for each December
       Number of days with at least 50 mm of precipitation for each December

     phenomenon ─ heavy rain
         season ─ by month
           form ─ series
           unit ─ day
          input ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, duration
            │   └─ Number of days with precipitation of at least 50 mm
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           dtRMA50mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRMA50mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d7a7bb6fa82d8017fe250267728c32c36bde7895</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtRMA50mm_month                                             12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ dtRMA50mm_jan (dtRMA50mm_janv)
       Nombre de jours de pluie extrême de chaque janvier
       Nombre de jours avec au moins 50 mm de précipitations de chaque janvier

     ◇ dtRMA50mm_feb (dtRMA50mm_fevr)
       Nombre de jours de pluie extrême de chaque février
       Nombre de jours avec au moins 50 mm de précipitations de chaque février

     ◇ dtRMA50mm_mar (dtRMA50mm_mars)
       Nombre de jours de pluie extrême de chaque mars
       Nombre de jours avec au moins 50 mm de précipitations de chaque mars

     ◇ dtRMA50mm_apr (dtRMA50mm_avril)
       Nombre de jours de pluie extrême de chaque avril
       Nombre de jours avec au moins 50 mm de précipitations de chaque avril

     ◇ dtRMA50mm_may (dtRMA50mm_mai)
       Nombre de jours de pluie extrême de chaque mai
       Nombre de jours avec au moins 50 mm de précipitations de chaque mai

     ◇ dtRMA50mm_jun (dtRMA50mm_juin)
       Nombre de jours de pluie extrême de chaque juin
       Nombre de jours avec au moins 50 mm de précipitations de chaque juin

     ◇ dtRMA50mm_jul (dtRMA50mm_juil)
       Nombre de jours de pluie extrême de chaque juillet
       Nombre de jours avec au moins 50 mm de précipitations de chaque juillet

     ◇ dtRMA50mm_aug (dtRMA50mm_aout)
       Nombre de jours de pluie extrême de chaque août
       Nombre de jours avec au moins 50 mm de précipitations de chaque août

     ◇ dtRMA50mm_sep (dtRMA50mm_sept)
       Nombre de jours de pluie extrême de chaque septembre
       Nombre de jours avec au moins 50 mm de précipitations de chaque
       septembre

     ◇ dtRMA50mm_oct
       Nombre de jours de pluie extrême de chaque octobre
       Nombre de jours avec au moins 50 mm de précipitations de chaque octobre

     ◇ dtRMA50mm_nov
       Nombre de jours de pluie extrême de chaque novembre
       Nombre de jours avec au moins 50 mm de précipitations de chaque
       novembre

     ◇ dtRMA50mm_dec
       Nombre de jours de pluie extrême de chaque décembre
       Nombre de jours avec au moins 50 mm de précipitations de chaque
       décembre

      phénomène ─ pluies fortes
         saison ─ par mois
          forme ─ série
          unité ─ jour
         entrée ─ R [mm]

            ╷
            ├── apply_threshold(R)
            │   │  select=all, durée
            │   └─ Nombre de jours avec des précipitations d'au moins 50 mm
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dtRMA50mm

  ──────────────────────────────────────────────────────────────────────────
  v1.0   precipitation/heavy-rain/series/dtRMA50mm_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d7a7bb6fa82d8017fe250267728c32c36bde7895</pre>

**Variables produced**  [`dtRMA50mm_jan`](../catalogue.md#dtRMA50mm_jan) · [`dtRMA50mm_feb`](../catalogue.md#dtRMA50mm_feb) · [`dtRMA50mm_mar`](../catalogue.md#dtRMA50mm_mar) · [`dtRMA50mm_apr`](../catalogue.md#dtRMA50mm_apr) · [`dtRMA50mm_may`](../catalogue.md#dtRMA50mm_may) · [`dtRMA50mm_jun`](../catalogue.md#dtRMA50mm_jun) · [`dtRMA50mm_jul`](../catalogue.md#dtRMA50mm_jul) · [`dtRMA50mm_aug`](../catalogue.md#dtRMA50mm_aug) · [`dtRMA50mm_sep`](../catalogue.md#dtRMA50mm_sep) · [`dtRMA50mm_oct`](../catalogue.md#dtRMA50mm_oct) · [`dtRMA50mm_nov`](../catalogue.md#dtRMA50mm_nov) · [`dtRMA50mm_dec`](../catalogue.md#dtRMA50mm_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/heavy-rain/series/dtRMA50mm_month.yaml) &middot; [back to the catalogue](../catalogue.md)
