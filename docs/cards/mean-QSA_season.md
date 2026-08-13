---
hide:
  - toc
---

# `mean-QSA_season`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-QSA_season                                              4 outputs  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-QSA_DJF
       Inter-annual mean of winter mean daily flows (months of December,
       January and February)

     ◇ mean-QSA_MAM
       Inter-annual mean of spring mean daily flows (months of March, April
       and May)

     ◇ mean-QSA_JJA
       Inter-annual mean of summer mean daily flows (months of June, July and
       August)

     ◇ mean-QSA_SON
       Inter-annual mean of fall mean daily flows (months of September,
       October and November)

     phenomenon ─ mean flows
         season ─ by season
           form ─ scalar
           unit ─ m³·s⁻¹
          input ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Mean
            │    ◦ One value per season of each year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            ▼
           QSA
            ╷
            ├── mean-QSA_DJF = nanmean(QSA_DJF)
            │   └─ Inter-annual mean
            ├── mean-QSA_MAM = nanmean(QSA_MAM)
            │   └─ Inter-annual mean
            ├── mean-QSA_JJA = nanmean(QSA_JJA)
            │   └─ Inter-annual mean
            ├── mean-QSA_SON = nanmean(QSA_SON)
            │   └─ Inter-annual mean
            │    ◦ No temporal aggregation
            ▼
           mean-QSA_DJF, mean-QSA_MAM, mean-QSA_JJA, mean-QSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/mean-QSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:429b125180e763bdf7aa32161b034b7b3b5a02fe</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  mean-QSA_season                                              4 sorties  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     ◇ mean-QSA_DJF (moyenne-QSA_DJF)
       Moyenne inter-annuelle des débits moyens journaliers d'hiver
       Mois de décembre, janvier et février

     ◇ mean-QSA_MAM (moyenne-QSA_MAM)
       Moyenne inter-annuelle des débits moyens journaliers de printemps
       Mois de mars, avril et mai

     ◇ mean-QSA_JJA (moyenne-QSA_JJA)
       Moyenne inter-annuelle des débits moyens journaliers d'été
       Mois de juin, juillet et août

     ◇ mean-QSA_SON (moyenne-QSA_SON)
       Moyenne inter-annuelle des débits moyens journaliers d'automne
       Mois de septembre, octobre et novembre

      phénomène ─ moyennes eaux
         saison ─ par saison
          forme ─ scalaire
          unité ─ m³·s⁻¹
         entrée ─ Q [m³·s⁻¹]

            ╷
            ├── nanmean(Q)
            │   └─ Moyenne
            │    ◦ Une valeur par saison de chaque année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            ▼
           QSA
            ╷
            ├── mean-QSA_DJF = nanmean(QSA_DJF)
            │   └─ Moyenne inter-annuelle
            ├── mean-QSA_MAM = nanmean(QSA_MAM)
            │   └─ Moyenne inter-annuelle
            ├── mean-QSA_JJA = nanmean(QSA_JJA)
            │   └─ Moyenne inter-annuelle
            ├── mean-QSA_SON = nanmean(QSA_SON)
            │   └─ Moyenne inter-annuelle
            │    ◦ Aucune agrégation temporelle
            ▼
           mean-QSA_DJF, mean-QSA_MAM, mean-QSA_JJA, mean-QSA_SON

  ──────────────────────────────────────────────────────────────────────────
  v1.1   flow/mean-flows/scalar/mean-QSA_season.yaml
  https://archive.softwareheritage.org/swh:1:cnt:429b125180e763bdf7aa32161b034b7b3b5a02fe</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#mean-QSA_DJF"><code>mean-QSA_DJF</code></a></dt><dd><span lang="en">Inter-annual mean of winter mean daily flows (months of December, January and February)</span><span lang="fr">Moyenne inter-annuelle des débits moyens journaliers d'hiver</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#mean-QSA_MAM"><code>mean-QSA_MAM</code></a></dt><dd><span lang="en">Inter-annual mean of spring mean daily flows (months of March, April and May)</span><span lang="fr">Moyenne inter-annuelle des débits moyens journaliers de printemps</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#mean-QSA_JJA"><code>mean-QSA_JJA</code></a></dt><dd><span lang="en">Inter-annual mean of summer mean daily flows (months of June, July and August)</span><span lang="fr">Moyenne inter-annuelle des débits moyens journaliers d'été</span><span class="u">m³·s⁻¹</span></dd><dt><a href="../../catalogue/#mean-QSA_SON"><code>mean-QSA_SON</code></a></dt><dd><span lang="en">Inter-annual mean of fall mean daily flows (months of September, October and November)</span><span lang="fr">Moyenne inter-annuelle des débits moyens journaliers d'automne</span><span class="u">m³·s⁻¹</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/mean-flows/scalar/mean-QSA_season.yaml) &middot; [back to the catalogue](../catalogue.md)
