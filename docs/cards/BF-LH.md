---
hide:
  - toc
---

# `BF-LH`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BF-LH                                     Base flow (Lyne and Hollick)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Base flow separated from the hydrograph by the Lyne and Hollick recursive
     filter, in three passes with a parameter of 0.925

     phenomenon ─ baseflow
         season ─ record
           form ─ scalar
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=LH
            │   └─ Extraction of the base flow (Lyne and Hollick)
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           BF-LH

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/scalar/BF-LH.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f16a55665d5f3f82c747e8c6a2aa9bdae3e369ba</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BF-LH                                  Débit de base (Lyne et Hollick)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Débit de base séparé de l'hydrogramme par le filtre récursif de Lyne et
     Hollick, en trois passes avec un paramètre de 0,925

      phénomène ─ débit de base
         saison ─ chronique
          forme ─ scalaire
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=LH
            │   └─ Extraction du débit de base (Lyne et Hollick)
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           BF-LH

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/baseflow/scalar/BF-LH.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f16a55665d5f3f82c747e8c6a2aa9bdae3e369ba</pre>

**Variables produced**  [`BF-LH`](../catalogue.md#BF-LH)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/BF-LH.yaml) &middot; [back to the catalogue](../catalogue.md)
