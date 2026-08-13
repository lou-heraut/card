---
hide:
  - toc
---

# `a-FDC`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  a-FDC      Slope of the segment between the 33 % and 66 % quantiles of  │
  │                                                 the flow duration curve  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Slope computed on the decimal logarithms of the flows: a steep slope
     indicates a highly variable regime

     phenomenon ─ mean flows
         season ─ record
           form ─ scalar
           unit ─ without unit
          input ─ Q [m³·s⁻¹]

            ╷
            ├── fdc_slope(Q)
            │   │  p=[0.33, 0.66]
            │   └─ Computation of the flow duration curve and differences
            │      between quantiles
            │    ◦ No temporal aggregation
            │    ◦ Cut beyond 10 missing years
            ▼
           a-FDC

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/scalar/a-FDC.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c74884c1b877d1df158501505f21a26342fd5384</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  a-FDC    Pente du segment entre les quantiles des débits journaliers à  │
  │                            33 % et 66 % de la courbe des débits classés  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Pente calculée sur les logarithmes décimaux des débits : une pente forte
     signale un régime très variable

      phénomène ─ moyennes eaux
         saison ─ chronique
          forme ─ scalaire
          unité ─ sans unité
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── fdc_slope(Q)
            │   │  p=[0.33, 0.66]
            │   └─ Calcul de la courbe des débits classés et des différences
            │      entre quantiles
            │    ◦ Aucune agrégation temporelle
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           a-FDC

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/mean-flows/scalar/a-FDC.yaml
  https://archive.softwareheritage.org/swh:1:cnt:c74884c1b877d1df158501505f21a26342fd5384</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#a-FDC"><code>a-FDC</code></a></dt><dd><span lang="en">Slope of the segment between the 33 % and 66 % quantiles of the flow duration curve</span><span lang="fr">Pente du segment entre les quantiles des débits journaliers à 33 % et 66 % de la courbe des débits classés</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/a-FDC.yaml) &middot; [back to the catalogue](../catalogue.md)
