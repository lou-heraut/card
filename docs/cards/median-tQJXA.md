---
hide:
  - toc
---

# `median-tQJXA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tQJXA    Inter-annual median of the dates of the annual maximum  │
  │                                                         daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
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
            ╷
            ├── circular_median(tQJXA)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-tQJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/median-tQJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:833c237a36ff089f306db466f929c866587eebf4</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tQJXA      Médiane inter-annuelle des dates du débit journalier  │
  │                                                          maximal annuel  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
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
            ╷
            ├── circular_median(tQJXA)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-tQJXA

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/median-tQJXA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:833c237a36ff089f306db466f929c866587eebf4</pre>

**Variables produced**  [`median-tQJXA`](../catalogue.md#median-tQJXA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/median-tQJXA.yaml) &middot; [back to the catalogue](../catalogue.md)
