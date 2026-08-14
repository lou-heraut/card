> **Statut : plan arrêté, implémentation à faire.** Décidé le 2026-08-14
> au terme d'une discussion qui a rouvert la forme du vocabulaire close
> la veille. Rien n'est implémenté : ce document dit ce qui doit changer,
> pourquoi, dans quel ordre, et ce qui ne doit PAS changer.
> `PLAN_THESAURUS.md` reste la référence de la FORME de l'arbre (racines,
> tableaux, libellés de nœud) et des notations officielles ; il n'est pas
> remis en cause. Ce plan-ci porte le CONTENU des concepts et la
> dépendance aux vocabulaires extérieurs.
> À archiver quand les quatre lots sont livrés et relus.

# Un thésaurus autoportant, fortement aligné

## La doctrine, en cinq phrases

1. **card se lit seul.** Tout concept que card définit porte son sens en
   français et en anglais, sans requête réseau et sans qu'un lecteur ait
   à ouvrir un autre vocabulaire.
2. **card ne redéfinit pas le mètre ni la moyenne.** Ce que le monde a
   déjà nommé sans ambiguïté reçoit un libellé et un alignement fort, pas
   une définition de politesse.
3. **Un alignement est additif, jamais porteur.** Aucune affirmation de
   card ne doit cesser d'être lisible si un vocabulaire extérieur
   disparaît. Les liens servent à comparer, pas à comprendre.
4. **L'effort de définition va où le corpus VARIE**, et cet endroit se
   mesure (§ suivant). Il n'est pas là où I-ADOPT le suggère.
5. **Chaque phrase écrite doit se lire naturellement dans les deux
   langues**, et elle est relue par l'utilisateur avant d'entrer.
   Un néologisme commode dans une langue est une faute dans les deux.

## Ce qui a été mesuré, et qui justifie tout le reste

Sur `docs/card.ttl` du 2026-08-14, 573 concepts, 13 398 triplets.

**La dépendance extérieure n'est pas dans les alignements.** Les
`skos:*Match` sont 17 triplets. La composition I-ADOPT, elle, en pointe
1 082 vers Theia, et QUDT en reçoit 833. Ce ne sont pas des liens de
courtoisie : ce sont les triplets qui disent de quoi une variable parle.

**Ces 1 082 assertions reposent sur SEPT concepts.**

```
hasProperty            Discharge 233   Volume per area 196   Temperature 42
hasObjectOfInterest    River 233   Precipitation 176   Air 42   Evapotranspiration 20
```

**Et aucun des 34 concepts extérieurs référencés ne porte de libellé dans
notre fichier.** Vérifié un par un : 19 Theia, 15 QUDT, zéro libellé. Un
lecteur voit `theia:c_7742e5f0` là où il devrait lire « débit ».

**L'axe ontologique ne discrimine presque rien, l'axe statistique
discrimine tout.** C'est le fait central, et il contredit la façon dont
I-ADOPT invite à décrire une variable :

| ce qui distingue une variable d'une autre | valeurs distinctes | pour 444 variables |
|---|---|---|
| objet d'intérêt | 4 | ce qui est mesuré ne varie pas |
| propriété | 3 | idem |
| aspect | 5 | |
| phénomène | 11 | |
| statistique | 18 | |
| contrainte paramétrée | 25 | ce qui varie vraiment |

I-ADOPT est bâti pour éviter qu'on confonde la température de l'eau et
celle de l'air. Le problème de card est ailleurs : distinguer `VCN10` de
`VCN3` sans ambiguïté statistique. Les deux ont le même objet, la même
propriété, le même aspect, le même phénomène, et ne diffèrent que par une
fenêtre de dix jours contre trois.

**Conséquence directe sur l'effort** : sept libellés suffisent du côté
ontologique, et tout le travail de définition va au statistique, au
phénomène et à la contrainte. C'est aussi pourquoi la piste « raffiner
`method` par étape » de `CHANTIERS.md` compte plus que n'importe quel
enrichissement I-ADOPT.

## Ce qu'un visualiseur affiche, vérifié le 2026-08-14

La documentation de Skosmos dit deux choses, et elles décident de la
forme retenue.

- Pour une **relation de mappage SKOS**, Skosmos cherche un libellé : dans
  un vocabulaire configuré dans la même instance s'il y en a un, sinon par
  une **requête HTTP** sur l'URI. Le mécanisme existe donc, mais la même
  documentation prévoit `skosmos:loadExternalResources: false` quand les
  pages « mettent excessivement longtemps à charger, voire ne chargent
  pas ». Chez un hébergeur multi-vocabulaire, il y a de bonnes chances
  qu'il soit éteint.
- **`iop:hasProperty` n'est pas une relation de mappage SKOS.** Elle ne
  passe donc par aucun de ces deux mécanismes, quel que soit le réglage.

Un concept réduit à une URI n'est donc lisible ni par l'humain ni par
l'outil, sauf configuration favorable qu'on ne maîtrise pas. C'est ce qui
transforme la préférence en nécessité.

## Ce qui change, en quatre lots

### Lot 1 : les sept concepts de composition

Le lot structurant, et le seul qui touche le générateur.

```turtle
# AUJOURD'HUI : 942 assertions illisibles sans leur fichier
card:variable/VCN10  iop:hasProperty  theia:c_7742e5f0 .

# APRÈS : elles pointent chez nous, et c'est notre concept qui s'aligne
card:variable/VCN10  iop:hasProperty  card:property/discharge .

card:property/discharge
    a                skos:Concept ;
    skos:prefLabel   "débit"@fr, "discharge"@en ;
    skos:exactMatch  theia:c_7742e5f0 .
```

Trois propriétés (`discharge`, `volume-per-area`, `temperature`) et
quatre objets d'intérêt (`river`, `precipitation`, `air`,
`evapotranspiration`). **Un libellé bilingue, pas de définition** : ce
sont exactement les notions que la doctrine dit de ne pas redéfinir.

Ce que le lot gagne : la dépendance passe de **942 triplets à 7**, le
français devient le nôtre, et une propriété nouvelle (une durée, un
volume) se crée sans rien demander à personne.

Ce qu'il coûte, et il faut l'assumer : I-ADOPT recommande de réutiliser
les atomes existants pour que deux fournisseurs soient comparables.
L'`exactMatch` préserve cette comparabilité, c'est son rôle, et SKOS le
déclare symétrique et transitif. Un consommateur qui ne comparerait que
des URI sans suivre les mappages verrait deux propriétés distinctes.
**Le geste est réversible en une ligne du générateur**, et c'est
précisément la déclaration d'équivalence qui le rend réversible.

### Lot 2 : des libellés pour tout ce qui reste extérieur

Les 15 unités QUDT, les 4 noms CF, et les concepts Theia et GEMET encore
visés par un `*Match`. **Un libellé, jamais une définition** : on ne
s'approprie pas leur concept, on rend notre fichier lisible.

Forme retenue : `rdfs:label`, qui est une aide à l'affichage, et non
`skos:prefLabel`, qui affirmerait que leur concept a chez eux le libellé
préféré qu'on lui donne. C'est une nuance de politesse, et elle est
gratuite.

Portée honnête de ce lot : il sert le lecteur du fichier brut et les
visualiseurs RDF génériques. Il ne change rien pour Skosmos, qui va
chercher ses libellés de mappage ailleurs (§ ci-dessus).

### Lot 3 : le contenu des concepts de vocabulaire

Là où le travail est réel. La règle qui sépare définition et libellé :
**on définit ce sur quoi un lecteur peut se tromper.**

| famille | quoi | qui valide |
|---|---|---|
| 11 phénomènes | définition bilingue, plus `closeMatch` GEMET pour 4 d'entre eux | **utilisateur, c'est de la science** |
| 5 aspects | définition courte, ancrée sur IHA (Richter et al. 1996) | utilisateur |
| 18 statistiques | définition pour celles dont le sens dans card n'est pas évident (élasticité, efficience, filtre, significativité) ; libellé seul pour les universelles ; `exactMatch` Theia conservé pour les 5 qui l'ont | utilisateur pour les non évidentes |
| 14 grandeurs d'entrée | définition courte de la GRANDEUR, jamais de son rôle dans card | utilisateur |
| 7 familles de contrainte | note de portée (ce sont nos inventions) | relecture |
| 6 fenêtres, 3 formes, 2 finalités | note de portée, usage et non science | relecture |
| 4 grandeurs | rien, elles ont déjà leur note de portée | |

Écrire les phénomènes **par branche et non un par un** : les quatre du
débit se définissent les uns contre les autres, et c'est en les lisant à
la suite qu'on voit que trois sont des périodes et que le débit de base
est une composante.

Ne JAMAIS écrire dans une définition ce que la branche contient
(« rassemble les indicateurs d'intensité et de durée ») : ça se dérive du
corpus, donc ça mentira, et l'arbre le montre déjà.

### Lot 4 : la relecture, qui n'est pas optionnelle

**Tout ce que la production du thésaurus écrit passe devant
l'utilisateur avant d'être publié**, en une passe unique et présentée en
entier : les définitions des trois lots précédents, mais aussi les
libellés de nœud des 68 tableaux, les notes de portée, et les phrases
déjà en place.

Raison écrite noir sur blanc parce qu'elle a un précédent : une note de
portée proposée le 2026-08-14 disait « donc la variable est
tendançable ». Le mot n'existe pas. Il était commode, il passait
inaperçu dans un fil de discussion, et il serait entré dans un
vocabulaire public. **Une phrase qui ne se lit pas naturellement dans les
deux langues est une faute, pas un détail de style.**

## Ce qui ne change PAS

À relire avant de se laisser emporter par la complétude.

- **Les 187 variables sans description** restent sans description. Leur
  `name` porte tout (« Summer minimum of monthly flows »), et la règle
  des trois champs humains le dit depuis le 2026-08-03.
- **Les 59 concepts engendrés** (25 mesures, 25 contraintes, 9 périodes)
  ne prennent aucune définition. Leur libellé EST l'information
  (« période de retour de 2 ans »), et ils portent déjà leur description
  machine en CPM, QUDT et OWL-Time.
- **Les unités ne sont pas redéfinies.** QUDT les tient.
- **`hasMatrix` et `hasContextObject` d'I-ADOPT restent ignorés.** Le
  milieu est l'axe qui ne discrimine rien chez nous.
- **La forme de l'arbre** (racines, tableaux ISO 25964, libellés de
  nœud) : `PLAN_THESAURUS.md`, close.
- **Aucune sortie de calcul** n'est touchée par ce plan.

## Ce qui empêchera que ça se défasse

Un plan livré se dégrade. Trois gardes, sur le modèle des tables de
libellés de nœud qui font déjà échouer la génération quand une facette
nouvelle n'est pas traitée.

1. **Un test refuse un concept de vocabulaire sans texte.** Toute valeur
   de `topics.yaml` doit porter soit une définition, soit une note de
   portée, dans les deux langues. Une facette ajoutée demain sans sa
   phrase casse la suite, elle ne passe pas en silence.
2. **Un test refuse un `iop:hasProperty` ou un `hasObjectOfInterest` qui
   sort de l'espace de noms de card.** C'est la garde du lot 1 : elle
   empêche que la dépendance revienne par une ligne d'`alignments.yaml`.
3. **Un test exige un libellé pour toute URI extérieure référencée.**
   C'est la garde du lot 2, et elle vaut pour les vocabulaires qu'on
   ajoutera.

## L'ordre, et pourquoi celui-là

1. **Lot 1**, parce qu'il décide de la forme et qu'il touche le
   générateur. Tant qu'il n'est pas fait, toute définition écrite risque
   d'être rangée au mauvais endroit.
2. **Lot 3, les 11 phénomènes seuls**, présentés par branche pour
   validation. C'est le seul contenu scientifique, et il donne la barre
   de qualité du reste.
3. **Lot 2 et le reste du lot 3**, qui sont mécaniques une fois la barre
   posée.
4. **Lot 4**, la relecture complète, avant toute publication.

Rien de tout cela ne bloque le courriel à Theia : ce qu'on leur demande
(hébergement, URIs, quatre `narrowMatch`) ne dépend d'aucun de ces lots.
Ce plan rend seulement le fichier meilleur à montrer.
