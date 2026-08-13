---
hide:
  - toc
---

# `median-vLF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-vLF      Inter-annual median of the deficit volume of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the sums of the differences between the 10-day mean and the
     maximum of VCN10, over the longest sequence below this threshold

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ hm³
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
            ├── deficit_volume(VC10)
            │   │  below upLim
            │   └─ Sum of volumes discharged each day in the longest period
            │      below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           vLF
            ╷
            ├── nanmedian(vLF)
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-vLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-vLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c1366503e9f3afec47e97009f0b6ffcad8efe7ee</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-vLF    Médiane inter-annuelle des volumes de déficit des basses  │
  │                                                                    eaux  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des sommes des écarts entre la moyenne sur 10 jours et le maximum
     des VCN10, sur la séquence la plus longue sous ce seuil

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ hm³
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
            ├── deficit_volume(VC10)
            │   │  sous upLim
            │   └─ Somme des volumes écoulés chaque jour de la plus longue
            │      période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           vLF
            ╷
            ├── nanmedian(vLF)
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-vLF

  ──────────────────────────────────────────────────────────────────────────
  v1.6   flow/low-flows/scalar/median-vLF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c1366503e9f3afec47e97009f0b6ffcad8efe7ee</pre>

**Variables produced**  [`median-vLF`](../catalogue.md#median-vLF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/median-vLF.yaml) &middot; [back to the catalogue](../catalogue.md)
