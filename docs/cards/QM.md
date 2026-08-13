---
hide:
  - toc
---

# `QM`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QM                        Mean monthly discharge over the whole record  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Mean flow of each calendar month over all the years of the period

     phenomenon ─ mean flows
         season ─ by month
           form ─ curve
           unit ─ m³·s⁻¹
         inputs ─ Q [m³·s⁻¹], period_start, period_end (optional)

            ╷
            ├── nanmean(Q)
            │   │  restricted to the requested period
            │   │  from date, period_start, period_end
            │   └─ Mean
            │    ◦ One value per month
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QM

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/mean-flows/curve/QM.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d1199d5f904228ff997cb18448b09d24d52bbdf</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QM                        Débit moyen mensuel sur la chronique entière  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit moyen de chaque mois calendaire sur toutes les années de la période

      phénomène ─ moyennes eaux
         saison ─ par mois
          forme ─ courbe
          unité ─ m³·s⁻¹
        entrées ─ Q [m³·s⁻¹], period_start, period_end (facultatifs)

            ╷
            ├── nanmean(Q)
            │   │  restreint à la période demandée
            │   │  d'après date, period_start, period_end
            │   └─ Moyenne
            │    ◦ Une valeur par mois
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QM

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/mean-flows/curve/QM.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5d1199d5f904228ff997cb18448b09d24d52bbdf</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QM"><code>QM</code></a></dt><dd><span lang="en">Mean monthly discharge over the whole record</span><span lang="fr">Débit moyen mensuel sur la chronique entière</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/QM.yaml) &middot; [back to the catalogue](../catalogue.md)
