---
hide:
  - toc
---

# `startBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  startBF                                             Start of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date when 10 % of the annual cumulative baseflow is reached

     phenomenon ─ baseflow
         season ─ annual
           form ─ series
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date when the baseflow (Wallingford) sum corresponds to 10
            │      % of the total sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           startBF

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/baseflow/series/startBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:80c8d8b8d80fe1c74d546a7fcbfa22c313f19218</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  startBF                                    Début des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Date à laquelle 10 % du cumul annuel du débit de base sont atteints

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ série
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_timing(Q)
            │   │  method=Wal
            │   └─ Date à laquelle la somme du débit de base (Wallingford)
            │      correspond à 10 % de la somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           startBF

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/baseflow/series/startBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:80c8d8b8d80fe1c74d546a7fcbfa22c313f19218</pre>

**Variables produced**  [`startBF`](../catalogue.md#startBF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/series/startBF.yaml) &middot; [back to the catalogue](../catalogue.md)
