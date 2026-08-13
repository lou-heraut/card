---
hide:
  - toc
---

# `fQ05A`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  fQ05A                                Annual frequency of exceeding Q05  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Annual frequency of exceeding Q &gt; Q05, where Q05 is the flow exceeded 5 %
     of the time, extracted from the ranked flow curve

     phenomenon ─ high flows
         season ─ annual
           form ─ series
           unit ─ without unit
          input ─ Q [m³·s⁻¹]

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile at the 5 % exceedance probability, taken as the
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
           fQ05A

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/series/fQ05A.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f33ac33439abf3f2bee962e213b4fd12b1281808</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  fQ05A                         Fréquence annuelle de dépassement du Q05  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Fréquence annuelle de dépassement de Q &gt; Q05, Q05 est le débit dépassé 5
     % du temps, extrait de la courbe des débits classés

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ série
          unité ─ sans unité
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── exceedance_quantile(Q)
            │   └─ Quantile à la probabilité de dépassement de 5 %, pris comme
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
           fQ05A

  ──────────────────────────────────────────────────────────────────────────
  v1.4   flow/high-flows/series/fQ05A.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f33ac33439abf3f2bee962e213b4fd12b1281808</pre>

**Variables produced**  [`fQ05A`](../catalogue.md#fQ05A)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/series/fQ05A.yaml) &middot; [back to the catalogue](../catalogue.md)
