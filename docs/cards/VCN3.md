---
hide:
  - toc
---

# `VCN3`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN3                      Annual minimum of 3-day mean daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 3-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC3
            ╷
            ├── nanmin(VC3)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN3

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/VCN3.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2fb861e75f2e7081b399fc43a8b9a777fc5342ea</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCN3      Minimum annuel de la moyenne sur 3 jours du débit journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 3 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC3
            ╷
            ├── nanmin(VC3)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN3

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/series/VCN3.yaml
  https://archive.softwareheritage.org/swh:1:cnt:2fb861e75f2e7081b399fc43a8b9a777fc5342ea</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#VCN3"><code>VCN3</code></a></dt><dd><span lang="en">Annual minimum of 3-day mean daily discharge</span><span lang="fr">Minimum annuel de la moyenne sur 3 jours du débit journalier</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/VCN3.yaml) &middot; [back to the catalogue](../catalogue.md)
