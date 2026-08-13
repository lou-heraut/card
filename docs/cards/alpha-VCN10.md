---
hide:
  - toc
---

# `alpha-VCN10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-VCN10                                                  2 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-VCN10
       Sen's slope of the series of annual minima of 10-day mean flows (VCN10)
           unit ─ m³·s⁻¹·year⁻¹

     ◇ hyp-alpha-VCN10
       Mann-Kendall test result on the series of annual minima of 10-day mean
       flows (VCN10)
           unit ─ bool

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN10
            ╷
            ├── alpha-VCN10 = mannkendall_slope(VCN10)
            │   │  level=0.1
            │   └─ Sen's slope of the trend
            ├── hyp-alpha-VCN10 = mannkendall_test(VCN10)
            │   └─ Significance of the trend by the Mann-Kendall test at a 10
            │      % risk level
            │    ◦ No temporal aggregation
            ▼
           alpha-VCN10, hyp-alpha-VCN10

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/alpha-VCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:ed3525a9f7f4d3641b4094e0384087cd612b863b</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-VCN10                                                  2 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-VCN10
       Pente de Sen de la série des minimums annuels des débits moyens sur 10
       jours (VCN10)
          unité ─ m³·s⁻¹·an⁻¹

     ◇ hyp-alpha-VCN10
       Résultat du test de Mann-Kendall sur la série des minimums annuels des
       débits moyens sur 10 jours (VCN10)
          unité ─ bool

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN10
            ╷
            ├── alpha-VCN10 = mannkendall_slope(VCN10)
            │   │  level=0.1
            │   └─ Pente de Sen de la tendance
            ├── hyp-alpha-VCN10 = mannkendall_test(VCN10)
            │   └─ Significativité de la tendance par le test de Mann-Kendall
            │      au risque de 10 %
            │    ◦ Aucune agrégation temporelle
            ▼
           alpha-VCN10, hyp-alpha-VCN10

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/alpha-VCN10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:ed3525a9f7f4d3641b4094e0384087cd612b863b</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#alpha-VCN10"><code>alpha-VCN10</code></a></dt><dd><span lang="en">Sen's slope of the series of annual minima of 10-day mean flows (VCN10)</span><span lang="fr">Pente de Sen de la série des minimums annuels des débits moyens sur 10 jours (VCN10)</span><span class="u">m³·s⁻¹·year⁻¹</span></dd><dt><a href="../../catalogue/#hyp-alpha-VCN10"><code>hyp-alpha-VCN10</code></a></dt><dd><span lang="en">Mann-Kendall test result on the series of annual minima of 10-day mean flows (VCN10)</span><span lang="fr">Résultat du test de Mann-Kendall sur la série des minimums annuels des débits moyens sur 10 jours (VCN10)</span><span class="u">bool</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/alpha-VCN10.yaml) &middot; [back to the catalogue](../catalogue.md)
