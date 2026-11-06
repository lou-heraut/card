> **Statut : brouillon, rien n'est envoyé.** Ce fichier porte les
> questions à poser à Theia/OZCAR, et rien d'autre : pas de mesure, pas
> de décision. Ce qui les justifie vit dans `PLAN_THESAURUS.md`, qui
> porte l'audit du 2026-08-14 et la forme retenue chez nous.
> Le reste du chantier avance sans attendre ces réponses. Aucune ne
> bloque, aucune ne demande de modifier une fiche.
> À supprimer une fois la conversation engagée, en reportant ce qu'elle
> aura tranché dans `PLAN_THESAURUS.md`.

# Questions à Theia/OZCAR

Écrit en tutoyant, comme un message entre collègues. Les questions sont
rangées de la moins engageante à la plus engageante : les trois premières
ne demandent aucune décision, la dernière en demande une vraie.

## De quoi il s'agit, en trois phrases

card est un recueil de définitions de variables hydroclimatiques, des
indicateurs calculés à partir de chroniques journalières de débit, de
précipitation et de température. Chaque définition est un fichier
versionné, et le vocabulaire SKOS qui les décrit est **engendré** depuis
ces fichiers, jamais écrit à la main.

Ton thésaurus décrit ce qu'on **mesure**. card décrit ce qu'on **calcule
sur** cette mesure. Les deux se touchent en un point exact, et c'est de
ça qu'on veut parler.

## 1. Trois choses relevées dans votre fichier

Relevé le 2026-08-14 sur l'export Turtle complet, en le parcourant en
entier. Aucune ne demande de décision, ce sont des corrections.

- **`iop:hasContraint` au lieu de `iop:hasConstraint`**, 39 fois, sur des
  variables de chimie des eaux souterraines. La propriété mal orthographiée
  n'existe pas dans I-ADOPT, donc ces 39 contraintes sont invisibles à
  tout outil qui lit le modèle.
- **`1 day mean karst water discharge`** déclare
  `cpm:statisticalMeasure` vers « 1 day cumulative ». Une moyenne qui
  pointe vers un cumul. Ses neuf sœurs sont correctes.
- **`10 minutes mean river discharge`** range sa statistique dans
  `iop:hasConstraint`, alors que ses neuf sœurs emploient
  `cpm:statisticalMeasure`. Une `cpm:StatisticalMeasure` employée comme
  contrainte.

## 2. Ce qu'on aimerait vous demander : quatre triplets

card publie de son côté quatre `skos:broadMatch` vers vos quatre
variables génériques :

```
card « indicateurs de débit de rivière »      →  River discharge
card « indicateurs de précipitation »         →  Precipitation amount
card « indicateurs de température de l'air »  →  Air temperature
card « indicateurs d'évapotranspiration »     →  Potential evapotranspiration
```

Ça suffit pour que qui part de card arrive chez vous. Ça ne suffit pas
pour l'inverse : Skosmos n'affiche que les correspondances portées par la
fiche qu'on regarde, jamais les correspondances entrantes. Donc pour
qu'un visiteur de votre portail voie qu'il existe des indicateurs
calculés sous `River discharge`, il faut les quatre `skos:narrowMatch`
réciproques dans votre fichier.

Quatre triplets, aucun concept à maintenir, réversible.

**Question : est-ce que vous les accepteriez ?**

## 3. Deux concepts qui ne disent rien

`Summer period` et `Winter period` sont dans la branche `Time` et ne
portent aucune définition, ni dates, ni durée, ni note. Ils servent
pourtant à composer `Summer cumulative` et `Winter cumulative`, donc à
définir des variables.

Une saison sans bornes n'est pas interprétable par un consommateur de
données. card a des fenêtres datées de son côté, mais elles sont
hydrologiques et propres à son domaine : on ne propose pas de vous les
imposer, seulement de signaler le trou.

**Question : est-ce que ces deux concepts ont une définition quelque part
qui n'est pas dans l'export ?**

## 4. Ce qui vous manque et qui ne dépend pas de card

Votre branche `Statistical method` compte sept opérations de tête et
trente-cinq concepts en tout. Elle couvre ce qu'un capteur produit
(moyenne, cumul, minimum, maximum, médiane, écart-type, intervalle
d'incertitude) et s'arrête là.

Treize opérations employées par card n'ont aucun équivalent chez vous :
quantile, quantile de dépassement, dépassement de seuil, période de
retour, pente de tendance, significativité de tendance, écart entre deux
périodes, rapport, biais, efficience, élasticité, corrélation, filtre de
séparation d'hydrogramme.

Et sur l'axe temporel : vous avez `1 year maximum` et `1 year cumulative`
mais pas `1 year minimum`, pas de moyenne ni de médiane annuelles, et
aucune moyenne mobile.

Aucune de ces vingt-six notions n'est propre à card : elles servent tout
observatoire qui publie autre chose que de la donnée brute. On peut vous
en donner les libellés dans les deux langues.

**Question : est-ce que ça vous intéresse comme extension de votre
branche `Statistical method`, indépendamment de la suite ?**

Même remarque pour la branche `Phenomenon` : elle a `Water cycle` et
`Streamflow`, mais aucun régime hydrologique. Ni crue, ni étiage, ni
sécheresse, ni débit de base. EnvThes, auquel vous alignez déjà beaucoup,
a `flood` (20383) et `drought` (20375).

## 5. Deux questions de modélisation, sans arrière-pensée

- **La statistique se dit `iop:hasStatisticalModifier` ou
  `cpm:statisticalMeasure` ?** Vous employez le second. I-ADOPT a ajouté
  le premier en 2025, après votre modélisation. card emploie les deux, le
  premier pour l'opération, le second pour l'opération avec sa fenêtre.
  Est-ce que c'est votre lecture aussi, ou est-ce que vous voyez une
  raison de n'en garder qu'un ?

- **`ozcar:simplifiedLabel`.** On a compris à quoi il sert : grouper les
  variantes d'une même idée, « 1 day mean river discharge » et « 15
  minutes mean river discharge » partageant « Surface water discharge ».
  card a exactement le même besoin, et il s'est avéré que le geste a un
  nom normalisé : c'est le **tableau** de l'ISO 25964, avec son libellé
  de nœud, mis en SKOS par la DCMI sous
  `isothes:ThesaurusArray` (une sous-classe de `skos:Collection`) et
  rattaché à son concept par `isothes:superOrdinate`. Le groupe devient
  une ressource avec son URI et ses libellés, au lieu d'une chaîne
  répétée sur 1 151 variables.

  Le point qui nous a décidés : un libellé de nœud **n'est pas un
  concept**, on n'indexe pas une donnée avec. Le typer en collection
  plutôt qu'en concept évite d'affirmer qu'une variable est une « sorte
  de » son casier de rangement. card les type aussi `iop:VariableSet`,
  qui dit la même chose côté I-ADOPT.

  **Est-ce que c'est une piste pour vous, ou est-ce que la chaîne répétée
  répond à un besoin qu'on n'a pas vu ?**

## 6. Deux questions de gouvernance

Elles décident de la forme du reste, donc autant les poser tôt.

- **Est-ce que vous accepteriez des libellés français ?** Votre export
  est en anglais seul, sans un seul `prefLabel@fr`. card est bilingue de
  bout en bout, et pourrait vous fournir le français des concepts qu'il
  cite chez vous.

- **Est-ce que vous accepteriez un `skos:notation` sur un concept ?**
  Vous n'en avez aucun. La porte d'entrée de card est le symbole
  (`VCN10`, `QMNA`), qui est ce que les hydrologues citent dans les
  publications et lisent dans les colonnes de leurs tableaux. Chez vous,
  une variable ne se désigne que par un libellé long.

## 7. L'hébergement

Vous exploitez déjà un Skosmos multi-vocabulaire à Montpellier, qui sert
`theia_in_situ`, `theia_spatial` et le thésaurus de l'UNESCO, donc un
vocabulaire qui n'est pas le vôtre.

**Question : est-ce que `card.ttl` pourrait y être servi de la même
façon, à côté du vôtre ?** Ce serait un graphe de plus et une entrée de
configuration : les URIs restent celles de card, vous n'éditez rien, et
on vous passe le fichier à chaque version.

C'est le meilleur résultat pour tout le monde, parce que qui cherche une
variable hydro la trouverait au même endroit. Ce n'est pas un prérequis :
le fichier est de toute façon en téléchargement chez nous.

## 8. La seule question qui décide vraiment

Tout ce qui précède suppose deux vocabulaires côte à côte. L'autre
scénario serait que les définitions de card deviennent des concepts de
**votre** thésaurus. On ne le propose pas, pour une raison technique et
une seule :

`card.ttl` est **engendré** depuis les fichiers de définition à chaque
changement, et un test refuse que les deux divergent. Le vocabulaire ne
PEUT PAS mentir sur le corpus. Si les concepts vivaient dans votre outil
d'édition, la définition existerait à deux endroits et plus rien ne les
tiendrait d'accord.

**Question : est-ce que vous chargeriez périodiquement un vocabulaire
engendré, plutôt que de l'éditer ?** Si oui, l'intégration complète
redevient discutable. Si non, deux vocabulaires côte à côte est le
meilleur des mondes et rien n'est perdu.
