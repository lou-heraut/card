---
hide:
  - toc
---

# `allLF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF                                                        5 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF
       Start of low flows
       Date of the first 10-day mean flow value below the threshold set at the
       maximum of VCN10
           unit ─ yearday

     ◇ centerLF
       Center of low flows
       Date of the minimal 10-day mean flow value below the threshold set at
       the maximum of VCN10
           unit ─ yearday

     ◇ endLF
       End of low flows
       Date of the last 10-day mean flow value below the threshold set at the
       maximum of VCN10
           unit ─ yearday

     ◇ dtLF
       Duration of low flows
       Duration of the longest continuous sequence with 10-day mean flows
       below the threshold set at the maximum of VCN10
           unit ─ day

     ◇ vLF
       Deficit volume of low flows
       Sum of the differences between the 10-day mean and the maximum of
       VCN10, over the longest sequence below this threshold
           unit ─ hm³

     phenomenon ─ low flows
         season ─ annual
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

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/low-flows/series/allLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f8c7d0212a16242f202dfdd0e206ac6c36bf762e</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  allLF                                                        5 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ startLF (debutBE)
       Début des basses eaux
       Date de la première valeur de débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ centerLF (centreBE)
       Centre des basses eaux
       Date de la valeur minimale des débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ endLF (finBE)
       Fin des basses eaux
       Date de la dernière valeur de débits moyens sur 10 jours sous le seuil
       fixé au maximum des VCN10
          unité ─ jour de l'année

     ◇ dtLF (dtBE)
       Durée des basses eaux
       Durée de la plus longue séquence continue avec des débits moyens sur 10
       jours sous le seuil fixé au maximum des VCN10
          unité ─ jour

     ◇ vLF (vBE)
       Volume de déficit des basses eaux
       Somme des écarts entre la moyenne sur 10 jours et le maximum des VCN10,
       sur la séquence la plus longue sous ce seuil
          unité ─ hm³

      phénomène ─ basses eaux
         saison ─ annuelle
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

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/low-flows/series/allLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f8c7d0212a16242f202dfdd0e206ac6c36bf762e</pre>

**Variables produced**  [`startLF`](../catalogue.md#startLF) · [`centerLF`](../catalogue.md#centerLF) · [`endLF`](../catalogue.md#endLF) · [`dtLF`](../catalogue.md#dtLF) · [`vLF`](../catalogue.md#vLF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/allLF.yaml) &middot; [back to the catalogue](../catalogue.md)
