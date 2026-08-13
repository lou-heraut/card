---
hide:
  - toc
---

# `median-dtBF`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-dtBF            Inter-annual median of the duration of baseflow  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the durations between the start and end of baseflow

     phenomenon ─ baseflow
         season ─ annual
           form ─ scalar
           unit ─ day
          input ─ Q [m³·s⁻¹]

            ╷
            ├── snowmelt_duration(Q)
            │   │  method=Wal
            │   └─ Number of days between the dates at which the baseflow
            │      (Wallingford) sum corresponds to 10 % and 90 % of the total
            │      baseflow sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           dtBF
            ╷
            ├── nanmedian(dtBF)
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-dtBF

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/scalar/median-dtBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0ece430056df3246ffe67a7c04a3362d49b0def8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-dtBF   Médiane inter-annuelle de la durée des écoulements lents  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des durées entre le début et la fin des écoulements lents

      phénomène ─ débit de base
         saison ─ annuelle
          forme ─ scalaire
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
            ╷
            ├── nanmedian(dtBF)
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-dtBF

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/scalar/median-dtBF.yaml
  https://archive.softwareheritage.org/swh:1:cnt:0ece430056df3246ffe67a7c04a3362d49b0def8</pre>

**Variables produced**  [`median-dtBF`](../catalogue.md#median-dtBF)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/median-dtBF.yaml) &middot; [back to the catalogue](../catalogue.md)
