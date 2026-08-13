---
hide:
  - toc
---

# `QNA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QNA                                  Annual minimum of daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmin(Q)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QNA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/series/QNA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b38c3094dbfc6af965208122e9c5a19224d2a8b0</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QNA                                 Minimum annuel du débit journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmin(Q)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QNA

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/series/QNA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b38c3094dbfc6af965208122e9c5a19224d2a8b0</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QNA"><code>QNA</code></a></dt><dd><span lang="en">Annual minimum of daily discharge</span><span lang="fr">Minimum annuel du débit journalier</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/series/QNA.yaml) &middot; [back to the catalogue](../catalogue.md)
