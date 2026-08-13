---
hide:
  - toc
---

# `mean-QA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-QA                Inter-annual mean of the annual mean daily flow  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean flows
         season ─ annual
           form ─ scalar
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
            ╷
            ├── nanmean(QA)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-QA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/mean-QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:142bfd1ba6b180c08acd3179220060a4b8bf0ca9</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-QA                   Moyenne inter-annuelle du débit moyen annuel  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ moyennes eaux
         saison ─ annuelle
          forme ─ scalaire
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
            ╷
            ├── nanmean(QA)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-QA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/mean-QA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:142bfd1ba6b180c08acd3179220060a4b8bf0ca9</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#mean-QA"><code>mean-QA</code></a></dt><dd><span lang="en">Inter-annual mean of the annual mean daily flow</span><span lang="fr">Moyenne inter-annuelle du débit moyen annuel</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/mean-QA.yaml) &middot; [back to the catalogue](../catalogue.md)
