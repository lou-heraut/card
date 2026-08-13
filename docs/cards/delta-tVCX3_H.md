---
hide:
  - toc
---

# `delta-tVCX3_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-tVCX3_H      Average change of the date of the annual maximum of  │
  │                         the 3-day mean of daily flow between the target  │
  │                                           horizon and historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ high flows
         season ─ annual
           form ─ scalar
           unit ─ day
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 3-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC3
            ╷
            ├── nanargmax(VC3)
            │   └─ Date of the maximum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           tVCX3
            ╷
            ├── delta(tVCX3, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-tVCX3

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/delta-tVCX3_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b8755677cf198577b6b761dd575250358b371045</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-tVCX3_H      Changement moyen de la date du maximum annuel de la  │
  │                           moyenne sur 3 jours du débit journalier entre  │
  │                                l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ hautes eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ jour
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 3 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC3
            ╷
            ├── nanargmax(VC3)
            │   └─ Date du maximum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           tVCX3
            ╷
            ├── delta(tVCX3, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-tVCX3

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/high-flows/scalar/delta-tVCX3_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:b8755677cf198577b6b761dd575250358b371045</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-tVCX3"><code>delta-tVCX3</code></a></dt><dd><span lang="en">Average change of the date of the annual maximum of the 3-day mean of daily flow between the target horizon and historical period</span><span lang="fr">Changement moyen de la date du maximum annuel de la moyenne sur 3 jours du débit journalier entre l'horizon cible et la période historique</span><span class="u">day</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/high-flows/scalar/delta-tVCX3_H.yaml) &middot; [back to the catalogue](../catalogue.md)
