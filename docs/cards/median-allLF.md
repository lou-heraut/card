---
hide:
  - toc
---

# `median-allLF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-allLF                                                 5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ median-startLF
       Inter-annual median of the start of low flows
       Median of the dates of the first 10-day mean flow value below the
       threshold set at the maximum of VCN10
           unit ─ yearday

     ◇ median-centerLF
       Inter-annual median of the center of low flows
       Median of the dates of the minimal 10-day mean flow value below the
       threshold set at the maximum of VCN10
           unit ─ yearday

     ◇ median-endLF
       Inter-annual median of the end of low flows
       Median of the dates of the last 10-day mean flow value below the
       threshold set at the maximum of VCN10
           unit ─ yearday

     ◇ median-dtLF
       Inter-annual median of the duration of low flows
       Median of the durations of the longest continuous sequence with 10-day
       mean flows below the threshold set at the maximum of VCN10
           unit ─ day

     ◇ median-vLF
       Inter-annual median of the deficit volume of low flows
       Median of the sums of the differences between the 10-day mean and the
       maximum of VCN10, over the longest sequence below this threshold
           unit ─ hm³

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
          input ─ Q [m³·s⁻¹]

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
            ├── median-startLF = circular_median(startLF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            ├── median-centerLF = circular_median(centerLF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            ├── median-endLF = circular_median(endLF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            ├── median-dtLF = nanmedian(dtLF)
            │   └─ Inter-annual median
            ├── median-vLF = nanmedian(vLF)
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-startLF, median-centerLF, median-endLF, median-dtLF,
           median-vLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-allLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bfe14e4a3517ae1eaac388b1af2e330538deb1b6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-allLF                                                 5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ median-startLF (mediane-debutBE)
       Médiane inter-annuelle du début des basses eaux
       Médiane des dates de la première valeur de débits moyens sur 10 jours
       sous le seuil fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ median-centerLF (mediane-centreBE)
       Médiane inter-annuelle du centre des basses eaux
       Médiane des dates de la valeur minimale des débits moyens sur 10 jours
       sous le seuil fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ median-endLF (mediane-finBE)
       Médiane inter-annuelle de la fin des basses eaux
       Médiane des dates de la dernière valeur de débits moyens sur 10 jours
       sous le seuil fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ median-dtLF (mediane-dtBE)
       Médiane inter-annuelle de la durée des basses eaux
       Médiane des durées de la plus longue séquence continue avec des débits
       moyens sur 10 jours sous le seuil fixé au maximum des VCN10
          unité ─ jour

     ◇ median-vLF (mediane-vBE)
       Médiane inter-annuelle des volumes de déficit des basses eaux
       Médiane des sommes des écarts entre la moyenne sur 10 jours et le
       maximum des VCN10, sur la séquence la plus longue sous ce seuil
          unité ─ hm³

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
         entrée ─ Q [m³·s⁻¹]

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
            ├── median-startLF = circular_median(startLF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            ├── median-centerLF = circular_median(centerLF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            ├── median-endLF = circular_median(endLF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            ├── median-dtLF = nanmedian(dtLF)
            │   └─ Médiane inter-annuelle
            ├── median-vLF = nanmedian(vLF)
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-startLF, median-centerLF, median-endLF, median-dtLF,
           median-vLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-allLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:bfe14e4a3517ae1eaac388b1af2e330538deb1b6</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-startLF"><code>median-startLF</code></a></dt><dd><span lang="en">Inter-annual median of the start of low flows</span><span lang="fr">Médiane inter-annuelle du début des basses eaux</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#median-centerLF"><code>median-centerLF</code></a></dt><dd><span lang="en">Inter-annual median of the center of low flows</span><span lang="fr">Médiane inter-annuelle du centre des basses eaux</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#median-endLF"><code>median-endLF</code></a></dt><dd><span lang="en">Inter-annual median of the end of low flows</span><span lang="fr">Médiane inter-annuelle de la fin des basses eaux</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#median-dtLF"><code>median-dtLF</code></a></dt><dd><span lang="en">Inter-annual median of the duration of low flows</span><span lang="fr">Médiane inter-annuelle de la durée des basses eaux</span><span class="u">day</span></dd><dt><a href="../../catalogue/#median-vLF"><code>median-vLF</code></a></dt><dd><span lang="en">Inter-annual median of the deficit volume of low flows</span><span lang="fr">Médiane inter-annuelle des volumes de déficit des basses eaux</span><span class="u">hm³</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/median-allLF.yaml) &middot; [back to the catalogue](../catalogue.md)
