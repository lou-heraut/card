# CHANTIERS — pistes ouvertes (mise à jour 2026-07-20)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

Sorti le 2026-07-18 : « card-api : suivi des jobs, identité et RGPD »
(jetons hachés affichés une fois, préfixe pseudonyme dans le journal
et sur les jobs, GET /v1/jobs par clé, tickets 64 bits, mention RGPD
dans le template d'issue ; clés conservées tant qu'actives, effacées
à la révocation).

## 2. Références bibliographiques externes dans les fiches

Ancrer les fiches standardisées sur leurs références : identifiants
climdex/ETCCDI (RCXA1 ↔ RX1day, RCXA5 ↔ RX5day, dtCDDA ↔ CDD,
dtCWDA ↔ CWD...), libellés SANDRE/eaufrance (QMNA, VCNd, module).
**À retravailler avec le système de biblio scientifique existant de
l'utilisateur** (ne pas inventer un format de citation avant d'avoir
vu le sien).

## 3. Lint temps réel sous Emacs

Objectif : valider les YAML pendant l'édition. Deux voies :
- générer un **JSON Schema** des fiches (depuis schema.py) et brancher
  `yaml-language-server` (paquet Emacs `lsp-mode` ou `eglot`) — la voie
  standard, autocomplétion incluse ;
- ou un checker flycheck maison qui appelle
  `python -m card.schema <fichier>` (déjà supporté en CLI, plus simple
  mais sans autocomplétion).

## 4. Revue de code du package (lisibilité, dé-boîte-noire)

Crainte utilisateur : code trop compliqué/alambiqué par endroits.
À son initiative, mais aides possibles : un `docs/dev/ARCHITECTURE.md`
qui explique le pipeline en langage simple (loader → stase →
compactage), et une passe de simplification ciblée (/simplify) sur
extraction.py qui concentre la complexité (kwargs-colonnes, sparse,
fan-out).

## 5. Documentation utilisateur étendue

- README : section « développer sa fiche » faite (copy_cards →
  extract(path=...) → python -m card.schema) ; à étoffer d'un exemple
  complet de fiche commentée ligne à ligne ?
- Pages : tutoriel pas-à-pas avec données réelles (lié au chantier 1 ?).

## 6. Export SKOS / thésaurus (différé de longue date)

La classification (docs/dev/TOPICS.md) fournit désormais les concepts
et les paires en/fr — chaque facette devient un concept scheme.
Réévaluer quand le besoin Skosmos se concrétise.

## 7. Fiches futures

- **Rc** (vrai coefficient de ruissellement adimensionnel) :
  86,4 × ΣQ/ΣR / S, avec la surface S en colonne constante d'entrée
  (déjà au registre inputs.yaml) ;
- **durées cumulées de dépassement** (jours/an, famille DC d'Oberlin,
  préfixe dt) si le besoin se confirme ;
- fiches personnelles de l'utilisateur (en local via copy_cards puis
  contribution).

### Complétion de symétrie restante (inventaire 2026-07-18)

Trous relevés lors de l'inventaire familles x déclinaisons, non créés
pour l'instant (décision : se limiter au lot climatologique
mean-QSA_season, mean-TMA_month, mean-RMA_month, ETPSA_season,
ETPMA_month et aux cases isolées median-centerLF, median-tVCX3,
median-tVCX10, faits le 2026-07-18). À reprendre si le besoin se
confirme :

- **delta saisonniers des caractéristiques d'étiage** (10 fiches) :
  delta-{dtLF, vLF, centerLF, startLF, endLF}\_{summer, winter}\_H,
  modèle direct delta-allLF_summer_H / delta-allLF_winter_H (les
  séries saisonnières correspondantes existent déjà) ;
- **compagnons de niveaux de retour** (4 fiches) : delta-VCN30-2_H et
  delta-QMNA-5_H (modèle delta-VCN10-5_H), n-VCN30-2_H et n-QMNA-5_H
  (modèle n-VCN10-5_H) ;
- **maxima saisonniers de précipitations** : RCXSA1_season,
  RCXSA5_season (modèle RSA_season + RCXA1/RCXA5) ;
- **coefficient d'écoulement mensuel** : CRM_month (modèle CRS_season) ;
- **miroirs basses eaux des fréquences fQ** : fQ90A, fQ95A, fQ99A
  (temps passé sous le quantile) + deltas ; opérateur inversé par
  rapport à fQ01A, pas une pure déclinaison ;
- absences uniformes assumées, à rediscuter seulement si un usage les
  demande : aucun median- saisonnier, aucune variante saisonnière côté
  hautes eaux (VCX*_summer...), ratios annuels uniquement, famille
  alpha- limitée au trio MAKAHO (QA, QJXA, VCN10).

## 8. Palettes : questions ouvertes (2026-07-18)

État : les fiches à grandeur non ambiguë sont toutes équipées (héritage
de la fiche mère ; voir RENAMING.md 2026-07-18 pour l'orientation ETP).
Quatre palettes sémantiques en usage : marron→vert (quantités d'eau),
bleu→rouge (température), violet→orange (dates et durées de crue),
vert→marron (durées/volumes d'étiage, ETP : assèchement).

- **Scores de performance et indices sans unité** (KGE, NSE et
  variantes, Bias, STD_ratio, epsilon_R/T, RAT_*, QR_ratio, RA_ratio,
  BFI-LH/Wal et leurs deltas, BFM, a-FDC) : laissés sans palette
  volontairement. Si on les équipe un jour, il faudra une palette
  divergente centrée sur la valeur de référence (1 pour KGE/NSE, 0 pour
  les deltas de BFI), décision non prise.
- **dtFlood** : partage la palette violet→orange avec les dates, et non
  la palette d'assèchement de dtLF/dtBF. Examiné le 2026-07-18 et
  conservé : une durée de crue représente un risque (dégâts), pas un
  assèchement, et une crue plus longue n'est pas « plus d'eau » ; la
  dynamique diffère de celle des étiages. Si on veut un jour distinguer
  le risque de crue des dates par une palette dédiée, c'est une
  décision à part.

## 9. Multi-seuils réglementaires : le suffix de stase (2026-07-20)

**Objectif.** Les fiches rp-VCN10, rp-VCN30, rp-QMNA donnent la période
de retour d'UN débit seuil réglementaire par série, passé en colonne
constante Q_lim. Une station a en pratique plusieurs seuils (DOE, DCR,
alerte...) et on veut toutes les périodes de retour en un appel, avec
des noms de sortie déterministes. La valeur d'un seuil étant propre à
chaque série, elle ne peut pas vivre dans l'id d'une fiche : le nom de
sortie doit venir d'un suffixe.

**Ce qui a été établi le 2026-07-20** (l'inventaire demandé, qui
corrige deux erreurs de la note précédente) :

- `suffix=` / `suffix_delimiter=` existent bel et bien dans
  `stase.extract` (paramètres publics, documentés, validés contre R par
  le scénario 20 du harnais). La note antérieure disait le contraire.
- Le mécanisme R n'est pas un « suffixe tout » : `process_extraction.R`
  calcule `where_no_suffix` et n'éclate que les fonctions dont au moins
  un argument admet une variante suffixée présente dans les données ;
  les autres sont dédupliquées et sorties sans suffixe. R sait donc déjà
  distinguer colonnes partagées et colonnes qui varient. Sa limite est
  la granularité : le choix se fait par FONCTION, si bien qu'une
  fonction mêlant une série partagée et une colonne variable voit ses
  arguments partagés partir en chaînes littérales. C'est exactement le
  P3 de rp-VCN10 (`return_period(VCN10, threshold=Qlim)`).

**Ce qui est fait.** stase applique désormais la règle référence par
référence : colonne suffixée si elle existe, colonne de base sinon,
kwargs-colonnes compris ; sortie suffixée dès qu'une référence l'a été ;
fonction sans référence variable émise une seule fois, sans suffixe.
Divergence tracée dans stase `docs/dev/ORIGINE_R.md`, couverte par
`stase/tests/test_suffix.py` (9 tests). Le comportement du cas nominal R
est inchangé, et rien dans card n'utilisait suffix : aucune sortie
existante n'est touchée.

Vérifié de bout en bout sur la chaîne rp-VCN10 avec deux seuils
(Q_lim_DOE, Q_lim_DCR) : P1 sort VC10 une seule fois, P2 sort VCN10 une
fois plus Qlim_DOE et Qlim_DCR, P3 sort rp-VCN10_DOE et rp-VCN10_DCR,
valeurs identiques au bit près à deux extractions mono-seuil.

### Conception des métadonnées évolutives (validée le 2026-07-20)

Conception arrêtée après discussion, à appliquer telle quelle. Elle est
écrite en détail parce qu'elle a déjà été perdue une fois.

**Principe directeur, qui justifie tout le reste.** Le mécanisme est
entièrement confiné aux MÉTADONNÉES. Aucun placeholder ne peut changer
un calcul : le fan-out des valeurs reste celui de stase, au niveau
colonne. Le pire défaut possible de ce chantier est donc une phrase
bancale, jamais un chiffre faux. Toute évolution future doit préserver
cette séparation.

**Le fait qui structure la conception.** Les fiches horizon
(`delta-*_H`, 55 fiches) ne sont PAS un suffixe stase : leur P2 énumère
à la main trois entrées `func` qui diffèrent par un paramètre littéral
(des dates substituées au chargement par `$Hx`). Le suffixe stase, lui,
fait varier une référence de COLONNE. Deux mécanismes de fan-out
différents qui convergent sur la même forme de sortie : N colonnes
`X_<clé>` issues d'un seul run. On unifie donc la couche vocabulaire et
métadonnées, PAS le fan-out (cf. §10).

Ces fiches portent déjà les traces de ce besoin mal servi :
`horizon_labels` est déclaré dans 55 fiches et lu par RIEN (ni code, ni
linter, ni tests, ni docs), et `{horizon}` apparaît dans 110 blocs de
méta (`method`, en et fr) sans être substitué nulle part. Le loader ne
substitue que les `$Hx` du process, qui sont des dates.

**Un suffixe est un enregistrement, pas une étiquette.** Entre `name`,
`description` et `method`, on veut pouvoir écrire un nom court (`H1`,
`DOE`, `rcp85`), un nom long (« horizon proche », « débit objectif
d'étiage », « scénario d'émission 8.5 ») et des informations
complémentaires (pour `H1`, la période « 2021-2050 »). D'où un
enregistrement par suffixe, déclarable dans la fiche et fournissable à
l'appel.

Dans une fiche à ensemble ouvert (cas seuil) :

```yaml
meta:
  fr:
    name: "Période de retour du {suffix.name} sur le débit minimal sur 10 jours"
    method: "... 3. période de retour du seuil {suffix}"
    suffix_default:
      name: seuil réglementaire d'étiage
      short: seuil
```

Dans une fiche à ensemble fermé (forme cible d'une fiche horizon, cf.
§10, à ne PAS appliquer maintenant) :

```yaml
  fr:
    name: "Changement moyen ... entre l'{suffix.name} ({suffix.period})
           et la période historique"
    suffixes:
      H1: {name: horizon proche,   period: "2021-2050"}
      H2: {name: horizon moyen,    period: "2041-2070"}
      H3: {name: horizon lointain, period: "2070-2099"}
    suffix_default:
      name: horizon futur
      period: "toutes périodes"
```

Les enregistrements vivent par langue (dans `meta.en` et `meta.fr`),
chacun autosuffisant : pas de règle de fusion entre `meta.global` et
les langues, au prix d'une répétition minime des champs neutres. C'est
le découpage que `horizon_labels` utilisait déjà.

À l'appel, deux formes :

```python
card.extract(data, cards=["rp-VCN10"], suffix=["DOE", "DCR"])

card.extract(data, cards=["rp-VCN10"], suffix={
    "DOE": {"en": {"name": "low-flow target discharge"},
            "fr": {"name": "débit objectif d'étiage"}},
    "DCR": {"en": {"name": "crisis discharge"},
            "fr": {"name": "débit de crise"}},
})
```

**Les placeholders forment un espace de noms ouvert.** `{suffix}` seul
vaut `{suffix.short}`, et `{suffix.short}` vaut la clé (`H1`, `DOE`)
sauf si un `short` est déclaré. Tout autre champ s'écrit
`{suffix.<champ>}`, le jeu de champs n'est pas fermé par le code : un
besoin nouveau s'exprime dans les fiches, pas dans une nouvelle
grammaire.

**Trois règles, dans cet ordre.**

1. INVARIANT : aucune accolade ne sort jamais non résolue d'un champ de
   `meta`. La substitution a toujours lieu ; sans suffixe elle utilise
   `suffix_default`.
2. LINT : toute fiche utilisant `{suffix.X}` doit déclarer `X` dans son
   `suffix_default`, dans CHAQUE langue. Vérifiable statiquement, sans
   données. Conséquence voulue : une fiche est lisible seule, et
   `metadata_only=True`, une extraction sans suffixe et le catalogue
   `docs/CARDS.md` produisent tous la même phrase.
3. REPLI quand un suffixe est fourni sans un champ : `name` et `short`
   retombent sur LA CLÉ (`DOE`), jamais sur le `suffix_default` de la
   fiche. Retomber sur le défaut donnerait le même `name` aux lignes
   DOE et DCR, soit exactement l'ambiguïté qu'on veut tuer. Pour un
   champ non standard exigé par la fiche (`period`), pas de repli
   sensible : erreur explicite nommant la fiche, le champ et le
   suffixe.

**Fiche sans placeholder recevant un suffixe.** Le cas historique R du
suffixe est `obs`/`sim`, applicable à N'IMPORTE LAQUELLE des 237 fiches,
dont aucune n'a de placeholder. Règle : le `name` est complété
automatiquement en fin de chaîne, « Débit moyen journalier annuel
(simulation) ». Sur `name` seul, puisque c'est lui qui sert de titre de
graphique ; `description` et `method` restent intacts. Aucune fiche à
modifier.

**Priorité fiche/appelant.** L'appelant gagne, champ par champ. La
fiche fournit le sens par défaut, l'appelant l'adapte à son étude sans
forker la fiche (passer « +2 °C » là où la fiche dit « horizon
proche »). Point le moins discuté de la conception, à rouvrir si besoin :
c'est une ligne de code.

**Une ligne de `meta` par variable.** Un suffixe change le nom de la
variable, donc c'est une autre variable, donc une autre ligne. S'ajoute
une colonne `suffix` (vide pour les lignes non suffixées) qui lève
l'ambiguïté sans re-parser les noms et permet le regroupement que
`stase.trend` fait déjà avec `extremes_by_suffix=`.

### Câblage côté card (à implémenter)

Périmètre : les 3 fiches `rp-*` UNIQUEMENT. Aucune fiche `delta-*_H`
n'est touchée par ce chantier.

- `card.extract(..., suffix=..., suffix_delimiter="_")` propagé à chaque
  `_run_process` (extraction.py). Accepte la liste ou le dict.
- `_check_input_vars` : une colonne `Q_lim_DOE` doit satisfaire
  l'exigence `Q_lim` d'une fiche.
- `_meta_rows` construit APRÈS le run, d'après les colonnes réellement
  sorties : pour chaque variable déclarée, `var` présente donne une
  ligne nue, `var_DOE` donne une ligne DOE. Raison : la règle de stase
  est conditionnelle (une fonction sans référence variable sort une
  seule fois, sans suffixe), donc card ne peut pas savoir avant le run
  quelles variables sont suffixées. Dans un même appel avec
  `suffix=["DOE","DCR"]`, `rp-VCN10` donne 2 lignes et `QA` en donne 1.
  Lire les colonnes de sortie est exact par construction et ne peut pas
  diverger de stase, contrairement à une réimplémentation de la
  propagation côté card. Implique d'inverser l'ordre de la boucle de
  `extract()` (aujourd'hui `_meta_rows` est appelé avant le calcul,
  extraction.py:384).
- `metadata_only=True` : rien ne tourne, donc forme par défaut, qui est
  la même que celle d'une extraction sans suffixe (règle 2).
- Nommage des colonnes d'entrée : la grammaire impose `Q_lim_DOE`, pas
  `Q_DOE`. Ce n'est pas cosmétique : `Q_DOE` serait capté comme la
  variante suffixée de la série de débit `Q` et remplacerait la
  chronique par la constante de seuil (cas figé dans
  `test_base_column_loses_to_its_own_variant`). Le `rename=` déjà
  présent dans `card.extract` couvre le besoin sans code nouveau.
- Au passage, nettoyer les variables internes `metaEX_parts` / `dataEX`
  d'extraction.py:382 : la sortie s'appelle `meta` et `data` depuis
  2026-07-16.

**Points tranchés.** Pas de liste de suffixes réservés : suffixer par
`_DJF` ou `_H1` peut être un choix délibéré d'une fiche qui vient de
faire un `compress`, l'interdire casserait un usage légitime ; le
`verbose=True` de `_resolve_column_references` trace déjà la colonne
retenue pour chaque référence. La grammaire est unique entre l'ajout de
suffixes à l'extraction et leur retrait dans `stase.trend`
(`suffix=`, `extremes_by_suffix=`). Sorties NaN quand le seuil est hors
du support de la loi (validé). Pas de produit cartésien : une seule
dimension de suffixe par appel.

**Limite assumée.** Le lint protège les fiches, pas les appels : une
étiquette mal choisie à l'appel donne une phrase bancale, dans les deux
langues, et c'est invérifiable automatiquement. Le risque existait déjà
avant ce chantier ; la relecture des phrases composées fait partie du
travail sur ces fiches plus complexes.

## 10. Arguments de fonction en colonnes (horizons, degrés de réchauffement)

Chantier SUIVANT, à ne pas mélanger avec le §9. Idée : faire passer les
dates des horizons en colonnes des données plutôt qu'en paramètres
littéraux. Les fiches `delta-*_H` deviendraient structurellement
identiques aux fiches de seuil (une colonne constante par série,
éclatée par le suffixe stase), leur P2 passerait de trois entrées `func`
à une seule, les noms de sortie resteraient `delta-QNA_summer_H1` (base
plus suffixe, à l'identique), et surtout les horizons par DEGRÉ DE
RÉCHAUFFEMENT deviendraient possibles, chaque chaîne de modèles
atteignant +2 °C à une date différente. Cas Explore2, pas cas d'école.

**Deux blocages vérifiés dans le code le 2026-07-20 :**

- `delta(X, dates, past, future, relative, ...)` prend des PAIRES
  (`functions/seasonal.py:33`, usage `past[0]`, `past[1]`). Une colonne
  fournit une valeur par ligne, pas une paire : il faudrait deux
  colonnes par période et une signature à quatre scalaires. Changement
  de signature, donc RENAMING.md et 59 fiches.
- stase ne résout en référence que les kwargs dont la valeur est une
  chaîne UNIQUE (`extraction.py:936`, `isinstance(v, str)`). Un
  `{past: ["H0_start", "H0_end"]}` repartirait en littéral. Il faut donc
  soit quatre kwargs scalaires, soit ajouter la résolution de listes de
  références dans stase.

**Coût annexe.** Quatre colonnes de dates constantes répétées sur chaque
ligne journalière (le précédent existe : `Q_lim` est déjà exactement
ça), et la perte de l'autodocumentation des horizons de référence dans
la fiche. Ce dernier point se rattrape : la fiche garde son
`meta.global.horizons` et `card.extract` matérialise ces dates en
colonnes constantes quand l'appelant n'en fournit pas. Défaut inchangé,
override par série possible.

**Déjà ouvert, vérifié.** Une sortie de process devient une colonne
disponible au process suivant, et un kwarg nommant une colonne est
résolu dynamiquement. Des dates CALCULÉES par un process amont et
consommées en aval sont donc structurellement possibles sans code
nouveau côté stase.

La couche métadonnées du §9 (`suffixes`, `suffix_default`,
placeholders, colonne `suffix`) est IDENTIQUE que les horizons restent
des paramètres littéraux ou deviennent des colonnes. Elle ne ferme
donc rien, et c'est la raison pour laquelle elle est construite en
premier.
