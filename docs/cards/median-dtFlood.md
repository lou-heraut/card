---
hide:
  - toc
---

# `median-dtFlood`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-dtFlood           Inter-annual median of the duration of floods  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Median of the durations of floods sampled by annual maxima

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ day
          input ─ Q [m³·s⁻¹]

            ╷
            ├── quickflow(Q)
            │   └─ Difference between the daily flow and the base flow
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           dQ
            ╷
            ├── nanmax(dQ)
            │   └─ Maximum of dQ
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           dQXA
            ╷
            ├── ratio_longest_run(dQXA, 2)
            │   └─ Division by two of dQXA to obtain a threshold
            │    ◦ One value per year
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           lowLim
            ╷
            ├── apply_threshold(dQ)
            │   │  dQ &gt;= lowLim, select=dQXA, duration
            │   └─ Number of days where dQ is above lowLim
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           dtFlood
            ╷
            ├── nanmedian(dtFlood)
            │   └─ Inter-annual median
            │    ◦ No temporal aggregation
            ▼
           median-dtFlood

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/high-flows/scalar/median-dtFlood.yaml
  https://archive.softwareheritage.org/swh:1:cnt:84fe5d1259fe449375a07bb78c4e82c4c5abeb5d</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  median-dtFlood            Médiane inter-annuelle de la durée des crues  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Médiane des durées des crues échantillonnées par maxima annuel

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── quickflow(Q)
            │   └─ Différence entre le débit journalier et le débit de base
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           dQ
            ╷
            ├── nanmax(dQ)
            │   └─ Maximum de dQ
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           dQXA
            ╷
            ├── ratio_longest_run(dQXA, 2)
            │   └─ Division par deux de dQXA pour obtenir un seuil
            │    ◦ Une valeur par année
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           lowLim
            ╷
            ├── apply_threshold(dQ)
            │   │  dQ &gt;= lowLim, select=dQXA, durée
            │   └─ Nombre de jours où dQ dépasse lowLim
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           dtFlood
            ╷
            ├── nanmedian(dtFlood)
            │   └─ Médiane inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           median-dtFlood

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/high-flows/scalar/median-dtFlood.yaml
  https://archive.softwareheritage.org/swh:1:cnt:84fe5d1259fe449375a07bb78c4e82c4c5abeb5d</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#median-dtFlood"><code>median-dtFlood</code></a></dt><dd><span lang="en">Inter-annual median of the duration of floods</span><span lang="fr">Médiane inter-annuelle de la durée des crues</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/median-dtFlood.yaml) &middot; [back to the catalogue](../catalogue.md)
