---
hide:
  - toc
---

# `QSA_JJASO`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QSA_JJASO             Annual mean daily discharge from June to October  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean flows
         season ─ summer
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
            │      ···············┃▓▓▓▓▓▓▓▓▓▓▓▓▓┃······
            │      Partial window, from 06-01 to 10-31
            ▼
           QSA_JJASO

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QSA_JJASO.yaml
  https://archive.softwareheritage.org/swh:1:cnt:55328e9c7a43399ccb3705073725282e557484ca</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  QSA_JJASO       Moyenne annuelle du débit journalier de juin à octobre  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ moyennes eaux
         saison ─ estivale
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
            │      ···············┃▓▓▓▓▓▓▓▓▓▓▓▓▓┃······
            │      Fenêtre partielle, du 01-06 au 31-10
            ▼
           QSA_JJASO

  ──────────────────────────────────────────────────────────────────────────
  v1.0   flow/mean-flows/series/QSA_JJASO.yaml
  https://archive.softwareheritage.org/swh:1:cnt:55328e9c7a43399ccb3705073725282e557484ca</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#QSA_JJASO"><code>QSA_JJASO</code></a></dt><dd><span lang="en">Annual mean daily discharge from June to October</span><span lang="fr">Moyenne annuelle du débit journalier de juin à octobre</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/series/QSA_JJASO.yaml) &middot; [back to the catalogue](../catalogue.md)
