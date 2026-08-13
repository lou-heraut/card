---
hide:
  - toc
---

# `delta-BFI-Wal_H`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-BFI-Wal_H       Average change of the baseflow index between the  │
  │                      target horizon and historical period (Wallingford)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Ratio between mean inter-annual base flow and mean inter-annual flow, the
     base flow being separated from the hydrograph by the smoothed minima
     method (Wallingford)

     phenomenon ─ baseflow
         season ─ record
           form ─ scalar
           unit ─ without unit
         inputs ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── baseflow(Q)
            │   │  method=Wal
            │   └─ Extraction of the base flow (Wallingford)
            │    ◦ One value per day
            │    ◦ Cut beyond 10 missing years
            ▼
           BF-Wal
            ╷
            ├── delta(BF-Wal, date)
            │   │  relative=False
            │   │  from ref_start, ref_end, horizon_start, horizon_end, Q
            │   └─ Calculation of the BFI change between the historical period
            │      and the target horizon
            │    ◦ No temporal aggregation
            ▼
           delta-BFI-Wal

     ◇ compares two windows, supplied as columns:
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/baseflow/scalar/delta-BFI-Wal_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:4267b9f632cc63ed3ae57184fc981395cb3cfc0b</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  delta-BFI-Wal_H    Changement moyen de l'indice de débit de base entre  │
  │                                l'horizon cible et la période historique  │
  │                                                           (Wallingford)  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Rapport entre débit de base moyen inter-annuel et débit moyen
     inter-annuel, le débit de base étant séparé de l'hydrogramme par la
     méthode des minima lissés (Wallingford)

      phénomène ─ débit de base
         saison ─ chronique
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ Q [m³·s⁻¹], ref_start, ref_end, horizon_start, horizon_end

            ╷
            ├── baseflow(Q)
            │   │  method=Wal
            │   └─ Extraction du débit de base (Wallingford)
            │    ◦ Une valeur par jour
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           BF-Wal
            ╷
            ├── delta(BF-Wal, date)
            │   │  relative=False
            │   │  d'après ref_start, ref_end, horizon_start, horizon_end, Q
            │   └─ Calcul du changement de BFI entre la période historique et
            │      l'horizon cible
            │    ◦ Aucune agrégation temporelle
            ▼
           delta-BFI-Wal

     ◇ compare deux fenêtres, fournies en colonnes :
       ├─ ref_start ─── ref_end ─┤
                           ├─ horizon_start ─── horizon_end ─┤

  ──────────────────────────────────────────────────────────────────────────
  v1.2   flow/baseflow/scalar/delta-BFI-Wal_H.yaml
  https://archive.softwareheritage.org/swh:1:cnt:4267b9f632cc63ed3ae57184fc981395cb3cfc0b</pre>

**Variables produced**  [`delta-BFI-Wal`](../catalogue.md#delta-BFI-Wal)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/baseflow/scalar/delta-BFI-Wal_H.yaml) &middot; [back to the catalogue](../catalogue.md)
