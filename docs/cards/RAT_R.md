---
hide:
  - toc
---

# `RAT_R`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAT_R                  Robustness test to a variation in precipitation  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     True when the model bias is correlated with precipitation, in the sense
     of a Spearman correlation significant at the 5 % level: performance then
     depends on that variable, so the model does not behave the same
     everywhere

         season ─ annual
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ bool
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹], R_obs [mm]

            ╷
            ├── BiasA = bias(Q_obs, Q_sim)
            │   └─ Relative bias of simulated vs observed flow
            ├── RA-mean = nanmean(R_obs)
            │   └─ Mean precipitation
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           BiasA, RA-mean
            ╷
            ├── RAT(BiasA, RA-mean)
            │   └─ RAT with a 5 % significance level
            │    ◦ No temporal aggregation
            ▼
           RAT_R

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/RAT_R.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a848c82a28f2d400e2ad1be80ec3a450b9c7fa2d</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAT_R             Test de robustesse à une variation de précipitations  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Vrai quand le biais du modèle est corrélé aux précipitations, au sens
     d'une corrélation de Spearman significative au seuil de 5 % : la
     performance dépend alors de cette variable, donc le modèle ne se comporte
     pas de la même façon partout

         saison ─ annuelle
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ bool
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹], R_obs [mm]

            ╷
            ├── BiasA = bias(Q_obs, Q_sim)
            │   └─ Biais relatif entre débits simulés et observés
            ├── RA-mean = nanmean(R_obs)
            │   └─ Précipitations moyennes
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           BiasA, RA-mean
            ╷
            ├── RAT(BiasA, RA-mean)
            │   └─ RAT avec un seuil de significativité de 5 %
            │    ◦ Aucune agrégation temporelle
            ▼
           RAT_R

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/RAT_R.yaml
  https://archive.softwareheritage.org/swh:1:cnt:a848c82a28f2d400e2ad1be80ec3a450b9c7fa2d</pre>

**Variables produced**

<dl class="card-vars"><dt><a href="../../catalogue/#RAT_R"><code>RAT_R</code></a></dt><dd><span lang="en">Robustness test to a variation in precipitation</span><span lang="fr">Test de robustesse à une variation de précipitations</span><span class="u">bool</span></dd></dl>

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/RAT_R.yaml) &middot; [back to the catalogue](../catalogue.md)
