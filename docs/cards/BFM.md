---
hide:
  - toc
---

# `BFM`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFM                                                 Baseflow magnitude  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Relative amplitude of the inter-annual daily regime of base flow: the gap
     between its maximum and its minimum, divided by the maximum

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
            ├── nanmean(BF-Wal)
            │   └─ Average of the base flow BFA
            │    ◦ One value per day of year
            │    ◦ At most 3 % missing
            ▼
           BFA
            ╷
            ├── BFM(BFA)
            │   └─ Calculation of the base flow magnitude BFM
            │    ◦ No temporal aggregation
            ▼
           BFM

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/baseflow/scalar/BFM.yaml
  https://archive.softwareheritage.org/swh:1:cnt:20cf8811bf948cddcf3b4bad0725e20243d54bde</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  BFM                                         Magnitude du débit de base  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Amplitude relative du régime journalier inter-annuel du débit de base :
     écart entre son maximum et son minimum, rapporté au maximum

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
            ├── nanmean(BF-Wal)
            │   └─ Moyenne du débit de base BFA
            │    ◦ Une valeur par jour de l'année
            │    ◦ Au plus 3 % de lacunes
            ▼
           BFA
            ╷
            ├── BFM(BFA)
            │   └─ Calcul du BFM
            │    ◦ Aucune agrégation temporelle
            ▼
           BFM

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/baseflow/scalar/BFM.yaml
  https://archive.softwareheritage.org/swh:1:cnt:20cf8811bf948cddcf3b4bad0725e20243d54bde</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#BFM"><code>BFM</code></a></dt><dd><span lang="en">Baseflow magnitude</span><span lang="fr">Magnitude du débit de base</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/BFM.yaml) &middot; [back to the catalogue](../catalogue.md)
