---
hide:
  - toc
---

# `tQJXA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tQJXA                       Date of the annual maximum daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ series
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanargmax(Q)
            │   └─ Date of the maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           tQJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/series/tQJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:899c828968ff7f68c5a39a3610b3ece50951921c</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  tQJXA                          Date du débit journalier maximal annuel  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ série
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanargmax(Q)
            │   └─ Date du maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           tQJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/series/tQJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:899c828968ff7f68c5a39a3610b3ece50951921c</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#tQJXA"><code>tQJXA</code></a></dt><dd><span lang="en">Date of the annual maximum daily discharge</span><span lang="fr">Date du débit journalier maximal annuel</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/tQJXA.yaml) &middot; [back to the catalogue](../catalogue.md)
