# TOPICS — Facettes à vocabulaire contrôlé pour les fiches CARD

> Proposition du 2026-07-16, arbitrée le jour même avec l'utilisateur
> (slugs de forme series/scalar/curve, bloc `classification:`,
> Ratio et Occurrence fondus, a-FDC→magnitude, régime sans objet =
> pas de ligne). **Reste ouvert : §4.6** (sort du champ `topic`
> actuel).
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
      regime: low-flows       # condition hydro-climatique visée (pas de ligne si sans objet)
      aspect: timing          # dimension analysée, typologie IHA (pas de ligne si sans objet)
      output: series          # forme du résultat : series | scalar | curve
      purpose: performance    # pas de ligne si simple description (défaut)
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

Pas de ligne `regime:` quand il n'y a pas de condition particulière :
précip « Moderate », température « Average/Mean », évapotranspiration,
performance, sensibilité (même logique que la règle des défauts,
NOMENCLATURE Règle 5 / CLAUDE.md).

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

Pas de ligne `aspect:` pour les fiches performance.

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
| Flow, Performance | flow | — | — | performance |
| Flow / Precipitations, Sensitivity... | [flow, precipitation] | — | — | sensitivity |
| Precipitations, Moderate, X | precipitation | — | X | — |
| Precipitations, Heavy/Low, Duration | precipitation | heavy-rain / light-rain | duration | — |
| Precipitations, Dry Period, Duration | precipitation | dry-spells | duration | — |
| Temperature, Average/Mean, Intensity | temperature | — | magnitude | — |
| Evapotranspiration, Average, Intensity | evapotranspiration | — | magnitude | — |

`output` est attribué fiche par fiche (dérivable du process à ~95 %,
vérifié à la main pour FDC/QJC/median-QJ : `curve`). Les bundles multi-variables
(topic en liste aujourd'hui) prennent des facettes en listes seulement
si les variables diffèrent (règle C2 amendée).

## 4. Arbitrages (rendus le 2026-07-16, sauf §4.6)

1. **Ratio → `magnitude`** (pas de slug hors IHA).
2. **Occurrence → `frequency`** (décompte d'années de dépassement).
3. **Parameterization (a-FDC) → `magnitude`** : la pente de la courbe
   des débits classés mesure la variabilité des débits, classée avec
   la magnitude comme en IHA.
4. **Régime sans objet = pas de ligne** (cohérent avec la règle des
   défauts), pas de slug `general`.
5. **Bloc regroupé**, nommé **`classification:`** (transparent dans
   les deux langues ; « topics » ne décrivait plus des facettes).
6. ⚠️ **Ouvert** — le champ `topic` actuel : supprimé, ou conservé en
   lecture seule (généré depuis les facettes) pendant une transition ?
