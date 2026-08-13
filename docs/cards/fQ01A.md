---
hide:
  - toc
---

# `fQ01A`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  fQ01A                                Annual frequency of exceeding Q01  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual frequency of exceeding Q &gt; Q01, where Q01 is the flow exceeded 1 %
     of the time, extracted from the ranked flow curve

     phenomenon ─ high flows
         season ─ annual
           form ─ series
           unit ─ without unit
          input ─ Q [m³·s⁻¹]

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile at the 1 % exceedance probability, taken as the
            │      threshold
            │    ◦ A single value, repeated over the whole record
            │    ◦ Cut beyond 10 missing years
            ▼
           lowLim
            ╷
            ├── exceedance_frequency(Q)
            │   │  below lowLim
            │   └─ Ratio of the number of days with flow exceeding lowLim to
            │      the number of days in the year
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           fQ01A

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/series/fQ01A.yaml
  https://archive.softwareheritage.org/swh:1:cnt:276496f90c67f3ecb24363bf1e354cb0cd5d3eae</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  fQ01A                         Fréquence annuelle de dépassement du Q01  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Fréquence annuelle de dépassement de Q &gt; Q01, Q01 est le débit dépassé 1
     % du temps, extrait de la courbe des débits classés

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ série
          unité ─ sans unité
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile à la probabilité de dépassement de 1 %, pris comme
            │      seuil
            │    ◦ Une seule valeur, répétée sur toute la chronique
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           lowLim
            ╷
            ├── exceedance_frequency(Q)
            │   │  sous lowLim
            │   └─ Rapport du nombre de jours où le débit dépasse lowLim par
            │      le nombre de jours dans l'année
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           fQ01A

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/series/fQ01A.yaml
  https://archive.softwareheritage.org/swh:1:cnt:276496f90c67f3ecb24363bf1e354cb0cd5d3eae</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#fQ01A"><code>fQ01A</code></a></dt><dd><span lang="en">Annual frequency of exceeding Q01</span><span lang="fr">Fréquence annuelle de dépassement du Q01</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/fQ01A.yaml) &middot; [back to the catalogue](../catalogue.md)
