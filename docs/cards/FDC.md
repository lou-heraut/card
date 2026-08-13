---
hide:
  - toc
---

# `FDC`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  FDC                          Flow duration curve over the whole record  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Curve of flow quantiles as a function of exceedance probability; the card
     outputs its two coordinates (FDC_p, unitless probabilities; FDC_Q, flow
     quantiles)

     ◇ FDC_p
           unit ─ without unit

     ◇ FDC_Q
           unit ─ m³·s⁻¹

     phenomenon ─ mean flows
         season ─ record
           form ─ curve
         inputs ─ Q [m³·s⁻¹], period_start, period_end (optional)

            ╷
            ├── FDC_p = fdc_probabilities(Q)
            │   │  norm_spacing=True
            │   └─ Exceedance probabilities of the 1000 points of the flow
            │      duration curve, spaced according to a centered reduced
            │      normal distribution
            ├── FDC_Q = fdc_quantiles(Q)
            │   │  norm_spacing=True
            │   │  restricted to the requested period
            │   │  from date, period_start, period_end
            │   └─ Flow quantiles of the 1000 points of the flow duration
            │      curve, spaced according to a centered reduced normal
            │      distribution
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           FDC_p, FDC_Q

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/curve/FDC.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d10d7bc8462f7b7eb242c5c06a5449027716e121</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  FDC                 Courbe des débits classés sur la chronique entière  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Courbe des quantiles de débit en fonction de la probabilité de
     dépassement ; la fiche produit ses deux coordonnées (FDC_p, probabilités
     sans unité ; FDC_Q, quantiles de débit)

     ◇ FDC_p (CDC_p)
          unité ─ sans unité

     ◇ FDC_Q (CDC_Q)
          unité ─ m³·s⁻¹

      phénomène ─ moyennes eaux
         saison ─ chronique
          forme ─ courbe
        entrées ─ Q [m³·s⁻¹], period_start, period_end (facultatifs)

            ╷
            ├── FDC_p = fdc_probabilities(Q)
            │   │  norm_spacing=True
            │   └─ Probabilités de dépassement des 1000 points de la courbe
            │      des débits classés, espacés selon une loi normale centrée
            │      réduite
            ├── FDC_Q = fdc_quantiles(Q)
            │   │  norm_spacing=True
            │   │  restreint à la période demandée
            │   │  d'après date, period_start, period_end
            │   └─ Quantiles de débit des 1000 points de la courbe des débits
            │      classés, espacés selon une loi normale centrée réduite
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           FDC_p, FDC_Q

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/curve/FDC.yaml
  https://archive.softwareheritage.org/swh:1:cnt:d10d7bc8462f7b7eb242c5c06a5449027716e121</pre>

**Variables produced**  [`FDC_p`](../catalogue.md#FDC_p) · [`FDC_Q`](../catalogue.md#FDC_Q)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/curve/FDC.yaml) &middot; [back to the catalogue](../catalogue.md)
