---
hide:
  - toc
---

# `BFI-LH`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFI-LH                               Baseflow index (Lyne and Hollick)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio between mean inter-annual base flow and mean inter-annual flow, the
     base flow being separated from the hydrograph by the Lyne and Hollick
     recursive filter

     phenomenon ─ baseflow
         season ─ record
           form ─ scalar
           unit ─ without unit
          input ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=LH
            │   └─ Extraction of the base flow (Lyne and Hollick)
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           BF-LH
            ╷
            ├── BFI(Q, BF-LH)
            │   └─ Calculation of the Base Flow Index (BFI)
            │    ◦ No temporal aggregation
            ▼
           BFI-LH

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/BFI-LH.yaml
  https://archive.softwareheritage.org/swh:1:cnt:eb4745d629bb3fddb5cf39ca37cb45db777d564d</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFI-LH                       Indice de débit de base (Lyne et Hollick)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport entre débit de base moyen inter-annuel et débit moyen
     inter-annuel, le débit de base étant séparé de l'hydrogramme par le
     filtre récursif de Lyne et Hollick

      phénomène ─ débit de base
         saison ─ chronique
          forme ─ scalaire
          unité ─ sans unité
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=LH
            │   └─ Extraction du débit de base (Lyne et Hollick)
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           BF-LH
            ╷
            ├── BFI(Q, BF-LH)
            │   └─ Calcul du BFI
            │    ◦ Aucune agrégation temporelle
            ▼
           BFI-LH

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/BFI-LH.yaml
  https://archive.softwareheritage.org/swh:1:cnt:eb4745d629bb3fddb5cf39ca37cb45db777d564d</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#BFI-LH"><code>BFI-LH</code></a></dt><dd><span lang="en">Baseflow index (Lyne and Hollick)</span><span lang="fr">Indice de débit de base (Lyne et Hollick)</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/BFI-LH.yaml) &middot; [back to the catalogue](../catalogue.md)
