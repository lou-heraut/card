---
hide:
  - toc
---

# `delta-allLF_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-allLF_H                                                5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-startLF
       Average change of the start of low flows between the target horizon and
       historical period
       Date of the first 10-day mean flow value below the threshold set at the
       maximum of VCN10
           unit ─ day

     ◇ delta-centerLF
       Average change of the center of low flows between the target horizon
       and historical period
       Date of the minimal 10-day mean flow value below the threshold set at
       the maximum of VCN10
           unit ─ day

     ◇ delta-endLF
       Average change of the end of low flows between the target horizon and
       historical period
       Date of the last 10-day mean flow value below the threshold set at the
       maximum of VCN10
           unit ─ day

     ◇ delta-dtLF
       Average change of duration of low flows between the target horizon and
       historical period
       Duration of the longest continuous sequence with 10-day mean flows
       below the threshold set at the maximum of VCN10
           unit ─ day

     ◇ delta-vLF
       Average change of the deficit volume of low flows between the target
       horizon and historical period
       Sum of the differences between the 10-day mean and the maximum of
       VCN10, over the longest sequence below this threshold
           unit ─ %

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum of VC10
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN10
            ╷
            ├── nanmax(VCN10)
            │   └─ Maximum of VCN10, taken as the threshold
            │    ◦ A single value, repeated over the whole record
            ▼
           upLim
            ╷
            ├── startLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, first day
            │   └─ Date of the first day of the longest period below upLim
            ├── centerLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, day of the minimum
            │   └─ Date of the minimum of VC10 over the longest period below
            │      upLim
            ├── endLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, last day
            │   └─ Date of the last day of the longest period below upLim
            ├── dtLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, duration
            │   └─ Number of days in the longest period below upLim
            ├── vLF = deficit_volume(VC10)
            │   │  below upLim
            │   └─ Sum of volumes discharged each day in the longest period
            │      below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           startLF, centerLF, endLF, dtLF, vLF
            ╷
            ├── delta-startLF = delta(startLF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-centerLF = delta(centerLF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-endLF = delta(endLF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-dtLF = delta(dtLF, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-vLF = delta(vLF, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-startLF, delta-centerLF, delta-endLF, delta-dtLF, delta-vLF

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/low-flows/scalar/delta-allLF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c3e0f9caf7fc63abbc615eca893fec9dfb9e5ea7</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-allLF_H                                                5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-startLF (delta-debutBE)
       Changement moyen du début des basses eaux entre l'horizon cible et la
       période historique
       Date de la première valeur de débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour

     ◇ delta-centerLF (delta-centreBE)
       Changement moyen du centre des basses eaux entre l'horizon cible et la
       période historique
       Date de la valeur minimale des débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour

     ◇ delta-endLF (delta-finBE)
       Changement moyen de la fin des basses eaux entre l'horizon cible et la
       période historique
       Date de la dernière valeur de débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour

     ◇ delta-dtLF (delta-dtBE)
       Changement moyen de la durée des basses eaux entre l'horizon cible et
       la période historique
       Durée de la plus longue séquence continue avec des débits moyens sur 10
       jours sous le seuil fixé au maximum des VCN10
          unité ─ jour

     ◇ delta-vLF (delta-vBE)
       Changement moyen du volume de déficit des basses eaux entre l'horizon
       cible et la période historique
       Somme des écarts entre la moyenne sur 10 jours et le maximum des VCN10,
       sur la séquence la plus longue sous ce seuil
          unité ─ %

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum de VC10
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN10
            ╷
            ├── nanmax(VCN10)
            │   └─ Maximum de VCN10, pris comme seuil
            │    ◦ Une seule valeur, répétée sur toute la chronique
            ▼
           upLim
            ╷
            ├── startLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, premier jour
            │   └─ Date du premier jour de la plus longue période sous upLim
            ├── centerLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, jour du minimum
            │   └─ Date du minimum de VC10 sur la plus longue période sous
            │      upLim
            ├── endLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, dernier jour
            │   └─ Date du dernier jour de la plus longue période sous upLim
            ├── dtLF = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, durée
            │   └─ Nombre de jours de la plus longue période sous upLim
            ├── vLF = deficit_volume(VC10)
            │   │  sous upLim
            │   └─ Somme des volumes écoulés chaque jour de la plus longue
            │      période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           startLF, centerLF, endLF, dtLF, vLF
            ╷
            ├── delta-startLF = delta(startLF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-centerLF = delta(centerLF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-endLF = delta(endLF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-dtLF = delta(dtLF, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-vLF = delta(vLF, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-startLF, delta-centerLF, delta-endLF, delta-dtLF, delta-vLF

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/low-flows/scalar/delta-allLF_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c3e0f9caf7fc63abbc615eca893fec9dfb9e5ea7</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-startLF"><code>delta-startLF</code></a></dt><dd><span lang="en">Average change of the start of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du début des basses eaux entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-centerLF"><code>delta-centerLF</code></a></dt><dd><span lang="en">Average change of the center of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du centre des basses eaux entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-endLF"><code>delta-endLF</code></a></dt><dd><span lang="en">Average change of the end of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la fin des basses eaux entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-dtLF"><code>delta-dtLF</code></a></dt><dd><span lang="en">Average change of duration of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la durée des basses eaux entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-vLF"><code>delta-vLF</code></a></dt><dd><span lang="en">Average change of the deficit volume of low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du volume de déficit des basses eaux entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-allLF_H.yaml) &middot; [back to the catalogue](../catalogue.md)
