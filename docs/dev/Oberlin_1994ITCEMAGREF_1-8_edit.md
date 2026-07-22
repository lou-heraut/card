> **Statut : référence externe.** Publication d'origine (OCR relu), non
> modifiable. C'est la source scientifique du système de nommage ; sa
> transposition à CARD est dans `NOMENCLATURE.md`.

# Normalisation des variables dans les modèles hydrologiques descriptifs

**G. Oberlin** — Informations Techniques du CEMAGREF, mars 1992, n° 85,
note 4, p. 1-8. Division Hydrologie-Hydraulique, groupement de Lyon.

> Transcription du scan `Oberlin_1994ITCEMAGREF_1-8_edit.pdf`
> (2026-07-13). Les passages douteux du scan sont marqués `[?]` ;
> la mise en page (colonnes, encadrés) est linéarisée.

---

## [Introduction]

L'Hydrologie est un domaine un peu négligé cette dernière décennie, et
dont l'importance réapparaît aujourd'hui avec la prise de conscience
que les réalités environnementales gouvernent à terme l'avenir de
notre planète Terre.

La perception de cette réalité conduit à un renouveau des recherches
sur les processus hydrologiques, avec une utilisation systématique de
la modélisation quantifiée des phénomènes analysés. Mais c'est surtout
la redécouverte de l'étendue du domaine qui conduit à développer de
très nombreux modèles finalisés.

Ces modèles décrivent, plus qu'ils ne créent, les connaissances
hydrologiques. Ils sont destinés à s'intégrer dans un domaine « aval »
qui peut aussi bien être une autre discipline scientifique
(l'hydrobiologie, l'hydrochimie ou la dynamique fluviale), une
approche pluridisciplinaire (le fonctionnement de grands bassins
versants ou le cycle détaillé de l'eau), ou une demande sociale
(l'aménagement d'un lit majeur, la gestion d'une ressource ou la lutte
contre les pollutions).

Dans cette problématique, les besoins de compréhension réciproque, de
comparaisons, d'évaluation, et souvent in fine d'arbitrages, sont
permanents. Ils exigent, entre autres, une définition aussi limpide
que possible des variables hydrologiques modélisées, qu'elles
concernent les entrées (données nécessaires), les sorties (résultats)
ou les intermédiaires (variables internes).

Compte tenu de la complexité inhérente au cycle de l'eau, il y a en
outre un besoin permanent de « rappel » des définitions et de leur
signification.

Mais de trop nombreux rappels encombrent un texte et ne peuvent pas
être tous inclus à l'intérieur d'un descriptif de modèle.

Il devient donc nécessaire d'utiliser des sigles pédagogiques et
sémantiquement clairs, décrivant sans risques de confusion les
variables utilisées.

L'objet de cette note est donc de proposer des règles générales de
définition des variables utilisées en hydrologie, et plus
particulièrement en modélisation, et de concrétiser ces règles par une
construction rigoureuse des sigles. L'objectif est ici pédagogique.

Comme ces variables sont, à un moment ou à un autre, analysées sous
leurs aspects aléatoires, on les désignera par le néologisme reconnu
de « **variates** ».

## Encadré — La confusion actuelle : quelques illustrations

De nombreuses confusions existent aujourd'hui sur la signification des
variables hydrologiques, y compris pour la plus triviale d'entre elles
qui est le débit. Moins forte parmi les hydrologues, elle est
considérable à l'extérieur. On peut remarquer [qu'il existe] encore à
des débats ou affirmations du genre :

- « Quel est le débit Q de la Rivière R à la STATION S ? Mon modèle
  exige d'entrer ce Q. Comment, il y en aurait plusieurs ?? » ;
- « Le problème des relations entre la pluie P et l'altitude z est
  résolu par le modèle M » ;
- « La variable QM est la plus pertinente pour l'estimation des
  potentialités du milieu ».

Si la première question est triviale, l'utilisateur incompétent en
hydrologie aurait au moins été alerté de la nécessité [de s'entourer
d'avis ?] si ce Q avait été présenté selon un sigle sémantiquement
plus précis. La seconde affirmation, émanant d'un scientifique
généraliste climatologue, est fausse ou incompréhensible tant qu'il
n'est pas précisé qu'il s'agit du quantile médian (ou de la moyenne
interannuelle) du débit médian (ou de la moyenne interannuelle) de la
pluie annuelle ou mensuelle [?]. Quant à la troisième, l'on comprend
qu'il s'agit d'un débit Mensuel (mais s'agit-il d'un débit Maximal
(mais lequel ?), d'un débit moyen (mais quelle Moyenne ?) [?]. À la
lecture du contexte, ou des propos, chacun perd son temps [?] et
l'on n'est jamais sûr qu'on n'a pas toujours les moyens ou le temps
(ou la documentation pertinente, et à jour) pour prendre connaissance,
« on line », de ce contexte.

Les scientifiques n'osent pas proposer des règles dont ils ne sentent
pas le besoin et qui sont contraignantes. Les utilisateurs n'ont que
peu conscience des difficultés. Les uns et les autres se satisfont
souvent d'un manque de transparence parfois bien commode. Ceci est
particulièrement vrai pour les décideurs qui n'osent trancher, ou pour
les divers opérateurs qui exploitent les ressources ou subissent les
risques liés aux Eaux Continentales. Moins de « glasnost » autorise
plus de liberté dans la conduite de leurs affaires. Dans tous les cas,
c'est l'environnement, et donc notre intérêt à terme, qui en pâtit.

## Les démarches actuelles pour clarifier

Cette situation fort dommageable évolue. La présente note est une
contribution à la nécessaire clarification en la matière, et s'appuie
sur plus de vingt-cinq ans d'expérience en Hydrologie et en
modélisation des Eaux Continentales, travaux menés dans le cadre d'un
laboratoire dédié à la recherche appliquée et de synthèse, sinon
finalisée. D'autres contributions sont en cours.

À simple titre d'exemples, et sans être exhaustif, dans ce très vaste
champ de l'hydrologie :

- l'OMM (Organisation Mondiale de la Météorologie) travaille sur un
  Glossaire International des termes utilisés en Hydrologie, mais
  c'est encore très loin des besoins précis et urgents définis ici ;
  la section française de l'Association Internationale des Sciences
  Hydrologiques (AISH) contribue à ce Glossaire ;
- le Royaume-Uni (BSI) propose actuellement à l'ISO (International
  Standards Organization) une norme en matière de mesures en
  hydrologie ;
- l'Allemagne (DIN) travaille sur un domaine proche de celui qui nous
  intéresse ici, mais il n'est pas focalisé sur les modèles ; il nous
  semble insuffisamment adapté à ces aspects cognitifs et
  scientifiques, et se trouve assez en amont du présent objectif ; il
  pourrait y avoir une certaine complémentarité entre les deux
  approches ; la diffusion de cette note est d'ailleurs un préalable
  nécessaire ;
- plus généralement, les laboratoires qui ont construit des modèles de
  synthèse, souvent dits « régionaux », ont dû définir un grand nombre
  de variables et de sigles, entrant ou sortant de ces modèles, par
  exemple au Royaume-Uni (FSR : Flood Studies Report ; idem en
  étiages) et en France (SNC : Synthèse Nationale des Crues, idem en
  étiages régionaux).

Cette note s'inspire largement des travaux français cités ci-dessus,
auxquels notre laboratoire a largement participé. Elle n'assure la
coordination avec les définitions britanniques que dans les limites
des concepts réellement communs. Mais, sur ce point, les contacts
scientifiques sont permanents, et assurés, entre autres via le Réseau
Euro-méditerranéen des BVRE (Bassins Versants Représentatifs et
Expérimentaux : laboratoires de terrain) et le projet européen FRIEND,
programmes où le laboratoire auteur est participant, voire créateur
et/ou pilote.

## Les caractéristiques des variates

On parlera d'une variate sensu stricto et donc bien définie, si les
principes de base sont satisfaits. Un certain nombre d'entre eux sont
indispensables. Ils sont donnés ici par ordre d'importance
décroissante.

- La **nature physique**, éventuellement mathématique ou topologique
  s'il s'agit d'une variable sans dimension, est indispensable et doit
  être précisée d'emblée. Elle doit toujours être rappelée.

- La **dimension « temps »** est essentielle. Outre la structure
  temporelle de base pour les chroniques, toute variable hydrologique
  peut être considérée comme susceptible d'évoluer dans le temps,
  changements climatiques et aménagements anthropiques obligent ! Il
  reste cependant à définir une nette différence de variabilité
  temporelle entre de réelles chroniques de variables courantes
  (débits, pluies, concentrations, cotes d'eau, …) et des
  « constantes » plus ou moins stables dans le temps (quantités
  statistiques, occupations des sols, caractéristiques
  climatiques, …). La manière d'introduire le temps (dates, durées, …)
  variera donc en fonction du poids de ces aspects temporels. Dans
  tous les cas, cet aspect temps doit absolument apparaître dans la
  définition et dans l'éventuel sigle.

- **L'espace**, quoique fondamental, n'est cité ici qu'en troisième
  position, par suite de sa liaison avec la grandeur physique ou la
  nature mathématique. Il faut néanmoins veiller à ce qu'il soit
  suffisamment précisé, tant en aire concernée (surface « représentée »
  par la variable) qu'en localisation si nécessaire (coordonnées), et
  il a également vocation à rester résident [?].

- Ces trois règles de base étant satisfaites, il faut mentionner
  nombre de **détails** plus ou moins indispensables devant être
  précisés pour qu'il n'y ait pas d'erreur d'interprétation sur la
  variate concernée, comme la représentativité saisonnière de la
  variable.

Il faut également préciser des règles opérationnelles et réputées
adaptables à tous.

## Les caractéristiques d'une variate v sont hiérarchisées

L'énoncé des caractéristiques de la variate est ordonné et
hiérarchisé. En cas de doute sur la pertinence d'un ordre, on tient
compte de la chronologie d'obtention de la variate.

### Préciser la nature et la grandeur physique, éventuellement mathématique

Un nom simple est parfois suffisant (débit). Il faut souvent un
complément ou un adjectif (débit de bassin, débit spécifique [?]),
voire deux (température dans le sol à 20 cm, débit de base ramené au
module). L'aspect spatial est le plus souvent intégré dans cette
définition (pluie locale, pluie de bassin, température ramenée au
niveau de la mer).

### Le pas de temps (pdt), ou la durée d, éventuellement la date ou le temps

Le cas des variables courantes, avec date et temps, est classique.
Celui des variates de synthèse l'est moins et doit être précisé.

Un adjectif suffit parfois (débit journalier, pluie horaire), mais il
en faut souvent davantage (débit-seuil dépassé continuellement pendant
6 heures, concentration sur 72 heures à partir d'échantillons
tri-horaires dans une proportionnalité aux débits). Dans tous les cas,
la durée que représente la variate doit être parfaitement claire.

La date est à préciser selon les conventions habituelles en chroniques
(voir les sigles).

Ces définitions sont toujours nécessaires, et parfois suffisantes, en
particulier pour les chroniques continues. On les symbolise
provisoirement sous le sigle **vd** pour une variate de synthèse et
**v(t)** s'il faut dater avec le temps courant t.

### La représentativité saisonnière

La définition d'une saison (ou d'une période spécifique) à laquelle
est affectée la variate vd est souvent nécessaire, en particulier en
variate non courante et non datée. Ceci va de pair avec la définition
de la représentativité de la variate dans cette saison. Cette
représentativité étant essentielle, on la définit d'abord. Par
exemple : débit journalier miNimal, pluie horaire maXimale, …

### La saison concernée

C'est alors un simple corollaire du choix précédent. Par exemple :
débit de 12 heures maXimal annuel (saison année), flux en nitrates de
10 jours (durée d) miNimal estival (saison été), …

### D'autres caractéristiques

Les quatre définitions précédentes sont, dans la majorité des cas,
suffisantes en hydrologie. L'usage de ces règles est tellement
satisfaisant que certains ont tendance à poursuivre le processus. Il
devient cependant difficile de donner des règles suffisamment
générales à ce niveau de détail.

On peut afficher les usages les plus fréquents et les plus
reproductibles (non exhaustif) :

- la **période moyenne de retour T**, s'il s'agit d'un quantile (pluie
  de 3 jours maximale hivernale centennale) ; en sigle sous forme d'un
  simple suffixe (ici T = 100) ;
- des précisions sur le **mode d'extraction** de la variate depuis la
  chronique initiale, s'il s'agit de variates extraites : par exemple
  « sup- » ou « sous- » seuils pour les variates liées à des
  modélisations appartenant aux approches dites « de renouvellement »,
  ou « nx plus fortes (plus faibles) » pour des variates choisies
  selon les protocoles de valeurs dites extrêmes (indice x par saison,
  le plus souvent) ; il faudra veiller à ce qu'une telle précision ne
  soit pas redondante car déjà incluse dans la définition de la
  représentativité et de la saison ; sigles de type vds ou vdx.

## Règle complémentaire

L'abus d'usage du terme moyenne et la présence des qualificatifs « pas
de temps (durée) » et « représentativité (dans la saison) » dans les
définitions recommandées, impose une règle qui doit accompagner les
expressions « moyenne dans le pas de temps (pdt), ou sur la durée d » :
**il ne faut pas utiliser l'adjectif moyenne dans ce cas trivial**,
mais le réserver à l'estimateur de l'espérance mathématique (moyenne
statistique expérimentale).

Ainsi, un débit mensuel sera toujours une moyenne de débit dans le
mois (ou du volume écoulé : mathématiquement équivalent, aux unités
près, la moyenne étant une intégrale sur le mois ramenée aux unités
d'un débit), un flux annuel une intégrale (moyenne, volume, …) sur
l'année, une pluie horaire, un total précipité en une heure, etc. Il
faut donc que les autres caractéristiques précisent ensuite de quels
mois, année ou heure il s'agit.

## Sigles correspondants

Si les périphrases issues des règles précédentes sont indispensables
et utiles, elles n'en sont pas moins encombrantes. Il n'est pas
pédagogique de trop souvent les rappeler. Un sigle qui les représente
est aussi nécessaire, bien sûr après une claire définition dans le
texte et une table analytique de rappel facile à utiliser.

Jusqu'à présent on considérait suffisant, pour les auteurs, quel que
soit le texte (de la théorie à la notice technique de logiciel), de
bien veiller à cette « liste des notations employées ». Mais vu la
difficulté de transférer connaissances et informations, que l'on
rencontre même à l'intérieur des laboratoires et entre spécialistes,
cette liste ne suffit plus. Il faut pouvoir lire et assimiler très
vite des informations foisonnantes, et disposer d'une aide instantanée
et rapide en cas de « trou de mémoire » (Help on-line performant…).
C'est en particulier indispensable pour le scientifique qui travaille
dans un domaine pluridisciplinaire et/ou sur des synthèses. Comme
l'hydrologie ne vit que dans la mesure où ses modèles sont compris et
utilisés en aval, il nous faut absolument satisfaire ces demandes de
« lisibilité » de nos modèles.

En partant de leur expérience de modélisation (surtout modèles
globaux, de synthèses et régionaux), les auteurs font les propositions
suivantes, testées de fait depuis longtemps et avec succès.
Strictement fidèles aux principes et règles générales ci-dessus, elles
conduisent à des sigles clairs et mnémotechniques qui soutiennent la
compréhension des variates et des modèles. Le bon accueil de nombre de
modèles ayant exploité ces sigles n'est peut-être pas étranger à la
clarté des significations que ces sigles y ont introduite.

## Grandeur physique, ou concept mathématique

Constitués a priori de Majuscules (de minuscules lorsque la tradition
ou des normes préexistantes l'imposent, éventuellement des deux), ils
sont complétés si nécessaire par des indices : ces indices sont a
priori en minuscules (en majuscules lorsque la tradition […]), et
« sur la ligne » pour éviter d'inutiles difficultés d'édition.

### Sigles de base (hors indices)

**Physique :**

| Sigle | Signification |
|---|---|
| C | Concentration |
| D | Déficit |
| d | durée |
| E | Évaporation |
| H | Hauteur d'eau ; il s'agit en fait d'une cote (rivière, nappe, …), un peu redondant avec z qui serait préférable, mais il faut respecter les traditions s'il n'y a pas risque de confusion, ce qui est le cas ici [?] |
| P | Pluie |
| Q | débit Q |
| R | état d'un stock (Réservoir, bassin, …) |
| T | Température |
| U | hUmidité |
| V | Vitesse |
| y | tirant d'eau (profondeur) |
| z | cote de l'eau (altitude) |

Cette liste n'est évidemment pas exhaustive, mais il est proposé de la
respecter strictement pour ce qui est déjà défini.

**Statistique :**

| Sigle | Signification |
|---|---|
| F | distribution de Fréquence annuelle, à base d'événements (épreuves) annuels, donc directement interprétables en périodes moyennes de retour exprimées en années ; correspond à une Fréquence au non-dépassement, F1 étant son complément à 1 qui correspond à la Fréquence de dépassement |
| f | densité de probabilité f d'une F |
| G | distribution de fréquence brute G à base d'événements non annuels, donc non interprétables directement en périodes moyennes de retour ; concerne des échantillons de taille différente (généralement supérieure) du nombre d'années dont les observations distribuées sont extraites |
| g | densité de probabilité g d'une G |
| m | moyenne, au sens statistique, d'une variate v ; on précise de quelle variable v par m(v) |
| N | dénombrement N au stade du résultat (d'où la majuscule) ; sert surtout à compléter F1 (voir ci-dessous) pour respecter la norme mathématique qui ne peut faire dépasser l'unité à une fonction de distribution |
| n | nombre d'années n (indépendantes) qui représente un échantillon ; complété par un indice (s ou x, cf. ci-après), il désigne une taille d'échantillon en sup- ou en nombre d'années (ns ou nx) |
| s | écart-type ; comme pour m, s(v) |
| T | période moyenne de retour T, selon les usages particuliers à l'Hydrologie ; donc exprimée en années, et pouvant être inférieure à l'unité |

### Indices complémentaires

**Physique :**

| Indice | Signification |
|---|---|
| B | Bassin, quand c'est nécessaire ; par exemple inutile pour un débit Q, toujours issu d'une aire définie, il est indispensable pour distinguer une Pluie Locale P (PL si on veut clarifier) d'une Pluie de Bassin PB (moyenne spatiale) |
| b | de base, associé à Q, pour caractériser l'écoulement de drainage des nappes et des réserves à longue mémoire, en soustrait [?] du débit total de la rivière |
| c | chimie ; il s'agit en fait d'un indice générique à remplacer par des indices plus précis, dont les « normes » sont encore à rechercher chez les chimistes |
| L | Local(e) ; permet parfois de préciser par opposition aux variates aréolaires, comme pour PL et PB |
| S | Solide ; associé à Q, il caractérise le débit des matières non solubles ; sans autre précision, il s'agit généralement du débit massique (sec) en suspension, mais il est utile de le rappeler, nécessaire de préciser les unités, et les indices complémentaires sont indispensables si la variate représente le charriage, le total, ou un débit volumique |
| TM, TP, TR | complémentaires à E (ETM, ETP, ETR – ET = évapotranspiration) |

**Statistique :**

| Indice | Signification |
|---|---|
| s | comme sup- (ou sous-) seuil, pour préciser que la variate concernée procède d'une approche de type « Renouvellement » |
| x | comme extrême, lorsque la variate concernée procède d'une approche de type « Valeurs extrêmes » |

### Sigles-indices intégrés

Ils sont décrits plus loin, au titre des sigles spécialisés, car leurs
indices ne se prêtent guère à d'autres usages.

## Durée (d) ou pas de temps (pdt)

À ne pas confondre avec les périodes définies en saisonnalisation
(voir plus loin), ces pdt ou durées s'entendent comme « continues »
(en un seul morceau sur une chronique).

### Sigles de base, hors indices

Ce sigle est donné **en seconde position**, après celui de la
grandeur.

| Sigle | Signification |
|---|---|
| A | pdt Année ; un indice peut préciser le civil d'une « hydrologique » |
| D | pdt Décade, au sens civil des décades calendaires ; les variates sur 10 jours « mobiles », libérées des contraintes du calendrier civil, ont leurs propres sigles spécialisés (voir ci-dessous) |
| H | pdt Horaire, au sens d'un pdt d'une heure à limites fixées a priori (heure « juste » légale) |
| h | pdt toujours précédé d'un nombre k quelconque ; il signifie non seulement un pdt plurihoraire de durée kh, mais encore une grandeur « centrée » sur ce pdt kh au sens des extrêmes, avec un centrage effectué au mieux à une heure près ; par exemple, une grandeur journalière sera siglée 24H si sa durée est mesurée sur une journée à limites fixées a priori, mais 24h si elle est centrée sur les valeurs les plus faibles ou les plus fortes [?], précision qui appelle d'ailleurs des sigles complémentaires (représentativité et saison) ; pour les débits, ce sigle est redondant avec ceux des grandeurs spécialisées de durées d, présentés plus loin (variates spécialisées), mais il est utile car encore souvent utilisé, quoique moins souple et destiné à disparaître |
| I | « pdt » Instantané ; le contexte définit le pdt minimal au-dessous duquel la variate est assimilable à une valeur instantanée |
| J | pdt Jour, au sens d'un Jour à limites fixées a priori (jour civil légal ou jour « météo ») |
| j | pdt toujours précédé d'un nombre k ; mêmes commentaires que pour h (kh), cette fois avec l'unité jour |
| M | pdt Mois, au sens civil du terme, avec un indice numérique de 1 à 12 pouvant éventuellement préciser le n° du mois |
| S | pdt générique pour Saison, au sens d'un pdt de durée saisonnière, à ne pas confondre avec les saisons au sens d'une partition du domaine d'étude (année), pour lesquelles il y a les sigles de saisonnalisation ; un indice, voire plusieurs, pour préciser cette Saison et sa durée sont indispensables ; un pdt saisonnier est généralement défini par la réunion de mois civils entiers ; un pdt étant obligatoirement continu, les mois doivent ici être adjacents (alors que c'est facultatif en saisonnalisation) |

### Indices complémentaires

| Indice | Signification |
|---|---|
| c | civil(e) ; pratiquement uniquement associé à A, et souvent omis car implicite alors |
| e | été ; utilisé essentiellement pour compléter la saison S |
| h | hiver / hydrologique ; hiver, comme pour e, sauf lorsqu'il est associé à A, auquel cas il signifie Année hydrologique |
| i | saison intermédiaire (voir ci-dessous) |

## La représentativité

Elle exprime donc ce que représente la variate de durée (pdt) d, à
l'intérieur d'un domaine temporel à définir (saison, le plus souvent),
et figure **en troisième position**.

Cette précision n'est présente que si le pdt est inférieur, et en
principe très largement, à la durée de la saison. Il y a alors
beaucoup de tels pdt, et si un seul (ou un nombre réduit) des pdt est
retenu, c'est par un critère très sélectif. En particulier, ce ne peut
être une valeur moyenne (au sens trivial déjà cité) sur le pdt, s'il
s'agit de la caractéristique statistique m notée m(v), v étant une
variate triviale (moyenne sur le pdt).

Les deux seuls cas réellement utilisés en hydrologie sont :

- **N** : pour miNimal(e), norme OMM ;
- **X** : pour maXimal(e), norme OMM.

On notera que ces deux sigles sont sémantiquement différents des
indices x (extrêmes) et s (sup- ou sous-seuils) cités en annexes aux
sigles des grandeurs : ils caractérisent ici l'objet des extrêmes,
alors qu'en indice complémentaire de sigle de grandeur, ils
caractériseraient une procédure d'échantillonnage. La différence
apparaît bien à la description des échantillons : les valeurs v
(grandeur et pdt définis) représentatives des extrêmes d'une saison
(vX ou vN) sont rassemblées dans des échantillons de taille :

- **n**, si une seule valeur v par saison (l'extrême unique) ;
- **ns**, si on extrait en moyenne ns/n valeurs par saison, triées en
  sup- ou sous-seuils ;
- **nx**, si on extrait systématiquement nx/n valeurs par saison,
  triées depuis l'extrême sensu stricto jusqu'à la nx/n-ième (et avec
  un critère d'indépendance cité ci-dessus en sup- ou sous-seuil, mais
  alors réputé « automatique »).

## Saisonnalisation

Le sigle doit donc exprimer la saison analysée, c'est-à-dire la
partition du temps sur lequel on échantillonne la variate, ou que la
variate est censée décrire. Ils sont **en quatrième position**.

Les sigles sont quasi identiques à ceux décrivant les pdt, mais leurs
indices complémentaires peuvent être différents.

### Sigles de base, hors indices

| Sigle | Signification |
|---|---|
| A | saison Année ; un indice éventuel précise le type |
| D | « saison » Décade ; rarement utilisé, mais des besoins pourraient apparaître en Biologie |
| E | saison Été, encore à préciser en dates exactes et en durée (les limites civiles sont rarement utilisées), le plus souvent par indice (contexte) |
| H | saison Hiver, encore à préciser… (voir Été) |
| J | « saison » Jour ; exceptionnellement utilisé pour des variates instantanées ou horaires |
| M | saison Mois, un indice numérique pouvant préciser lequel |
| S | Saison en général, à préciser en indice complémentaire (outre contexte pour dates exactes et durée) |

On notera que ces saisons, contrairement aux pdt, peuvent
éventuellement être constituées de **périodes non jointives**. Ainsi
d'une saison dite intermédiaire, souvent siglée Si (cf. indices
complémentaires ci-dessous), qui n'est que le complément à l'année
d'une partition que l'on voudrait complète et qui a été structurée sur
des choix saisonniers principaux bien typés (ex. : on ne s'intéresse
réellement qu'à l'hiver et à l'été, et on rassemble les mois restants
dans une saison dite intermédiaire).

### Indices complémentaires

Ils sont peu nombreux. On peut citer les mêmes qu'en pdt (c, e, i et
h), auxquels on ajoute un nombre de 1 à 12 si on veut caractériser le
n° civil d'un mois-saison. Par extension, on voit parfois des n°
civils de Jour ou de Décade, mais le contexte doit les définir car ils
sont peu connus.

## Exemples déjà classiques

Le tableau 1 présente des définitions et sigles choisis parmi les plus
employés aujourd'hui. À tous ces sigles peut être associée une date
(t) s'il s'agit d'une variate courante v(t), ou une période moyenne de
retour (T) s'il s'agit d'un quantile, le sigle représentativité
indiquant si c'est une T au dépassement (crues, etc.) ou au
non-dépassement (étiages, etc.).

Cette liste est potentiellement infinie et chaque jour de nouvelles
initiatives exploitent des combinaisons de grandeur, de pdt et de
représentativité saisonnière nouvelles.

On notera que seules les deux premières caractéristiques, de grandeur
et de pdt, sont toujours présentes.

**Tableau 1 — Sigles de variates physiques**

| Sigle | Grandeur | Pdt | Représentativité | Saison |
|---|---|---|---|---|
| PA | Pluie | Année | (totale) | — |
| PMXA | Pluie | Mois | maXimale | Année |
| PJXSh | Pluie | Jour | maXimale | S. hiver |
| P2hXE | Pluie | 2 heures (centrée) | maXimale | Été |
| PBM | Pluie/Bassin | Mois | (totale) | — |
| QA | débit (Q) | Année | (moyen) | — |
| QM | débit (Q) | Mois | (moyen) | — |
| QMNA | débit (Q) | Mois | miNimal | Année |
| QDXH | débit (Q) | Décade | maXimale | Hiver |
| QJ | débit (Q) | Jour | (moyen) | — |
| QJXM [?] | débit (Q) | Jour | maXimal | Mois |
| Q6hXA | débit (Q) | 6 heures | maXimale | Année |
| QHNJ | débit (Q) | H. civile | miNimal | Jour |
| QIXSh | débit (Q) | instant. | maXimal | S. hiver |
| ETRM | ÉvapoTr. Réel. | Mois | (totale) | — |
| ETPDXA | ÉvapoTr. Pot. | Décade | maXimale | Année |
| TJNS | Température | Jour | miNimale | Saison |
| C(N)3JXA [?] | Conc. azote (N) | 3 J. civils | maXimale | Année |

Les sigles d'objets mathématiques (utilisés en hydrologie) se prêtent
moins à des tableaux d'exemples. Voici quelques illustrations,
combinant éventuellement des sigles physiques et mathématiques :

- **Fs(QJXH)** : distribution de Fréquence annuelle d'un débit (Q)
  Journalier (civil) maXimal par saison Hiver, échantillonné en
  « sup-seuil » ;
- **Gs(P6hXA)** : distribution de fréquence brute (G) non annuelle
  d'une Pluie de 6 heures (centrée) maXimale Annuelle, échantillonnée
  en sup-seuil ;
- **F(PBA)** : distribution de Fréquence annuelle d'une Pluie de
  Bassin Annuelle ;
- **NF1 (ou NF)** : extension de F1 (Fréquence au dépassement,
  complément à l'unité de F), pour F1 > 1 ; permet d'introduire des
  périodes de retour T inférieures à l'unité (T = 1/F1 pour les
  maXimaux, et = 1/F pour les miNimaux) ;
- **Ts** : période moyenne de retour (T) au sens des « sup-seuils » ;
- **Tx** : période moyenne de retour (T) au sens des « extrêmes ».

## Les variates spécialisées

Certaines variates, d'usage assez généralisé pour nécessiter un sigle,
ont une définition trop complexe pour pouvoir entrer dans les règles
précédentes.

Ce sont pour l'essentiel les variates représentatives de débits (ou
autres grandeurs) sur des durées, et les variates synthétiques qui se
sont imposées dans la description des régimes hydrologiques.

S'y ajoutent des concepts statistiques spécifiques à l'Hydrologie et
introduits par extension de signification.

### Grandeur-durée-Fréquence (vdF ou vdT)

La durée d y est presque plus importante que la grandeur v.

Cette dernière est souvent le débit Q, ou la pluie notée ici
traditionnellement I (Intensité), plus un paramètre de qualité des
eaux, ou une caractéristique quantitative utile en hydrobiologie
(d'habitat, par exemple).

Dans ce qui suit, on présentera variates et sigles pour Q, la
généralisation aux autres grandeurs étant immédiate.

La **première lettre** précise la grandeur, au-delà du seul débit,
pour mnémotechniquement rappeler comment elle est liée à la durée :

- **V** : à la place de Q quand il s'agit d'une valeur moyenne sur une
  durée continue, c'est-à-dire d'un Volume ;
- **Q** : conforme au sigle générique de la grandeur débit Q, quand il
  s'agit d'un débit sensu stricto (intensité), c'est-à-dire d'un seuil
  à durée (continue) ;
- **D** : pour des motifs historiques, et pour appuyer encore sur
  l'importance des Durées, quand il s'agit de représenter des Durées
  cumulées, par ailleurs non continues.

La **seconde lettre** est systématiquement **C**, de Caractéristique,
pour bien distinguer cette famille des sigles classiques. Pour les
DC…, elle permet en outre de rappeler qu'il s'agit de Durées Cumulées.

La **troisième lettre** est conforme à la 3e des sigles classiques, et
affiche la représentativité, c'est-à-dire en fait le maXimum ou le
miNimum, la saison étant à préciser dans le contexte.

La **durée d** n'apparaît qu'à la 4e et dernière place, bien que son
rôle soit aussi essentiel que la grandeur (première place), et s'écrit
selon les règles ci-dessus (kj ou kh).

On aboutit ainsi, pour les débits, aux sigles bien connus suivants,
relatifs à une saison donnée :

- **VCXd (ou VCNd)** : extrêmes (maXimaux ou miNimaux) de débits
  moyens (notés : Volumes) sur une durée continue d ;
- **QCXd (ou QCNd)** : extrêmes (maXimaux ou miNimaux) de débits
  seuils (dépassés ou non dépassés) sur une durée continue d ;
- **DCXd (ou DCNd)** : extrêmes (maXimaux ou miNimaux) de débits sur
  une Durée Cumulée d (donc non continue a priori).

### Régimes hydrologiques

Les variates sont nombreuses, les classiques étant commodes pour
représenter les régimes et donc largement utilisées et suffisantes. On
notera, sans exhaustivité, pour les débits (idem en pluies P, en
concentrations C, …) :

- **QME** : débit (Q) MEnsuel d'Étiage : le QM du mois (civil) au sens
  moyenne (statistique interannuelle) le plus faible ; la date (n° de
  mois civil) est fixée, elle se distingue donc du QMNA dont la date
  peut varier d'une année à l'autre ;
- **QMC** : le symétrique en Crue du précédent (diffère du QMXA).

### Statistiques

Il s'agit essentiellement de nommer des variates qui sortent des
conventions statistiques habituelles :

- **annuel** : se dit d'un quantile dont la période moyenne de retour
  T est l'année (T = 1, F ou F1 = 1) ; à ne pas confondre avec un
  échantillonnage annuel [?] ; exige un échantillonnage avec nx ou
  ns > n ;
- **sous-annuel** : se dit d'un quantile de période moyenne de retour
  T inférieure à 1 an ; F et F1 ne sont alors plus définis, et la
  fréquence est siglée NF1 ou NF (cf. ci-dessus) ; exige un
  échantillonnage avec nx ou ns > n/T ; exige également que la saison
  soit bien définie, si nécessaire, car un tel quantile sous-annuel ne
  signifie pas qu'il est dépassé (non dépassé) en moyenne tous les T
  fractions d'années, mais NF1 (NF) fois par an (éventuellement dans
  la seule saison).

## Conclusion

Malgré la rigueur des règles proposées ici, la compréhension des
sigles correspondants n'en est pas pour autant immédiate en première
lecture. On ne saurait donc prendre prétexte de l'application de cette
note pour se libérer de l'obligation de bien définir les sigles et
notations employées, ainsi que d'expliciter [de définir] les variates
qu'ils représentent. On peut éventuellement se passer du rappel, voire
de la référence, à la présente note : le caractère pédagogique et
mnémotechnique doit apparaître de lui-même.

Largement mis en œuvre dans nombre de modèles, ces règles et sigles ne
sont sans doute pas étrangers au très bon accueil des travaux et
modèles de synthèse diffusés qui les utilisent. Outre la clarté qui en
résulte, les lecteurs arrivent mieux à percevoir les complémentarités
des modèles, et en particulier les complémentarités ou substitutions
« dans le temps », lorsque de nouvelles publications ou notes
techniques s'ajoutent aux précédentes. Il semble que le respect de ces
règles aide les utilisateurs à gérer rationnellement l'évolution
permanente et concomitante entre de nouveaux outils mis
progressivement à disposition, et d'anciens outils qui se périment.

Par exemple, en estimation régionale des crues, les règles montrent
bien les différences entre les anciens modèles SOCOSE et CRUPE(T) qui
donnent des QIXA(T), les nouveaux modèles complémentaires QdF qui
donnent des VCXd(T) ou des QCXd(T), et la famille des modèles GRid qui
donne des Q(t). En outre, les variables ou paramètres d'entrées sont
clairement définis : le QIXA(10) des QdF, la PLJXA(10) de CRUPEDIX,
les Pd(t) des GRid, etc. Enfin, on établit mieux les liaisons entre
ces modèles, comme par exemple :

- l'identité entre le VCX1j(T = 10) et le QJXA décennal (débit
  journalier décennal) en saison « année civile » ;
- l'identité entre le QCXIH(T = 2) et le QIXH biennal (débit Q
  instantané biennal) en saison Hiver ;
- la différence entre un QMNA (débit Q du Mois civil miNimal de
  l'Année) et un VCN30j (débit de 30 jours glissants miNimal de
  l'Année) ;
- etc.

Le handicap apparent de ces règles est lié, d'une part, au point de
vue des utilisateurs de l'hydrologie, à leur apparente complexité et à
l'aspect a priori barbare des sigles, et d'autre part, du point de vue
des scientifiques, à leur caractère en apparence facultatif. Mais il
faut construire des ponts durables et rationnels entre utilisateurs et
scientifiques. Ceci ne peut se faire sans moyens spécifiques et sans
efforts, car la distance qui les sépare est importante, sinon
inquiétante. ∎

---

*Pour obtenir des informations complémentaires, on pourra consulter
l'auteur : Guy Oberlin, groupement de Lyon du CEMAGREF, 3 bis quai
Chauveau, 69336 Lyon Cedex 09.*

*Extrait des Informations Techniques du CEMAGREF, Centre National du
Machinisme Agricole, du Génie Rural, des Eaux et des Forêts.*
