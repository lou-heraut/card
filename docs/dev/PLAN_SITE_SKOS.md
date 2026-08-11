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

**Un point à trancher en codant, et à ne pas improviser** : le
modificateur statistique d'une variable (`N`, `D`, `X`, rien, `Pq`) n'est
**déclaré nulle part aujourd'hui**. `list_cards` expose `operator`, dérivé
du PRÉFIXE de l'identifiant, pas la statistique d'ordre en position 3.
Deux voies : le déclarer dans les fiches, ou le dériver du nom. La
seconde revient à faire dépendre une sortie d'un nom écrit en dur, ce qui
a déjà coûté cher au dépôt (cf. `compute_Qp`, CLAUDE.md). Si on la
retient malgré tout, elle exige un test qui couvre **tout** le corpus et
refuse une variable non classée.

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

## Ce que le site contient, et ne contient pas

```
site de card = LA porte de l'écosystème
├── Accueil          ce que card calcule, installation, première extraction
├── Catalogue        une page bilingue, générée, un concept par ligne
├── Grammaire        décodage d'un nom, nomenclature
├── Référence API    généré des docstrings (anglais, sections NumPy)
├── Écosystème       card / card4r / card-api / stase
└── (plus tard)      les concepts, posés sur le Catalogue
```

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
| 0 | API publique en anglais, sections NumPy, garde dans les deux paquets | rien | **fait** (card 0.5.1, stase 0.6.3) |
| 1 | docstrings hydro de `functions/` en anglais NumPy, `docstring.py` et son test retirés | décision | à valider |
| 2 | `src/card/alignments.yaml` et sa validation par le linter | rien | à faire |
| 3 | `scripts/generate_skos.py`, `card.ttl`, base d'URI manifestement provisoire, garde de fraîcheur | 2 | à faire |
| 4 | Skosmos **local** sur ce `.ttl`, pour voir le rendu | 3 | à faire |
| 5 | site MkDocs Material **en localhost**, sans `dev/`, URLs minuscules, catalogue bilingue en une page | rien | à faire |
| 6 | échange avec Theia/OZCAR : extension statistique, ou alignement seul ? | utilisateur | à faire |
| 7 | base d'URI définitive, domaine, dépôt AgroPortal, publication | 6 | différé |

### Pourquoi l'étape 1 est proposée

Mesuré le 2026-08-11 : `card/docstring.py`, qui lit les blocs
`en:`/`fr:`, n'est appelé **par aucun code de production**, seulement par
un test. La figure a cessé de lire les docstrings de fonctions quand
`method` a pris le relais. Les blocs français ont donc un lecteur humain
et aucun lecteur machine, et ce qu'un hydrologue francophone doit savoir
d'une **variable** vit dans la fiche (`meta.fr`), qui reste bilingue et
publiée. Unifier retire un module, un test et une convention, au lieu
d'ajouter.

## Questions ouvertes

1. **Theia/OZCAR** : veulent-ils l'extension statistique et temporelle,
   ou seulement l'alignement de nos entrées ? Décide du dimensionnement.
   À leur demander, pas à deviner.
2. **Modificateur statistique** : déclaré dans les fiches, ou dérivé du
   nom avec un test qui couvre tout le corpus ?
3. **Référence d'API du site** : les fonctions publiques seules, ou aussi
   les fonctions hydro ?
4. **Skosmos local** : conteneur jetable pour voir, ou le `.ttl` et un
   validateur suffisent ?
