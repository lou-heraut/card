---
hide:
  - toc
---

# `QJC10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJC10    Inter-annual daily flow regime over the whole record smoothed  │
  │                                                            over 10 days  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Mean flow of each day of the year over the whole record, then 10-day
     centered moving average (365 values)

     phenomenon ─ mean flows
         season ─ record
           form ─ curve
           unit ─ m³·s⁻¹
         inputs ─ Q [m³·s⁻¹], period_start, period_end (optional)

            ╷
            ├── nanmean(Q)
            │   │  restricted to the requested period
            │   │  from date, period_start, period_end
            │   └─ Mean
            │    ◦ One value per day of year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QJ
            ╷
            ├── rollmean_center(QJ)
            │   │  cyclical=True
            │   └─ 10-day centered moving average
            │    ◦ No temporal aggregation
            ▼
           QJC10

  ──────────────────────────────────────────────────────────────────────────
  v2.1   flow/mean-flows/curve/QJC10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b4cc3a4551dd530d5ab11a68b854d008b1dccef6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJC10    Régime journalier inter-annuel sur la chronique entière lissé  │
  │                                                            sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Moyenne des débits de chaque jour de l'année sur la chronique entière,
     puis moyenne mobile centrée sur 10 jours (365 valeurs)

      phénomène ─ moyennes eaux
         saison ─ chronique
          forme ─ courbe
          unité ─ m³·s⁻¹
        entrées ─ Q [m³·s⁻¹], period_start, period_end (facultatifs)

            ╷
            ├── nanmean(Q)
            │   │  restreint à la période demandée
            │   │  d'après date, period_start, period_end
            │   └─ Moyenne
            │    ◦ Une valeur par jour de l'année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QJ
            ╷
            ├── rollmean_center(QJ)
            │   │  cyclical=True
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Aucune agrégation temporelle
            ▼
           QJC10

  ──────────────────────────────────────────────────────────────────────────
  v2.1   flow/mean-flows/curve/QJC10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b4cc3a4551dd530d5ab11a68b854d008b1dccef6</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QJC10"><code>QJC10</code></a></dt><dd><span lang="en">Inter-annual daily flow regime over the whole record smoothed over 10 days</span><span lang="fr">Régime journalier inter-annuel sur la chronique entière lissé sur 10 jours</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/QJC10.yaml) &middot; [back to the catalogue](../catalogue.md)
