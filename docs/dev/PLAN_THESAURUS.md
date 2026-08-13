> **Statut : plan ouvert, rien n'est publié.** Porte UNE question, celle
> qui reste après la livraison du site et de l'export SKOS (card 0.12.0) :
> le vocabulaire de card vit-il à côté de celui de Theia/OZCAR, ou
> dedans ? Et si c'est dedans, qu'est-ce que ça coûte, et que faut-il
> leur apporter ?
> Contient la mesure de LEUR thésaurus, faite sur le fichier entier, ce
> que card ajouterait, les trois options et leurs coûts.
> La construction du site et de l'export, elle, est close :
> `PLAN_SITE_SKOS.md` la garde, avec l'audit des vocabulaires qui reste
> la référence du modèle.
> À archiver quand la question sera tranchée et le vocabulaire publié.

# Où vit le vocabulaire de card

## La question, en une phrase

Le plan précédent a tranché « thésaurus à part, aligné depuis chez
nous », sur trois arguments : le volume, le contenu, la gouvernance. Deux
des trois se sont affaiblis quand on a enfin regardé leur thésaurus en
entier, et il faut donc rouvrir proprement.

## D'abord, comment on a mesuré, et ce que ça change

Les mesures des 2026-08-11 et 13 interrogeaient leur service **par
mots-clés**, concept par concept. On voyait ce qu'on cherchait. Le
2026-08-14, le vocabulaire a été **téléchargé en entier** (1,2 Mo de
Turtle, un seul appel), et l'image est différente.

```
23 086 triplets, 2 067 concepts
  1 152  iop:Variable
    302  iop:Entity
    233  ozcar:CategoryOfVariable      ← jamais vu avant
    140  iop:Property
    133  iop:Constraint
     35  cpm:StatisticalMeasure
     16  sosa:Sensor
```

**Ce qu'on avait raté : ils ont un arbre thématique de 233 catégories**,
avec de vrais mots, sous lequel pendent leurs variables. Ce n'est pas
l'arbre I-ADOPT des neuf composants, c'est un second axe, celui par
lequel un humain cherche :

```
Variable
├── Atmosphere variable
│   ├── Atmospheric temperature variable → Air temperature → 10 déclinaisons
│   └── Precipitation variable → Precipitation amount → 8 déclinaisons
├── Biosphere variable
├── Cryosphere variable
├── Land surface variable
└── Terrestrial hydrosphere variable
    ├── Groundwater hydrology
    ├── Karst hydrology
    ├── Surface water hydrology
    │   └── Surface water physic variable
    │       ├── Surface water discharge → River discharge → 10 déclinaisons
    │       ├── Surface water level, velocity, turbidity…
    └── Unsaturated zone variable
```

C'est exactement la « famille claire avec de vrais mots » qu'on se
demandait s'il faudrait inventer. **Elle existe déjà chez eux.**

## Le volume, mesuré : l'argument s'effondre

Le plan disait « une dizaine de concepts communs sur 2 506 chez eux et
des centaines chez nous, c'est un voisin, pas une sous-branche ». Les
chiffres réels :

| | concepts | variables |
|---|---|---|
| leur thésaurus entier | 2 067 | 1 152 |
| leur branche **hydrosphère continentale** | 970 | **821** |
| ce que card apporterait | ~490 | **444** |

Leur thésaurus est **déjà majoritairement de l'eau**. card ajouterait
54 % à cette branche et 38 % au total : c'est beaucoup, ce n'est pas
absurde. L'argument du volume ne suffit donc plus à décider.

## Ce qu'ils savent déjà dire, et c'est plus que prévu

Leurs 35 mesures statistiques forment une hiérarchie propre :

```
Accumulation → Temporal accumulation → 1 day / 1 hour / 1 year cumulative
                                        Summer cumulative, Winter cumulative
                                        Accumulation since the beginning of the year
Average      → Temporal mean          → 1 day / 1 month / 10-15-30 minutes mean
             → Spatial mean
Maximum      → Temporal maximum       → 1 day maximum, 1 year maximum,
                                        Maximum during wind gust
Minimum      → Temporal minimum       → 1 day minimum, 10 minutes minimum
Median       → Spatial median → 360° median
Standard deviation, Uncertainty interval, Instantaneous
```

Donc : ils ont **l'année** (`1 year cumulative`, `1 year maximum`), ils
ont **la saison** (`Summer cumulative`, dont la période est un concept
`Summer period`), et ils composent chaque mesure avec sa durée. C'est le
même geste que card.

## Les trous, précisément : ce que card apporterait

C'est la bonne façon de poser la chose, et c'est la proposition à leur
faire. Sur les dix-huit opérations de la facette `statistic` de card,
**cinq ont un équivalent chez eux** (moyenne, médiane, minimum, maximum,
cumul) et **treize n'en ont aucun** :

| ce que card ajoute | où ça se range chez eux |
|---|---|
| quantile, quantile de dépassement | sous `Statistical method` |
| période de retour | idem |
| pente de tendance, significativité de tendance | idem |
| écart entre deux périodes | idem |
| rapport, biais, efficience, élasticité, corrélation | idem |
| dépassement de seuil | idem |
| filtre (séparation d'hydrogramme) | idem |

Et sur les **spécialisations temporelles**, qui sont leur façon de
composer :

| ce que card ajoute | remarque |
|---|---|
| `1 year minimum` | ils ont le maximum et le cumul annuels, **pas le minimum** |
| `1 year mean`, `1 year median` | ils s'arrêtent au mois |
| moyenne mobile sur 3, 5, 10, 30 jours | aucune moyenne mobile chez eux |
| **année hydrologique** (12 mois à partir du 1er septembre) | leur `1 year` est une durée sans origine |
| fenêtres d'étiage datées | leurs `Summer period` et `Winter period` **n'ont aucune définition**, pas même des dates |

Ce dernier point mérite d'être dit tel quel : **leurs saisons ne sont
définies nulle part**. card en a de datées, et c'est un apport, pas une
critique.

Compté large, la contribution serait d'une **vingtaine de concepts
génériques**, utiles à tout observatoire qui publie autre chose que de
la donnée brute. C'est ce qu'on leur propose, et ça ne dépend pas de la
question de nos 444 variables.

## Les trois options

| | ce que ça veut dire | ce que ça coûte |
|---|---|---|
| **A. À côté, aligné** (l'état actuel) | nos concepts, nos URIs, notre génération ; des liens vers les leurs | rien de plus. Mais qui cherche une variable hydro chez eux ne trouve pas card |
| **B. Dedans** | nos 444 variables deviennent des concepts de LEUR thésaurus | quatre obstacles réels, plus bas |
| **C. À côté, mais rangé dans leur arbre** | nos concepts restent chez nous et déclarent `skos:broadMatch` vers leurs variables génériques ; on leur propose les composants manquants | quatre lignes de table dans `alignments.yaml` et une propriété de plus à l'export |

`skos:broadMatch` est la propriété SKOS faite exactement pour ça : une
hiérarchie qui traverse deux vocabulaires. `card:variable/VCN10` se
rangerait sous leur `River discharge` sans rien déplacer.

## Ce qui bloque vraiment l'option B

Le volume n'est plus l'argument. Restent quatre points, et les deux
premiers sont des faits vérifiés sur le fichier :

1. **Leur thésaurus est en ANGLAIS SEULEMENT.** `languages: ['en']`, et
   aucun `prefLabel@fr` dans les 23 086 triplets. La moitié de ce que
   les fiches de card écrivent n'aurait nulle part où aller.
2. **Ils n'emploient aucun `skos:notation`.** La porte d'entrée de card
   est le symbole (`VCN10`), qui est cité dans les publications, dans les
   sorties de calcul et dans les colonnes des tableaux. Chez eux, une
   variable se désigne par un libellé long.
3. **On perdrait la génération.** Aujourd'hui `card.ttl` se régénère à
   chaque changement du corpus et un test refuse l'écart : le thésaurus
   ne PEUT PAS diverger des fiches. Si les concepts vivent dans leur
   outil d'édition, la définition existe à deux endroits et plus rien ne
   les tient d'accord. C'est le seul argument technique décisif.
4. **La cadence et la charge.** Une version de fiche change une
   définition ; leur thésaurus est une référence de communauté qui bouge
   lentement. Qui met à jour, et à quel rythme ?

Les points 1 et 2 se règlent s'ils veulent bien : ajouter une langue et
une notation est une décision, pas un obstacle technique. Le point 3 est
le vrai sujet, et il se pose autrement : **ce n'est pas « à côté ou
dedans », c'est « qui génère »**.

## Ce que je recommande, et ce qu'il faut leur demander

**Option C, et la proposition des trous.** Concrètement :

1. leur proposer les **vingt composants génériques** qui leur manquent,
   qui servent tout le monde et qu'ils peuvent intégrer sans rien devoir
   à card ;
2. déclarer chez nous le `skos:broadMatch` vers leurs variables
   génériques, pour que nos 444 variables se rangent dans leur arbre
   thématique ;
3. leur poser les trois questions qui décident de la suite :
   - **acceptez-vous des libellés français** dans le thésaurus ?
   - **acceptez-vous une notation** (un symbole) sur un concept ?
   - **accepteriez-vous qu'un vocabulaire ENGENDRÉ soit chargé
     périodiquement chez vous**, plutôt qu'édité à la main ? C'est la
     question qui décide entre A/C et B.

Si la réponse aux trois est oui, l'intégration complète devient
souhaitable et le passage est mécanique : nos concepts portent déjà la
même composition que les leurs. Si elle est non sur la troisième, C est
le meilleur des mondes et rien n'est perdu.

## Ce que ça change pour les familles

La question « faut-il des familles claires, avec de vrais mots, comme
eux ? » a maintenant une réponse : **leur arbre thématique est déjà cette
famille-là**, et il vaut mieux s'y rattacher que d'en inventer un
deuxième. Nos 133 familles calculées ne sont pas la même chose : elles
groupent les variantes d'un même concept par paramètre (`QNA`, `VCN3`,
`VCN10`, `VCN30`), ce qu'aucun arbre thématique ne fait. Les deux axes
cohabitent :

- **leur arbre** dit de quoi on parle (eau de surface, débit de rivière) ;
- **nos familles** disent quelles variantes existent d'une même idée.

Le doute sur le libellé des familles (`débit · basses eaux · minimum ·
annuelle · série`) perd donc de son poids : ce libellé n'est plus la
porte d'entrée, il n'est qu'une étiquette de regroupement.

## Pour la prochaine session

Rien n'est à coder avant le courriel. Dans l'ordre :

1. **le courriel à Theia**, avec les trois questions ci-dessus et la
   liste des composants proposés ;
2. selon la réponse : implémenter C (petit) ou préparer B (autre
   chantier) ;
3. la base d'URI et l'hébergement, qui restent la seule décision
   irréversible et qui dépendent de cette réponse.

Ce qui est déjà tranché et qu'on ne rouvre pas est dans
`PLAN_SITE_SKOS.md`, y compris l'audit des vocabulaires, qui reste la
référence du modèle : ce que SKOS, I-ADOPT, CPM, CF, QUDT et OWL-Time
savent dire, et ce que card publie avec chacun.
