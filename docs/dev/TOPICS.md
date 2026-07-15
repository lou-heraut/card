# TOPICS — Facettes à vocabulaire contrôlé pour les fiches CARD

> Proposition du 2026-07-16, arbitrée le jour même avec l'utilisateur
> (slugs de forme series/scalar/curve, bloc `classification:`,
> Ratio et Occurrence fondus, a-FDC→magnitude, `regime: general`
> explicite, champ `topic` supprimé à la migration). Prêt à appliquer ;
> trois cas de migration marqués « à confirmer » (§3).
> Remplace le champ libre bilingue `topic: "Flow, Low Flows,
> Seasonality"` par des facettes en slugs neutres, avec un vocabulaire
> central unique (labels en/fr générés, plus de dérive par fiche).
> Objectif : regrouper/trier les fiches pour des groupements
> d'analyse, et s'aligner sur un standard (IHA/EFC).

## 1. Le modèle

```yaml
meta:
  global:
    classification:
      domain: flow            # grandeur concernée (liste si plusieurs)
      regime: low-flows       # condition visée ; 'general' si aucune
      aspect: timing          # dimension analysée, typologie IHA
      output: series          # forme du résultat : series | scalar | curve
      purpose: performance    # seule ligne optionnelle (défaut : description)

# Règle de complétude (vérifiée par le linter) :
#  - fiches descriptives : domain, regime, aspect, output tous requis
#    (regime: general si pas de condition particulière) ;
#  - purpose présent (performance | sensitivity) : regime et aspect
#    INTERDITS — la ligne purpose explique leur absence.
```

- Les slugs sont **anglais, kebab-case, langue-neutres** : la fiche ne
  porte plus aucun libellé de topic. Les labels affichés (en/fr),
  définitions et correspondances externes vivent dans **un fichier
  unique** `src/card/topics.yaml` — une seule source de vérité (les
  ~15 bugs de topics trouvés pendant la conversion venaient tous de la
  duplication en/fr par fiche).
- `card.list_cards()` expose chaque facette en colonne → filtrage
  direct (`domain="flow", aspect="duration"`), et le catalogue
  `CARDS.md` gagne les colonnes correspondantes (dont **output**,
  aujourd'hui invisible : la moitié de l'arborescence n'a pas de
  dossiers serie/criteria, et le dossier classe mal FDC/QJC10).
- L'**opérateur** (delta, tendance, médiane inter-annuelle...) n'est
  PAS une facette stockée : il est dérivé du préfixe de l'id (grammaire
  NOMENCLATURE.md) et exposé comme colonne calculée de `list_cards()`.

## 2. Les facettes et leur vocabulaire

### domain — la grandeur (liste autorisée)

| Slug | en | fr |
|---|---|---|
| flow | Flow | Débit |
| precipitation | Precipitation | Précipitations |
| temperature | Temperature | Température |
| evapotranspiration | Evapotranspiration | Évapotranspiration |

Les fiches de sensibilité croisée déclarent une liste :
`domain: [flow, precipitation]` (ex. QR_ratio, epsilon_R, RAT_R).

### regime — la condition visée (optionnel : omis quand sans objet)

| Slug | en | fr | Couvre les topics actuels |
|---|---|---|---|
| low-flows | Low flows | Basses eaux | Low Flows |
| mean-flows | Mean flows | Moyennes eaux | Mean Flows |
| high-flows | High flows | Hautes eaux | High Flows |
| baseflow | Baseflow | Débit de base | Baseflow / Base Flow (unifiés) |
| dry-spells | Dry spells | Périodes sèches | Dry Period |
| light-rain | Light rain | Pluies faibles | Low (précip) |
| heavy-rain | Heavy rain | Pluies fortes | Heavy |
| general | General | Général | Moderate (précip), Average/Mean (temp., ETP) — pas de condition particulière |

`regime: general` est écrit explicitement (décision 2026-07-16 : une
ligne absente ne distingue pas « sans objet » d'« oublié »). Seules les
fiches performance/sensibilité n'ont pas de regime (interdit, justifié
par la ligne `purpose`).

### aspect — la dimension analysée (typologie IHA/EFC ; optionnel)

Ancrage : *Indicators of Hydrologic Alteration* (Richter et al. 1996 ;
Olden & Poff 2003) — magnitude, timing, duration, frequency, rate of
change.

| Slug | en | fr | Couvre les topics actuels |
|---|---|---|---|
| magnitude | Magnitude | Intensité | Intensity, Ratio, Parameterization (a-FDC — la pente de la FDC est un indicateur de variabilité, classé magnitude comme en IHA) |
| timing | Timing | Saisonnalité | Seasonality |
| duration | Duration | Durée | Duration |
| frequency | Frequency | Fréquence | Frequency, Occurrence (n-* : décomptes d'années) |
| rate-of-change | Rate of change | Taux de variation | (aucune fiche actuelle — réservé) |

`aspect` requis pour toutes les fiches descriptives ; interdit quand
`purpose` est présent (performance, sensibilité).

### output — la forme du résultat (obligatoire, nouvelle information)

| Slug | en | fr | Définition | Usage type |
|---|---|---|---|---|
| series | Series | Série | une valeur par pas de temps (année, mois, saison) | analyse de tendance |
| scalar | Scalar | Scalaire | un seul nombre par station | comparaison en carte |
| curve | Curve | Courbe | résultat indexé par autre chose que le temps (jour de l'année, probabilité) | tracé de régime ou de courbe classée |

Exemples : QA/VCN10/QMA_month → series ; delta-*/median-*/KGE/QMNA-5 →
scalar ; FDC*/QJC10/median-QJ* → curve. Contrôle de cohérence
facette↔process ajouté au linter (`python -m card.schema`).

### purpose — la finalité (optionnel, défaut `description`)

| Slug | en | fr | Fiches |
|---|---|---|---|
| (description) | — | — | défaut, omis — décrire le comportement observé |
| performance | Model performance | Performance de modèle | NSE*, KGE*, Bias*, STD_ratio, CR, CRS_season |
| sensitivity | Climate sensitivity | Sensibilité climatique | epsilon_*, RAT_*, QR_ratio, Rc futur |

## 3. Migration (table complète à générer au moment de l'application)

Les chaînes actuelles se projettent mécaniquement :

| Topic actuel (en) | domain | regime | aspect | purpose |
|---|---|---|---|---|
| Flow, Low/Mean/High Flows, X | flow | low/mean/high-flows | X | — |
| Flow, Baseflow ou Base Flow, X | flow | baseflow | X | — |
| Flow, Performance | flow | (interdit) | (interdit) | performance |
| Flow / Precipitations, Sensitivity... | [flow, precipitation] | (interdit) | (interdit) | sensitivity |
| Precipitations, Moderate, X | precipitation | general | X | — |
| Precipitations, Heavy/Low, Duration | precipitation | heavy-rain / light-rain | duration | — |
| Precipitations, Dry Period, Duration | precipitation | dry-spells | duration | — |
| Temperature, Average/Mean, Intensity | temperature | general | magnitude | — |
| Evapotranspiration, Average, Intensity | evapotranspiration | general | magnitude | — |

`output` est attribué fiche par fiche (dérivable du process à ~95 %,
vérifié à la main pour FDC/QJC/median-QJ : `curve`). Les bundles multi-variables
(topic en liste aujourd'hui) prennent des facettes en listes seulement
si les variables diffèrent (règle C2 amendée).

**Cas à confirmer à la migration** (proposition + relecture) :

1. dtRA01mm / dtRMA01mm_month / dtRSA01mm_season : « Low » actuel, mais
   le calcul compte TOUS les jours pluvieux (≥ 1 mm) — proposition :
   `regime: general` plutôt que `light-rain` (à confirmer, voire créer
   `wet-days` si tu veux la symétrie avec dry-spells).
2. Précipitations solides/liquides (RAs, RAl, RMAs_month, RAs_ratio...) :
   `regime: general` (la distinction solide/liquide est portée par la
   variable) ou slug `snow` pour les solides — à confirmer.
3. Fiches à cheval (mean-RA, RA_ratio) : purpose absent (descriptives)
   malgré leur usage en diagnostic — confirmé descriptives.

## 4. Arbitrages (rendus le 2026-07-16, sauf §4.6)

1. **Ratio → `magnitude`** (pas de slug hors IHA).
2. **Occurrence → `frequency`** (décompte d'années de dépassement).
3. **Parameterization (a-FDC) → `magnitude`** : la pente de la courbe
   des débits classés mesure la variabilité des débits, classée avec
   la magnitude comme en IHA.
4. **Régime sans objet = `regime: general` explicite** (révisé le
   2026-07-16 : l'absence de ligne ne distingue pas « sans objet »
   d'« oublié ») ; regime/aspect interdits quand `purpose` est présent,
   le linter vérifie la complétude.
5. **Bloc regroupé**, nommé **`classification:`** (transparent dans
   les deux langues ; « topics » ne décrivait plus des facettes).
6. **Le champ `topic` est supprimé à la migration** : toute
   l'information vient de `classification` (labels en/fr générés depuis
   le vocabulaire central pour le catalogue et card.info).
