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
