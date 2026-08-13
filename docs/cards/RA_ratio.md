---
hide:
  - toc
---

# `RA_ratio`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA_ratio                                                     2 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ Rl_ratio
       Ratio of liquid to total precipitation

     ◇ Rs_ratio
       Ratio of solid to total precipitation

     phenomenon ─ snow
         season ─ annual
           form ─ scalar
           unit ─ without unit
         inputs ─ R [mm], Rl [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Sum of total precipitation
            ├── RAl = nansum_strict(Rl)
            │   └─ Sum of liquid precipitation
            ├── RAs = nansum_strict(Rs)
            │   └─ Sum of solid precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           RA, RAl, RAs
            ╷
            ├── mean-RA = nanmean(RA)
            │   └─ Inter-annual mean
            ├── mean-RAl = nanmean(RAl)
            │   └─ Inter-annual mean
            ├── mean-RAs = nanmean(RAs)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-RA, mean-RAl, mean-RAs
            ╷
            ├── Rl_ratio = ratio(mean-RAl, mean-RA)
            │   └─ Liquid/total ratio
            ├── Rs_ratio = ratio(mean-RAs, mean-RA)
            │   └─ Solid/total ratio
            │    ◦ No temporal aggregation
            ▼
           Rl_ratio, Rs_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/scalar/RA_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8ec79783e6296d5b7af0e929cea4a45a17174c95</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RA_ratio                                                     2 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ Rl_ratio
       Rapport des précipitations liquides aux précipitations totales

     ◇ Rs_ratio
       Rapport des précipitations solides aux précipitations totales

      phénomène ─ neige
         saison ─ annuelle
          forme ─ scalaire
          unité ─ sans unité
        entrées ─ R [mm], Rl [mm], Rs [mm]

            ╷
            ├── RA = nansum_strict(R)
            │   └─ Somme des précipitations totales
            ├── RAl = nansum_strict(Rl)
            │   └─ Somme des précipitations liquides
            ├── RAs = nansum_strict(Rs)
            │   └─ Somme des précipitations solides
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           RA, RAl, RAs
            ╷
            ├── mean-RA = nanmean(RA)
            │   └─ Moyenne inter-annuelle
            ├── mean-RAl = nanmean(RAl)
            │   └─ Moyenne inter-annuelle
            ├── mean-RAs = nanmean(RAs)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-RA, mean-RAl, mean-RAs
            ╷
            ├── Rl_ratio = ratio(mean-RAl, mean-RA)
            │   └─ Rapport liquide/total
            ├── Rs_ratio = ratio(mean-RAs, mean-RA)
            │   └─ Rapport solide/total
            │    ◦ Aucune agrégation temporelle
            ▼
           Rl_ratio, Rs_ratio

  ──────────────────────────────────────────────────────────────────────────
  v1.1   precipitation/snow/scalar/RA_ratio.yaml
  https://archive.softwareheritage.org/swh:1:cnt:8ec79783e6296d5b7af0e929cea4a45a17174c95</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#Rl_ratio"><code>Rl_ratio</code></a></dt><dd><span lang="en">Ratio of liquid to total precipitation</span><span lang="fr">Rapport des précipitations liquides aux précipitations totales</span><span class="u">without unit</span></dd><dt><a href="../../catalogue/#Rs_ratio"><code>Rs_ratio</code></a></dt><dd><span lang="en">Ratio of solid to total precipitation</span><span lang="fr">Rapport des précipitations solides aux précipitations totales</span><span class="u">without unit</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/precipitation/snow/scalar/RA_ratio.yaml) &middot; [back to the catalogue](../catalogue.md)
