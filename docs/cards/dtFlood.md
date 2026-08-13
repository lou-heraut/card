---
hide:
  - toc
---

# `dtFlood`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtFlood                                             Duration of floods  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Duration of floods, sampled by annual maxima. The series exploited is the
     difference between the raw flow and the base flow, assimilated to runoff
     Qr. Floods are identified based on the annual maximum in the Qr series,
     and for each flood, the duration is defined as the number of days where
     Qr is above half of the annual maxima.

     phenomenon ─ high flows
         season ─ annual
           form ─ series
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

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/high-flows/series/dtFlood.yaml
  https://archive.softwareheritage.org/swh:1:cnt:005f6d5b9cbf8c3291695b5452a616e77cf7a1b8</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  dtFlood                                                Durée des crues  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Durée des crues, échantillonnées par maxima annuel. La série exploitée
     est la différence entre le débit brut et le débit de base, assimilé au
     ruissellement Qr. Les crues sont identifiées sur la base du maximum
     annuel dans la série des Qr et pour chaque crue, la durée est définie
     comme le nombre de jours où Qr est supérieur au maxima annuel divisé par
     2.

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ série
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

  ──────────────────────────────────────────────────────────────────────────
  v3.0   flow/high-flows/series/dtFlood.yaml
  https://archive.softwareheritage.org/swh:1:cnt:005f6d5b9cbf8c3291695b5452a616e77cf7a1b8</pre>

**Variables produced**  [`dtFlood`](../catalogue.md#dtFlood)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/dtFlood.yaml) &middot; [back to the catalogue](../catalogue.md)
