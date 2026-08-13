---
hide:
  - toc
---

# `mean-RA`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RA            Inter-annual mean of the annual total precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     phenomenon ─ mean precipitation
         season ─ annual
           form ─ scalar
           unit ─ mm
          input ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Sum
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA
            ╷
            ├── nanmean(RA)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/scalar/mean-RA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f9e9a1d3e9ccbe84fe4f4aaf7df988855ce62132</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-RA      Moyenne inter-annuelle du cumul annuel des précipitations  │
  │                                                                 totales  │
  ╰──────────────────────────────────────────────────────────────────────────╯

      phénomène ─ précipitations moyennes
         saison ─ annuelle
          forme ─ scalaire
          unité ─ mm
         entrée ─ R [mm]

            ╷
            ├── nansum_strict(R)
            │   └─ Somme
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA
            ╷
            ├── nanmean(RA)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RA

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/mean-precipitation/scalar/mean-RA.yaml
  https://archive.softwareheritage.org/swh:1:cnt:f9e9a1d3e9ccbe84fe4f4aaf7df988855ce62132</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#mean-RA"><code>mean-RA</code></a></dt><dd><span lang="en">Inter-annual mean of the annual total precipitation</span><span lang="fr">Moyenne inter-annuelle du cumul annuel des précipitations totales</span><span class="u">mm</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/mean-precipitation/scalar/mean-RA.yaml) &middot; [back to the catalogue](../catalogue.md)
