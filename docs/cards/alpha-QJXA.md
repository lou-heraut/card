---
hide:
  - toc
---

# `alpha-QJXA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-QJXA                                                   2 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-QJXA
       Sen's slope of the series of annual maximum daily flows (QJXA)
           unit ─ m³·s⁻¹·year⁻¹

     ◇ hyp-alpha-QJXA
       Mann-Kendall test result on the series of annual maximum daily flows
       (QJXA)
           unit ─ bool

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QJXA
            ╷
            ├── alpha-QJXA = mannkendall_slope(QJXA)
            │   │  level=0.1
            │   └─ Sen's slope of the trend
            ├── hyp-alpha-QJXA = mannkendall_test(QJXA)
            │   └─ Significance of the trend by the Mann-Kendall test at a 10
            │      % risk level
            │    ◦ No temporal aggregation
            ▼
           alpha-QJXA, hyp-alpha-QJXA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/high-flows/scalar/alpha-QJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d5b9f938eb4c362c657f5df6c938c744dc58358b</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  alpha-QJXA                                                   2 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ alpha-QJXA
       Pente de Sen de la série des débits journaliers maximaux annuels (QJXA)
          unité ─ m³·s⁻¹·an⁻¹

     ◇ hyp-alpha-QJXA
       Résultat du test de Mann-Kendall sur la série des débits journaliers
       maximaux annuels (QJXA)
          unité ─ bool

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QJXA
            ╷
            ├── alpha-QJXA = mannkendall_slope(QJXA)
            │   │  level=0.1
            │   └─ Pente de Sen de la tendance
            ├── hyp-alpha-QJXA = mannkendall_test(QJXA)
            │   └─ Significativité de la tendance par le test de Mann-Kendall
            │      au risque de 10 %
            │    ◦ Aucune agrégation temporelle
            ▼
           alpha-QJXA, hyp-alpha-QJXA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/high-flows/scalar/alpha-QJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d5b9f938eb4c362c657f5df6c938c744dc58358b</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#alpha-QJXA"><code>alpha-QJXA</code></a></dt><dd><span lang="en">Sen's slope of the series of annual maximum daily flows (QJXA)</span><span lang="fr">Pente de Sen de la série des débits journaliers maximaux annuels (QJXA)</span><span class="u">m³·s⁻¹·year⁻¹</span></dd><dt><a href="../../catalogue/#hyp-alpha-QJXA"><code>hyp-alpha-QJXA</code></a></dt><dd><span lang="en">Mann-Kendall test result on the series of annual maximum daily flows (QJXA)</span><span lang="fr">Résultat du test de Mann-Kendall sur la série des débits journaliers maximaux annuels (QJXA)</span><span class="u">bool</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/alpha-QJXA.yaml) &middot; [back to the catalogue](../catalogue.md)
