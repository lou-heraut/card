---
hide:
  - toc
---

# `delta-allLF_summer_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-allLF_summer_H                                         5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-startLF_summer
       Average change of the start of summer low flows between the target
       horizon and historical period
       In summer, date of the first 10-day mean flow value below the threshold
       set at the maximum of VCN10 (May to November)
           unit ─ day

     ◇ delta-centerLF_summer
       Average change of the center of summer low flows between the target
       horizon and historical period
       In summer, date of the minimal 10-day mean flow value below the
       threshold set at the maximum of VCN10 (May to November)
           unit ─ day

     ◇ delta-endLF_summer
       Average change of the end of summer low flows between the target
       horizon and historical period
       In summer, date of the last 10-day mean flow value below the threshold
       set at the maximum of VCN10 (May to November)
           unit ─ day

     ◇ delta-dtLF_summer
       Average change of duration of summer low flows between the target
       horizon and historical period
       In summer, duration of the longest continuous sequence with 10-day mean
       flows below the threshold set at the maximum of VCN10 (May to November)
           unit ─ day

     ◇ delta-vLF_summer
       Average change of the deficit volume of summer low flows between the
       target horizon and historical period
       In summer, sum of the differences between the 10-day mean and the
       maximum of VCN10, over the longest sequence below this threshold (May
       to November)
           unit ─ %

     phenomenon ─ low flows
         season ─ summer
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
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           VCN10_summer
            ╷
            ├── nanmax(VCN10_summer)
            │   └─ Maximum of VCN10_summer, taken as the threshold
            │    ◦ A single value, repeated over the whole record
            ▼
           upLim
            ╷
            ├── startLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, first day
            │   └─ Date of the first day of the longest period below upLim
            ├── centerLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, day of the minimum
            │   └─ Date of the minimum of VC10 over the longest period below
            │      upLim
            ├── endLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, last day
            │   └─ Date of the last day of the longest period below upLim
            ├── dtLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, duration
            │   └─ Number of days in the longest period below upLim
            ├── vLF_summer = deficit_volume(VC10)
            │   │  below upLim
            │   └─ Sum of volumes discharged each day in the longest period
            │      below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           startLF_summer, centerLF_summer, endLF_summer, dtLF_summer,
           vLF_summer
            ╷
            ├── delta-startLF_summer = delta(startLF_summer, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-centerLF_summer = delta(centerLF_summer, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-endLF_summer = delta(endLF_summer, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-dtLF_summer = delta(dtLF_summer, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            ├── delta-vLF_summer = delta(vLF_summer, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-startLF_summer, delta-centerLF_summer, delta-endLF_summer,
           delta-dtLF_summer, delta-vLF_summer

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/low-flows/scalar/delta-allLF_summer_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:75bc82053f0b9b492005bddbcce24541d5305074</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-allLF_summer_H                                         5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ delta-startLF_summer (delta-debutBE_été)
       Changement moyen du début des basses eaux estivales entre l'horizon
       cible et la période historique
       En été, date de la première valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour

     ◇ delta-centerLF_summer (delta-centreBE_été)
       Changement moyen du centre des basses eaux estivales entre l'horizon
       cible et la période historique
       En été, date de la valeur minimale des débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour

     ◇ delta-endLF_summer (delta-finBE_été)
       Changement moyen de la fin des basses eaux estivales entre l'horizon
       cible et la période historique
       En été, date de la dernière valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour

     ◇ delta-dtLF_summer (delta-dtBE_été)
       Changement moyen de la durée des basses eaux estivales entre l'horizon
       cible et la période historique
       En été, durée de la plus longue séquence continue avec des débits
       moyens sur 10 jours sous le seuil fixé au maximum des VCN10 (mois de
       mai à novembre)
          unité ─ jour

     ◇ delta-vLF_summer (delta-vBE_été)
       Changement moyen du volume de déficit des basses eaux estivales entre
       l'horizon cible et la période historique
       En été, somme des écarts entre la moyenne sur 10 jours et le maximum
       des VCN10, sur la séquence la plus longue sous ce seuil (mois de mai à
       novembre)
          unité ─ %

      phénomène ─ basses eaux
         saison ─ estivale
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
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           VCN10_summer
            ╷
            ├── nanmax(VCN10_summer)
            │   └─ Maximum de VCN10_summer, pris comme seuil
            │    ◦ Une seule valeur, répétée sur toute la chronique
            ▼
           upLim
            ╷
            ├── startLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, premier jour
            │   └─ Date du premier jour de la plus longue période sous upLim
            ├── centerLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, jour du minimum
            │   └─ Date du minimum de VC10 sur la plus longue période sous
            │      upLim
            ├── endLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, dernier jour
            │   └─ Date du dernier jour de la plus longue période sous upLim
            ├── dtLF_summer = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, durée
            │   └─ Nombre de jours de la plus longue période sous upLim
            ├── vLF_summer = deficit_volume(VC10)
            │   │  sous upLim
            │   └─ Somme des volumes écoulés chaque jour de la plus longue
            │      période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           startLF_summer, centerLF_summer, endLF_summer, dtLF_summer,
           vLF_summer
            ╷
            ├── delta-startLF_summer = delta(startLF_summer, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-centerLF_summer = delta(centerLF_summer, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-endLF_summer = delta(endLF_summer, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-dtLF_summer = delta(dtLF_summer, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            ├── delta-vLF_summer = delta(vLF_summer, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-startLF_summer, delta-centerLF_summer, delta-endLF_summer,
           delta-dtLF_summer, delta-vLF_summer

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/low-flows/scalar/delta-allLF_summer_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:75bc82053f0b9b492005bddbcce24541d5305074</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-startLF_summer"><code>delta-startLF_summer</code></a></dt><dd><span lang="en">Average change of the start of summer low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du début des basses eaux estivales entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-centerLF_summer"><code>delta-centerLF_summer</code></a></dt><dd><span lang="en">Average change of the center of summer low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du centre des basses eaux estivales entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-endLF_summer"><code>delta-endLF_summer</code></a></dt><dd><span lang="en">Average change of the end of summer low flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la fin des basses eaux estivales entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-dtLF_summer"><code>delta-dtLF_summer</code></a></dt><dd><span lang="en">Average change of duration of summer low flows between the target horizon and historical period</span><span lang="fr">Changement moyen de la durée des basses eaux estivales entre l'horizon cible et la période historique</span><span class="u">day</span></dd><dt><a href="../../catalogue/#delta-vLF_summer"><code>delta-vLF_summer</code></a></dt><dd><span lang="en">Average change of the deficit volume of summer low flows between the target horizon and historical period</span><span lang="fr">Changement moyen du volume de déficit des basses eaux estivales entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-allLF_summer_H.yaml) &middot; [back to the catalogue](../catalogue.md)
