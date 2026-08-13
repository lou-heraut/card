---
hide:
  - toc
---

# `n-VCN10-5_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  n-VCN10-5_H       Number of years in the target horizon where VCN10 is  │
  │                    below or equal to VCN10-5 from the historical period  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ low flows
         season ─ annual
           form ─ scalar
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ 10-day centered moving average
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Adaptive window, specific to each series
            ▼
           VCN10
            ╷
            ├── return_level(VCN10)
            │   │  water_type=low
            │   │  from date, ref_start, ref_end
            │   └─ Calculation of the 5-year return period flow with the
            │      log-normal distribution from the historical period
            │    ◦ A single value, repeated over the whole record
            ▼
           VCN10-5
            ╷
            ├── apply_threshold(VCN10)
            │   │  VCN10 &lt;= VCN10-5, select=all, duration
            │   │  from date, horizon_start, horizon_end
            │   └─ Counting the number of VCN10 in the target horizon below or
            │      equal to VCN10-5
            │    ◦ No temporal aggregation
            ▼
           n-VCN10-5

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/n-VCN10-5_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:ebee4465a59545f4ee18fed2e48159562e873d80</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  n-VCN10-5_H         Nombre d'années de l'horizon cible où le VCN10 est  │
  │                   inférieur ou égal au VCN10-5 de la période historique  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ basses eaux
         saison ─ annuelle
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── rollmean_center(Q)
            │   └─ Moyenne mobile centrée sur 10 jours
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           VC10
            ╷
            ├── nanmin(VC10)
            │   └─ Minimum
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre adaptative, propre à chaque série
            ▼
           VCN10
            ╷
            ├── return_level(VCN10)
            │   │  water_type=low
            │   │  d'après date, ref_start, ref_end
            │   └─ Calcul du débit de période de retour 5 ans avec la loi
            │      log-normal sur la période historique
            │    ◦ Une seule valeur, répétée sur toute la chronique
            ▼
           VCN10-5
            ╷
            ├── apply_threshold(VCN10)
            │   │  VCN10 &lt;= VCN10-5, select=all, durée
            │   │  d'après date, horizon_start, horizon_end
            │   └─ Décompte du nombre de VCN10 de l'horizon cible inférieurs
            │      ou égaux au VCN10-5
            │    ◦ Aucune agrégation temporelle
            ▼
           n-VCN10-5

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/low-flows/scalar/n-VCN10-5_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:ebee4465a59545f4ee18fed2e48159562e873d80</pre>

**Variables produced**  [`n-VCN10-5`](../catalogue.md#n-VCN10-5)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/low-flows/scalar/n-VCN10-5_H.yaml) &middot; [back to the catalogue](../catalogue.md)
