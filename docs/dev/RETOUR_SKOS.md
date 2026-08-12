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
