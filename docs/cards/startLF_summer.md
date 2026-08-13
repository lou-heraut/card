---
hide:
  - toc
---

# `startLF_summer`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  startLF_summer                               Start of summer low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     In summer, date of the first 10-day mean flow value below the threshold
     set at the maximum of VCN10 (May to November)

     phenomenon ─ low flows
         season ─ summer
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, longest episode, first day
            │   └─ Date of the first day of the longest period below upLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           startLF_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/low-flows/series/startLF_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:62e68a408245eece6134ea9ba9d40338e956702a</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  startLF_summer                         Début des basses eaux estivales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     En été, date de la première valeur de débits moyens sur 10 jours sous le
     seuil fixé au maximum des VCN10 (mois de mai à novembre)

      phénomène ─ basses eaux
         saison ─ estivale
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
            ├── apply_threshold(VC10)
            │   │  VC10 &lt;= upLim, plus long épisode, premier jour
            │   └─ Date du premier jour de la plus longue période sous upLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           startLF_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/low-flows/series/startLF_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:62e68a408245eece6134ea9ba9d40338e956702a</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#startLF_summer"><code>startLF_summer</code></a></dt><dd><span lang="en">Start of summer low flows</span><span lang="fr">Début des basses eaux estivales</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/startLF_summer.yaml) &middot; [back to the catalogue](../catalogue.md)
