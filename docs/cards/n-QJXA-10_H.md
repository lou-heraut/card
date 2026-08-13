---
hide:
  - toc
---

# `n-QJXA-10_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  n-QJXA-10_H        Number of years in the target horizon where QJXA is  │
  │                          superior to QJXA-10 from the historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmax(Q)
            │   └─ Maximum of Q
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           QJXA
            ╷
            ├── return_level(QJXA)
            │   │  water_type=high
            │   │  from date, ref_start, ref_end
            │   └─ Calculation of the flow with a 10-year return period using
            │      the Gumbel distribution from the historical period
            │    ◦ A single value, repeated over the whole record
            ▼
           QJXA-10
            ╷
            ├── apply_threshold(QJXA)
            │   │  QJXA &gt;= QJXA-10, select=all, duration
            │   │  from date, horizon_start, horizon_end
            │   └─ Counting the number of QJXA in the target horizon above
            │      QJXA-10
            │    ◦ No temporal aggregation
            ▼
           n-QJXA-10

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/high-flows/scalar/n-QJXA-10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a8e278b017aff89c9d761bc1202c8ac3d20ec2b6</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  n-QJXA-10_H          Nombre d'années de l'horizon cible où le QJXA est  │
  │                           supérieur au QJXA-10 de la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── nanmax(Q)
            │   └─ Maximum de Q
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           QJXA
            ╷
            ├── return_level(QJXA)
            │   │  water_type=high
            │   │  d'après date, ref_start, ref_end
            │   └─ Calcul du débit de période de retour 10 ans avec la loi de
            │      Gumbel sur la période historique
            │    ◦ Une seule valeur, répétée sur toute la chronique
            ▼
           QJXA-10
            ╷
            ├── apply_threshold(QJXA)
            │   │  QJXA &gt;= QJXA-10, select=all, durée
            │   │  d'après date, horizon_start, horizon_end
            │   └─ Décompte du nombre de QJXA de l'horizon cible au dessus du
            │      QJXA-10
            │    ◦ Aucune agrégation temporelle
            ▼
           n-QJXA-10

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/high-flows/scalar/n-QJXA-10_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a8e278b017aff89c9d761bc1202c8ac3d20ec2b6</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#n-QJXA-10"><code>n-QJXA-10</code></a></dt><dd><span lang="en">Number of years in the target horizon where QJXA is superior to QJXA-10 from the historical period</span><span lang="fr">Nombre d'années de l'horizon cible où le QJXA est supérieur au QJXA-10 de la période historique</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/n-QJXA-10_H.yaml) &middot; [back to the catalogue](../catalogue.md)
