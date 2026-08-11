> **Statut : plan en cours, rien n'est publié.** Deux chantiers liés,
> tenus ensemble parce qu'ils partagent une décision : un site de
> documentation pour card, et l'export SKOS de la classification. Tout se
> fait et se regarde **en local** tant que la question des identifiants
> pérennes n'est pas tranchée, et elle ne le sera pas ici : elle demande
> des interlocuteurs, pas une réflexion de plus.
> Contient l'état des lieux mesuré, la reconnaissance du thésaurus
> Theia/OZCAR, l'architecture retenue, le modèle de données et les
> pièges à ne pas rencontrer en codant.
> À archiver quand les deux chantiers seront livrés.

# Site de documentation et export SKOS

## Le problème, en une phrase

Le corpus card n'appartient ni à R ni à Python, mais c'est le **front R**
qui a une vitrine moderne, et le corpus qui est servi comme du markdown
brut. Et la classification, qui est déjà un vocabulaire structuré, n'est
lisible que par un humain qui ouvre un tableau.

## Ce qui existe, mesuré le 2026-08-11

| | site | ce qu'un visiteur voit |
|---|---|---|
| **card4r** (R) | pkgdown Bootstrap 5 | barre, recherche, référence des fonctions, article, changelog, thème clair/sombre |
| **card** (Python) | Pages par défaut | markdown rendu en une colonne, sans barre, sans recherche, sans thème |

La pratique Python n'est pas « PyPI plus GitHub » : un paquet
scientifique a un site généré (Sphinx ou MkDocs, sur Read the Docs ou
Pages), avec une référence d'API construite depuis les docstrings. La
page PyPI est une vitrine d'une page, pas de la documentation.

**Ce qui bloquait n'était pas le français.** Mesuré : les fonctions hydro
étaient déjà bilingues, la machinerie interne ne se publie pas, et l'API
publique représentait 1 132 mots. Converties le 2026-08-11 (card 0.5.1,
stase 0.6.3), avec une garde dans les deux dépôts. Ce chantier est donc
**déjà levé**.

## Reconnaissance du thésaurus Theia/OZCAR (2026-08-11)

Faite par l'API REST de leur Skosmos, qui répond publiquement :
`https://in-situ.theia-land.fr/skosmos/rest/v1/theia_ozcar_thesaurus/`.
**Aucun export à demander, tout est interrogeable**, y compris concept par
concept en Turtle. La vérification d'un alignement est donc automatisable.

### Leur modèle

- **2 506 concepts**, dont 439 dépréciés. Ils ne suppriment pas, ils
  déprécient : à imiter.
- **Neuf concepts de tête**, et ce sont les composants I-ADOPT :
  Variable, Property, Physical entity, Phenomenon, Process, Constraint,
  Instrument, Time, Method.
- Leurs variables sont **composées**, pas nommées. Mesuré sur
  « Surface water discharge » :

  ```turtle
  ozcar:c_4e0d7c14  a skos:Concept, iop:Variable ;
      skos:prefLabel "Surface water discharge"@en ;
      iop:hasObjectOfInterest ozcar:c_d73ddccf ;
      iop:hasProperty         ozcar:c_7742e5f0 .   # Discharge
  ```

- Leurs URIs sont **opaques** et sous **w3id.org** :
  `https://w3id.org/ozcar-theia/c_7742e5f0`. Le libellé n'est jamais
  l'identifiant.
- Ils alignent vers l'extérieur : `Discharge` porte un `skos:exactMatch`
  vers EnvThes.
- **Aucun `skos:notation`** sur les concepts examinés. Ils n'ont pas de
  symbole, seulement des libellés longs.
- Leur branche `Property` (40 sous-concepts directs) est une hiérarchie
  de grandeurs physiques génériques : Rate, Temperature, Pressure,
  Volume, Concentration, Duration, Flux…
- Leur branche `Statistical method` contient **sept** concepts :
  Accumulation, Average, Minimum, Maximum, Median, Standard deviation,
  Uncertainty interval.
- Leur branche `Constraint` porte des contraintes **physiques**
  (rayonnement, phase, sédiment, instrument, espace), **jamais une
  fenêtre temporelle**.

### La zone de recouvrement, mesurée

| dimension card | chez eux |
|---|---|
| `Q` débit | **oui**, `Discharge`, propriété, alignée vers EnvThes |
| `T` température de l'air | **oui**, variable, avec variantes par hauteur |
| `R` précipitation | **oui**, `Precipitation amount` / `rate` |
| `ETP` | entité présente, variable à confirmer |
| moyenne, minimum, maximum, médiane, cumul, écart-type | **oui**, six de leurs sept |
| quantile / percentile (`Pq`, Q90, FDC) | non |
| moyenne mobile sur d jours (VCN10) | non |
| fenêtre annuelle, année hydrologique, saison | non |
| période de retour (`rp-`) | non |
| moyenne inter-annuelle (`mean-`, `median-`) | non |
| écart entre deux périodes (`delta-`) | non |
| pente de tendance (`alpha-`), compte d'années (`n-`) | non |

**Une dizaine de concepts en commun.** Tout le reste de card, c'est-à-dire
la dimension temporelle et statistique hydrologique, n'a aucun équivalent
chez eux. Ce n'est pas un recoupement, c'est **un axe complémentaire**.

## L'architecture retenue : deux étages, un alignement

La crainte à lever est celle d'une nomenclature forcée dans un standard,
qui rendrait illisible le lien avec les fiches. Elle ne tient pas, parce
que les deux objets ne répondent pas à la même question.

| | catalogue card | thésaurus Theia/OZCAR |
|---|---|---|
| répond à | qu'est-ce que je peux **calculer** ? | que **signifie** cette colonne ? |
| porte | méthode, process, unité, version, swhid | sens, hiérarchie, alignements |
| identifie | une définition calculable | une propriété observée |
| cadence | logiciel versionné, bouge à chaque publication | référence de communauté, bouge lentement |

`VCN10` n'est pas une propriété observée, c'est une statistique dérivée
d'une propriété observée. I-ADOPT décrit exactement cela.

**On ne traduit aucun nom, on déclare des composants.** Et la grammaire
d'Oberlin EST déjà cette décomposition : `Q` la propriété, `A` le pas de
temps, `N`/`X` le modificateur statistique, `_summer` la contrainte.

### Verdict : thésaurus à part, aligné

Ni sous-branche du leur, ni intégration. Trois raisons, la troisième
étant décisive :

1. **le volume** : une dizaine de concepts communs sur 2 506 chez eux et
   des centaines chez nous. C'est un voisin, pas une sous-branche ;
2. **le contenu** : `method`, `process`, `version` de fiche et swhid
   n'ont pas leur place dans un thésaurus, qui porte du sens et non une
   implémentation ;
3. **la gouvernance et la cadence** : intégrer un catalogue logiciel
   rapide dans un thésaurus communautaire lent leur imposerait une
   obligation de maintenance à chaque version de card. C'est le meilleur
   argument à leur présenter, parce qu'il les protège eux.

Ce qu'on leur propose n'est donc pas « intégrez mes variables », mais
deux choses nettes :

- **un alignement**, chez nous, sans qu'ils aient rien à faire ;
- **une extension optionnelle** : les composants qui leur manquent
  (moyenne mobile, fenêtre annuelle, période de retour, quantile) sont
  **génériques**, pas propres à card, et serviraient à tout observatoire
  publiant autre chose que de la donnée brute. C'est un cadeau, pas une
  charge.

Ils ont demandé « les variables de card » en croyant qu'elles complétaient
leur liste, alors qu'elles ajoutent un axe. Le dire ainsi vaut mieux que
d'envoyer un fichier.

**La séparation est ÉDITORIALE, pas géographique.** Que le vocabulaire
soit un objet distinct du leur n'implique pas qu'il vive ailleurs, et
c'est même l'inverse qui est souhaitable : qui cherche des variables
hydro doit les trouver au même endroit. Ordre de préférence pour
l'hébergement, le jour où on publiera :

1. **Theia/OZCAR sert le `.ttl` à côté du leur.** Skosmos est
   multi-vocabulaire par conception, c'est pourquoi leur API a un point
   `/vocabularies` qui rend une liste, aujourd'hui d'un seul élément.
   Deux vocabulaires côte à côte, alignements natifs dans l'interface,
   séparation éditoriale intacte. **Meilleur résultat.**
2. **[EarthPortal](https://ontoportal.github.io/documentation/user_guide/EarthPortal)**,
   sinon : catalogue d'artefacts sémantiques pour les sciences de la
   Terre, technologie OntoPortal, porté par l'infrastructure **Data
   Terra** dont Theia est un pôle. Public, français, et le bon domaine.
   **Pas AgroPortal**, qui est l'instance agronomie : ce n'est pas notre
   sujet.
3. **De toute façon, le `.ttl` est en téléchargement sur le site de
   card.** On met à disposition, qui le veut le prend. Aucun de ces
   hébergements n'est un prérequis, et aucun n'est bloquant.

### À quoi ressemble l'alignement

```turtle
card:VCN10
    a  skos:Concept , iop:Variable ;
    skos:inScheme   card: ;
    skos:notation   "VCN10" ;                       # la porte d'entrée de card
    skos:prefLabel  "Annual minimum of 10-day mean daily discharge"@en ,
                    "Minimum annuel du débit moyen sur 10 jours"@fr ;

    # ── l'alignement : pointe CHEZ EUX ────────────────────────────
    iop:hasProperty            ozcar:c_7742e5f0 ;   # Discharge
    iop:hasObjectOfInterest    ozcar:c_d73ddccf ;   # eau de surface
    iop:hasStatisticalModifier ozcar:c_……… ;        # Minimum

    # ── ce qu'ils n'ont pas : défini chez nous ────────────────────
    card:hasTemporalAggregation  card:rolling-mean-10d ;
    card:hasSamplingWindow       card:hydrological-year ;

    # ── ce qu'un thésaurus ne peut pas porter : reste ici ─────────
    card:computedBy  card:card-VCN10 ;              # la FICHE
    card:method      "annual aggregation [09-01, 08-31] - minimum of 10-day mean" ;
    card:version     "1.1" ;
    card:swhid       "swh:1:cnt:…" .
```

**Le point qui dimensionne tout** : ces trois lignes d'alignement
réutilisent **les mêmes dix concepts cibles** pour toutes les variables.
Le fichier d'alignement n'est pas une correspondance par variable, c'est
**une table d'une dizaine de paires** que le générateur applique.

### Le symbole contre le libellé

La porte d'entrée de card est l'acronyme, la leur est le libellé long.
SKOS prévoit les deux, et pour le symbole c'est **`skos:notation`**, dont
c'est la définition : un code dans un système de notation.

card publie donc `skos:notation` **et** `skos:prefLabel` dans les deux
langues. Que leurs concepts n'aient pas de notation est un manque de leur
côté, pas une contrainte du nôtre, et c'est une remarque à leur remonter :
un thésaurus de variables sans symbole oblige chaque producteur de données
à retrouver un concept par une chaîne longue.

## Où vit ce thésaurus chez nous

**Règle première : le `.ttl` est GÉNÉRÉ, jamais édité.** Même doctrine que
`CARDS.md`, et même garde de fraîcheur qu'impose `test_catalogue.py`. Un
fichier RDF écrit à la main diverge de son corpus en deux semaines.

Ce qui est **dérivable** des sources existantes, donc à ne surtout pas
recopier :

| élément SKOS | source |
|---|---|
| concepts de facette, `prefLabel` fr/en | `src/card/topics.yaml` |
| `skos:notation` | l'identifiant de la fiche |
| `prefLabel` d'une variable | `meta.<lang>.name` |
| `definition` | `meta.<lang>.description` |
| unité | `meta.<lang>.unit` |
| rattachement aux facettes | bloc `classification` |
| `card:method`, `version`, `swhid`, `computedBy` | la fiche et `list_cards()` |
| propriété d'entrée | `input_vars` et `src/card/inputs.yaml` |

Ce qui **n'est pas dérivable** et doit être déclaré, dans un fichier
nouveau et petit, à ranger à côté de ses voisins (`topics.yaml`,
`inputs.yaml`) :

```
src/card/alignments.yaml     # la table de correspondance vers l'extérieur
```

Il porte, et rien d'autre :

- `input_vars` → URI de propriété externe (`Q` → `ozcar:c_7742e5f0`) ;
- facette `domain` → URI d'objet d'intérêt ;
- opérateur statistique → URI de méthode statistique externe ;
- les concepts que card définit lui-même faute d'équivalent (moyenne
  mobile, fenêtre annuelle, période de retour, quantile), avec leurs
  libellés fr/en.

Une dizaine de lignes utiles. Le linter (`python -m card.schema`) doit le
valider comme il valide `topics.yaml` : toute URI citée doit être
résolvable, et tout `input_vars` du registre doit être couvert ou
explicitement marqué « pas d'équivalent ».

### Confrontation avec I-ADOPT, faite le 2026-08-11

**Résultat : aucune fiche n'a besoin d'un champ de plus.** Le pronostic
« il manque le modificateur statistique et la fenêtre temporelle » est
FAUX, et c'est pour ça qu'on mesure au lieu de croire.

Ce que le cadre exige, et où ça se trouve déjà :

| I-ADOPT | obligatoire | où c'est déclaré dans card |
|---|---|---|
| `hasProperty` | oui, exactement 1 | `input_vars` de la fiche, et le registre `inputs.yaml` |
| `hasObjectOfInterest` | oui, exactement 1 | idem : la grandeur et son objet vont **par paire**, pas séparément |
| `hasStatisticalModifier` | non | la **chaîne de process** et le drapeau `is_transform` |
| `hasConstraint` | non | `time_step` et `sampling_period` **du process** |
| `hasMatrix`, `hasContextObject` | non | sans objet ici |

**Le modificateur statistique se lit dans la chaîne, pas dans le nom.**
C'est le point qui change tout. Une fiche déclare ses process, et chaque
fonction dit si elle transforme ou réduit :

```
VCN10 :  T:rollmean_center → R:nanmin
         « minimum d'une moyenne mobile de 10 jours »
```

C'est de la donnée DÉCLARÉE, pas un nom analysé, donc le piège
`compute_Qp` ne s'applique pas. Mesuré : 226 fiches, de 1 à 5 process,
42 fonctions employées, 5 déclarées `is_transform`.

**La contrainte temporelle est déclarée aussi.** `time_step` est écrit
dans TOUS les process, le linter l'exige : `none` 249, `year` 208,
`year-month` 22, `year-season` 18, `yearday` 5, `month` et `season` 1.
Et `sampling_period` du process vaut `None` (298), `adaptive` (96), une
paire partielle (53), `09-01` (39) ou `01-01` (18).

> **Attention au piège** : c'est le `sampling_period` du **process** qu'il
> faut lire, machine-lisible, et non `meta.sampling_period`, qui mélange
> prose et littéral (piste ouverte connue de `CHANTIERS.md`). De même,
> la colonne `operator` ne vient que du PRÉFIXE de l'identifiant et ne
> dit rien de la statistique d'ordre : elle est vide sur 322 lignes.

**Ce qui manque n'est pas de la donnée, ce sont des TABLES de
correspondance.** Trois, toutes destinées à `alignments.yaml` :

1. **19 combinaisons d'`input_vars`** vers des paires (propriété, objet
   d'intérêt). Les six paramètres de type `date` de `inputs.yaml`
   (`ref_start`, `horizon_end`…) se filtrent tout seuls : ce sont des
   paramètres, pas des grandeurs observées ;
2. **42 fonctions** vers des concepts, dont **19 sont des modificateurs**
   appliqués à une grandeur (`nanmin`, `exceedance_quantile`, `delta`,
   `return_level`…) et **23 DÉFINISSENT une grandeur nouvelle** (`BFI`,
   `KGE`, `elasticity`, `runoff_coefficient`, `deficit_volume`…). Les
   secondes ne sont pas des modificateurs : ce sont des propriétés que
   card doit définir lui-même, aucune n'existant chez Theia ;
3. **les formes de fenêtre** vers des contraintes temporelles, sept pas
   de temps et cinq formes de fenêtre.

**Un cas à modéliser, 26 fiches sur 226.** I-ADOPT exige EXACTEMENT une
propriété et un objet, or ces fiches ont plusieurs entrées réelles :
`Q_obs, Q_sim` (12), `Q, R` (6), `Q, T` (5), `R, Rl, Rs` (5)… Le cadre
prévoit ce cas, avec `AsymmetricSystem` et ses `hasNumerator` /
`hasDenominator` / `hasSource` / `hasTarget`. Et le rôle est dérivable :
**l'ordre des arguments du tuple `func` le donne**, `ratio(Q, R)`
désignant sans ambiguïté son numérateur et son dénominateur.

Enfin, la facette `aspect` (typologie IHA : magnitude, duration, timing,
frequency) **n'a aucun équivalent I-ADOPT**. Elle reste une facette de
classification propre à card, publiée comme telle.

## Comment ça se lie à la documentation de card

Le catalogue et le thésaurus ne sont pas deux objets, ce sont **deux
rendus d'une même source**, produits par le même passage :

```
le corpus (les YAML) + topics.yaml + inputs.yaml + alignments.yaml
        │
        ├── catalogue humain   pages du site, bilingue
        └── card.ttl           machines, SKOS + I-ADOPT
```

Trois conséquences à tenir :

1. **Ils ne peuvent pas diverger**, puisqu'ils sortent du même script et
   tombent sous la même garde de fraîcheur. C'est la seule raison
   acceptable d'avoir deux artefacts.
2. **Le bilinguisme se règle enfin correctement.** Les deux fichiers
   `CARDS.md` et `CARDS.fr.md` existent parce que le markdown ne sait pas
   porter deux langues sur un même objet. Un concept, lui, porte
   `prefLabel@fr` et `prefLabel@en`, et l'interface bascule. Le catalogue
   du site devient **une page avec un sélecteur**, ce que fait Skosmos.
3. **Chaque ligne du catalogue est un concept**, donc chaque variable a
   une page ou une ancre stable, et le lien entre la doc et le thésaurus
   est le même identifiant des deux côtés.

Côté service, card-api pourrait exposer un `GET /v1/concepts` renvoyant
vers ces URIs. C'est un renvoi, pas une source : la vérité reste dans le
corpus.

## Pièges à ne pas rencontrer en codant

Chacun a déjà mordu ce dépôt, ou mord tous les projets RDF.

- **Les placeholders de suffixe.** Une fiche `delta-` écrit
  « between the {suffix.name} horizon ». Le générateur doit passer par la
  forme RÉSOLUE par défaut, comme `list_cards()` et le catalogue, sinon
  le `.ttl` publie des accolades. C'est exactement le défaut corrigé en
  0.4.1, sur quatre surfaces ; le `.ttl` en serait une cinquième.
- **Le concept est la VARIABLE, pas la fiche.** Une fiche `_month` produit
  douze variables. Chaque variable est un concept, et pointe vers la
  fiche qui la calcule par `card:computedBy`. La colonne `card` de
  `list_cards()` (0.5.0) donne exactement ce lien.
- **Une seule `prefLabel` par langue et par concept**, c'est une
  contrainte SKOS. Les fiches multi-sorties dont les métadonnées sont des
  listes doivent être éclatées, pas concaténées.
- **Toujours un tag de langue.** Jamais de `prefLabel` sans `@fr` ou
  `@en` : un littéral sans tag est un troisième objet qui casse les
  outils.
- **Ne jamais supprimer un concept.** Une fiche retirée ou renommée donne
  `owl:deprecated true` et `dcterms:isReplacedBy`, comme le font
  Theia/OZCAR avec leurs 439 concepts dépréciés. Une URI qui disparaît
  casse le travail de qui l'a citée.
- **URIs lisibles ou opaques.** Theia a choisi opaque. card peut se
  permettre lisible (`card:VCN10`) parce que l'identifiant d'une fiche
  est déjà stable et vérifié par le linter, qu'il est publié dans chaque
  sortie et cité dans les publications. Le prix est qu'un renommage crée
  une URI morte, d'où la dépréciation ci-dessus, et `RENAMING.md` qui
  trace déjà les renommages.
- **La version de fiche n'est pas l'identité du concept.** Une fiche qui
  passe en 2.0 reste la même variable ; sa version est une propriété, et
  l'historique vit dans git et le swhid.
- **La base d'URI est provisoire et doit se voir.** Rien n'est publié :
  la base sera réécrite. Elle doit donc être manifestement fausse dans le
  fichier généré, jamais une adresse plausible que quelqu'un pourrait
  citer par mégarde.
- **Les unités restent des chaînes** (`m^{3}.s^{-1}`). Les rendre
  machine-lisibles est un autre chantier, déjà au registre (UCUM), et il
  ne faut pas le faire à moitié en passant.
- **Le schéma de concepts a besoin de ses propres métadonnées**, et on
  les oublie toujours : `dcterms:title`, `dcterms:creator`,
  `dcterms:license`, `dcterms:created`, `dcterms:modified`,
  `owl:versionInfo`. **La licence est un vrai trou** : card est en
  GPL-3, ce qui est une licence de LOGICIEL et ne dit rien d'un
  vocabulaire. Un artefact sémantique se publie usuellement en CC-BY.
  À trancher avant publication, pas après.
- **La dépréciation demande une source lisible par une machine.**
  `RENAMING.md` trace les renommages, mais c'est de la prose : le
  générateur ne peut pas en tirer un `dcterms:isReplacedBy`. Soit on
  déclare les fiches retirées et leurs remplaçantes dans
  `alignments.yaml`, soit on assume qu'aucune dépréciation ne sera
  émise. La première option est la seule qui tienne dès qu'une URI est
  publiée.
- **Le déploiement du site : les leçons de card4r, apprises à ses
  dépens.** Un générateur de site ramasse volontiers ce qu'on ne lui
  demande pas (pkgdown publiait `CLAUDE.md`), et une action de
  déploiement en `clean: false` continue de servir un fichier qui n'est
  plus produit. Vérifier ce que la branche publiée contient VRAIMENT,
  pas ce que la construction a produit.
- **La garde de fraîcheur doit couvrir les trois sorties.**
  `test_catalogue.py` surveille aujourd'hui deux fichiers markdown ; il
  devra surveiller la page catalogue, le JSON et le `.ttl`, sans quoi
  deux d'entre eux périment en silence.
- **`generate_catalog.py` a un second métier qu'on oublie** : il tient le
  décompte du README entre les balises `<!-- cards:count -->`, seul
  décompte du dépôt, et `test_catalogue.py` le vérifie. Toute
  réorganisation du script doit le préserver, sous peine de faire mentir
  la première phrase du README.
- **Vérifier ce qui pointe vers l'ancien site avant de bouger les
  chemins.** Inventaire du 2026-08-11 : huit liens dans le README de
  card, quatre dans celui de card4r, un dans son `_pkgdown.yml`. card-api
  n'en cite aucun. Les six qui visent `dev/` doivent partir vers GitHub,
  les autres suivre les nouveaux chemins en minuscules.

## Ce que le site contient, et ne contient pas

```
site de card = LA porte de l'écosystème
├── Accueil               l'aiguillage actuel (docs/index.md), PAS le README
├── Catalogue             une page bilingue, générée, filtrable
├── Grammaire             décodage d'un nom, nomenclature
├── Fonctions
│   ├── scientifiques     baseflow, compute_FDC, return_level…
│   └── du paquet         extract, trend, list_cards, info…
├── Écosystème            card / card4r / card-api / stase
└── card.ttl              le fichier machine, en téléchargement
```

**« Documentation des fonctions », jamais « référence API ».** Le mot API
désigne déjà **card-api**, le service web, et l'ambiguïté a coûté un
échange complet. Ce dont il s'agit ici, c'est la documentation des
fonctions Python de card, générée depuis leurs docstrings : ce que
`help(card.extract)` affiche, rendu en pages web.

Elle se scinde en **deux sections**, et c'est une décision :

- **fonctions scientifiques** (`card/functions/`) : `baseflow`,
  `compute_FDC`, `return_level`, `apply_threshold`… C'est la mécanique
  interne des fiches, mais un hydrologue veut pouvoir lire ce que fait
  exactement `baseflow(method="Wal")` **sans ouvrir le paquet**. C'est
  même le premier public du site après ceux qui installent ;
- **fonctions du paquet** : les douze publiques, celles qu'on appelle.

Cette séparation ne change rien au code, seulement au regroupement dans
la navigation.

**L'accueil reste `docs/index.md`**, l'aiguillage, et non le README. La
décision est du 2026-08-06 et sa raison tient : deux vitrines divergent,
un aiguillage ne peut pas mentir. Le README sert GitHub et PyPI, le site
sert la navigation. Ne pas « simplifier » en fusionnant les deux.

### Le catalogue filtrable n'est pas un bonus

**Une page de plusieurs centaines de variables sans recherche ni filtre
ne vaut pas mieux que le markdown d'aujourd'hui**, c'est le même tableau
en plus long. Une page catalogue sans filtre ne mérite pas d'être
construite.

```
scripts/generate_catalog.py  →  la page catalogue, en HTML complet
                             →  docs/catalogue.json   (depuis list_cards)
                             →  docs/card.ttl

sur la page : recherche plein texte · filtres par facette (domaine,
phénomène, saison, forme, finalité) · tri de colonnes · bascule fr/en
```

Trois contraintes de réalisation, chacune pour une raison :

- **sans dépendance** : du JavaScript sans framework, une centaine de
  lignes. Il n'implémente aucune logique de corpus, il filtre ce que
  `list_cards()` a produit, donc il ne peut pas diverger ;
- **le tableau complet est rendu à la construction, en HTML**, et le
  JavaScript ne fait que **masquer des lignes déjà présentes**. Sans ça,
  la page est vide pour un moteur de recherche, pour un lecteur d'écran
  mal servi et pour qui coupe JS. Le catalogue markdown actuel est
  indexable ; on ne doit pas régresser là-dessus ;
- **la bascule de langue devient triviale** puisque chaque ligne porte
  ses deux libellés, ce que deux fichiers markdown ne savaient pas
  faire.

Décidé, et à ne pas rediscuter en codant :

- **pas `docs/dev/`.** Les rouages restent lisibles dans le dépôt, ce qui
  est un coût d'entrée légitime. Conséquence à ne pas rater : six liens
  du README de card et un de celui de card4r pointent vers
  `/card/dev/...` et devront pointer vers GitHub ;
- **pas le CHANGELOG**, il vit sur GitHub, règle déjà écrite ;
- **pas de tutoriel dupliqué** de l'article de card4r ;
- **aucune page qui énumère des variables à la main** ;
- **pas de référence d'API pour la machinerie interne** ;
- chemins en **minuscules** (`/catalogue/` et non `/CARDS`), la casse
  haute venant de la convention des fichiers racine, pas des adresses
  web ;
- casser les URLs actuelles est **accepté**, à condition de corriger les
  liens que nous référençons, inventoriés à treize.

## Souveraineté et identifiants

Deux faits recadrent l'inquiétude, légitime pour un établissement public :

- **Theia/OZCAR utilise déjà w3id**, `https://w3id.org/ozcar-theia/`. Une
  infrastructure de recherche publique française y est donc déjà ;
- **INRAE a son propre dispositif** : [VO@INRAE](https://vocabulaires-ouverts.inrae.fr/)
  publie le thésaurus INRAE (plus de 16 000 concepts, SKOS, français et
  anglais) sur un portail **Skosmos**, déposé sur **AgroPortal** sous
  `INRAETHES`, avec API.

**Mais la décision ne se prend pas maintenant.** Une URI n'est
irréversible qu'une fois **publiée**. Tant que le fichier reste local, la
base se réécrit d'une ligne. D'où la règle de ce plan : on génère, on
regarde, **on ne publie rien**.

## Le plan

| # | quoi | dépend de | état |
|---|---|---|---|
| 0 | fonctions publiques en anglais, sections NumPy, garde dans les deux paquets | rien | **fait** (card 0.5.1, stase 0.6.3) |
| 1 | docstrings hydro de `functions/` en anglais NumPy, `docstring.py` et son test retirés | décision | à valider |
| 2 | **confrontation** métadonnées des fiches contre attendus I-ADOPT | rien | **fait** : rien à ajouter aux fiches |
| 3 | ~~champs manquants dans les fiches~~ | — | **sans objet**, l'étape 2 l'a montré |
| 4 | `src/card/alignments.yaml` : trois tables de correspondance, et sa validation par le linter | 2 | à faire |
| 5 | `scripts/generate_skos.py` → `card.ttl`, base d'URI manifestement provisoire, métadonnées de schéma, garde de fraîcheur étendue | 3, 4 | à faire |
| 6 | Skosmos **local** sur ce `.ttl`, pour voir le rendu avant tout dépôt | 5 | à faire |
| 7 | site MkDocs Material **en localhost** : sans `dev/`, URLs minuscules, catalogue filtrable rendu en HTML, fonctions en deux sections | rien | à faire |
| 8 | courriel à Theia/OZCAR : l'alignement existe, veulent-ils l'extension, veulent-ils servir le `.ttl` ? | utilisateur | à faire |
| 9 | base d'URI définitive, licence du vocabulaire, domaine, hébergement, publication | 8 | différé |

### Pourquoi l'étape 1 est proposée

Mesuré le 2026-08-11 : `card/docstring.py`, qui lit les blocs
`en:`/`fr:`, n'est appelé **par aucun code de production**, seulement par
un test. La figure a cessé de lire les docstrings de fonctions quand
`method` a pris le relais. Les blocs français ont donc un lecteur humain
et aucun lecteur machine, et ce qu'un hydrologue francophone doit savoir
d'une **variable** vit dans la fiche (`meta.fr`), qui reste bilingue et
publiée. Unifier retire un module, un test et une convention, au lieu
d'ajouter.

## Licence, cycle de vie, hébergement, URIs

### Licence Ouverte, et l'équivalence affichée

**Licence Ouverte 2.0 (Etalab)**, qui se déclare elle-même compatible
avec CC-BY 4.0, ODbL et l'OGL britannique, et qui existe en français et
en anglais. C'est la licence des données publiques françaises, et elle
répond au réflexe de souveraineté. GPL-3 ne convient pas : c'est une
licence de logiciel, elle ne dit rien d'un vocabulaire.

L'équivalence s'**affiche** plutôt que de se deviner, pour qu'un
moissonneur qui ne connaît que CC-BY comprenne :

```turtle
card: a skos:ConceptScheme ;
    dcterms:license <https://www.etalab.gouv.fr/licence-ouverte-open-licence> ;
    dcterms:rights  "Licence Ouverte 2.0 (Etalab), compatible CC-BY 4.0"@en ,
                    "Licence Ouverte 2.0 (Etalab), compatible CC-BY 4.0"@fr .
```

### Un champ de cycle de vie, qui en absorbe un autre

`meta.global.is_experimental` existe et **aucune fiche ne l'utilise**
(mesuré le 2026-08-11). Il ne sert qu'à filtrer `list_cards`. Il est
remplacé par un champ unique :

```yaml
meta:
  global:
    status: active          # experimental | active | deprecated
    replaced_by: VCN10      # seulement si deprecated
```

**Et le point qui compte : une fiche dépréciée ne se supprime pas.**
Effacer le YAML tue le concept, donc tue l'URI que quelqu'un a citée. La
fiche devient **sa propre pierre tombale** : elle reste dans le corpus,
n'est plus proposée à l'extraction ni listée par défaut, et continue de
produire un concept `owl:deprecated true` avec son `dcterms:isReplacedBy`.
C'est ce que fait Theia/OZCAR avec ses 439 concepts dépréciés.

Réserve à ne pas escamoter : `is_experimental` est une **colonne de
sortie publique** de `meta`. La remplacer est un changement de sorties,
donc une entrée `RENAMING.md` et une version.

### Aucun serveur, y compris avec le catalogue filtrable

**Le JavaScript s'exécute dans le navigateur du visiteur, pas sur un
serveur.** Un site statique avec du JS reste statique : GitHub Pages le
sert, et le filtrage se fait sur la machine de qui consulte. Le domaine
INRAE personnalisé fonctionne aussi avec Pages, par un enregistrement
DNS, comme card-api. **Rien dans ce plan ne demande la VM.** La seule
chose qui en demanderait un est Skosmos, et on ne le déploie pas.

### Un identifiant n'est pas un emplacement

Nos concepts portent **nos** URIs, dès la première génération. Si
Theia/OZCAR sert notre `.ttl` dans leur Skosmos, les URIs à l'intérieur
restent les nôtres : ils affichent nos concepts avec nos identifiants, et
les alignements vers les leurs. Héberger un fichier ne change pas les
identifiants qu'il contient, sinon aucun alignement ne tiendrait entre
vocabulaires.

Ce que l'hébergement change est la **résolution** : ce qu'un navigateur
reçoit en ouvrant l'URI. C'est la seule décision réellement
irréversible, et elle reste différée.

## Ce qui est tranché, et qu'on ne rouvre pas

- **Vocabulaire à part, aligné depuis chez nous.** Ils n'ont rien à
  faire ; l'interopérabilité est garantie et la séparation éditoriale
  préservée. S'ils élargissent un jour leur périmètre, on leur passe le
  fichier et les liens repointent, ce qui est indolore puisque leurs
  URIs sont sous w3id.
- **Le modificateur statistique se déclare** dans les fiches plutôt que
  de se deviner depuis un nom, sauf si la confrontation de l'étape 2
  montre qu'il est déjà porté ailleurs de façon fiable.
- **La documentation des fonctions couvre les deux familles**,
  scientifiques et paquet, en deux sections. Un hydrologue doit pouvoir
  lire `baseflow` sans ouvrir le paquet.
- **Hébergement, par ordre de préférence** : Theia/OZCAR à côté du leur,
  sinon EarthPortal, et de toute façon en téléchargement chez nous.
- **Le catalogue est filtrable, rendu en HTML complet**, le JavaScript ne
  faisant que masquer des lignes.

- **Licence Ouverte 2.0**, équivalence CC-BY 4.0 affichée.
- **`status` remplace `is_experimental`**, et une fiche dépréciée reste
  dans le corpus comme sa propre pierre tombale.
- **Pas de serveur**, GitHub Pages suffit, JS compris.
- **Skosmos en conteneur local**, pour voir le rendu avant tout dépôt.

## Questions ouvertes

1. **Domaine du site** : `card.riverly.inrae.fr` comme card-api, ou on
   reste sur github.io tant que rien n'est publié ?
2. **Résolution des URIs** le jour de la publication : redirection par un
   service tiers, ou adresse maîtrisée par INRAE ? Seule décision
   irréversible du chantier, et elle attend les interlocuteurs.
