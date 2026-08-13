---
hide:
  - toc
---

# `centerLF_winter`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  centerLF_winter                             Center of winter low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     In winter, date of the minimal 10-day mean flow value below the threshold
     set at the maximum of VCN10 (November to April)

     phenomenon ─ low flows
         season ─ winter
           form ─ series
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, day of the minimum
            │   └─ Date of the minimum of VC10 over the longest period below
            │      upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           centerLF_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/low-flows/series/centerLF_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cade2ce2c0942d17cd85514049938f5821f9e575</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  centerLF_winter                      Centre des basses eaux hivernales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     En hiver, date de la valeur minimale des débits moyens sur 10 jours sous
     le seuil fixé au maximum des VCN10 (mois de novembre à avril)

      phénomène ─ basses eaux
         saison ─ hivernale
          forme ─ série
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, jour du minimum
            │   └─ Date du minimum de VC10 sur la plus longue période sous
            │      upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           centerLF_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/low-flows/series/centerLF_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:cade2ce2c0942d17cd85514049938f5821f9e575</pre>

**Variables produced**  [`centerLF_winter`](../catalogue.md#centerLF_winter)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/centerLF_winter.yaml) &middot; [back to the catalogue](../catalogue.md)
