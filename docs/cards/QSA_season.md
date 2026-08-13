---
hide:
  - toc
---

# `QSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QSA_season                                                   4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QSA_DJF
       Average daily flows for each winter
       Months of December, January, and February

     ◇ QSA_MAM
       Average daily flows for each spring
       Months of March, April, and May

     ◇ QSA_JJA
       Average daily flows for each summer
       Months of June, July, and August

     ◇ QSA_SON
       Average daily flows for each autumn
       Months of September, October, and November

     phenomenon ─ mean flows
         season ─ by season
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7a4abefd9fefd8ec3517dd50fd2b97893da7c289</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QSA_season                                                   4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ QSA_DJF
       Moyenne des débits journaliers de chaque hiver
       Mois de décembre, janvier et février

     ◇ QSA_MAM
       Moyenne des débits journaliers de chaque printemps
       Mois de mars, avril et mai

     ◇ QSA_JJA
       Moyenne des débits journaliers de chaque été
       Mois de juin, juillet et août

     ◇ QSA_SON
       Moyenne des débits journaliers de chaque automne
       Mois de septembre, octobre et novembre

      phénomène ─ moyennes eaux
         saison ─ par saison
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QSA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7a4abefd9fefd8ec3517dd50fd2b97893da7c289</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QSA_DJF"><code>QSA_DJF</code></a></dt><dd><span lang="en">Average daily flows for each winter</span><span lang="fr">Moyenne des débits journaliers de chaque hiver</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QSA_MAM"><code>QSA_MAM</code></a></dt><dd><span lang="en">Average daily flows for each spring</span><span lang="fr">Moyenne des débits journaliers de chaque printemps</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QSA_JJA"><code>QSA_JJA</code></a></dt><dd><span lang="en">Average daily flows for each summer</span><span lang="fr">Moyenne des débits journaliers de chaque été</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#QSA_SON"><code>QSA_SON</code></a></dt><dd><span lang="en">Average daily flows for each autumn</span><span lang="fr">Moyenne des débits journaliers de chaque automne</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/series/QSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
