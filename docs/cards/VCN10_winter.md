---
hide:
  - toc
---

# `VCN10_winter`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN10_winter             Winter minimum of 10-day mean daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ winter
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           VCN10_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/VCN10_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e48aa9b5f7f10c1dca3c2dd51ad065b43b0ca07a</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN10_winter      Minimum hivernal de la moyenne sur 10 jours du débit  │
  │                                                              journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ hivernale
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           VCN10_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/VCN10_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:e48aa9b5f7f10c1dca3c2dd51ad065b43b0ca07a</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#VCN10_winter"><code>VCN10_winter</code></a></dt><dd><span lang="en">Winter minimum of 10-day mean daily discharge</span><span lang="fr">Minimum hivernal de la moyenne sur 10 jours du débit journalier</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/VCN10_winter.yaml) &middot; [back to the catalogue](../catalogue.md)
