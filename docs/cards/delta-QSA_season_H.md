---
hide:
  - toc
---

# `delta-QSA_season_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QSA_season_H                                           4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-QSA_DJF
       Average change of average daily flows for each winter between the
       target horizon and historical period
       Months of December, January, and February

     ◇ delta-QSA_MAM
       Average change of average daily flows for each spring between the
       target horizon and historical period
       Months of March, April, and May

     ◇ delta-QSA_JJA
       Average change of average daily flows for each summer between the
       target horizon and historical period
       Months of June, July, and August

     ◇ delta-QSA_SON
       Average change of average daily flows for each autumn between the
       target horizon and historical period
       Months of September, October, and November

     phenomenon ─ mean flows
         season ─ by season
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QSA
            ╷
            ├── delta-QSA_DJF = delta(QSA_DJF, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QSA_MAM = delta(QSA_MAM, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QSA_JJA = delta(QSA_JJA, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QSA_SON = delta(QSA_SON, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-QSA_DJF, delta-QSA_MAM, delta-QSA_JJA, delta-QSA_SON

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-QSA_season_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:16343d715b7fed52531da7fd8257ffbab5833f1f</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QSA_season_H                                           4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-QSA_DJF
       Changement moyen de la moyenne des débits journaliers de chaque hiver
       entre l'horizon cible et la période historique
       Mois de décembre, janvier et février

     ◇ delta-QSA_MAM
       Changement moyen de la moyenne des débits journaliers de chaque
       printemps entre l'horizon cible et la période historique
       Mois de mars, avril et mai

     ◇ delta-QSA_JJA
       Changement moyen de la moyenne des débits journaliers de chaque été
       entre l'horizon cible et la période historique
       Mois de juin, juillet et août

     ◇ delta-QSA_SON
       Changement moyen de la moyenne des débits journaliers de chaque automne
       entre l'horizon cible et la période historique
       Mois de septembre, octobre et novembre

      phénomène ─ moyennes eaux
         saison ─ par saison
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QSA
            ╷
            ├── delta-QSA_DJF = delta(QSA_DJF, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QSA_MAM = delta(QSA_MAM, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QSA_JJA = delta(QSA_JJA, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QSA_SON = delta(QSA_SON, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-QSA_DJF, delta-QSA_MAM, delta-QSA_JJA, delta-QSA_SON

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-QSA_season_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:16343d715b7fed52531da7fd8257ffbab5833f1f</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-QSA_DJF"><code>delta-QSA_DJF</code></a></dt><dd><span lang="en">Average change of average daily flows for each winter between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque hiver entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QSA_MAM"><code>delta-QSA_MAM</code></a></dt><dd><span lang="en">Average change of average daily flows for each spring between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque printemps entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QSA_JJA"><code>delta-QSA_JJA</code></a></dt><dd><span lang="en">Average change of average daily flows for each summer between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque été entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QSA_SON"><code>delta-QSA_SON</code></a></dt><dd><span lang="en">Average change of average daily flows for each autumn between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque automne entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/delta-QSA_season_H.yaml) &middot; [back to the catalogue](../catalogue.md)
