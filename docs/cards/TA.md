---
hide:
  - toc
---

# `TA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TA                                             Annual mean temperature  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean temperatures
         season ─ annual
           form ─ series
           unit ─ °C
          input ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Mean
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           TA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:adec15c2268543028fee50e587cc6b991767078a</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  TA                                        Température moyenne annuelle  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ températures moyennes
         saison ─ annuelle
          forme ─ série
          unité ─ °C
         entrée ─ T [°C]

            ╷
            ├── nanmean(T)
            │   └─ Moyenne
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           TA

  ──────────────────────────────────────────────────────────────────────────
  v1.0.1   temperature/mean-temperatures/series/TA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:adec15c2268543028fee50e587cc6b991767078a</pre>

**Variables produced**  [`TA`](../catalogue.md#TA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/series/TA.yaml) &middot; [back to the catalogue](../catalogue.md)
