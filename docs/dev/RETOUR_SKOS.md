> **Statut : journal d'exécution, temporaire.** Ce que chaque étape du
> chantier SKOS a donné, ce qui a résisté, et les doutes qui restent. La
> CONCEPTION vit dans `PLAN_SITE_SKOS.md` ; ici on ne consigne que le
> déroulé, pour que la reprise à froid ne reparte pas de zéro.
> À SUPPRIMER quand le chantier est livré : son contenu utile aura
> rejoint le CHANGELOG et le plan.

# Journal d'exécution du chantier SKOS

## Étape 4b : la colonne `family` — **faite**

### Ce qui marche

La famille se calcule depuis les facettes que la fiche déclare déjà, plus
ses variables d'entrée, et rien d'autre. **132 familles** sur les 472
variables, le même compte que l'analyse préalable, donc l'implémentation
reproduit ce qui avait servi à décider.

Les cas qu'on voulait voir marcher marchent :

```
family_of("VCN10")  →  QNA, VCN3, VCN10, VCN30
family_of("KGE")    →  KGE, KGEsqrt, NSE, NSEinv, NSElog, NSEsqrt
family_of("QMA_jan")→  les douze mois
```

`QNA` dans la famille des VCN est la validation la plus parlante : c'est
le cas d'une moyenne mobile d'un jour, et aucune recherche par nom ne le
trouverait.

Deux défauts corrigés en cours de route, tous deux trouvés en regardant
les valeurs plutôt qu'en relisant le code :

- les **paramètres de période** (`ref_start`, `horizon_end`…) entraient
  dans l'identité, ce qui séparait `delta-VCN10` de ses frères pour une
  raison qui n'a rien de sémantique. Filtrés par `type: date` du registre
  `inputs.yaml` ;
- l'ordre des entrées n'était pas stable (`Q` majuscule triait avant les
  minuscules), donc deux fiches équivalentes pouvaient recevoir deux
  identifiants. Normalisé avant tri.

### Ce qui marche moins, et c'est un doute à regarder ensemble

**La famille est parfois plus GROSSIÈRE qu'un jeu de frères.** Elle est
exacte pour les variables de premier ordre, et coarse pour celles qui
s'appliquent à une AUTRE variable :

```
family_of("delta-VCN10")  →  delta-Q90A, delta-Q95A, delta-Q99A,
                             delta-QNA, delta-VCN10, delta-VCN10-5,
                             delta-VCN3, delta-VCN30, delta-vLF
```

Ce ne sont pas des variantes d'un même concept : ce sont les écarts de
variables de base DIFFÉRENTES. Elles partagent « écart d'une magnitude de
basses eaux, annuel, scalaire », ce qui est vrai mais large.

La cause est nette : pour une variable dérivée, l'identité dépend de sa
variable de BASE, et la variable de base n'est pas une facette. Elle vit
dans la chaîne de process et dans le nom.

**Ce n'est pas faux pour autant.** `skos:broader` veut dire « a pour
concept plus large », pas « est une variante paramétrée ». Un
`delta-VCN10 broader <écart d'une magnitude de basses eaux>` est un
énoncé juste, simplement moins fin qu'ailleurs. Les familles concernées
sont celles des statistiques de second ordre : `change` (83 variables),
`median` inter-annuelle, `trend`.

Trois cas mesurés où la famille est trop large :

| famille | membres | pourquoi c'est large |
|---|---|---|
| `…change.annual.scalar.q` (basses eaux) | 9 | écarts de bases différentes |
| `…timing.median.annual.scalar.q` | 4 | médianes de dates différentes |
| `…wet-days.duration.threshold-exceedance.by-season` | 8 | mélange `dtCWDSA` et `dtRSA01mm` |

**Piste, non retenue pour l'instant** : déclarer la variable de base
d'une variable dérivée. Ça affinerait la hiérarchie, ça coûterait un
champ sur les fiches dérivées, et ça n'est nécessaire que si le rendu
dans Skosmos montre que la grossièreté gêne. À décider en voyant, pas
avant.

### Choix d'implémentation, et pourquoi

- **Calculée dans `_meta_rows`**, donc disponible partout où `meta` l'est :
  `extract`, `list_cards`, card-api. Une seule source.
- **Par VARIABLE et non par fiche** : `allLF` produit cinq variables
  d'`aspect` différents, donc de familles différentes. `cfield` donnait
  déjà le découpage.
- **Import tardif de `schema`** : `schema` importe `extraction`, donc
  l'inverse au niveau module ferait un cycle. `render` fait déjà ainsi.
- **Deux filtres** : `family=` pour la valeur brute, et surtout
  `family_of="VCN10"` qui répond à la vraie question, « donne-moi ses
  variantes », sans qu'on ait à lire un identifiant. Un nom inconnu lève
  une erreur explicite au lieu de rendre un tableau vide, parce qu'une
  famille vide et une variable inexistante se ressemblent trop.

### Vérifications

Suite complète verte, linter des fiches vert, ruff propre.
`tests/test_family.py` couvre les six invariants : la famille rassemble
les variantes, elle diffère d'une recherche par sous-chaîne, les
paramètres de période ne la scindent pas, elle est faite de slugs et non
d'étiquettes, aucune variable n'en est dépourvue, et un nom inconnu lève.

## Étape 5 : `alignments.yaml` — **faite**

### Ce qui marche

**Les quatre grandeurs d'entrée de card sont alignées chez Theia**, et
les URIs ont été RELEVÉES sur leur service, jamais devinées :

| entrée | propriété | objet d'intérêt |
|---|---|---|
| `Q` | Discharge | Surface water |
| `R` | Volume per area | Precipitation |
| `T` | Temperature | Air |
| `ETP` | Volume per area | Evapotranspiration |

Plus deux correspondances de VARIABLE entière (`same_as`), quand elle
existe chez eux : `T` vers « Air temperature », `ETP` vers « Potential
evapotranspiration ». Et cinq des dix-huit statistiques : Average,
Median, Minimum, Maximum, Accumulation.

`scripts/verifie_alignements.py` résout les **30 références externes** sur
leur service : toutes répondent.

### Une découverte qui a changé la table

Leur « Air temperature » est un `iop:Variable` **sans décomposition** :
seuls ses enfants (« at 2 meters height »…) portent `hasProperty` et
`hasObjectOfInterest`. Donc les entrées de card ne s'alignent pas sur
leurs *propriétés* mais correspondent à leurs *variables*, dont il faut
lire les composants. D'où deux champs distincts dans la table : les
composants pour bâtir nos variables, et `same_as` pour l'alignement
proprement dit. Une table à un seul champ aurait été fausse.

### Le test a fait son travail avant moi

`test_every_parameter_of_the_corpus_is_decided` a refusé le fichier :
trois paramètres employés par le corpus n'y figuraient nulle part,
`cyclical`, `norm_spacing` et `relative`. Je ne les avais pas vus.

Les trois sont des options et non des contraintes, et la raison est
écrite dans le fichier pour chacune. Le cas de `relative` mérite d'être
retenu : un écart en pourcentage et un écart en unité SONT deux
grandeurs différentes, donc j'ai hésité. Mais la différence est déjà dite
par `meta.unit`, et le choix découle de la nature de la variable
(`meta.global.relative`) au lieu de distinguer deux fiches frères. Il ne
crée donc pas de contrainte.

### Ce qui reste en doute

**`S`, la surface du bassin, n'a aucun alignement.** Je n'ai pas trouvé
d'équivalent chez eux et j'ai préféré laisser `null` que rattacher de
force. C'est une colonne constante fournie par l'appelant, pas une
grandeur observée, donc l'absence se défend. À revoir si un jour une
fiche la publie en sortie.

**Le réseau n'est pas dans la suite de tests**, et c'est un choix : un
test qui sort échoue les jours où le service d'en face tousse, et ce
qu'on apprend alors n'est pas ce qu'on cherchait. La suite vérifie la
cohérence interne (toute entrée traitée, tout slug réel, tout paramètre
décidé, aucun déclaré deux fois, aucune famille vide), et le script
vérifie la résolution à la demande.

## Étape 6 : `generate_skos.py` et `card.ttl` — **faite**

### Ce qui marche

```
docs/card.ttl : 10 455 triplets, 657 concepts, 132 familles
base d'URI PROVISOIRE : https://example.invalid/card/  (rien n'est publié)
```

`.invalid` est réservé par la RFC 2606 et ne résoudra **jamais** : personne
ne peut prendre une URI de ce fichier pour un identifiant pérenne. Un test
refuse toute URI hors de cette base, pour que le jour où la vraie arrive,
ce soit une DÉCISION et non un oubli.

Un concept complet, tel qu'il sort :

```turtle
card:variable/VCN10
    a skos:Concept, iop:Variable ;
    skos:notation   "VCN10" ;
    skos:prefLabel  "Annual minimum of 10-day mean daily discharge"@en ,
                    "Minimum annuel de la moyenne sur 10 jours du débit journalier"@fr ;
    skos:broader    card:family/flow.low-flows.magnitude.minimum.annual.series.q ;
    iop:hasProperty            theia:c_7742e5f0 ;   # Discharge, chez EUX
    iop:hasObjectOfInterest    theia:c_d73ddccf ;   # Surface water, chez EUX
    iop:hasStatisticalModifier card:statistic/minimum ;
    iop:hasConstraint          card:constraint/rolling-window-10 ;
    rdfs:isDefinedBy           card:card/VCN10 ;
    dcterms:subject card:domain/flow, card:phenomenon/low-flows,
                    card:aspect/magnitude, card:season/annual,
                    card:output/series .
```

`VCN10-5` porte bien ses **deux** contraintes, durée et période de retour.

### Trois défauts de libellé, trouvés en lisant les valeurs

Aucun n'aurait été vu en relisant le code :

- « fenêtre glissante de 10 **day** » : l'unité n'était pas traduite. Les
  unités sont devenues bilingues dans `alignments.yaml` ;
- « seuil de précipitation de 20 **mms** » : ma règle de pluriel prenait
  `mm` pour un mot. `invariable` est maintenant DÉCLARÉ, parce que « an »
  et « mm » font deux caractères chacun et qu'aucune règle de forme ne
  les sépare ;
- `fdc_slope` reçoit `p: (0.33, 0.66)`, une PAIRE et non une valeur : la
  contrainte est un intervalle, et elle se lit désormais « exceedance
  probability between 0.33 and 0.66 ».

### Le libellé des familles : liste, pas phrase

`flow · low flows · minimum · annual · series`. J'ai d'abord essayé une
phrase (« annual minimum of flow »), et le français casse à la première
question d'accord : « minimum annuel » mais « moyenne annuelle ». Le
séparateur dit franchement qu'on énumère, ce qui est la vérité, et une
`editorialNote` précise que le parent est généré.

À revoir en voyant le rendu dans Skosmos : c'est exactement le genre de
chose qui se juge à l'écran.

### Le test a encore trouvé avant moi, et cette fois dans le CORPUS

`test_one_preflabel_per_language_and_concept` a refusé le fichier : quatre
variables portaient deux `skos:prefLabel` anglais. La cause n'est pas le
générateur, c'est que **28 variables sont produites par deux fiches** et
que **sept d'entre elles sont décrites autrement selon la fiche** :

```
RA   « Cumulative annual total precipitation »  (fiche RA)
     « Annual total precipitation »             (fiche RA_all)
vLF  « Volume deficit of low flows »            (fiche allLF)
     « Low flow deficit volume »                (fiche vLF)
```

Ce sont des synonymes, pas deux sens. Le générateur retient le premier et
fait de l'autre un `skos:altLabel`, ce qui respecte la norme et ne perd
rien. Mais **c'est une dérive du corpus**, et elle grandira à chaque fiche
groupée ajoutée : consignée dans `CHANTIERS.md` avec les deux façons de
la traiter.

### Choix d'implémentation

- **rdflib plutôt qu'un gabarit de texte** : l'échappement Turtle, les
  étiquettes de langue et la sérialisation canonique ne se réécrivent pas
  à la main sans se tromper une fois sur dix. Il reste hors des
  dépendances d'exécution (`dev` seulement) : personne n'installe card
  pour produire du RDF.
- **La garde est un test qui RELANCE le générateur** et compare, comme
  `test_catalogue.py`. La ligne `dcterms:modified` est exclue de la
  comparaison, sans quoi le test échouerait chaque jour sans que rien
  n'ait bougé.
- **Aucune référence pendante** : un test vérifie que toute URI interne
  citée est aussi décrite. Les URIs externes sont exclues, elles sont
  décrites chez leur propriétaire, c'est tout l'intérêt d'un alignement.

### Ce qui reste en doute

**Le libellé des familles**, à juger à l'écran.

**Les 202 `skos:definition` absentes** : c'est la règle du corpus, mais un
navigateur de thésaurus affichera 202 concepts sans définition. À voir si
ça choque dans Skosmos, sachant que `card:method` porte l'énoncé du
calcul et pourrait servir de repli.

**Rien n'est fait pour la dépréciation** : aucune fiche n'est retirée
aujourd'hui, donc `owl:deprecated` n'a pas de cas d'usage. Le jour où une
fiche part, il faudra le champ `status` prévu au plan, sans quoi le
concept disparaîtra du fichier au lieu d'être marqué.

### Une dépendance d'ordre, trouvée par la garde

Le `.ttl` porte `owl:versionInfo` du PAQUET. Il périme donc à chaque coupe
de version, et il faut le régénérer **après** `set_version.py`, jamais
avant. C'est le test qui me l'a appris, en refusant le fichier juste après
la montée en 0.8.0. La règle est écrite dans le CLAUDE.md, à côté de celle
du catalogue.

## Étape 7 : voir le rendu — **partiellement faite**

### Ce qui a marché, et c'est le plus utile

**`skosify`, l'outil de qualité SKOS écrit par l'équipe de Skosmos
elle-même**, passe sur le fichier. C'est le signal qui compte : si leur
propre validateur est content, leur navigateur le sera.

Il a trouvé deux vrais défauts de structure, corrigés :

- **le schéma n'avait pas de libellé** : `dcterms:title` ne suffit pas,
  les outils cherchent `rdfs:label`. Un vocabulaire sans nom s'affiche
  sans nom ;
- **188 concepts orphelins**, c'est-à-dire sans parent ni statut de tête,
  donc qu'un navigateur ne sait pas par où prendre. Corrigé en découpant
  en **un schéma de concepts par facette**, plus un pour les contraintes,
  ce que la conception d'origine prévoyait d'ailleurs. Il en reste zéro.

Deux tests gardent l'acquis sans imposer la dépendance : aucun concept
orphelin, aucun schéma sans libellé.

Ce que le fichier donne maintenant, tel qu'un navigateur l'afficherait :

```
Schémas
   card:                    132 concepts de tête   (les familles)
   card:scheme/statistic     18
   card:scheme/phenomenon    11
   card:scheme/constraint     7
   …

Une famille dépliée : « débit · basses eaux · minimum · annuelle · série »
   └─ Minimum annuel du débit journalier
   └─ Minimum annuel de la moyenne sur 10 jours du débit journalier
        contrainte : fenêtre glissante de 10 jours
   └─ Minimum annuel de la moyenne sur 3 jours du débit journalier
        contrainte : fenêtre glissante de 3 jours
   └─ Minimum annuel de la moyenne sur 30 jours du débit journalier
        contrainte : fenêtre glissante de 30 jours
```

C'est exactement ce qu'on voulait obtenir, et `QNA` y figure sans
contrainte, ce qui est juste : c'est le cas d'une fenêtre d'un jour.

### Ce qui n'a pas marché : Skosmos en conteneur

J'ai arrêté après deux tentatives, et je préfère le dire que de laisser
croire que c'est fait.

- **l'image officielle est fermée** : `ghcr.io/natlibfi/skosmos` répond
  `denied` sans authentification ;
- **les images tierces ont zéro étoile** et ne sont pas maintenues ;
- **Fuseki démarre**, mais l'image la plus suivie (`secoresearch/fuseki`,
  15 étoiles) sert son jeu de données en **lecture seule** : `POST` et
  `PUT` répondent `405`. Il faudrait une autre image ou une configuration
  Fuseki écrite à la main, puis un second conteneur Skosmos avec son
  fichier de configuration PHP.

Ça devenait le tank qu'on voulait éviter, pour un gain esthétique : la
question « est-ce que ça marchera chez eux » est déjà répondue par
`skosify`, qui est leur outil.

**À reprendre si tu veux vraiment l'écran**, et ce sera une session à
part : soit avec les images du dépôt Skosmos construites localement, soit
en demandant à Theia de charger le fichier chez eux, ce qui est de toute
façon l'étape suivante.

### Ce qui reste en doute

**Le libellé des familles** reste à juger : « débit · basses eaux ·
minimum · annuelle · série ». Il est honnête et il ne peut pas dériver,
mais il n'est pas beau. Maintenant qu'on voit la hiérarchie dépliée, la
question se pose autrement : le parent sert surtout à REGROUPER, et son
libellé est lu une fois pour dix libellés d'enfants qui, eux, sont
parfaits. Je le laisserais tel quel.

**Les 202 concepts sans définition** ne se voient pas dans ce rendu
textuel. Ils se verront à l'écran.
