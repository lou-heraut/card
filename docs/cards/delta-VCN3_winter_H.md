---
hide:
  - toc
---

# `delta-VCN3_winter_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN3_winter_H     Average change of winter minimum of 3-day mean  │
  │                          daily discharge between the target horizon and  │
  │                                                       historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ winter
           form ─ scalar
           unit ─ %
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 3-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC3
            ╷
            ├── nanmin(VC3)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Partial window, from 11-01 to 04-30
            ▼
           VCN3_winter
            ╷
            ├── delta(VCN3_winter, date)
            │   │  relative=True
            │   │  from ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calculation of the average change between the historical
            │      period and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-VCN3_winter

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/scalar/delta-VCN3_winter_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f5009dd66b816d57175eba04f064f0a08cb1daaf</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-VCN3_winter_H         Changement moyen du minimum hivernal de la  │
  │                           moyenne sur 3 jours du débit journalier entre  │
  │                                l'horizon cible et la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ hivernale
          forme ─ scalaire
          unité ─ %
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 3 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC3
            ╷
            ├── nanmin(VC3)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓··················┃┃··················▓▓▓▓▓▓
            │      Fenêtre partielle, du 01-11 au 30-04
            ▼
           VCN3_winter
            ╷
            ├── delta(VCN3_winter, date)
            │   │  relative=True
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end
            │   └─ Calcul du changement moyen entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-VCN3_winter

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/low-flows/scalar/delta-VCN3_winter_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f5009dd66b816d57175eba04f064f0a08cb1daaf</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#delta-VCN3_winter"><code>delta-VCN3_winter</code></a></dt><dd><span lang="en">Average change of winter minimum of 3-day mean daily discharge between the target horizon and historical period</span><span lang="fr">Changement moyen du minimum hivernal de la moyenne sur 3 jours du débit journalier entre l'horizon cible et la période historique</span><span class="u">%</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/delta-VCN3_winter_H.yaml) &middot; [back to the catalogue](../catalogue.md)
