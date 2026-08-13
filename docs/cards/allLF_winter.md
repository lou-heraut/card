---
hide:
  - toc
---

# `allLF_winter`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF_winter                                                 5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF_winter
       Start of winter low flows
       In winter, date of the first 10-day mean flow value below the threshold
       set at the maximum of VCN10 (November to April)
           unit ─ yearday

     ◇ centerLF_winter
       Center of winter low flows
       In winter, date of the minimal 10-day mean flow value below the
       threshold set at the maximum of VCN10 (November to April)
           unit ─ yearday

     ◇ endLF_winter
       End of winter low flows
       In winter, date of the last 10-day mean flow value below the threshold
       set at the maximum of VCN10 (November to April)
           unit ─ yearday

     ◇ dtLF_winter
       Duration of winter low flows
       In winter, duration of the longest continuous sequence with 10-day mean
       flows below the threshold set at the maximum of VCN10 (November to
       April)
           unit ─ day

     ◇ vLF_winter
       Deficit volume of winter low flows
       In winter, sum of the differences between the 10-day mean and the
       maximum of VCN10, over the longest sequence below this threshold
       (November to April)
           unit ─ hm³

     phenomenon ─ low flows
         season ─ winter
           form ─ series
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
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           VCN10_winter
            ╷
            ├── nanmax(VCN10_winter)
            │   └─ Maximum of VCN10_winter, taken as the threshold
            │    ◦ A single value, repeated over the whole record
            ▼
           upLim
            ╷
            ├── startLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, first day
            │   └─ Date of the first day of the longest period below upLim
            ├── centerLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, day of the minimum
            │   └─ Date of the minimum of VC10 over the longest period below
            │      upLim
            ├── endLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, last day
            │   └─ Date of the last day of the longest period below upLim
            ├── dtLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, duration
            │   └─ Number of days in the longest period below upLim
            ├── vLF_winter = deficit_volume(VC10)
            │   │  below upLim
            │   └─ Sum of volumes discharged each day in the longest period
            │      below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           startLF_winter, centerLF_winter, endLF_winter, dtLF_winter,
           vLF_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/series/allLF_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:29553c2a77d73b5bcc59eb2ea4c20ca3e0584786</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF_winter                                                 5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF_winter (debutBE_hiver)
       Début des basses eaux hivernales
       En hiver, date de la première valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de novembre à avril)
          unité ─ jour de l'année

     ◇ centerLF_winter (centreBE_hiver)
       Centre des basses eaux hivernales
       En hiver, date de la valeur minimale des débits moyens sur 10 jours
       sous le seuil fixé au maximum des VCN10 (mois de novembre à avril)
          unité ─ jour de l'année

     ◇ endLF_winter (finBE_hiver)
       Fin des basses eaux hivernales
       En hiver, date de la dernière valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de novembre à avril)
          unité ─ jour de l'année

     ◇ dtLF_winter (dtBE_hiver)
       Durée des basses eaux hivernales
       En hiver, durée de la plus longue séquence continue avec des débits
       moyens sur 10 jours sous le seuil fixé au maximum des VCN10 (mois de
       novembre à avril)
          unité ─ jour

     ◇ vLF_winter (vBE_hiver)
       Volume de déficit des basses eaux hivernales
       En hiver, somme des écarts entre la moyenne sur 10 jours et le maximum
       des VCN10, sur la séquence la plus longue sous ce seuil (mois de
       novembre à avril)
          unité ─ hm³

      phénomène ─ basses eaux
         saison ─ hivernale
          forme ─ série
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
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           VCN10_winter
            ╷
            ├── nanmax(VCN10_winter)
            │   └─ Maximum de VCN10_winter, pris comme seuil
            │    ◦ Une seule valeur, répétée sur toute la chronique
            ▼
           upLim
            ╷
            ├── startLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, premier jour
            │   └─ Date du premier jour de la plus longue période sous upLim
            ├── centerLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, jour du minimum
            │   └─ Date du minimum de VC10 sur la plus longue période sous
            │      upLim
            ├── endLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, dernier jour
            │   └─ Date du dernier jour de la plus longue période sous upLim
            ├── dtLF_winter = apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, durée
            │   └─ Nombre de jours de la plus longue période sous upLim
            ├── vLF_winter = deficit_volume(VC10)
            │   │  sous upLim
            │   └─ Somme des volumes écoulés chaque jour de la plus longue
            │      période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           startLF_winter, centerLF_winter, endLF_winter, dtLF_winter,
           vLF_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/series/allLF_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:29553c2a77d73b5bcc59eb2ea4c20ca3e0584786</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#startLF_winter"><code>startLF_winter</code></a></dt><dd><span lang="en">Start of winter low flows</span><span lang="fr">Début des basses eaux hivernales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#centerLF_winter"><code>centerLF_winter</code></a></dt><dd><span lang="en">Center of winter low flows</span><span lang="fr">Centre des basses eaux hivernales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#endLF_winter"><code>endLF_winter</code></a></dt><dd><span lang="en">End of winter low flows</span><span lang="fr">Fin des basses eaux hivernales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#dtLF_winter"><code>dtLF_winter</code></a></dt><dd><span lang="en">Duration of winter low flows</span><span lang="fr">Durée des basses eaux hivernales</span><span class="u">day</span></dd><dt><a href="../../catalogue/#vLF_winter"><code>vLF_winter</code></a></dt><dd><span lang="en">Deficit volume of winter low flows</span><span lang="fr">Volume de déficit des basses eaux hivernales</span><span class="u">hm³</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/allLF_winter.yaml) &middot; [back to the catalogue](../catalogue.md)
