---
hide:
  - toc
---

# `delta-VCN30_summer_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN30_summer_H   Average change of summer minimum of 30-day mean  │
  │                          daily discharge between the target horizon and  │
  │                                                       historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ summer
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 30-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC30
            ╷
            ├── nanmin(VC30)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Partial window, from 05-01 to 11-30
            ▼
           VCN30_summer
            ╷
            ├── delta(VCN30_summer, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-VCN30_summer

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/scalar/delta-VCN30_summer_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:6a12187274a4ffb576f2bd2f05d02ff6d7a545b9</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN30_summer_H         Changement moyen du minimum estival de la  │
  │                          moyenne sur 30 jours du débit journalier entre  │
  │                                l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ estivale
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 30 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC30
            ╷
            ├── nanmin(VC30)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ············┃▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃···
            │      Fenêtre partielle, du 01-05 au 30-11
            ▼
           VCN30_summer
            ╷
            ├── delta(VCN30_summer, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-VCN30_summer

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/scalar/delta-VCN30_summer_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:6a12187274a4ffb576f2bd2f05d02ff6d7a545b9</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-VCN30_summer"><code>delta-VCN30_summer</code></a></dt><dd><span lang="en">Average change of summer minimum of 30-day mean daily discharge between the target horizon and historical period</span><span lang="fr">Changement moyen du minimum estival de la moyenne sur 30 jours du débit journalier entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-VCN30_summer_H.yaml) &middot; [back to the catalogue](../catalogue.md)
