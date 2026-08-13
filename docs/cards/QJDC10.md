---
hide:
  - toc
---

# `QJDC10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJDC10     Inter-annual median daily flow regime over the whole record  │
  │                                                   smoothed over 10 days  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median flow of each day of the year over the whole record, then 10-day
     centered moving average (365 values)

     phenomenon ─ mean flows
         season ─ record
           form ─ curve
           unit ─ m³·s⁻¹
         inputs ─ Q [m³·s⁻¹], period_start, period_end (optional)

            ╷
            ├── nanmedian(Q)
            │   │  restricted to the requested period
            │   │  from date, period_start, period_end
            │   └─ Median
            │    ◦ One value per day of year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QJD
            ╷
            ├── rollmean_center(QJD)
            │   │  cyclical=True
            │   └─ 10-day centered moving average
            │    ◦ No temporal aggregation
            ▼
           QJDC10

  ──────────────────────────────────────────────────────────────────────────
  v4.0   flow/mean-flows/curve/QJDC10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f271232a68abeed3324af077a5ea9cc83f5dc509</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJDC10          Régime journalier médian inter-annuel sur la chronique  │
  │                                              entière lissé sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des débits de chaque jour de l'année sur la chronique entière,
     puis moyenne mobile centrée sur 10 jours (365 valeurs)

      phénomène ─ moyennes eaux
         saison ─ chronique
          forme ─ courbe
          unité ─ m³·s⁻¹
        entrées ─ Q [m³·s⁻¹], period_start, period_end (facultatifs)

            ╷
            ├── nanmedian(Q)
            │   │  restreint à la période demandée
            │   │  d'après date, period_start, period_end
            │   └─ Médiane
            │    ◦ Une valeur par jour de l'année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QJD
            ╷
            ├── rollmean_center(QJD)
            │   │  cyclical=True
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Aucune agrégation temporelle
            ▼
           QJDC10

  ──────────────────────────────────────────────────────────────────────────
  v4.0   flow/mean-flows/curve/QJDC10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f271232a68abeed3324af077a5ea9cc83f5dc509</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QJDC10"><code>QJDC10</code></a></dt><dd><span lang="en">Inter-annual median daily flow regime over the whole record smoothed over 10 days</span><span lang="fr">Régime journalier médian inter-annuel sur la chronique entière lissé sur 10 jours</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/QJDC10.yaml) &middot; [back to the catalogue](../catalogue.md)
