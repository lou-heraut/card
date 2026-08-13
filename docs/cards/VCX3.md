---
hide:
  - toc
---

# `VCX3`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCX3         Annual maximum of the 3-day moving average of daily flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
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
            ├── nanmax(VC3)
            │   └─ Maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCX3

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/series/VCX3.yaml
  https://archive.softwareheritage.org/swh:1:cnt:17908a4b7e125e2a8f5f61bddc562472b379b206</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  VCX3        Maximum annuel de la moyenne mobile sur 3 jours des débits  │
  │                                                             journaliers  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
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
            ├── nanmax(VC3)
            │   └─ Maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCX3

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/high-flows/series/VCX3.yaml
  https://archive.softwareheritage.org/swh:1:cnt:17908a4b7e125e2a8f5f61bddc562472b379b206</pre>

**Variables produced**  [`VCX3`](../catalogue.md#VCX3)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/VCX3.yaml) &middot; [back to the catalogue](../catalogue.md)
