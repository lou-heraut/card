---
hide:
  - toc
---

# `dtBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtBF                                             Duration of low flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Duration between the start and end of low flows

     phenomenon ─ baseflow
         season ─ annual
           form ─ series
           unit ─ day
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_duration(Q)
            │   │  method=Wal
            │   └─ Number of days between the dates when the baseflow
            │      (Wallingford) sum corresponds to 10 % and 90 % of the total
            │      sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtBF

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/series/dtBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c26e8e91b2819c26d96e52f6ee0253145e6853b2</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtBF                                       Durée des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Durée entre le début et la fin des écoulements lents

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ série
          unité ─ jour
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_duration(Q)
            │   │  method=Wal
            │   └─ Nombre de jours entre les dates auxquelles la somme du
            │      débit de base (Wallingford) correspond à 10 % et 90 % de la
            │      somme totale
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           dtBF

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/series/dtBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c26e8e91b2819c26d96e52f6ee0253145e6853b2</pre>

**Variables produced**  [`dtBF`](../catalogue.md#dtBF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/series/dtBF.yaml) &middot; [back to the catalogue](../catalogue.md)
