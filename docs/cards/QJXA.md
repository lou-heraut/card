---
hide:
  - toc
---

# `QJXA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJXA                                         Annual maximum daily flow  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/series/QJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:82ee03262d7b119bfa07e5512319ddf965b3f7ac</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QJXA                                   Débit journalier maximal annuel  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmax(Q)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/series/QJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:82ee03262d7b119bfa07e5512319ddf965b3f7ac</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QJXA"><code>QJXA</code></a></dt><dd><span lang="en">Annual maximum daily flow</span><span lang="fr">Débit journalier maximal annuel</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/QJXA.yaml) &middot; [back to the catalogue](../catalogue.md)
