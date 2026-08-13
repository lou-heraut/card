---
hide:
  - toc
---

# `RAT_ET0`

The card as `card.info()` prints it, as `card4r` prints it, and as card-api serves it. One drawing, read in three places.

<div class="cat-controls cat-controls--lang">
<label>labels<select id="cat-lang"><option value="en">English</option><option value="fr">Français</option></select></label>
</div>

<pre class="fig" lang="en" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAT_ET0                    Robustness test to a variation in reference  │
  │                                                      evapotranspiration  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     True when the model bias is correlated with the reference
     evapotranspiration, in the sense of a Spearman correlation significant at
     the 5 % level: performance then depends on that variable, so the model
     does not behave the same everywhere

         season ─ annual
           form ─ scalar
        purpose ─ climate sensitivity
           unit ─ bool
         inputs ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹], ET0_obs [mm]

            ╷
            ├── BiasA = bias(Q_obs, Q_sim)
            │   └─ Relative bias of simulated vs observed flow
            ├── ET0A = nanmean(ET0_obs)
            │   └─ Mean reference evapotranspiration
            │    ◦ One value per year
            │    ◦ At most 3 % missing
            │    ◦ Cut beyond 10 missing years
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Window from 09-01 to 08-31
            ▼
           BiasA, ET0A
            ╷
            ├── RAT(BiasA, ET0A)
            │   └─ RAT with a 5 % significance level
            │    ◦ No temporal aggregation
            ▼
           RAT_ET0

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/RAT_ET0.yaml
  https://archive.softwareheritage.org/swh:1:cnt:4b2cfe98c96ddda8e6afbb2ac70b6c84836161b5</pre>
<pre class="fig" lang="fr" data-search-exclude>  ╭──────────────────────────────────────────────────────────────────────────╮
  │  RAT_ET0     Test de robustesse à une variation d'évapotranspiration de  │
  │                                                               référence  │
  ╰──────────────────────────────────────────────────────────────────────────╯

     Vrai quand le biais du modèle est corrélé à l'évapotranspiration de
     référence, au sens d'une corrélation de Spearman significative au seuil
     de 5 % : la performance dépend alors de cette variable, donc le modèle ne
     se comporte pas de la même façon partout

         saison ─ annuelle
          forme ─ scalaire
       finalité ─ sensibilité climatique
          unité ─ bool
        entrées ─ Q_obs [m³·s⁻¹], Q_sim [m³·s⁻¹], ET0_obs [mm]

            ╷
            ├── BiasA = bias(Q_obs, Q_sim)
            │   └─ Biais relatif entre débits simulés et observés
            ├── ET0A = nanmean(ET0_obs)
            │   └─ Évapotranspiration de référence moyenne
            │    ◦ Une valeur par année
            │    ◦ Au plus 3 % de lacunes
            │    ◦ Coupée au-delà de 10 années manquantes
            │    ◦ J  F  M  A  M  J  J  A  S  O  N  D  
            │      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓┃▓▓▓▓▓▓▓▓▓▓▓
            │      Fenêtre du 01-09 au 31-08
            ▼
           BiasA, ET0A
            ╷
            ├── RAT(BiasA, ET0A)
            │   └─ RAT avec un seuil de significativité de 5 %
            │    ◦ Aucune agrégation temporelle
            ▼
           RAT_ET0

  ──────────────────────────────────────────────────────────────────────────
  v2.0   flow/climate-sensitivity/scalar/RAT_ET0.yaml
  https://archive.softwareheritage.org/swh:1:cnt:4b2cfe98c96ddda8e6afbb2ac70b6c84836161b5</pre>

**Variables produced**  [`RAT_ET0`](../catalogue.md#RAT_ET0)

[The card itself, on GitHub](https://github.com/lou-heraut/card/blob/main/src/card/cards/flow/climate-sensitivity/scalar/RAT_ET0.yaml) &middot; [back to the catalogue](../catalogue.md)
