---
hide:
  - toc
---

# `VCN30_summer`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN30_summer             Summer minimum of 30-day mean daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ summer
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 30-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC30
            ╷
            ├── nanmin(VC30)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           VCN30_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/VCN30_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c4a6960cd33a17fca293aa3c05152889291bc1a8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN30_summer       Minimum estival de la moyenne sur 30 jours du débit  │
  │                                                              journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ estivale
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 30 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC30
            ╷
            ├── nanmin(VC30)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           VCN30_summer

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/VCN30_summer.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c4a6960cd33a17fca293aa3c05152889291bc1a8</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#VCN30_summer"><code>VCN30_summer</code></a></dt><dd><span lang="en">Summer minimum of 30-day mean daily discharge</span><span lang="fr">Minimum estival de la moyenne sur 30 jours du débit journalier</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/VCN30_summer.yaml) &middot; [back to the catalogue](../catalogue.md)
