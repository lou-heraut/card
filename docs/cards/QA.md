---
hide:
  - toc
---

# `QA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QA                                         Annual mean daily discharge  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean flows
         season ─ annual
           form ─ series
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           QA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f87e5d44869458c5bf47af3bbc98665de2b1deee</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QA                                Moyenne annuelle du débit journalier  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ moyennes eaux
         saison ─ annuelle
          forme ─ série
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           QA

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f87e5d44869458c5bf47af3bbc98665de2b1deee</pre>

**Variables produced**  [`QA`](../catalogue.md#QA)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/series/QA.yaml) &middot; [back to the catalogue](../catalogue.md)
