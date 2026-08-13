---
hide:
  - toc
---

# `alpha-QA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-QA                                                     2 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-QA
       Sen's slope of the series of annual mean daily flows
           unit ─ m³·s⁻¹·year⁻¹

     ◇ hyp-alpha-QA
       Mann-Kendall test result on the series of annual mean daily flows
           unit ─ bool

     phenomenon ─ mean flows
         season ─ annual
           form ─ scalar
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           QA
            ╷
            ├── alpha-QA = mannkendall_slope(QA)
            │   │  level=0.1
            │   └─ Sen's slope of the trend
            ├── hyp-alpha-QA = mannkendall_test(QA)
            │   └─ Significance of the trend by the Mann-Kendall test at a 10
            │      % risk level
            │    ◦ No temporal aggregation
            ▼
           alpha-QA, hyp-alpha-QA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/scalar/alpha-QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0afa3d8a973f0636126f6aa5dab83e1052f9b952</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-QA                                                     2 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-QA
       Pente de Sen de la série des débits moyens annuels
          unité ─ m³·s⁻¹·an⁻¹

     ◇ hyp-alpha-QA
       Résultat du test de Mann-Kendall sur la série des débits moyens annuels
          unité ─ bool

      phénomène ─ moyennes eaux
         saison ─ annuelle
          forme ─ scalaire
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           QA
            ╷
            ├── alpha-QA = mannkendall_slope(QA)
            │   │  level=0.1
            │   └─ Pente de Sen de la tendance
            ├── hyp-alpha-QA = mannkendall_test(QA)
            │   └─ Significativité de la tendance par le test de Mann-Kendall
            │      au risque de 10 %
            │    ◦ Aucune agrégation temporelle
            ▼
           alpha-QA, hyp-alpha-QA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/scalar/alpha-QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0afa3d8a973f0636126f6aa5dab83e1052f9b952</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#alpha-QA"><code>alpha-QA</code></a></dt><dd><span lang="en">Sen's slope of the series of annual mean daily flows</span><span lang="fr">Pente de Sen de la série des débits moyens annuels</span><span class="u">m³·s⁻¹·year⁻¹</span></dd><dt><a href="../../catalogue/#hyp-alpha-QA"><code>hyp-alpha-QA</code></a></dt><dd><span lang="en">Mann-Kendall test result on the series of annual mean daily flows</span><span lang="fr">Résultat du test de Mann-Kendall sur la série des débits moyens annuels</span><span class="u">bool</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/alpha-QA.yaml) &middot; [back to the catalogue](../catalogue.md)
