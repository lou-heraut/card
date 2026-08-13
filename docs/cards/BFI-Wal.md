---
hide:
  - toc
---

# `BFI-Wal`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFI-Wal                                   Baseflow index (Wallingford)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio between mean inter-annual base flow and mean inter-annual flow, the
     base flow being separated from the hydrograph by the smoothed minima
     method (Wallingford)

     phenomenon ─ baseflow
         season ─ record
           form ─ scalar
           unit ─ without unit
          input ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=Wal
            │   └─ Extraction of the base flow (Wallingford)
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           BF-Wal
            ╷
            ├── BFI(Q, BF-Wal)
            │   └─ Calculation of the Base Flow Index (BFI)
            │    ◦ No temporal aggregation
            ▼
           BFI-Wal

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/BFI-Wal.yaml
  https://archive.softwareheritage.org/swh:1:cnt:09676c5346276258419ce22dcf2dd3c266a7ba8c</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFI-Wal                          Indice de débit de base (Wallingford)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport entre débit de base moyen inter-annuel et débit moyen
     inter-annuel, le débit de base étant séparé de l'hydrogramme par la
     méthode des minima lissés (Wallingford)

      phénomène ─ débit de base
         saison ─ chronique
          forme ─ scalaire
          unité ─ sans unité
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── baseflow(Q)
            │   │  method=Wal
            │   └─ Extraction du débit de base (Wallingford)
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           BF-Wal
            ╷
            ├── BFI(Q, BF-Wal)
            │   └─ Calcul du BFI
            │    ◦ Aucune agrégation temporelle
            ▼
           BFI-Wal

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/baseflow/scalar/BFI-Wal.yaml
  https://archive.softwareheritage.org/swh:1:cnt:09676c5346276258419ce22dcf2dd3c266a7ba8c</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#BFI-Wal"><code>BFI-Wal</code></a></dt><dd><span lang="en">Baseflow index (Wallingford)</span><span lang="fr">Indice de débit de base (Wallingford)</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/BFI-Wal.yaml) &middot; [back to the catalogue](../catalogue.md)
