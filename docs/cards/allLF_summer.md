---
hide:
  - toc
---

# `allLF_summer`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF_summer                                                 5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF_summer
       Start of summer low flows
       In summer, date of the first 10-day mean flow value below the threshold
       set at the maximum of VCN10 (May to November)
           unit ─ yearday

     ◇ centerLF_summer
       Center of summer low flows
       In summer, date of the minimal 10-day mean flow value below the
       threshold set at the maximum of VCN10 (May to November)
           unit ─ yearday

     ◇ endLF_summer
       End of summer low flows
       In summer, date of the last 10-day mean flow value below the threshold
       set at the maximum of VCN10 (May to November)
           unit ─ yearday

     ◇ dtLF_summer
       Duration of summer low flows
       In summer, duration of the longest continuous sequence with 10-day mean
       flows below the threshold set at the maximum of VCN10 (May to November)
           unit ─ day

     ◇ vLF_summer
       Deficit volume of summer low flows
       In summer, sum of the differences between the 10-day mean and the
       maximum of VCN10, over the longest sequence below this threshold (May
       to November)
           unit ─ hm³

     phenomenon ─ low flows
         season ─ summer
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

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/series/allLF_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5e47eaf271563e24457935b622819d30b4f8659b</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF_summer                                                 5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF_summer (debutBE_été)
       Début des basses eaux estivales
       En été, date de la première valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour de l'année

     ◇ centerLF_summer (centreBE_été)
       Centre des basses eaux estivales
       En été, date de la valeur minimale des débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour de l'année

     ◇ endLF_summer (finBE_été)
       Fin des basses eaux estivales
       En été, date de la dernière valeur de débits moyens sur 10 jours sous
       le seuil fixé au maximum des VCN10 (mois de mai à novembre)
          unité ─ jour de l'année

     ◇ dtLF_summer (dtBE_été)
       Durée des basses eaux estivales
       En été, durée de la plus longue séquence continue avec des débits
       moyens sur 10 jours sous le seuil fixé au maximum des VCN10 (mois de
       mai à novembre)
          unité ─ jour

     ◇ vLF_summer (vBE_été)
       Volume de déficit des basses eaux estivales
       En été, somme des écarts entre la moyenne sur 10 jours et le maximum
       des VCN10, sur la séquence la plus longue sous ce seuil (mois de mai à
       novembre)
          unité ─ hm³

      phénomène ─ basses eaux
         saison ─ estivale
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

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/series/allLF_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:5e47eaf271563e24457935b622819d30b4f8659b</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#startLF_summer"><code>startLF_summer</code></a></dt><dd><span lang="en">Start of summer low flows</span><span lang="fr">Début des basses eaux estivales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#centerLF_summer"><code>centerLF_summer</code></a></dt><dd><span lang="en">Center of summer low flows</span><span lang="fr">Centre des basses eaux estivales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#endLF_summer"><code>endLF_summer</code></a></dt><dd><span lang="en">End of summer low flows</span><span lang="fr">Fin des basses eaux estivales</span><span class="u">yearday</span></dd><dt><a href="../../catalogue/#dtLF_summer"><code>dtLF_summer</code></a></dt><dd><span lang="en">Duration of summer low flows</span><span lang="fr">Durée des basses eaux estivales</span><span class="u">day</span></dd><dt><a href="../../catalogue/#vLF_summer"><code>vLF_summer</code></a></dt><dd><span lang="en">Deficit volume of summer low flows</span><span lang="fr">Volume de déficit des basses eaux estivales</span><span class="u">hm³</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/allLF_summer.yaml) &middot; [back to the catalogue](../catalogue.md)
