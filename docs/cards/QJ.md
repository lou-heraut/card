---
hide:
  - toc
---

# `QJ`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJ                Inter-annual daily flow regime over the whole record  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Mean flow of each calendar day over all the years of the period: the 365
     values describe the mean hydrological regime

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

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/curve/QJ.yaml
  https://archive.softwareheritage.org/swh:1:cnt:96ddffbb0d485b45659f2f1fabbf221bf65b5772</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJ             Régime journalier inter-annuel sur la chronique entière  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit moyen de chaque jour calendaire sur toutes les années de la période
     : les 365 valeurs décrivent le régime hydrologique moyen

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

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/curve/QJ.yaml
  https://archive.softwareheritage.org/swh:1:cnt:96ddffbb0d485b45659f2f1fabbf221bf65b5772</pre>

**Variables produced**  [`QJ`](../catalogue.md#QJ)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/QJ.yaml) &middot; [back to the catalogue](../catalogue.md)
