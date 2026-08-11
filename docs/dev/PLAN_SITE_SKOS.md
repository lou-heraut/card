> **Statut : plan en cours, rien n'est publié.** Deux chantiers liés,
> tenus ensemble parce qu'ils partagent une décision : un site de
> documentation pour card, et l'export SKOS de la classification. Tout se
> fait et se regarde **en local** tant que la question des identifiants
> pérennes n'est pas tranchée, et elle ne le sera pas ici : elle demande
> des interlocuteurs, pas une réflexion de plus.
> Contient l'état des lieux mesuré, la reconnaissance du thésaurus
> Theia/OZCAR, l'architecture retenue et les questions ouvertes.
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
**Aucun export à demander, tout est interrogeable.**

Ce qu'elle a rendu :

- **neuf concepts de tête**, et ce sont les composants I-ADOPT :
  Variable, Property, Physical entity, Phenomenon, Process, Constraint,
  Instrument, Time, Method ;
- leurs variables sont **composées**, pas nommées :
  `iop:hasObjectOfInterest` plus `iop:hasProperty`. Exemple mesuré,
  « Surface water discharge » pointe vers l'objet « eau de surface » et
  vers la propriété « Discharge » ;
- leurs URIs sont **opaques** et sous **w3id.org** :
  `https://w3id.org/ozcar-theia/c_7742e5f0`. Le libellé n'est pas
  l'identifiant ;
- ils alignent vers l'extérieur, `Discharge` porte un `skos:exactMatch`
  vers EnvThes ;
- **aucun `skos:notation`** sur les concepts examinés : ils n'ont pas de
  symbole, seulement des libellés.

Et surtout, la limite qui décide de tout :

> **Leur agrégation temporelle s'arrête au pas d'observation.** On trouve
> « Instantaneous karst water discharge » et « 1 day mean karst water
> discharge », les concepts `Minimum` et `Mean`, mais **aucun concept
> annuel**, et leur branche `Constraint` porte des contraintes physiques
> (rayonnement, phase, sédiment, instrument), jamais une fenêtre
> temporelle.

Autrement dit : la statistique hydrologique annuelle, la moyenne mobile,
la période de retour, la fenêtre saisonnière, **cette couche n'existe pas
chez eux**.

## L'architecture retenue : deux étages, un alignement

La crainte à lever est celle d'une nomenclature forcée dans un standard,
qui rendrait illisible le lien avec les fiches. Elle ne tient pas, parce
que les deux objets ne répondent pas à la même question.

| | catalogue card | thésaurus Theia/OZCAR |
|---|---|---|
| répond à | qu'est-ce que je peux **calculer** ? | que **signifie** cette colonne ? |
| porte | méthode, process, unité, version, swhid | sens, hiérarchie, alignements |
| identifie | une définition calculable | une propriété observée |

`VCN10` n'est pas une propriété observée, c'est une statistique dérivée
d'une propriété observée. I-ADOPT existe pour décrire exactement cela :
une `Variable` a une `Property`, un `ObjectOfInterest`, et des composants
dont un modificateur statistique et des contraintes.

```
VCN10
├── Property            → leur concept « Discharge »
├── ObjectOfInterest    → leur concept d'eau de surface
├── StatisticalModifier → minimum d'une moyenne mobile de 10 jours
└── Constraint          → fenêtre annuelle adaptative
```

**On ne traduit aucun nom, on déclare des composants.** `VCN10` garde son
identifiant, sa méthode, sa version. Ce qui voyage, ce sont les liens
entre ses composants et leurs concepts.

Le point qui débloque : **la grammaire d'Oberlin EST déjà cette
décomposition.** `Q` la propriété, `A` le pas de temps, `N`/`X` le
modificateur statistique, `_summer` la contrainte. Le travail conceptuel
est fait ; I-ADOPT lui donne un format.

**Conséquence sur le coût** : l'alignement se compte en **composants**,
une trentaine, pas en variables, il y en a des centaines. Les variables
suivent par construction.

### Le symbole contre le libellé

Le doute est légitime et la réponse est dans la norme. La porte d'entrée
de card est l'acronyme (`VCN10`), la leur est le libellé long. SKOS
prévoit les deux, et pour le symbole c'est **`skos:notation`**, dont
c'est la définition même : un code dans un système de notation.

Donc card publie `skos:notation "VCN10"` **et** `skos:prefLabel` dans les
deux langues. Rien à sacrifier. Que leurs concepts n'aient pas de
notation est un manque de leur côté, pas une contrainte du nôtre, et
c'est une remarque à leur faire : un thésaurus de variables sans symbole
oblige chaque producteur de données à retrouver un concept par une
chaîne de caractères longue.

## Ce qu'on leur donne, et ce qu'on garde

**On garde le catalogue card**, parce que leur thésaurus ne peut pas
porter ce qui fait sa valeur : le `method`, le `process`, la version de
fiche, le swhid, le lien avec le paquet qui calcule. Un thésaurus porte
du sens, pas une implémentation.

**On contribue chez eux** parce que c'est là que se croisent les
observatoires. Mais la reconnaissance ci-dessus redimensionne la
promesse :

- les **variables d'entrée** de card (le registre `inputs.yaml`) sont des
  propriétés observées. Elles correspondent à ce qu'ils ont déjà, ou s'y
  ajoutent sans discussion. C'est une matinée ;
- les **variables dérivées** sont une couche qu'ils n'ont pas. Les leur
  proposer, ce n'est pas livrer un fichier, c'est **proposer une
  extension** de leur thésaurus sur la dimension statistique et
  temporelle. C'est une collaboration, et elle vaut d'être proposée
  comme telle plutôt qu'envoyée par courriel.

**Le format d'échange ne se décide pas non plus seul.** Trois voies, à
trancher avec eux : un `.ttl` qu'on leur remet, un `.ttl` qu'on expose et
qu'ils moissonnent, ou nos deux vocabulaires alignés l'un vers l'autre
par des triplets. La troisième est la plus juste au vu de l'architecture
ci-dessus, mais c'est leur infrastructure qui décide.

## Ce que le site contient, et ne contient pas

```
site de card = LA porte de l'écosystème
├── Accueil          ce que card calcule, installation, première extraction
├── Catalogue        bilingue, généré
├── Grammaire        décodage d'un nom, nomenclature
├── Référence API    généré des docstrings (anglais, sections NumPy)
├── Écosystème       card / card4r / card-api / stase
└── (plus tard)      les concepts, qui se posent sur le Catalogue
```

Et ce qu'il ne contient pas, décidé :

- **pas `docs/dev/`.** Les rouages restent lisibles dans le dépôt, ce qui
  est un coût d'entrée légitime. Conséquence à ne pas rater : six liens
  du README de card et un de celui de card4r pointent vers
  `/card/dev/...` et devront pointer vers GitHub ;
- **pas le CHANGELOG**, il vit sur GitHub, règle déjà écrite ;
- **pas de tutoriel dupliqué** de l'article de card4r ;
- **aucune page qui énumère des variables à la main** ;
- **pas de référence d'API pour la machinerie interne**.

Deux points de forme tranchés : les chemins passent en **minuscules**
(`/catalogue/` plutôt que `/CARDS`), la casse haute venant de la
convention des fichiers racine et non des adresses web ; et casser les
URLs actuelles est accepté, à condition de **corriger les liens que nous
référençons**, inventoriés à treize.

**Le bilinguisme du catalogue se règle par le SKOS**, et c'est un argument
de plus pour le faire d'abord : deux fichiers markdown existent parce que
le markdown ne sait pas porter deux langues sur un même objet, là où un
concept porte `prefLabel@fr` et `prefLabel@en` et où l'interface bascule.
Skosmos fonctionne ainsi.

## Souveraineté et identifiants

L'inquiétude est légitime pour un établissement public. Deux faits la
recadrent :

- **Theia/OZCAR utilise déjà w3id**, `https://w3id.org/ozcar-theia/`. Une
  infrastructure de recherche publique française y est donc déjà ;
- **INRAE a son propre dispositif** : [VO@INRAE](https://vocabulaires-ouverts.inrae.fr/)
  publie le thésaurus INRAE (plus de 16 000 concepts, SKOS, français et
  anglais) sur un portail **Skosmos**, déposé sur **AgroPortal** sous
  `INRAETHES`, avec API. C'est un chemin institutionnel qui existe.

**Mais la décision ne se prend pas maintenant.** Une URI n'est
irréversible qu'une fois **publiée**. Tant que le fichier reste local, la
base se réécrit d'une ligne. D'où la règle de ce plan : on génère, on
regarde, **on ne publie rien**.

## Le plan

| # | quoi | dépend de | état |
|---|---|---|---|
| 0 | API publique en anglais, sections NumPy, garde dans les deux paquets | rien | **fait** (card 0.5.1, stase 0.6.3) |
| 1 | docstrings hydro de `functions/` en anglais NumPy, `docstring.py` et son test retirés | décision | à valider |
| 2 | `scripts/generate_skos.py`, `card.ttl`, base d'URI provisoire | rien | à faire |
| 3 | Skosmos **local** sur ce `.ttl`, pour voir le rendu | 2 | à faire |
| 4 | site MkDocs Material **en localhost**, sans `dev/`, URLs minuscules | rien | à faire |
| 5 | échange avec Theia/OZCAR : extension statistique, ou entrées seules ? | utilisateur | à faire |
| 6 | base d'URI définitive, domaine, dépôt AgroPortal, publication | 5 | différé |

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

1. **Theia/OZCAR** : veulent-ils une extension statistique et temporelle
   de leur thésaurus, ou seulement les propriétés d'entrée ? Décide de
   tout le dimensionnement. À leur demander.
2. **Format d'échange** : fichier remis, fichier moissonné, ou
   alignement mutuel ?
3. **Référence d'API du site** : les fonctions publiques seules, ou aussi
   les fonctions hydro, qui intéressent un hydrologue ?
4. **Skosmos local** : conteneur jetable pour voir, ou le `.ttl` et un
   validateur suffisent ?
