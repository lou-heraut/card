---
hide:
  - toc
---

# `delta-QMA_month_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QMA_month_H                                           12 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-QMA_jan
       Average change of average daily discharge for each January between the
       target horizon and historical period

     ◇ delta-QMA_feb
       Average change of average daily discharge for each February between the
       target horizon and historical period

     ◇ delta-QMA_mar
       Average change of average daily discharge for each March between the
       target horizon and historical period

     ◇ delta-QMA_apr
       Average change of average daily discharge for each April between the
       target horizon and historical period

     ◇ delta-QMA_may
       Average change of average daily discharge for each May between the
       target horizon and historical period

     ◇ delta-QMA_jun
       Average change of average daily discharge for each June between the
       target horizon and historical period

     ◇ delta-QMA_jul
       Average change of average daily discharge for each July between the
       target horizon and historical period

     ◇ delta-QMA_aug
       Average change of average daily discharge for each August between the
       target horizon and historical period

     ◇ delta-QMA_sep
       Average change of average daily discharge for each September between
       the target horizon and historical period

     ◇ delta-QMA_oct
       Average change of average daily discharge for each October between the
       target horizon and historical period

     ◇ delta-QMA_nov
       Average change of average daily discharge for each November between the
       target horizon and historical period

     ◇ delta-QMA_dec
       Average change of average daily discharge for each December between the
       target horizon and historical period

     phenomenon ─ mean flows
         season ─ by month
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per month of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QMA
            ╷
            ├── delta-QMA_jan = delta(QMA_jan, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_feb = delta(QMA_feb, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_mar = delta(QMA_mar, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_apr = delta(QMA_apr, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_may = delta(QMA_may, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_jun = delta(QMA_jun, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_jul = delta(QMA_jul, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_aug = delta(QMA_aug, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_sep = delta(QMA_sep, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_oct = delta(QMA_oct, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_nov = delta(QMA_nov, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-QMA_dec = delta(QMA_dec, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-QMA_jan, delta-QMA_feb, delta-QMA_mar, delta-QMA_apr,
           delta-QMA_may, delta-QMA_jun, delta-QMA_jul, delta-QMA_aug,
           delta-QMA_sep, delta-QMA_oct, delta-QMA_nov, delta-QMA_dec

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-QMA_month_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8441275c1a3a9c4e31bb8f909ce2865061b7a866</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-QMA_month_H                                           12 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-QMA_jan (delta-QMA_janv)
       Changement moyen de la moyenne des débits journaliers de chaque janvier
       entre l'horizon cible et la période historique

     ◇ delta-QMA_feb (delta-QMA_fevr)
       Changement moyen de la moyenne des débits journaliers de chaque février
       entre l'horizon cible et la période historique

     ◇ delta-QMA_mar (delta-QMA_mars)
       Changement moyen de la moyenne des débits journaliers de chaque mars
       entre l'horizon cible et la période historique

     ◇ delta-QMA_apr (delta-QMA_avril)
       Changement moyen de la moyenne des débits journaliers de chaque avril
       entre l'horizon cible et la période historique

     ◇ delta-QMA_may (delta-QMA_mai)
       Changement moyen de la moyenne des débits journaliers de chaque mai
       entre l'horizon cible et la période historique

     ◇ delta-QMA_jun (delta-QMA_juin)
       Changement moyen de la moyenne des débits journaliers de chaque juin
       entre l'horizon cible et la période historique

     ◇ delta-QMA_jul (delta-QMA_juil)
       Changement moyen de la moyenne des débits journaliers de chaque juillet
       entre l'horizon cible et la période historique

     ◇ delta-QMA_aug (delta-QMA_aout)
       Changement moyen de la moyenne des débits journaliers de chaque août
       entre l'horizon cible et la période historique

     ◇ delta-QMA_sep (delta-QMA_sept)
       Changement moyen de la moyenne des débits journaliers de chaque
       septembre entre l'horizon cible et la période historique

     ◇ delta-QMA_oct
       Changement moyen de la moyenne des débits journaliers de chaque octobre
       entre l'horizon cible et la période historique

     ◇ delta-QMA_nov
       Changement moyen de la moyenne des débits journaliers de chaque
       novembre entre l'horizon cible et la période historique

     ◇ delta-QMA_dec
       Changement moyen de la moyenne des débits journaliers de chaque
       décembre entre l'horizon cible et la période historique

      phénomène ─ moyennes eaux
         saison ─ par mois
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par mois de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QMA
            ╷
            ├── delta-QMA_jan = delta(QMA_jan, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_feb = delta(QMA_feb, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_mar = delta(QMA_mar, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_apr = delta(QMA_apr, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_may = delta(QMA_may, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_jun = delta(QMA_jun, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_jul = delta(QMA_jul, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_aug = delta(QMA_aug, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_sep = delta(QMA_sep, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_oct = delta(QMA_oct, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_nov = delta(QMA_nov, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-QMA_dec = delta(QMA_dec, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-QMA_jan, delta-QMA_feb, delta-QMA_mar, delta-QMA_apr,
           delta-QMA_may, delta-QMA_jun, delta-QMA_jul, delta-QMA_aug,
           delta-QMA_sep, delta-QMA_oct, delta-QMA_nov, delta-QMA_dec

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/delta-QMA_month_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8441275c1a3a9c4e31bb8f909ce2865061b7a866</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-QMA_jan"><code>delta-QMA_jan</code></a></dt><dd><span lang="en">Average change of average daily discharge for each January between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque janvier entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_feb"><code>delta-QMA_feb</code></a></dt><dd><span lang="en">Average change of average daily discharge for each February between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque février entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_mar"><code>delta-QMA_mar</code></a></dt><dd><span lang="en">Average change of average daily discharge for each March between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque mars entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_apr"><code>delta-QMA_apr</code></a></dt><dd><span lang="en">Average change of average daily discharge for each April between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque avril entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_may"><code>delta-QMA_may</code></a></dt><dd><span lang="en">Average change of average daily discharge for each May between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque mai entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_jun"><code>delta-QMA_jun</code></a></dt><dd><span lang="en">Average change of average daily discharge for each June between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque juin entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_jul"><code>delta-QMA_jul</code></a></dt><dd><span lang="en">Average change of average daily discharge for each July between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque juillet entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_aug"><code>delta-QMA_aug</code></a></dt><dd><span lang="en">Average change of average daily discharge for each August between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque août entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_sep"><code>delta-QMA_sep</code></a></dt><dd><span lang="en">Average change of average daily discharge for each September between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque septembre entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_oct"><code>delta-QMA_oct</code></a></dt><dd><span lang="en">Average change of average daily discharge for each October between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque octobre entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_nov"><code>delta-QMA_nov</code></a></dt><dd><span lang="en">Average change of average daily discharge for each November between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque novembre entre l'horizon cible et la période historique</span><span class="u">%</span></dd><dt><a href="../../catalogue/#delta-QMA_dec"><code>delta-QMA_dec</code></a></dt><dd><span lang="en">Average change of average daily discharge for each December between the target horizon and historical period</span><span lang="fr">Changement moyen de la moyenne des débits journaliers de chaque décembre entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/delta-QMA_month_H.yaml) &middot; [back to the catalogue](../catalogue.md)
