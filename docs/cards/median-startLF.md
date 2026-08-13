---
hide:
  - toc
---

# `median-startLF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-startLF           Inter-annual median of the start of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the dates of the first 10-day mean flow value below the
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
            │   │  VC10 &lt;= upLim, longest episode, first day
            │   └─ Date of the first day of the longest period below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           startLF
            ╷
            ├── circular_median(startLF)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-startLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-startLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b73989f771c88c3154c56fa59fa7b7d18632988d</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-startLF         Médiane inter-annuelle du début des basses eaux  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des dates de la première valeur de débits moyens sur 10 jours
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
            │   │  VC10 &lt;= upLim, plus long épisode, premier jour
            │   └─ Date du premier jour de la plus longue période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           startLF
            ╷
            ├── circular_median(startLF)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-startLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-startLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b73989f771c88c3154c56fa59fa7b7d18632988d</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-startLF"><code>median-startLF</code></a></dt><dd><span lang="en">Inter-annual median of the start of low flows</span><span lang="fr">Médiane inter-annuelle du début des basses eaux</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/median-startLF.yaml) &middot; [back to the catalogue](../catalogue.md)
