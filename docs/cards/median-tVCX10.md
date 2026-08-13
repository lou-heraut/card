---
hide:
  - toc
---

# `median-tVCX10`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tVCX10   Inter-annual median of the dates of the annual maximum  │
  │                                                    of 10-day mean flows  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ yearday
          input ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanargmax(VC10)
            │   └─ Date of the maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           tVCX10
            ╷
            ├── circular_median(tVCX10)
            │   │  periodicity=365.25
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-tVCX10

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/median-tVCX10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b8dd6e1b87f6ed31767fc7920e06a867bd69b282</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-tVCX10   Médiane inter-annuelle des dates du maximum annuel des  │
  │                                              débits moyens sur 10 jours  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour de l'année
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanargmax(VC10)
            │   └─ Date du maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           tVCX10
            ╷
            ├── circular_median(tVCX10)
            │   │  periodicity=365.25
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-tVCX10

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/median-tVCX10.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b8dd6e1b87f6ed31767fc7920e06a867bd69b282</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-tVCX10"><code>median-tVCX10</code></a></dt><dd><span lang="en">Inter-annual median of the dates of the annual maximum of 10-day mean flows</span><span lang="fr">Médiane inter-annuelle des dates du maximum annuel des débits moyens sur 10 jours</span><span class="u">yearday</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/median-tVCX10.yaml) &middot; [back to the catalogue](../catalogue.md)
