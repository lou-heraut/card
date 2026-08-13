---
hide:
  - toc
---

# `median-centerLF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-centerLF         Inter-annual median of the center of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the dates of the minimal 10-day mean flow value below the
     threshold set at the maximum of VCN10

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ yearday
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, day of the minimum
            │   └─ Date of the minimum of VC10 over the longest period below
            │      upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           centerLF
            ╷
            ├── circular_median(centerLF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-centerLF

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/low-flows/scalar/median-centerLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c5ff9b43bb134256a9481413938f95a0472c5801</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-centerLF       Médiane inter-annuelle du centre des basses eaux  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des dates de la valeur minimale des débits moyens sur 10 jours
     sous le seuil fixé au maximum des VCN10

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour de l'année
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, jour du minimum
            │   └─ Date du minimum de VC10 sur la plus longue période sous
            │      upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           centerLF
            ╷
            ├── circular_median(centerLF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-centerLF

  ──────────────────────────────────────────────────────────────────────────
  v1.5   flow/low-flows/scalar/median-centerLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c5ff9b43bb134256a9481413938f95a0472c5801</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-centerLF"><code>median-centerLF</code></a></dt><dd><span lang="en">Inter-annual median of the center of low flows</span><span lang="fr">Médiane inter-annuelle du centre des basses eaux</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/median-centerLF.yaml) &middot; [back to the catalogue](../catalogue.md)
