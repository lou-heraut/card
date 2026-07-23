> **Statut : norme en vigueur.** Modèle de classification et vocabulaire
> autorisé. Le vocabulaire exécutable est `src/card/topics.yaml`, vérifié
> par le linter ; ce document en porte le modèle et les arbitrages.

# TOPICS : Facettes à vocabulaire contrôlé pour les fiches CARD

> Proposition du 2026-07-16, arbitrée le jour même avec l'utilisateur
> en plusieurs itérations. Modèle final : **labels bilingues dans les
> fiches** (autoportantes, plot-direct), validés par le linter contre
> le vocabulaire central à ensembles fermés ; 4 axes contrôlés +
> purpose + tags libres-recommandés ; `regime` abandonné au profit des
> tags ; nouvel axe `season` (position 4 d'Oberlin) ; champ `topic`
> supprimé à la migration. Prêt à appliquer après relecture de la
> table de migration.
> Remplace le champ libre bilingue `topic: "Flow, Low Flows,
> Seasonality"` par des facettes en slugs neutres, avec un vocabulaire
> central unique (labels en/fr générés, plus de dérive par fiche).
> Objectif : regrouper/trier les fiches pour des groupements
> d'analyse, et s'aligner sur un standard (IHA/EFC).

## 1. Le modèle

Un bloc `classification` dans **chaque bloc de langue** (`meta.en`,
`meta.fr`), avec les labels de la langue ; les fiches restent
autoportantes et les métadonnées d'extraction (metaEX) sont
directement traçables sur les graphiques, comme le reste des
métadonnées bilingues :

```yaml
meta:
  en:
    classification:
      domain: flow            # grandeur (liste si plusieurs)
      phenomenon: low flows   # phénomène visé (scalaire, liste si multiple, absent si aucun)
      aspect: timing          # dimension analysée (typologie IHA)
      season: annual          # fenêtre d'échantillonnage (Oberlin pos. 4)
      output: series          # forme du résultat
  fr:
    classification:
      domain: débit
      phenomenon: basses eaux
      aspect: saisonnalité
      season: annuelle
      output: série
```

Convention thésaurus : **tout en minuscules** (les outils d'affichage
capitalisent au besoin).

- **Doctrine à trois niveaux** : rédigé (name/description/method) =
  bilingue libre ; classifié (classification) = bilingue **validé** ;
  technique (input_vars, func, palette) = neutre non traduit.
- **Le vocabulaire central `src/card/topics.yaml` est la référence de
  contrôle**, pas une jointure : il liste, pour chaque concept, la
  paire (label_en, label_fr), la définition et l'ancrage externe
  (IHA, ETCCDI). Le linter vérifie chaque valeur ET l'appariement
  en/fr entre les deux blocs : une divergence (la cause des ~15 bugs
  de l'ancien `topic` en texte libre) devient une erreur de lint,
  plus jamais un bug silencieux.
- **Règle de complétude** (linter) : `domain`, `aspect`, `season`,
  `output` requis pour les fiches descriptives ; `purpose`
  (performance | sensitivity) optionnel : s'il est présent, `aspect`
  est interdit (la ligne purpose explique son absence) ; `tags` libre
  (0..n).
- `card.list_cards()` expose chaque facette en colonne dans les deux
  langues → filtrage dans sa langue (`aspect="Intensité"` ou
  `aspect="Magnitude"`), y compris `tags` (appartenance). Le catalogue
  CARDS.md gagne les colonnes correspondantes (dont **output**,
  aujourd'hui invisible : la moitié de l'arborescence n'a pas de
  dossiers serie/criteria, et le dossier classe mal FDC/QJC10).
- L'**opérateur** (delta, tendance, médiane inter-annuelle...) n'est
  PAS une facette stockée : il est dérivé du préfixe de l'id (grammaire
  NOMENCLATURE.md) et exposé comme colonne calculée de `list_cards()`.

## 2. Les facettes et leur vocabulaire

### domain : la grandeur (liste autorisée)

| Slug | en | fr |
|---|---|---|
| flow | Flow | Débit |
| precipitation | Precipitation | Précipitations |
| temperature | Temperature | Température |
| evapotranspiration | Evapotranspiration | Évapotranspiration |

Les fiches de sensibilité croisée déclarent une liste :
`domain: [flow, precipitation]` (ex. QR_ratio, epsilon_R, RAT_R).

### phenomenon : le phénomène hydro-climatique visé (scalaire ou liste)

L'ex-« régime », correctement nommé : basses eaux, débit de base,
périodes sèches, neige... sont des **phénomènes**, mot valable pour
tous les domaines. Champ scalaire dans le cas courant, **liste si une
fiche relève réellement de plusieurs phénomènes** (même polymorphisme
que name/palette ; ex. futur : fonte des neiges → `[neige, hautes
eaux]`), **absent uniquement quand un `purpose` prend sa place** (les
scores de performance et de sensibilité climatique ne sont pas des
régimes hydro-climatiques). Le vocabulaire est fermé et le linter
contrôle les valeurs.

**Toute variate a désormais un phénomène** (décision du 2026-07-24,
pour ranger le corpus par régime observé, cf. `phenomenon` en tête du
chemin des dossiers et du catalogue). La magnitude moyenne de chaque
domaine est un phénomène à part entière, pendant de « moyennes eaux »
côté débit : les cumuls de pluie, les températures moyennes et la
demande évaporative avaient l'air « sans régime » seulement parce que le
corpus est mince pour ces domaines.

| en | fr | Couvre les topics actuels | Domaine typique |
|---|---|---|---|
| low flows | basses eaux | Low Flows | flow |
| mean flows | moyennes eaux | Mean Flows | flow |
| high flows | hautes eaux | High Flows | flow |
| baseflow | débit de base | Baseflow / Base Flow (unifiés) | flow |
| dry spells | périodes sèches | Dry Period | precipitation |
| wet days | jours pluvieux | Low (précip ≥ 1 mm, reclassé) | precipitation |
| heavy rain | pluies fortes | Heavy | precipitation |
| snow | neige | précip solides Rs/RAs, fractions liquide/solide | precipitation |
| mean precipitation | précipitations moyennes | cumuls RA/RMA/RSA (ex-sans-phénomène) | precipitation |
| mean temperatures | températures moyennes | TA/TMA/TSA (ex-sans-phénomène) | temperature |
| evaporative demand | demande évaporative | ETPA/ETPMA/ETPSA (ex-sans-phénomène) | evapotranspiration |

Places réservées mais vides tant qu'aucune fiche ne les peuple :
extrêmes de température (fortes chaleurs, gel) par analogie avec les
pluies fortes et les périodes sèches. La grille anticipe, on n'ajoute au
vocabulaire que ce qui a des fiches.

### aspect : la dimension analysée (typologie IHA/EFC ; optionnel)

Ancrage : *Indicators of Hydrologic Alteration* (Richter et al. 1996 ;
Olden & Poff 2003) : magnitude, timing, duration, frequency, rate of
change.

| Slug | en | fr | Couvre les topics actuels |
|---|---|---|---|
| magnitude | Magnitude | Intensité | Intensity, Ratio, Parameterization (a-FDC : la pente de la FDC est un indicateur de variabilité, classé magnitude comme en IHA) |
| timing | Timing | Saisonnalité | Seasonality |
| duration | Duration | Durée | Duration |
| frequency | Frequency | Fréquence | Frequency, Occurrence (n-* : décomptes d'années) |
| rate-of-change | Rate of change | Taux de variation | (aucune fiche actuelle, réservé) |

`aspect` requis pour toutes les fiches descriptives ; interdit quand
`purpose` est présent (performance, sensibilité).

### season : la fenêtre d'échantillonnage (obligatoire ; position 4 d'Oberlin)

Axe fermé, une valeur par fiche, déterminable mécaniquement depuis le
process :

| en | fr | Définition | Exemples |
|---|---|---|---|
| Annual | Annuelle | fenêtre annuelle, fixe ou adaptative | QA, VCN10, QJXA, RCXA1 |
| Summer | Estivale | fenêtre saisonnière fixe côté été | VCN10_summer, QSA_JJASO |
| Winter | Hivernale | fenêtre saisonnière fixe côté hiver | QNA_winter |
| By season | Par saison | fan-out 4 saisons DJF/MAM/JJA/SON | QSA_season, TSA_season |
| By month | Par mois | fan-out 12 mois | QMA_month, RMA_month |
| Record | Chronique | chronique entière, pas de découpage | Q90, FDC, KGE, deltas _H |

### output : la forme du résultat (obligatoire, nouvelle information)

| Slug | en | fr | Définition | Usage type |
|---|---|---|---|---|
| series | Series | Série | une valeur par pas de temps (année, mois, saison) | analyse de tendance |
| scalar | Scalar | Scalaire | un seul nombre par station | comparaison en carte |
| curve | Curve | Courbe | résultat indexé par autre chose que le temps (jour de l'année, probabilité) | tracé de régime ou de courbe classée |

Exemples : QA/VCN10/QMA_month → series ; delta-*/median-*/KGE/QMNA-5 →
scalar ; FDC*/QJC10/median-QJ* → curve. Contrôle de cohérence
facette↔process ajouté au linter (`python -m card.schema`).

### purpose : la finalité (optionnel, défaut `description`)

| Slug | en | fr | Fiches |
|---|---|---|---|
| (description) |  |  | défaut, omis : décrit le comportement observé |
| performance | Model performance | Performance de modèle | NSE*, KGE*, Bias*, STD_ratio, CR, CRS_season |
| sensitivity | Climate sensitivity | Sensibilité climatique | epsilon_*, RAT_*, QR_ratio, Rc futur |

## 3. Migration (table complète à générer au moment de l'application)

Les chaînes actuelles se projettent mécaniquement :

| Topic actuel (en) | domain | tags | aspect | purpose |
|---|---|---|---|---|
| Flow, Low/Mean/High Flows, X | Flow | [Low/Mean/High flows] | X |  |
| Flow, Baseflow ou Base Flow, X | Flow | [Baseflow] | X |  |
| Flow, Performance | Flow | [] | (interdit) | Model performance |
| Flow / Precipitations, Sensitivity... | [Flow, Precipitation] | [] | (interdit) | Climate sensitivity |
| Precipitations, Moderate, X | Precipitation | [] | X |  |
| Precipitations, Heavy, X | Precipitation | [Heavy rain] | X |  |
| Precipitations, Low, Duration | Precipitation | [Wet days] | Duration |  |
| Precipitations, Dry Period, Duration | Precipitation | [Dry spells] | Duration |  |
| Rs/RAs/RMAs (précip solides) | Precipitation | [Snow] | selon fiche |  |
| Temperature, Average/Mean, Intensity | Temperature | [] | Magnitude |  |
| Evapotranspiration, Average, Intensity | Evapotranspiration | [] | Magnitude |  |

(labels anglais montrés ; les blocs fr reçoivent les labels français
appariés du vocabulaire ; `season` et `output` attribués fiche par
fiche depuis le process)

`output` est attribué fiche par fiche (dérivable du process à ~95 %,
vérifié à la main pour FDC/QJC/median-QJ : `curve`). Les bundles multi-variables
(topic en liste aujourd'hui) prennent des facettes en listes seulement
si les variables diffèrent (règle C2 amendée).

**Les trois cas jadis ambigus sont résolus par la nature des tags**
(multiples, non forcés) : dtRA*01mm → [Wet days] ; précipitations
solides → [Snow] ; mean-RA / RA_ratio → descriptives sans purpose.
La table complète fiche par fiche sera générée et soumise à relecture
avant application.

## 4. Arbitrages (rendus le 2026-07-16, sauf §4.6)

1. **Ratio → `magnitude`** (pas de slug hors IHA).
2. **Occurrence → `frequency`** (décompte d'années de dépassement).
3. **Parameterization (a-FDC) → `magnitude`** : la pente de la courbe
   des débits classés mesure la variabilité des débits, classée avec
   la magnitude comme en IHA.
4. **`regime` abandonné comme axe** (révisé deux fois le 2026-07-16,
   décision finale) : ce n'était pas une facette mais un mélange :
   remplacé par **`tags`**, mots-clés multiples non forcés à
   vocabulaire recommandé ; le filtre par « régime » reste un filtre
   par tag, et une fiche peut appartenir à plusieurs groupes.
5. **Bloc regroupé**, nommé **`classification:`** (transparent dans
   les deux langues ; « topics » ne décrivait plus des facettes).
7. **Labels bilingues DANS les fiches** (décision finale 2026-07-16) :
   les fiches restent autoportantes et les métadonnées d'extraction
   directement traçables (but historique du bilinguisme) ; la sûreté
   vient du vocabulaire fermé + lint d'appariement en/fr, pas de la
   centralisation du stockage. topics.yaml = référence de contrôle.
8. **Nouvel axe `season`** (fenêtre d'échantillonnage, position 4
   d'Oberlin) : annual, summer, winter, by season, by month, record :
   fermé, mécaniquement déterminable.
9. **Minuscules partout** (convention thésaurus, 2026-07-16) : les
   outils d'affichage capitalisent au besoin.
10. **`tags` renommé `phenomenon`** (2026-07-16) : le mot précis que
    « tags » n'était pas ; scalaire dans le cas courant, liste si
    réellement multiple, absent si aucun phénomène particulier.
11. **Arborescence physique `cards/<domain>/<output>/`** (2026-07-16) :
    remplace l'arbre thématique historique. Ces deux facettes sont les
    seules fermées, obligatoires et mono-valuées → l'arborescence est
    dérivable de la classification et le linter vérifie
    `chemin == f(domain, output)` (fiches bi-domaines : rangées sous le
    domaine premier de la liste). Dossiers en anglais : flow,
    precipitation, temperature, evapotranspiration × series, scalar,
    curve. Navigation humaine : ~10 dossiers de 15 à 90 fiches, et le
    catalogue pour le tri fin.
6. **Le champ `topic` est supprimé à la migration** : toute
   l'information vient de `classification` (labels en/fr générés depuis
   le vocabulaire central pour le catalogue et card.info).
