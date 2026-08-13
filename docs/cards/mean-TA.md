---
hide:
  - toc
---

# `mean-TA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TA               Inter-annual mean of the annual mean temperature  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean temperatures
         season ─ annual
           form ─ scalar
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
            ╷
            ├── nanmean(TA)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-TA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:66769e374884980a8c24ac90ce349c3a00b831ee</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-TA      Moyenne inter-annuelle de la température moyenne annuelle  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ températures moyennes
         saison ─ annuelle
          forme ─ scalaire
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
            ╷
            ├── nanmean(TA)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-TA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   temperature/mean-temperatures/scalar/mean-TA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:66769e374884980a8c24ac90ce349c3a00b831ee</pre>

**Variables produced**  [`mean-TA`](../catalogue.md#mean-TA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/temperature/mean-temperatures/scalar/mean-TA.yaml) &middot; [back to the catalogue](../catalogue.md)
