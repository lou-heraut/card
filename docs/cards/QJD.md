---
hide:
  - toc
---

# `QJD`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJD        Inter-annual median daily flow regime over the whole record  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median flow of each calendar day over all the years of the period: the
     365 values describe the median hydrological regime

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

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/mean-flows/curve/QJD.yaml
  https://archive.softwareheritage.org/swh:1:cnt:aecddf9fb4547681af10a0bc43393e41dad55966</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJD     Régime journalier médian inter-annuel sur la chronique entière  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit médian de chaque jour calendaire sur toutes les années de la
     période : les 365 valeurs décrivent le régime hydrologique médian

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

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/mean-flows/curve/QJD.yaml
  https://archive.softwareheritage.org/swh:1:cnt:aecddf9fb4547681af10a0bc43393e41dad55966</pre>

**Variables produced**  [`QJD`](../catalogue.md#QJD)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/QJD.yaml) &middot; [back to the catalogue](../catalogue.md)
