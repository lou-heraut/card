---
hide:
  - toc
---

# `tVCN10_winter`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10_winter          Date of the winter minimum of 10-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Months from November to April

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
            ├── nanargmin(VC10)
            │   └─ Date of the minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           tVCN10_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/tVCN10_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7b59c6c9ac83824eee476781486cf2427001bf94</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tVCN10_winter        Date du minimum hivernal des débits moyens sur 10  │
  │                                                                   jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Mois de novembre à avril

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
            ├── nanargmin(VC10)
            │   └─ Date du minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           tVCN10_winter

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/low-flows/series/tVCN10_winter.yaml
  https://archive.softwareheritage.org/swh:1:cnt:7b59c6c9ac83824eee476781486cf2427001bf94</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#tVCN10_winter"><code>tVCN10_winter</code></a></dt><dd><span lang="en">Date of the winter minimum of 10-day mean flows</span><span lang="fr">Date du minimum hivernal des débits moyens sur 10 jours</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/tVCN10_winter.yaml) &middot; [back to the catalogue](../catalogue.md)
