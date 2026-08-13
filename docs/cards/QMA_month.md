---
hide:
  - toc
---

# `QMA_month`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMA_month                                                   12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QMA_jan
       Average daily discharge for each January

     ◇ QMA_feb
       Average daily discharge for each February

     ◇ QMA_mar
       Average daily discharge for each March

     ◇ QMA_apr
       Average daily discharge for each April

     ◇ QMA_may
       Average daily discharge for each May

     ◇ QMA_jun
       Average daily discharge for each June

     ◇ QMA_jul
       Average daily discharge for each July

     ◇ QMA_aug
       Average daily discharge for each August

     ◇ QMA_sep
       Average daily discharge for each September

     ◇ QMA_oct
       Average daily discharge for each October

     ◇ QMA_nov
       Average daily discharge for each November

     ◇ QMA_dec
       Average daily discharge for each December

     phenomenon ─ mean flows
         season ─ by month
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:12859c9e0bb9417db8645687d7489db36f1e8ff0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QMA_month                                                   12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QMA_jan (QMA_janv)
       Moyenne des débits journaliers de chaque janvier

     ◇ QMA_feb (QMA_fevr)
       Moyenne des débits journaliers de chaque février

     ◇ QMA_mar (QMA_mars)
       Moyenne des débits journaliers de chaque mars

     ◇ QMA_apr (QMA_avril)
       Moyenne des débits journaliers de chaque avril

     ◇ QMA_may (QMA_mai)
       Moyenne des débits journaliers de chaque mai

     ◇ QMA_jun (QMA_juin)
       Moyenne des débits journaliers de chaque juin

     ◇ QMA_jul (QMA_juil)
       Moyenne des débits journaliers de chaque juillet

     ◇ QMA_aug (QMA_aout)
       Moyenne des débits journaliers de chaque août

     ◇ QMA_sep (QMA_sept)
       Moyenne des débits journaliers de chaque septembre

     ◇ QMA_oct
       Moyenne des débits journaliers de chaque octobre

     ◇ QMA_nov
       Moyenne des débits journaliers de chaque novembre

     ◇ QMA_dec
       Moyenne des débits journaliers de chaque décembre

      phénomène ─ moyennes eaux
         saison ─ par mois
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QMA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QMA_month.yaml
  https://archive.softwareheritage.org/swh:1:cnt:12859c9e0bb9417db8645687d7489db36f1e8ff0</pre>

**Variables produced**  [`QMA_jan`](../catalogue.md#QMA_jan) · [`QMA_feb`](../catalogue.md#QMA_feb) · [`QMA_mar`](../catalogue.md#QMA_mar) · [`QMA_apr`](../catalogue.md#QMA_apr) · [`QMA_may`](../catalogue.md#QMA_may) · [`QMA_jun`](../catalogue.md#QMA_jun) · [`QMA_jul`](../catalogue.md#QMA_jul) · [`QMA_aug`](../catalogue.md#QMA_aug) · [`QMA_sep`](../catalogue.md#QMA_sep) · [`QMA_oct`](../catalogue.md#QMA_oct) · [`QMA_nov`](../catalogue.md#QMA_nov) · [`QMA_dec`](../catalogue.md#QMA_dec)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/series/QMA_month.yaml) &middot; [back to the catalogue](../catalogue.md)
