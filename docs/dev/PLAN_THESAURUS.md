> **Statut : construction close, publication en attente.** Le vocabulaire
> a sa forme définitive depuis le 2026-08-14 : un arbre thématique, des
> tableaux de thésaurus, une soudure vers Theia/OZCAR et les deux
> notations officielles françaises, celle du SCHAPI et celle du Sandre.
> **Rien n'est publié**, la base d'URI reste manifestement fausse, et la
> seule chose qui manque est une réponse de Theia.
> Ce document porte la mesure de LEUR thésaurus faite sur le graphe
> entier, la forme retenue chez nous et POURQUOI, et la liste de ce qui
> reste ouvert, en fin de document et à un seul endroit.
> Ce qu'il faut LEUR demander est dans `QUESTIONS_THEIA.md`, et nulle
> part ailleurs.
> La construction du site et de l'export, elle, est close :
> `PLAN_SITE_SKOS.md` la garde, avec l'audit des vocabulaires qui reste
> la référence du modèle.
> À archiver quand la question sera tranchée et le vocabulaire publié.

# Où vit le vocabulaire de card

## La question, en une phrase

Le plan initial avait tranché « thésaurus à part, aligné depuis chez
nous », sur trois arguments : le volume, le contenu, la gouvernance. Deux
des trois se sont affaiblis quand on a regardé leur thésaurus en entier,
puis l'un des deux s'est retourné quand on l'a regardé au bon endroit.

## Comment on a mesuré, et pourquoi ça a changé trois fois

- **2026-08-11 et 13** : interrogation de leur service **par mots-clés**,
  concept par concept. On voyait ce qu'on cherchait.
- **2026-08-14, matin** : vocabulaire **téléchargé en entier** (1,2 Mo de
  Turtle, un seul appel). Découverte de leur arbre thématique de 233
  catégories, qu'aucun sondage n'avait montré.
- **2026-08-14, audit** : parcours du graphe entier avec `rdflib`, en
  comptant les branches au lieu de les regarder. C'est ce passage qui a
  donné les chiffres ci-dessous, et ils contredisent ceux du matin.

```
23 086 triplets, 2 067 concepts (les ~439 dépréciés sont hors export)
  1 152  iop:Variable
    302  iop:Entity
    233  ozcar:CategoryOfVariable
    140  iop:Property
    133  iop:Constraint
     35  cpm:StatisticalMeasure
```

## Le volume : l'argument ne s'effondre pas, il change de camp

Le matin du 2026-08-14, on comparait 444 variables card aux 821 variables
de leur branche « hydrosphère continentale », et on en concluait « c'est
beaucoup, ce n'est pas absurde ». **La comparaison était fausse de deux
ordres de grandeur**, parce que leur hydrosphère est de la CHIMIE :

```
Terrestrial hydrosphere variable ........................ 846 variables
├── Groundwater hydrology .............................. 233   (162 chimie)
├── Karst hydrology .................................... 218   (189 chimie)
├── Unsaturated zone variable .......................... 140
└── Surface water hydrology ............................ 251
    ├── Surface water chemistry ........................ 218
    ├── Surface water chemicophysical variable .........   8
    ├── Surface water microbiology .....................   0
    └── Surface water physic variable ..................  25   ← la branche de card
```

**card entrerait dans une branche de 25 variables**, qu'il multiplierait
par dix-huit. Ce n'est pas une contribution, c'est une reprise. L'argument
du volume ne s'effondre donc pas : il devient l'argument le plus fort
CONTRE l'intégration, et il protège leur thésaurus autant que le nôtre.

## Le point de jonction : il y en a exactement un

```
Surface water physic variable                            [25 variables]
├── Surface water discharge
│   └── River discharge                                  c_9c959860
│       ├── Instantaneous river discharge
│       ├── 10 minutes mean river discharge
│       ├── 15 minutes mean river discharge
│       ├── 1 hour mean river discharge
│       ├── 1 day mean river discharge   c_dabd2d39  ← le `Q` de card
│       ├── 1 month mean river discharge
│       └── 4 bornes d'intervalle d'incertitude
├── Surface water level ................ 3
├── Surface water suspended sediment concentration ... 3
├── Surface water suspended sediment flux ............ 1
├── Surface water turbidity .......................... 1
└── Surface water velocity ........................... 0
```

Leurs onze concepts de débit sont **onze pas de temps d'acquisition**.
Pas un indicateur. Le recouvrement n'est donc pas « une dizaine de
concepts », il est de **un** : `1 day mean river discharge` est
exactement `card:input/Q`. Ils décrivent ce qu'on mesure, card décrit ce
qu'on calcule dessus, et les deux se touchent en ce point.

Cherché sur le fichier entier, zéro occurrence de : `flood`, `drought`,
`low flow`, `high flow`, `baseflow`, `recession`, `return period`,
`quantile`, `trend`, `rolling`, `moving`, `exceedance`, `threshold`,
`hydrological year`, `duration curve`, `deficit`. Ce que card apporterait
n'est pas un complément, c'est **une moitié du domaine qu'ils n'ont pas
commencée**.

## Ce que leur modèle fait, mesuré propriété par propriété

| propriété | usages | lecture |
|---|---|---|
| `iop:hasProperty` | 1 152 | systématique |
| `iop:hasObjectOfInterest` | 1 151 | systématique |
| `iop:hasMatrix` | 745 | le milieu, très employé ; card l'ignore |
| `iop:hasConstraint` | 694 | systématique |
| `ozcar:simplifiedLabel` | 1 385 | propriété maison, cf. ci-dessous |
| `cpm:statisticalMeasure` | **81** | **7 % de leurs variables** |
| `cpm:aggregationTimePeriod` | 21 | 21 couples durée × opération |
| `skos:notation` | **0** | aucune |
| `prefLabel@fr` | **0** | anglais seul |

Leur composition I-ADOPT est solide et systématique. **Leur étage
statistique, lui, est marginal** : card en publie 254 sur 444, avec neuf
fenêtres datées. Sur cet axe, card est en avance, pas en dette.

### `ozcar:simplifiedLabel` est notre `family`, en moins bien

```
"1 day mean river discharge"      simplifiedLabel → "Surface water discharge"
"15 minutes mean river discharge" simplifiedLabel → "Surface water discharge"
"River discharge"                 simplifiedLabel → "Surface water discharge"
```

Ils ont eu exactement le besoin de card (grouper les variantes d'une même
idée) et l'ont résolu par **une chaîne répétée sur 1 151 concepts**, avec
une propriété non standard. card le résout par un `iop:VariableSet`, qui
a une URI, deux libellés et des `hasApplicable…`. C'est la même idée, et
notre forme est la meilleure des deux : à leur dire comme un constat.

### Trois défauts relevés dans leur fichier

Ils ne coûtent rien à personne et ouvrent la conversation. Détail et
formulation : `QUESTIONS_THEIA.md`.

1. `iop:hasContraint` au lieu de `hasConstraint`, 39 triplets.
2. `1 day mean karst water discharge` pointe vers la mesure
   « 1 day cumulative ».
3. `10 minutes mean river discharge` range sa statistique dans
   `hasConstraint`, seul de ses dix frères.

## La forme retenue, et pourquoi

**Option C : à côté, rangé dans leur arbre.** Deux gestes séparés, qui se
tiennent l'un sans l'autre.

### Geste 1 : une colonne vertébrale chez nous (fait)

Le vrai défaut était antérieur à la question Theia. Les 133 familles
étaient **133 racines**, donc la page d'accueil d'un navigateur les
listait toutes, à plat. Personne n'entre par là.

```
card:  (6 concepts de tête)
├── débit
│   ├── basses eaux
│   │   ├── intensité · minimum · annuelle · série
│   │   │   ├── QNA, VCN3, VCN10, VCN30
│   │   ├── saisonnalité · minimum · annuelle · série
│   │   └── …
│   ├── moyennes eaux · hautes eaux · débit de base
├── précipitations · température · évapotranspiration
├── performance de modèle
└── sensibilité climatique
```

Quatre décisions à ne pas rediscuter en codant :

- **la racine EST la facette `domain`**, pas un concept nouveau. Deux
  URIs de même extension auraient été un doublon ; le rayon du catalogue
  et la grandeur sont la même chose vue de deux côtés. Ce que la facette
  ne pouvait pas dire (« il s'agit d'indicateurs calculés ») est un
  `skos:scopeNote`, la propriété SKOS faite pour ça ;
- **le rattachement phénomène → grandeur se MESURE**, il ne se déclare
  pas. Les fiches déclarent les deux, et le générateur refuse un
  phénomène qui apparaîtrait sous deux grandeurs. L'écrire dans
  `topics.yaml` aurait été une seconde source, donc une source qui peut
  mentir ;
- **les 31 variables à `purpose` pendent sous leur finalité**, pas sous
  une grandeur : leur domaine est multiple (`flow, precipitation`) et
  elles ne décrivent pas un régime mais une comparaison. Les deux
  facettes sont exclusives, le corpus est donc couvert sans reste ;
- **`aspect` entre dans le libellé de famille**, et `domain` et
  `phenomenon` en sortent puisque le parent les porte. Sans `aspect`, 57
  familles portaient le libellé d'une voisine, `VCN10` et `tVCN10` étant
  tous deux « minimum · annuelle · série ».

### Geste 1 bis : une famille est un TABLEAU, pas un concept

Tranché le 2026-08-14, après avoir regardé l'arbre. La question n'était
pas cosmétique : elle porte sur ce que le fichier AFFIRME.

Une famille regroupe les variables qui ne diffèrent que par un paramètre,
`QNA`, `VCN3`, `VCN10`, `VCN30`. C'est une construction classique de
thésaurus, antérieure à SKOS : le **tableau** de l'ISO 25964, avec son
**libellé de nœud** qui dit par quel caractère on divise. L'exemple
canonique du guide SKOS est « lait par animal d'origine », qui regroupe
lait de vache, de chèvre et de bufflonne.

**Un libellé de nœud n'est pas un concept**, et le guide SKOS le dit
noir sur blanc : le modéliser en concept est plus intuitif mais fait
perdre de la justesse. Personne n'indexe une donnée avec « Minimum
(annuelle, série) », on l'indexe avec `VCN10`.

Ce que card affirmait, et qui était faux :

```turtle
card:variable/VCN10  skos:broader  card:family/…
card:family/…        skos:broader  card:phenomenon/low-flows
```

`skos:broader` se lit « est une sorte de ». La chaîne disait donc que
`VCN10` est une sorte de casier de rangement. Ce qu'elle dit maintenant,
en deux affirmations séparées et chacune vraie :

```turtle
card:variable/VCN10  skos:broader           card:phenomenon/low-flows

card:array/…   a isothes:ThesaurusArray , iop:VariableSet ;
    isothes:superOrdinate  card:phenomenon/low-flows ;
    skos:member            card:variable/VCN10 , card:variable/VCN3 , … .
```

`isothes:` est la mise en SKOS de l'ISO 25964, publiée par la DCMI.
`ThesaurusArray` est une sous-classe de `skos:Collection`, et
`superOrdinate` est la seule façon normalisée de placer une collection
dans l'arbre, `skos:broader` lui étant interdit par le modèle SKOS.

Trois conséquences, et ce sont elles qui justifient le changement :

- **le décompte des concepts devient honnête**, 573 au lieu de 706 :
  card définit des variables et un arbre, pas 133 casiers que personne
  ne peut employer pour décrire une donnée ;
- **la hiérarchie ne passe plus par du calculé.** Les familles se
  recalculent à chaque génération ; tant qu'elles portaient la chaîne,
  une recompilation pouvait déplacer `VCN10` dans l'arbre. C'est aussi
  ce qui règle l'inquiétude sur la stabilité de leurs URI : ce qui bouge
  n'est plus dans le chemin ;
- **replier un tableau d'un seul membre ne coûte plus rien.** 65 des 133
  familles n'avaient qu'un membre ; elles ne sont plus émises, il reste
  68 tableaux qui subdivisent vraiment.

Le prix de ce choix est un défaut d'affichage, listé avec les autres
limites connues en fin de document.

#### Les 65 familles solitaires, triées

Mesuré avant de replier, et c'est une information sur le CORPUS, pas sur
le vocabulaire. Le test est simple : la variable porte-t-elle un
paramètre sémantique ? S'il y en a un, d'autres valeurs peuvent exister.

- **28 sont des trous de complétude.** `Q10`, `Q50` et `Q90` sont les
  trois seuls quantiles sur chronique entière, et ils tombent dans trois
  phénomènes différents, donc ils ne peuvent pas être frères ; `Q95` et
  `Q99` n'existent qu'en annuel. Toute la série `dtBE`, `vBE`, `tVCN10`,
  `alpha-VCN10` fige `d = 10 jours`, sans `dtBE3` ni `tVCN30`.
- **37 le resteront**, leur variable ne portant aucun paramètre : `QA`,
  `QMNA`, `QB-LH`, `dtCrue`, `RA`, `TA`, `ETPA`, et les huit fiches de
  finalité. Les grouper n'aurait aucun sens.

Les 28 premières sont un chantier de CORPUS, repris en fin de document.

### Le libellé de nœud : une phrase, puis des coordonnées

Un libellé de nœud a deux moitiés qui ne se valent pas.

```
prefLabel  « Minimum (annuelle, série) »
altLabel   « intensité · minimum · annuelle · série »
```

- **à gauche, ce que la valeur EST**, et là une phrase apporte quelque
  chose que la liste de facettes ne disait pas : `saisonnalité ×
  quantile` devient « Date d'atteinte d'un quantile », et ses membres
  sont bien début, centre et fin des écoulements lents ;
- **à droite, ses coordonnées**, qui restent les étiquettes des facettes.
  Mises en prose, elles donnaient « une valeur unique, sur la série
  annuelle » sur presque chaque voisine : six mots pour deux, répétés,
  qui noyaient la moitié qui compte. Essayé le 2026-08-14, abandonné le
  jour même.

Le synonyme garde la liste complète, et ce n'est pas une redite : c'est
ce qu'un lecteur tape dans une recherche.

**Deux tables écrites et relues, pas une grammaire.** Une règle qui
fabriquerait la phrase depuis les étiquettes se casserait au premier
accord (« minimum annuel » mais « moyenne annuelle ») et surtout au
premier sens : `saisonnalité × minimum` est « la date du minimum »,
`durée × médiane` est « la médiane d'une durée », et aucune règle ne
devine que l'aspect gouverne dans un cas et est gouverné dans l'autre.
Chaque entrée a été confrontée aux noms de ses membres.

Les tables sont petites parce que les facettes le sont : **31 couples
(aspect, opération) et 13 couples (fenêtre, forme)** couvrent le corpus
entier. Elles vivent dans `generate_skos.py`, seul artefact qui les lise.
**Un couple absent fait échouer la génération**, sans quoi une facette
ajoutée demain produirait une phrase muette dont personne ne verrait
qu'elle ment.

Deux points de forme, chacun pour une raison :

- **la phase d'une précipitation vient d'`alignments.yaml`**, qui déclare
  déjà que `Rl` est contraint à la phase liquide et `Rs` à la solide.
  Sans elle, onze tableaux portaient le libellé d'un voisin, « cumul
  annuel » ne distinguant pas la pluie de la neige. Avec, **plus aucune
  collision** ;
- **les grandeurs vont entre parenthèses**, et seulement pour les
  tableaux de finalité, dont la branche ne les dit pas.

Un tableau s'annonce « phase liquide et phase solide » alors qu'il
groupe un cumul total : ce n'est pas un défaut de libellé mais une limite
de la façon dont une famille se calcule, listée en fin de document.

### Geste 2 : la soudure, huit lignes déclarées

Dans `alignments.yaml`, section `topics:` pour les quatre premières,
section `inputs:` pour les autres :

```
card:domain/flow            skos:broadMatch  theia:c_9c959860  River discharge
card:domain/precipitation   skos:broadMatch  theia:c_a9b2927c  Precipitation amount
card:domain/temperature     skos:broadMatch  theia:c_6f0c66da  Air temperature
card:domain/evapotranspir…  skos:broadMatch  theia:c_6db0faac  Potential evapotr.

card:input/Q    skos:exactMatch  theia:c_dabd2d39  1 day mean river discharge
card:input/R    skos:exactMatch  theia:c_ee31e37f  1 day cumulative precip. amount
card:input/T    skos:exactMatch  theia:c_6496391a  Mean air temperature
card:input/ETP  skos:exactMatch  theia:c_6db0faac  Potential evapotranspiration
```

Le `broadMatch` est posé au SOMMET, et c'est ce qui le rend si petit :
leur concept générique est plus large que tout ce que card calcule sur
cette grandeur, donc la hiérarchie fait le reste. Quatre triplets, pas
444.

### Ce que le geste 2 ne suffit PAS à faire

**Skosmos n'affiche que les alignements portés par la fiche qu'on
regarde, jamais les alignements entrants** (vérifié sur leur
documentation le 2026-08-14). Donc :

- qui part de card arrive chez eux ;
- qui part de chez eux **ne voit pas card**.

D'où la seule demande structurelle : **quatre `skos:narrowMatch`
réciproques dans leur fichier**. Quatre triplets, aucun concept à
maintenir, réversible. Si c'est non, tout fonctionne quand même, en sens
unique, et rien n'est perdu.

## Les notations officielles françaises, alignées le 2026-08-14

Ce n'était pas dans ce plan, et ça y a sa place : c'est un alignement, il
vit dans `alignments.yaml`, et il ne demande rien à personne.

**Il y a deux registres, pas un**, et c'est le fait qu'on a mis le plus
de temps à voir. Le SCHAPI, avec INRAE, maintient pour le réseau
Vigicrues une **grammaire de notations statistiques**, celle qu'affiche
l'interface d'HydroPortail. Le Sandre maintient à côté la **nomenclature
513**, « type de grandeur de l'observation élaborée Hydro », dont les
codes viennent de l'ancienne Banque Hydro. `VCN10` et `Q10J-N` sont la
même variable dans les deux.

**Les trois grammaires descendent du même texte**, la nôtre comprise.
Leur dictionnaire dit avoir été bâti, entre autres, sur « Normalisation
des variables dans les modèles hydrologiques descriptifs », G. Oberlin,
1992, qui est aussi la source de la nomenclature de card (cf.
`NOMENCLATURE.md`). Ce n'est donc pas un rapprochement de circonstance,
c'est une divergence entre héritiers, et c'est pourquoi card a hérité de
`VCN10` et de `QMNA` sans jamais les copier.

Les tables sont dans `alignments.yaml`, une par registre, et ne sont
recopiées nulle part.

**Ne figure que ce qui est certain** : ce que leur documentation ou leur
interface donnent explicitement, et ce qui s'en déduit par simple
substitution d'un nombre. Une seule ligne fait exception, `QNA` vers
`QJ-N`, déduite d'une grille dont trois cases sur quatre sont attestées,
et elle le dit dans le fichier.

### Ce qui a été mesuré sur leur usage réel, et non sur leur dictionnaire

Fait le 2026-08-14, après avoir constaté que le dictionnaire ne suffisait
pas : lecture des quatre documents publics, de l'aide en ligne, de la
nomenclature Sandre, et de la fiche de statistiques d'une station réelle
(le Célé à Orniac, `O8133520`).

- **Une station publie quatre analyses de référence**, nommées
  `<notation nouvelle> (<sigle ancien>)` : `QJ-annuel` en toutes eaux,
  `QM-N (QMNA)` et `Q3J-N (VCN3)` en basses eaux, `Q-X (CRUCAL)` et
  `QJ-X (CRUCAL)` en hautes eaux.
- **`QJ-annuel` EST le `QA` de card**, et la fiche affiche ses
  paramètres : année hydrologique du 01/09 au 31/08, extracteur moyenne,
  grandeur `QmnJ` à un jour. Même fenêtre par défaut que card, sans que
  personne l'ait cherché.
- **Le module a un code à lui**, `Module` au Sandre, « débit moyen
  inter-annuel ». C'est `mean-QA`, et il n'y a donc rien à composer.
- **Ils ont plusieurs écritures par variable et le disent** : « `Qm1J`,
  raccourci en `QmJ` même plutôt `QJ` », « `QmM-N`, raccourci en
  `QM-N` ». Publier plusieurs `skos:notation` par registre n'est pas une
  licence qu'on prend, c'est refléter leur pratique.

Ce que cette lecture a relevé chez eux vit dans `RETOURS_SCHAPI.md`, et
nulle part ailleurs. Ce qu'ils calculent et que card n'a pas est un
inventaire de corpus, dans `CHANTIERS.md`.

### Ce qui est écarté, et pourquoi

- **les fenêtres saisonnières** (`_summer`, `_winter`) : leur extracteur
  est annuel par défaut et une fenêtre partielle n'est pas dans leur
  grammaire ;
- **les quantiles annuels** (`Q90A`…) : leur notation de fréquence porte
  sur la chronique entière, pas sur chaque année, et leur ligne le dit,
  « sur la chronique analysée » ;
- **les réductions inter-annuelles autres que la moyenne** (`median-`,
  `delta-`, `alpha-`) : voir plus bas, la question est close ;
- **les codes paramétrés du Sandre** (`VCN`, `VCX`, `DCn`) : `VCN`
  désigne `VCN3`, `VCN10` et `VCN30` à la fois. Un code qui désigne trois
  concepts n'est pas une notation, c'est une famille.

**Deux faux amis à connaître.** `QJ` désigne chez eux la chronique des
débits moyens journaliers, et chez card le régime journalier
inter-annuel : c'est l'entrée `Q` de card qui est alignée sur leur `QJ`,
jamais la variable `QJ`. Et chez eux, `QJ(Min)` est le minimum sur la
chronique entière quand `QJ-N` est la série des minimums annuels. C'est
la raison pour laquelle la table est écrite à la main.

### Comment ça sort en RDF

Une notation SKOS est un code dans un système de notation, et le système
se dit par le TYPE du littéral. C'est la mécanique prévue pour qu'un même
concept porte plusieurs codes sans qu'on les confonde :

```turtle
card:variable/VCN10
    skos:notation  "VCN10" ;
    skos:notation  "Q10J-N"^^card:notation/hydroportail ;
    skos:notation  "Qm10J-N"^^card:notation/hydroportail .

card:variable/QA
    skos:notation  "QA" ;
    skos:notation  "QJ-annuel"^^card:notation/hydroportail ;
    skos:notation  "QmA"^^card:notation/sandre-nsa513 .
```

La notation propre à card reste un littéral nu, qui est la lecture par
défaut du vocabulaire ; les notations étrangères s'annoncent. Chaque type
est déclaré dans le fichier, avec le titre du registre, son adresse et
les documents qui le définissent.

Le nom du registre suffit à le faire sortir : `alignments.yaml` porte les
deux sous une seule clé `notations:`, le générateur la parcourt, et le
type du littéral se déduit du nom. **Un troisième registre ne demanderait
aucune ligne de code.**

Trois tests le gardent honnête : toute clé des tables est une vraie
variable du corpus, tout registre déclare sa source, et **aucun code
n'est attribué deux fois DANS UN REGISTRE**, seul symptôme qu'une machine
puisse voir d'une correspondance erronée entre deux grammaires aussi
proches. Le doublon se mesure registre par registre parce qu'un même code
peut vivre dans les deux sans rien dire de faux : `QMNA` est le symbole
de card et le code du Sandre.

## Ce qui bloque l'option B, après audit

Le volume a changé de camp (§ ci-dessus). Restent, inchangés :

1. **Leur thésaurus est en ANGLAIS SEULEMENT.** Aucun `prefLabel@fr`
   dans les 23 086 triplets. La moitié de ce que les fiches écrivent
   n'aurait nulle part où aller.
2. **Ils n'emploient aucun `skos:notation`.** La porte d'entrée de card
   est le symbole, cité dans les publications et dans les colonnes des
   tableaux.
3. **On perdrait la génération.** `card.ttl` se régénère à chaque
   changement et un test refuse l'écart : le thésaurus ne PEUT PAS
   diverger des fiches. Dans leur outil d'édition, la définition
   existerait à deux endroits. **C'est le seul argument technique
   décisif**, et c'est la dernière question de `QUESTIONS_THEIA.md`.
4. **La cadence et la charge.** Une version de fiche change une
   définition ; leur thésaurus est une référence de communauté qui bouge
   lentement.

## L'hébergement : un précédent qu'ils ont posé eux-mêmes

Ils exploitent un Skosmos multi-vocabulaire à Montpellier
(`skosmos.msem.univ-montp2.fr`) qui sert `theia_in_situ`,
`theia_spatial` et **le thésaurus de l'UNESCO**, donc un vocabulaire qui
n'est pas le leur. Servir `card.ttl` de la même façon est un graphe de
plus et une entrée de configuration, pas une demande d'infrastructure.

Un vocabulaire vit dans son propre espace, avec ses propres URIs, sa
propre page d'accueil et sa propre recherche. Ils n'éditent rien, on leur
passe le fichier à chaque version. Ordre de préférence inchangé : chez
eux, sinon EarthPortal, et de toute façon en téléchargement chez nous.

### L'objet d'intérêt du débit : `River`, tranché le 2026-08-14

card déclarait `Surface water` (c_d73ddccf) là où leur `River discharge`
déclare `River` (c_97bb7b91). Le corpus est bâti sur des chroniques de
stations hydrométriques de cours d'eau et aucune fiche ne vise un plan
d'eau : c'est donc `River`, sur les quatre entrées de débit (`Q`,
`Q_obs`, `Q_sim`, `Q_lim`) et par conséquent sur les 229 variables qui en
dérivent.

Ce n'est pas un changement de camp mais une descente d'un cran dans LEUR
hiérarchie, `River` étant un enfant de `Surface water`. Et c'est ce qui
autorise l'`exactMatch` de `card:input/Q` vers
`1 day mean river discharge` : viser leur concept de rivière en disant
« eau de surface » aurait affirmé plus qu'on ne savait.

Les trois autres grandeurs n'étaient pas concernées, leur objet étant
déjà juste (Precipitation, Air, Evapotranspiration).

## Ce qui reste ouvert

Un seul endroit, pour n'avoir à en lire qu'un. Rien de ce qui suit ne
bloque quoi que ce soit : le vocabulaire est complet et se régénère.

### Ce qui attend une action de l'utilisateur

**Le courriel à Theia/OZCAR.** Son contenu est dans `QUESTIONS_THEIA.md`
et nulle part ailleurs. Tant qu'il n'est pas parti, la base d'URI,
l'hébergement et la publication restent différés, et c'est la seule
décision irréversible du chantier.

**Le retour au SCHAPI**, si tu veux le faire. Son contenu est dans
`RETOURS_SCHAPI.md` et nulle part ailleurs. Rien n'en dépend chez nous :
l'alignement tient sans réponse. Deux points leur seraient utiles, la
forme de notation qui fait foi et l'écriture du module.

### Les réductions inter-annuelles : question close, et pas par prudence

Elle l'était par prudence jusqu'au 2026-08-14 ; elle l'est maintenant par
mesure, et il ne faut pas la rouvrir sur un souvenir.

La forme `Variable(Opérateur)` **s'applique bien à une variable déjà
extraite**, contrairement à ce qui était écrit ici : leur tableau donne
`Qjanvier(Moyen)`, « moyenne interannuelle des débits mensuels de
janvier », avec la formule qui réduit sur l'ensemble des années. Ce n'est
donc pas la forme qui manquait.

Ce qui manque est ailleurs, et rien ne le comblera :

- **`median-`** : les quinze variables `median-` de card réduisent des
  dates, des durées et des volumes d'étiage, dont **aucune base n'a de
  notation officielle**. Il n'y a rien à composer ;
- **`delta-`, `alpha-`, `n-`** : leur opérateur est une statistique
  descriptive d'un échantillon, « Moyen, Médian, Min ou Max… ». Un écart
  entre deux horizons, une pente de Sen et un décompte d'années n'en sont
  pas. Et la parenthèse numérique est déjà prise par la période de
  retour, donc `delta-VCN10` ne pourrait pas s'écrire sans collision ;
- **`mean-QA`** est le seul cas qui restait, et il est réglé : le Sandre
  lui donne `Module`. Aucune composition à inventer.

### Trois limites connues du modèle

- **Les tableaux dépendent d'une option d'affichage.** Un navigateur ne
  les montre que s'il est configuré pour, `arrayClass` chez Skosmos.
  Sans elle, les variables apparaissent à plat sous leur phénomène.
  C'est le prix de la justesse, assumé le 2026-08-14, et une ligne de
  plus à demander à l'hébergeur le jour venu.
- **Une famille se calcule sur les entrées de la FICHE**, pas sur celles
  de la variable. `RA` n'a besoin que de `R`, mais la fiche groupée qui
  le produit lit aussi `Rl` et `Rs` : il appartient donc à deux tableaux,
  dont l'un s'annonce « phase liquide et phase solide ». Trois variables
  sont dans ce cas. Se corrigerait en dérivant la famille des entrées
  réellement consommées, ce que `list_cards()` ne rend pas.
- **La grossièreté des tableaux de variables dérivées.** `delta-VCN10` se
  retrouve avec les écarts d'autres variables de base, parce que
  l'identité d'une variable dérivée dépend de sa variable de BASE, qui
  n'est pas une facette. Ce n'est pas faux, c'est moins fin qu'ailleurs.
  Affiner demanderait de déclarer la variable de base sur les fiches
  `delta-`, `median-`, `alpha-`. À trancher seulement si ça gêne à
  l'usage.

### Un chantier de CORPUS, pas de vocabulaire

**Les 28 trous de complétude** relevés en repliant les tableaux : `Q95` et
`Q99` n'existent qu'en annuel quand `Q90` existe aussi sur la chronique ;
toute la série `dtBE`, `vBE`, `tVCN10`, `alpha-VCN10` fige `d = 10 jours`
sans `dtBE3` ni `tVCN30`. Ce sont des choix scientifiques. La liste se
recalcule en repérant les tableaux d'un membre dont la variable porte un
paramètre, elle n'a donc pas à être recopiée.

### Un abandon qui tient toujours

**Skosmos en local**, abandonné après deux tentatives : l'image
officielle est fermée, les images tierces ne sont pas maintenues, et
Fuseki sert son jeu de données en lecture seule. Ce qu'on voulait savoir
(« est-ce que ça passera chez eux ? ») est répondu par `skosify`, qui est
leur propre outil de qualité et qui passe.

---

Ce qui est déjà tranché et qu'on ne rouvre pas est dans
`PLAN_SITE_SKOS.md`, y compris l'audit des vocabulaires, qui reste la
référence du modèle : ce que SKOS, I-ADOPT, CPM, CF, QUDT et OWL-Time
savent dire, et ce que card publie avec chacun.
