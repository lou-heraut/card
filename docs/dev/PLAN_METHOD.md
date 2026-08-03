> **Statut : plan de travail ouvert.** Refonte du champ `method` des
> fiches, et séparation des responsabilités entre une fonction (sa
> docstring) et une fiche (son `method` et ses `process`). Un lot livré
> en sort et devient une entrée de `CHANGELOG.md`. Quand tous les lots
> sont sortis, ce fichier disparaît.
>
> Mesures refaites le 2026-08-03 sur le corpus entier, au commit
> `60caa8c`, par exécution du vrai code. Elles datent : les refaire si le
> corpus a bougé, ce sont des observations, pas des invariants.

# `method` : une phrase par colonne produite

## En trois phrases

**Le but.** Séparer deux responsabilités confondues : la docstring d'une
fonction décrit la fonction *en général*, le `method` d'une fiche décrit
ce que *cette* fiche fait à chaque étape. La figure affichait des
docstrings, qui ne peuvent jamais être assez précises.

**Ce qui est fait au 2026-08-03.** Les **lots A, A-bis, B, C et D sont
livrés** : le corpus entier est migré, `card/method.py` assemble la forme
publiée, le linter tient les sept règles, la chaîne publiée se lit sans
les clés, et la moitié gauche est confrontée au process à chaque
passage en CI, la figure affiche la phrase de la fiche au lieu de la
docstring de la fonction, et les moitiés droites ont été relues sous la
charte. Le détail de ce qui a bougé est dans `CHANGELOG.md`, sous
`## Non publié`.

**Ce qui reste.** Les lots E et F en fin de document.

**Arbitrage à ne pas rouvrir.** `method` donne à voir les ÉTAPES du
process d'agrégation, pas chaque subtilité : quand le geste est simple et
direct, « calcul du NSE » suffit. La complétude est portée par `name` et
`description`, dont l'absence sur une fiche sur deux est un chantier à
part (CHANTIERS).

## Le problème de départ

La figure de `dtFlood` affiche, sous `apply_threshold(dQ)   dQ >= lowLim,
select=dQXA, durée`, la phrase « Analyse des épisodes où X franchit un
seuil lim ». La ligne d'appel venait de rendre le geste concret, la glose
le ré-abstrait avec les noms de la signature.

Cause structurelle : une glose est attachée à une **fonction**, donc elle
ne peut dire que du général. `apply_threshold` sert dans `dtFlood` à
mesurer une durée de crue et dans `median-startLF` à dater un début
d'étiage. Aucune phrase unique ne peut servir les deux.

Le texte qui manque à la figure existe déjà : c'est `method`. Mais
`method` est une chaîne numérotée, sans aucun lien machine avec le
process qu'elle décrit. Rien ne peut y chercher « la phrase de P4 ».
**Rendre `method` adressable est le geste central ; tout le reste en
découle ou en est indépendant.**

## Les quatre responsabilités

- **La fonction et sa docstring.** Ce que la fonction fait *en général*,
  pour qui l'appelle. `X`, `lim`, `a`, `b` y sont corrects, c'est la
  signature. N'a rien à faire dans une figure de fiche.
- **La fiche et son `method`.** Ce que fait *cette* fiche, étape par
  étape, en langage humain, une ligne complète et autoportante, copiable
  dans un document sans rien exécuter. Donnée primaire.
- **La fiche et ses `process`.** La vérité machine.
- **Le lien entre les deux derniers.** `method` et `process` sont deux
  énoncés **indépendants** de la même étape. C'est parce qu'ils sont
  indépendants qu'ils peuvent se contredire, donc qu'un test peut les
  confronter. **Générer l'un depuis l'autre détruirait ce contrôle.**

La figure ASCII n'est aucune de ces quatre choses : c'est un rendu parmi
d'autres, remplaçable. La donnée YAML doit survivre au code.

## La règle

> **Une entrée par colonne que ce process produit, indexée par le nom de
> cette colonne.**

`method` est une table indexée par process, et la valeur de chaque
process est une table indexée par colonne produite. Toujours, y compris
quand le process ne produit qu'une colonne, et y compris quand les textes
se répètent. Une seule forme, aucune exception : une forme qui change
selon le contenu se lit mal et cache les trous, et c'est cette variation
qui a laissé `allLF` diverger.

### Ce qu'est une colonne produite

Elle se lit dans le `process`, sans données :

| `compress` | `time_step` | colonnes produites par une entrée `func` |
|---|---|---|
| absent ou faux | quel qu'il soit | la clé de `func`, telle quelle |
| vrai | `season`, `year-season` | la clé suffixée `_<saison>`, une par saison de `seasons:` |
| vrai | `month`, `year-month` | la clé suffixée `_jan` … `_dec` |
| vrai | autre (`none`, `year`) | la clé, telle quelle |

C'est `compress` qui décide, pas le pas de temps. Mesuré le 2026-08-03,
même fiche exécutée deux fois :

```
QSA_season, compress: true      colonnes : QSA_DJF, QSA_MAM, QSA_JJA, QSA_SON
QSA_season, compress retiré     colonnes : QSA, year_season   (format long)
```

La clé `QSA` du bloc `func:` n'existe alors nulle part dans la sortie :
elle n'est pas une colonne, c'est un nom intermédiaire que stase suffixe.
Indexer `method` par elle mettrait un seul texte dans la fiche pour
quatre colonnes de sortie, et laisserait le code fabriquer les trois
autres. **La fiche est dimensionnée comme sa sortie.**

### La clé n'est pas traduite

Les mêmes clés en `meta.en` et en `meta.fr`, parce que ce sont des
identifiants. `variable:` en français (`debutBE`, `centreBE`) est un
libellé d'affichage : il ne nomme aucune colonne, il ne garantit rien
dans l'enchaînement des process. L'unicité et le chaînage reposent sur le
code neutre, qui suit historiquement la nomenclature anglaise, sans slug
intermédiaire. C'est déjà la règle de `process:`, dont les clés ne sont
pas traduites, et celle de `render.py`, qui affiche l'identifiant et met
le libellé traduit entre parenthèses.

Conséquence pratique : la parité fr/en de `method` se teste en une
comparaison d'ensembles de clés.

### Deux fan-out, et un seul est énumérable

Une colonne de sortie peut être démultipliée de deux façons, et la
distinction commande tout ce qui suit.

| | `compress` | `suffix` |
|---|---|---|
| Exemple | `QSA` donne `QSA_DJF` … `QSA_SON` | `rp-VCN10` donne `rp-VCN10_DOE`, `rp-VCN10_DCR` |
| D'où viennent les clés | de la fiche (`seasons:`, ou les douze mois) | de l'appel (`suffix=['DOE', 'DCR']`) |
| D'où viennent les valeurs | des données d'entrée | de colonnes d'entrée suffixées (`Q_lim_DOE`) |
| Connu à l'écriture de la fiche | oui, fermé | non, ouvert |
| Porté par | une entrée de `method` par colonne | un placeholder `{suffix.…}` |

D'où la règle qui sépare ce qu'on écrit de ce qu'on laisse fabriquer :

> **Ce que la fiche peut énumérer, elle l'écrit. Ce qu'elle ne peut pas
> énumérer, elle le déclare par un placeholder, avec son défaut.**

Les deux moitiés de cette règle se tiennent. Déduire `[01-03, 31-05]`
depuis `sampling_period` serait fabriquer du texte que la fiche connaît
et refuse d'écrire. Un placeholder est l'inverse : la fiche marque un
trou qu'elle est incapable de remplir, et déclare dans `suffix_default`
de quoi le boucher en l'absence de suffixe, ce qui la garde lisible
telle quelle. Aucune accolade ne sort jamais d'un champ de `meta`
(CHANTIERS §9, règle 1).

Les placeholders restent donc pleinement en service dans `method`, et
c'est la **seule** couche mécanique admise entre le YAML et la phrase
publiée.

## Ce que ça donne

### `dtFlood`, une colonne par process

```yaml
# avant
    method: |
      1. aucune agrégation temporelle - différence Qr entre les valeurs
         journalières de débit par le débit de base
      2. agrégation annuelle [Mois du minimum des débits mensuels] - maximum de Qr
      3. agrégation annuelle [Mois du minimum des débits mensuels] - division par
         deux des maxima annuels pour obtenir un seuil
      4. agrégation annuelle [Mois du minimum des débits mensuels] - nombre de
         jours où la différence est supérieure au seuil

# après
    method:
      P1:
        dQ: aucune agrégation temporelle - différence Qr entre le débit journalier et le débit de base
      P2:
        dQXA: agrégation annuelle [Mois du minimum des débits mensuels] - maximum de dQ
      P3:
        lowLim: agrégation annuelle [Mois du minimum des débits mensuels] - division par deux des maxima annuels pour obtenir un seuil
      P4:
        dtFlood: agrégation annuelle [Mois du minimum des débits mensuels] - nombre de jours où dQ dépasse lowLim
```

Le `method` a désormais la forme du `process` : mêmes clés de process,
mêmes clés de colonne, dans le même ordre. Les deux blocs se lisent côte
à côte.

### `allLF`, cinq colonnes au dernier process

Avant : cinq blocs de quatre lignes, vingt lignes, dont quinze décrivent
trois process qui ne produisent qu'une colonne chacun, recopiés cinq fois
et divergents.

```yaml
# après (meta.fr ; meta.en porte les mêmes clés et le texte anglais)
    method:
      P1:
        VC10: aucune agrégation temporelle - moyenne mobile centrée sur 10 jours
      P2:
        VCN10: agrégation annuelle [Mois du maximum des débits mensuels] - minimum de VC10
      P3:
        upLim: aucune agrégation temporelle - le maximum de VCN10 est pris comme seuil
      P4:
        startLF:  agrégation annuelle [Mois du maximum des débits mensuels] - date du premier jour de la plus longue période sous upLim
        centerLF: agrégation annuelle [Mois du maximum des débits mensuels] - date du minimum des VC10 sur la plus longue période sous upLim
        endLF:    agrégation annuelle [Mois du maximum des débits mensuels] - date du dernier jour de la plus longue période sous upLim
        dtLF:     agrégation annuelle [Mois du maximum des débits mensuels] - nombre de jours de la plus longue période sous upLim
        vLF:      agrégation annuelle [Mois du maximum des débits mensuels] - somme des volumes écoulés chaque jour de la plus longue période sous upLim
```

Les trois formulations de « minimum » (`minimum`, `minimum (série des
VCN10)`, `minimum (extraction de la série des VCN10)`) ne peuvent plus
revenir : il n'y a plus qu'un endroit où l'écrire. Toutes les références
se résolvent, `VC10` étant introduit en P1, `VCN10` en P2, `upLim` en P3.

### `QSA_season`, fan-out saisonnier

Le contenu ne change pas d'un mot, il change de clé :

```yaml
    method:
      P1:
        QSA_DJF: agrégation annuelle saisonnalisée [01-12, 28(29)-02] - moyenne
        QSA_MAM: agrégation annuelle saisonnalisée [01-03, 31-05] - moyenne
        QSA_JJA: agrégation annuelle saisonnalisée [01-06, 31-08] - moyenne
        QSA_SON: agrégation annuelle saisonnalisée [01-09, 30-11] - moyenne
```

C'est exactement ce que la sortie publie aujourd'hui, une ligne de méta
par colonne, chacune avec sa fenêtre.

### `QMA_month`, douze colonnes pour une phrase

`QMA_month` a douze sorties et un seul bloc de `method`. La migration
duplique la phrase douze fois, à l'identique, sans rien inventer :

```yaml
    method:
      P1:
        QMA_jan: agrégation mensuelle par année - moyenne
        QMA_feb: agrégation mensuelle par année - moyenne
        …                                                  # douze en tout
```

Douze lignes identiques ne sont pas du bruit : la sortie porte douze
lignes de méta, la fiche doit porter les douze textes. Les préciser mois
par mois, si c'est souhaitable, relève de la relecture éditoriale (lot D),
pas de la migration.

### La chaîne se lit sans les clés

Les clés lèvent l'ambiguïté machine et accordent `method` à `process`.
Elles ne sont **pas** le support de lecture : la valeur publiée ne les
montre pas, un lecteur reçoit des phrases numérotées. D'où une seconde
règle, qui porte sur la prose et non sur la structure :

> **Un nom cité doit avoir été présenté.** La prose du process qui
> produit une colonne la nomme dès qu'une étape ultérieure la cite.

Le dispositif est celui que le corpus employait déjà (`… sur la période
historique (QJXA-10)`) : le nom entre parenthèses en fin de phrase, une
seule orthographe, la même dans les deux langues. Deux raisons de le
préférer à une tournure intégrée du type « notée VC10 » : il est
identique en anglais et en français, et il évite l'accord (`notée`
moyenne, `noté` minimum) qui se serait trompé quelque part sur 34 fiches.
Là où la syntaxe accueille le nom sans détour, elle le garde (« est pris
comme seuil (upLim) »).

Une phrase qui doit se présenter dit aussi sur quoi elle opère : un
« minimum » nu ne se lit pas dans une chaîne, il devient « minimum de
VC10 (VCN10) ». L'opérande n'est pas choisi, il est lu dans le `func`.

Conséquence assumée : deux fiches au calcul identique peuvent différer
d'un `(nom)`, selon qu'une étape ultérieure le cite ou non. `QJXA-10` dit
« maximum », `n-QJXA-10_H` dit « maximum de Q (QJXA) », parce que seule
la seconde s'y réfère ensuite. La présentation existe pour la chaîne, pas
pour la décoration. À revoir dans la passe finale d'uniformisation.

## Ce que le linter vérifie

Sans données, à la lecture du seul YAML. Ces règles rejoignent
`python -m card.schema`.

1. Les clés de `method` sont exactement les process de la fiche, `P1`
   à `Pn`. Aucun process sans entrée, aucune entrée sans process.
2. Les clés de `method[Pn]` sont exactement les colonnes produites par
   `Pn`, calculées par la table ci-dessus. Aucune colonne sans phrase,
   aucune phrase sans colonne.
3. `meta.en.method` et `meta.fr.method` ont les mêmes clés, à tous les
   niveaux.
4. Chaque valeur porte le séparateur ` - `, une fois et une seule. Le
   corpus le respecte déjà partout, mesuré le 2026-08-03.
5. La moitié gauche appartient au vocabulaire fermé (voir plus bas).
6. Une colonne citée par une étape ultérieure est nommée par la phrase
   qui la produit. C'est ce qui empêche la relecture éditoriale du lot D
   de reperdre la chaîne, et le test l'éprouve en la cassant.
7. Un nombre écrit dans la prose existe dans le process. Le contrôle va
   dans ce sens et pas dans l'autre : exiger qu'un paramètre se retrouve
   dans la phrase serait faux, `Q50A` appelant « médiane » le quantile à
   50 % et ayant raison. Les identifiants sont retirés d'abord, le « 10 »
   de `VC10` n'étant pas une durée.
8. La moitié gauche s'accorde avec ce que le process calcule. Le pas de
   temps ne suffit pas à conclure : un process qui opère sur des séries
   déjà à son propre pas n'agrège rien, et le dit. Le grain d'une
   colonne se lit dans la chaîne, avec une exception qui compte, `keep:
   all`, qui rediffuse la valeur sur la grille d'entrée.

Les règles 1 à 3 sont ce qui rend la forme sûre : une fiche mal migrée ne
peut pas passer inaperçue, et un `func` ajouté plus tard sans sa phrase
rougit tout de suite.

## Ce que la sortie publie

**Rien ne change pour qui consomme `card.extract`.** La table `meta`
garde une ligne par variable et une case `method_fr` / `method_en`
contenant la chaîne numérotée, dans la forme d'aujourd'hui.

Cette chaîne est le **collage** des phrases de la fiche : pour une
colonne de sortie `V`, on prend à chaque process l'entrée de clé `V` si
ce process produit `V`, sinon toutes ses entrées. Aucune phrase n'est
déduite d'un paramètre, aucune n'est fabriquée : seul le séparateur et la
numérotation sont ajoutés.

La distinction est de doctrine, et elle est le fil rouge de ce document :

- **fabriquer du texte** (déduire `[01-03, 31-05]` depuis
  `sampling_period` parce que la fiche ne l'écrirait plus) est interdit,
  et c'est ce qui a fait écarter l'indexation par clé de `func` ;
- **coller des phrases toutes écrites dans la fiche** est admis, et
  c'est ce qui évite de changer le type de `method_fr` chez tous les
  consommateurs.

La même fonction de collage sert de **test d'aller-retour** de la
migration : elle régénère la chaîne d'origine pour toutes les fiches et
les deux langues, et la compare à git. Le filet de sécurité de la
migration est donc du code de production, qui ne pourrit pas.

## Ce qui ne change pas

- `method` reste dans `meta.<lang>`. Le texte humain reste dans `meta`,
  le calcul dans `process`. Aucune prose n'entre dans `process`.
- Chaque phrase garde ses **deux moitiés**, séparateur compris.
- Les placeholders `{suffix.name}`, `{suffix.short}` restent pleinement
  en service dans `method` : c'est la couche qui porte le fan-out non
  énumérable (voir « Deux fan-out »). Attention, ce n'est pas gratuit :
  c'est le piège principal de la migration, détaillé ci-dessous.
- La parité fr/en est maintenue et testée.
- La forme de la sortie, voir ci-dessus.

## Ce que le code doit suivre

`method` cesse d'être une chaîne, donc tout ce qui la traite comme une
chaîne ou comme une liste doit apprendre la table. Relevé le 2026-08-03,
à vérifier avant d'écrire la première ligne du lot A.

| Où | Ce qu'il faut faire |
|---|---|
| `suffix.substitute` | **Le piège.** Il descend dans les listes, pas dans les tables : une table lui passe devant intacte, sans substitution. Beaucoup de fiches portent un `{suffix.…}` dans leur `method` (familles `delta-*_H`, `rp-*`, `FDC`, `QJ`, `QM`). Sans correctif, l'accolade sort non résolue, ce que la règle 1 de CHANTIERS §9 interdit. À corriger **avant** la migration. |
| `suffix.fields_used` | Même angle mort, conséquence plus sournoise. Le linter s'en sert pour exiger qu'une fiche qui écrit `{suffix.X}` déclare `X` (règle 2), et pour signaler un `suffix_default` que plus rien n'utilise. S'il cesse de voir les placeholders de `method`, il déclarera « champ mort » un `suffix_default` vivant. Mesuré le 2026-08-03 : aucune fiche n'a aujourd'hui son unique placeholder dans `method`, donc rien ne rougirait tout de suite. Le mensonge attendrait la première fiche écrite ainsi. |
| Test de garde | Parcourir le corpus et refuser toute accolade non résolue en sortie, dans les deux langues, avec et sans suffixe. Le test existe pour `name` et `description`, il doit couvrir `method` sous sa nouvelle forme. |
| `extraction._meta_rows` | `method_en` / `method_fr` passent par la fonction de collage au lieu de `_as_list`, qui recopierait la table dans chaque ligne. |
| `management.info` | `_fmt` sait aplatir une liste, pas une table : même fonction de collage. |
| `loader._TEXTES` et `_unwrap` | Le repli de confort n'a plus lieu d'être : une phrase s'écrit en scalaire simple, et PyYAML replie déjà les lignes de continuation en une seule chaîne (vérifié). `_unwrap` doit au minimum traverser une table sans la casser. |
| `schema` | Les règles 1 à 5 ci-dessus, puis la 6 au lot B. |
| `render` | Lot C. |

## La migration : ce qui bouge, déclaré

Tout doit revenir octet pour octet par le test d'aller-retour, sauf les
divergences suivantes, déclarées à l'avance et listées une par une. Une
fiche qui diverge autrement n'est pas migrée, elle est signalée.

1. **Les renvois anaphoriques remplacés par un nom de variable.** Mesuré
   le 2026-08-03 : ils touchent une trentaine de fiches, dont la majorité
   pour la seule famille `allLF`. « sous le précédent seuil » devient
   « sous upLim ».
2. **`agrégation mensuelle` devient `agrégation mensuelle par année`**
   (famille QMNA), formulation majoritaire pour un calcul identique.
3. **Les incises `(série des X)` disparaissent.** Elles servaient à
   nommer la colonne produite ; la clé le fait mieux, et sans les trois
   orthographes concurrentes d'`allLF`.
4. **Les lignes de la famille `allLF` sont dédupliquées**, un texte par
   colonne produite au lieu d'un bloc par sortie de la fiche.
5. **Le repli des lignes longues disparaît**, une phrase tenant désormais
   sur une ligne.

La moitié gauche n'est **jamais** réécrite en dehors du point 2, et aucun
grain n'y est ajouté (voir « Décisions prises »).

Ordre de travail : par lots d'une dizaine de fiches, récapitulatif avec
niveau de confiance, et le go de l'utilisateur avant de continuer.

## Charte de rédaction des moitiés droites

Mesuré le 2026-08-03 : au niveau process, le corpus compte environ cinq
cent cinquante étapes pour **une centaine de phrases distinctes**. Ce
n'est donc pas une relecture ligne à ligne, c'est un vocabulaire à
normaliser, et « une seule formulation par geste » devient tenable.

1. **Phrase nominale, sans verbe conjugué**, qui nomme le geste :
   « maximum de Qr », « moyenne mobile centrée sur 10 jours », « division
   par deux des maxima annuels pour obtenir un seuil ». C'est la forme
   dominante du corpus, on la généralise.
2. **Toute variable citée est nommée**, jamais désignée par sa position :
   « sous upLim », pas « sous le précédent seuil ».
3. **Le geste, jamais le nom de la fonction** : « division par deux des
   maxima annuels », pas « ratio_longest_run ».
4. **La finalité quand elle n'est pas évidente** : « … pour obtenir un
   seuil ». C'est ce qui manque aux notes creuses (« moyenne », « calcul
   du KGE »), qui sont le gros du travail.
5. **Les paramètres numériques du process en clair** : « sur 10 jours »,
   « de période de retour 5 ans », « avec un seuil de significativité de
   5 % ».
6. **Aucune redite de la moitié gauche** : la maille d'agrégation ne se
   réécrit pas à droite.
7. **Une seule formulation par geste dans tout le corpus.**

## Le partage : gauche schématique, droite sémantique

- **Moitié gauche : un schéma, à vocabulaire fermé**, décalque des
  paramètres machine du process. `aucune agrégation temporelle`,
  `agrégation annuelle [...]`, `agrégation annuelle saisonnalisée [...]`,
  `agrégation mensuelle par année`, `agrégation saisonnière [...]`,
  `agrégation par jour de l'année`. On n'en ajoute pas.
- **Moitié droite : de la sémantique, en prose libre.** C'est là que la
  nature réelle du geste se dit, et elle s'y dit déjà dans la quasi
  totalité des cas. Là où elle ne s'y dit pas, c'est cette ligne qu'on
  récrit.

## Les lots

| | Lot | Contenu | Dépend de |
|---|---|---|---|
| A | **Structure** | traversée des tables par `suffix` (d'abord) ; `method` indexé par process et par colonne produite ; règles 1 à 5 du linter ; fonction de collage ; migration du corpus avec les divergences déclarées | |
| A-bis | **La chaîne se lit seule** | règle 6 : un nom cité est présenté par la phrase qui le produit ; les gestes nus nomment leur opérande, lu dans le `func` | A |
| B | **Concordance** | règle 7 : la moitié gauche confrontée à ce que le process calcule, dans le linter donc en CI | A |
| C | **La figure lit la fiche** | la moitié droite de `method[Pn][colonne]` s'affiche sous chaque étape ; la glose de docstring quitte `render.py` | A |
| D | **Relecture éditoriale** | la centaine de phrases distinctes, sous la charte | C |
| E | **Rendu de fonction** | `card.function()` puis `/v1/functions` : les docstrings changent de destinataire | C |
| F | **Finitions** | typographie de la figure, réglages encore en code brut, descriptions qui transcrivent la chaîne | C, D |

**C avant D, et c'est le point d'ordonnancement important.** Dès que la
figure affiche le texte de la fiche, chaque phrase creuse devient un
défaut visible à l'écran plutôt qu'une ligne dans un audit. C'est ce qui
rend la relecture tenable, et ce qui permet de valider par lots de fiches
en regardant des figures.

Détail du lot C : la figure n'affiche **que la moitié droite**, puisqu'elle
dessine déjà l'agrégation (ligne de grain et bande de douze mois).
Réafficher « agrégation annuelle » serait la redite que la charte
interdit. La ligne de grain reste : elle est mesurée, juste, et elle dit
ce que `method` ne dit pas.

Détail du lot E : la docstring d'une fonction hydro, avec ses blocs `en:`
et `fr:`, n'est pas perdue quand la figure cesse de l'afficher. Elle
devient le contenu d'un rendu de fonction : signature réelle, où `X`,
`lim`, `a`, `b` redeviennent corrects, docstring entière sans coupe ni
limite de longueur, notes hors bloc qui n'ont aujourd'hui nulle part où
aller, `is_transform`, et l'index inverse des fiches qui emploient la
fonction.

## Décisions prises, à ne pas rouvrir

Consignées parce que chacune a été suivie puis abandonnée, et qu'elles
reviendraient sinon.

**Ne pas générer la moitié gauche depuis les process.** Elle est
techniquement reconstructible depuis `time_step` et `sampling_period`.
Ce n'est pas la question. Une phrase **écrite** peut contredire le code,
donc révéler un bug ; une phrase **générée** est d'accord avec le code par
construction, y compris quand le code a tort. Et qui ouvre le YAML doit
pouvoir lire l'étape sans rien exécuter. La règle « ne jamais recopier ce
qui vit ailleurs » vaut pour des **valeurs qui dérivent** (versions,
plafonds), pas pour de la prose destinée à des humains.

Corollaire à ne pas escamoter : une assertion sans test n'est pas un
contrôle, c'est un commentaire qui dérive. Le lot B n'est donc pas
facultatif, c'est **ce qui donne sa valeur à la moitié gauche**. Preuve
par le corpus : les huit `agrégation mensuelle` imprécises ont vécu
jusqu'à ce que quelqu'un fasse le croisement à la main.

**Ne pas indexer par position.** Une liste positionnelle sur les colonnes
d'un process ne se dérive pas mécaniquement quand le process a
`compress` : l'ordre du fan-out est un détail d'implémentation de stase.
Sur `epsilon_R_season` P1, deux fonctions et quatre saisons donnent huit
colonnes pour quatre textes existants, et rien ne dit dans quel ordre les
apparier. La clé nommée supprime la question.

**Ne pas indexer par clé de `func`.** C'était la proposition du
2026-08-03, écartée le jour même par la mesure : la clé `func` n'est pas
une colonne quand le process a `compress`. Elle aurait mis un texte dans
la fiche pour quatre ou douze colonnes de sortie, et laissé le code
fabriquer les autres.

**Ne pas préciser le grain après « aucune agrégation ».** L'idée était
d'écrire « aucune agrégation, une valeur par jour » là où le calcul
distingue transformation, diffusion et absence d'agrégation. Vérification
faite, les moitiés droites disent déjà le grain par leur verbe : une
moyenne mobile rend une valeur par jour, c'est sa définition, et « pris
comme seuil » dit que c'est une constante. Ajouter la mention serait une
redondance. Et la distinction vient de `is_transform`, qui existe pour
que la **figure** dessine juste ; `method` ne dessine rien, il décrit.

**Ne pas construire de table `fonction -> prose`.** C'est la liste de
noms en dur qui a fait mentir `render.py` deux fois dans la semaine du
2026-07-30. Une chaîne qui nomme une fonction est un lien que rien ne
vérifie.

**Ne pas mettre de prose bilingue dans `process`.** Tout le texte humain
vit dans `meta.<lang>` : `loader._TEXTES`, `suffix.TEXT_FIELDS` et la
découpe fr/en/global en dépendent.

## Hors périmètre, à noter dans CHANTIERS

Trois sujets rencontrés en chemin, réels, mais qui ne sont pas ce
chantier et ne doivent pas le retarder.

**Nommage des variables intermédiaires.** La clé de `method[Pn]` étant le
nom de la colonne produite, ces noms deviennent visibles dans la fiche et
dans la figure. Une passe de vérification et d'uniformisation des noms
intermédiaires (`dQ`, `VC10`, `upLim`, `lowLim`, `QlimM`) donnerait sa
cohérence à la nomenclature. Non bloquant : la migration marche avec les
noms actuels, quels qu'ils soient.

**`difference_longest_run`, `circular_ratio`, `circular_difference` :
zéro fiche les emploie.** La première a été créée par symétrie le
2026-07-31 et peut partir. Les deux autres sont des portages de R, donc
la question est une question de parité, pas de ménage.

La scission de `ratio` en `ratio` et `ratio_longest_run`, elle, **reste**,
et pour une raison qui ne doit rien à la figure : un drapeau qui change la
cardinalité du retour est deux fonctions dans une, et rend le pas de temps
d'un process indécidable à la lecture de la fiche. Trois fiches emploient
`ratio_longest_run`, versions déjà montées, valeurs inchangées. Aucun lot
de ce plan n'en dépend.

**`meta.sampling_period` est incohérent** : prose humaine pour une partie
du corpus (« Mois du maximum des débits mensuels »), littéral Python brut
pour une autre (`['01-09', '31-08']`). Même famille de problème, sujet
distinct.
