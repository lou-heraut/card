> **Statut : brouillon, rien n'est envoyé.** Ce fichier porte ce qu'on a
> relevé dans la documentation et dans l'outil du SCHAPI en alignant card
> sur leur notation, et rien d'autre : pas de décision, pas de mesure du
> corpus. Ce que card fait de leur notation vit dans
> `src/card/alignments.yaml` et dans `PLAN_THESAURUS.md`.
> Aucun de ces points ne bloque quoi que ce soit chez nous : l'alignement
> tient sans eux. Ils leur sont utiles, à eux.
> Même rôle que `QUESTIONS_THEIA.md`, et même sort : à supprimer une fois
> la conversation engagée, en reportant ce qu'elle aura tranché.

# Ce qu'on a relevé dans la notation HydroPortail

Relevé le 2026-08-14 en alignant les quinze variables de card qui ont un
équivalent officiel. Tout a été lu en entier, documents et interface.

## Ce qu'on a lu, et où

Le point d'entrée public, `hydro.eaufrance.fr/documentation/
notations-statistiques`, ne porte aucun contenu : il renvoie à deux PDF.
C'est un détail, mais il coûte un aller-retour à qui cherche la règle.

| document | ce qu'il porte |
|---|---|
| `/uploads/Publications/NotationsStatistiquesV6_anonymisee.pdf` | la grammaire, V6, mars 2022 |
| `/uploads/Publications/ListeAnalysesStatistiques.pdf` | le tableau des analyses et les sigles répandus |
| `/uploads/Publications/ProceduresVsAnalysesStatistiques.pdf` | la correspondance HYDRO 2 vers HydroPortail V3, avril 2021 |
| `/uploads/Publications/Calcul_module_QMNA_VCN_vf.pdf` | le pas à pas QMNA5 / VCN10 / module |
| `/aide/donnees-et-noms-des-variables` | les règles telles que l'outil les applique |
| `/sitehydro/O8133520/statistiques` | ce qu'une station publie réellement |
| `id.eaufrance.fr/nsa/513` | la nomenclature Sandre des grandeurs élaborées |

## 1. Le dictionnaire de référence est en retard sur l'outil

C'est le point le plus important, parce que la V6 est le document que
toutes vos pages citent.

La V6 décrit une donnée de base comme `Grandeur · Filtre statistique ·
Filtre temporel`, et donne `QJ`, `QM`, `Q3J`, `QXh`. Elle ne connaît pas
les marqueurs `i` et `m`.

L'aide en ligne, elle, décrit la même chose avec ces marqueurs, et c'est
cette forme que l'interface emploie : la liste déroulante « Grandeur »
d'une analyse affiche `QmnJ - Débit moyen sur n jours`, et l'aide écrit
`Qm3J-N`, `QmM-N`, `QiXnJ-N`, `QiNnJ-X`.

Les deux écritures sont réconciliables, l'aide donnant les raccourcis
(« `Qm1J`, raccourci en `QmJ` même plutôt `QJ` », « `QmM-N`, raccourci en
`QM-N` », « `Qi-X` en général simplifié en `Q-X` »). Mais elles sont dans
deux documents, dont le plus officiel est le moins à jour.

**Ce qui manquerait le plus à quelqu'un qui cite votre notation : dire
laquelle des deux formes fait foi.** Un raccourci est commode dans une
interface ; dans une publication ou un catalogue de données, il faut
savoir si on écrit `Qm3J-N` ou `Q3J-N`. Vos propres documents ne
choisissent pas : la fiche de station affiche `Q3J-N (VCN3)`, l'aide
écrit `Qm3J-N`.

## 2. Cinq écritures pour le débit moyen annuel

En cherchant comment nommer la moyenne annuelle des débits journaliers,
on a trouvé cinq écritures dans votre écosystème, sans qu'aucun document
ne les mette en regard :

```
QA            V6, § variables hydrologiques  « Le débit moyen annuel QA ou Q-Moy »
Q-Moy         V6, même ligne
QJ-Annuel     ListeAnalysesStatistiques, sigle répandu « Moyenne annuelle »
QJ-annuel     aide en ligne et fiche de station, analyse de référence toutes eaux
QmA           Sandre, nomenclature 513, « Débit moyen annuel »
```

Et le résultat de cette analyse s'affiche sous un sixième nom, `Module`,
qui est aussi un code Sandre à part entière (« Débit moyen inter-annuel »).

L'ambiguïté n'est pas seulement typographique. `Q-Moy` se décompose en
donnée de base `Q`, qui est chez vous l'instantané ; `QA` ne dit pas sur
quel pas de temps porte la moyenne ; `QJ-annuel` est la seule des trois
dont la donnée de base soit explicitement journalière, et c'est la seule
que l'outil affiche. C'est celle que card retient.

Deux détails de la même famille :

- la casse diffère entre `QJ-Annuel` (plaquette) et `QJ-annuel` (aide et
  interface) ;
- la ligne `QJ-Annuel` du tableau des analyses porte le descriptif de sa
  voisine, « Quantiles des Débits moyens journaliers », alors que son
  sigle dit « Moyenne annuelle » et que sa formule est bien une moyenne
  annuelle. C'est la ligne qui sert de référence pour le module.

## 3. Deux lignes qui lisent le même indice à l'envers

Votre indice de fréquence est celui du **non** dépassement, et la V6 le
dit explicitement, titre de section compris. Trois lignes le confirment :
`QJ0,0274` pour le débit non dépassé 10 jours par an, `Q0,9726` pour le
débit dépassé 10 jours par an, `Freq[QJ ≤ QJn/12] = n/12` pour le DCNn.

Dans le tableau des analyses, section Hautes Eaux, deux lignes voisines
lisent pourtant le même indice `355j/an` de deux façons opposées :

```
Q355/365, Q1-10/365, Q355j/an   « Le débit instantané dépassé en moyenne
                                  10 jours par an »            (DCC)
QJ355j/an                       « Le débit moyen journalier dépassé
                                  pendant 98 % du temps »
```

Le premier est un débit de crue, le second un débit d'étiage. Sous la
convention du non dépassement, c'est la seconde ligne qui est fausse.

Plus bénin, la formule de `QJ0,5` s'écrit `Freq[QJ > QJ0,5] = 0,5`, avec
un signe de dépassement là où les autres lignes de fréquence emploient le
non dépassement. Sur la médiane ça ne se voit pas, et c'est justement la
ligne qu'on prend pour exemple.

## 4. La période de retour s'écrit de deux façons

`QM-N(5)` et `Q3J-N(5)` dans le tableau des analyses et dans la V6,
`Q10J-N5` et `Q3J-N5` dans le document QMNA5 / VCN10 / module. La
parenthèse est ce que la grammaire définit, donc c'est elle qui devrait
l'emporter partout.

## 5. Une phrase de l'aide dit le contraire de ce qu'elle veut dire

Dans « Données et noms des variables » :

> QCNn, dans Hydro2 était le débit seuil pour les étiages, le plus petit
> maximum de n débits journaliers consécutifs. On l'obtient [...] en
> sélectionnant [...] les QiXnJ **minima** de débits instantanés sur n
> jours puis l'extracteur minimum.

`QiXnJ` est le débit instantané **maximal** n journalier, comme le dit
votre propre nomenclature Sandre, et comme l'exige la définition de QCNn
que la phrase donne elle-même. La phrase jumelle sur QCXn, juste
au-dessus, est correcte.

## 6. Un lien public pointe vers un environnement de préproduction

La plaquette « Les analyses statistiques », page 2, renvoie à
`www.proto.hydroportail.developpement-durable.gouv.fr/publication/
notations-statistiques` pour le détail des notations. C'est un serveur de
proto dans un document public.

## Côté Sandre, deux remarques qui ne vous appartiennent peut-être pas

La nomenclature 513, « Type de grandeur de l'observation élaborée Hydro »,
est ce qui se rapproche le plus d'un registre officiel citable pour ces
grandeurs. Deux choses la rendent difficile à employer comme référence.

- **Aucun code n'a d'adresse propre.** `id.eaufrance.fr/nsa/513/QmJ`
  renvoie la nomenclature entière, octet pour octet identique à
  `id.eaufrance.fr/nsa/513`. Un code ne peut donc pas être cité
  individuellement, ce qui est précisément ce qu'un catalogue de données
  a besoin de faire. C'est une entrée de configuration, pas un chantier.
- **`Qm` et `QmnJ` portent le même libellé**, « Débit moyen sur n jours »,
  le premier gelé, le second validé. Un lecteur qui rencontre `Qm` dans
  une donnée ancienne n'a rien qui le renvoie vers son successeur.

## Ce qu'on ne demande pas

Rien. card publie ses correspondances de son côté, elles n'engagent
personne, et la table est écrite à la main précisément parce que vos deux
grammaires et la nôtre descendent du même texte, Oberlin 1992, et se
ressemblent assez pour qu'une correspondance fausse passe inaperçue.

Ce qui serait utile, en revanche, et qui ne coûte que deux décisions :
dire quelle forme fait foi (§ 1), et laquelle des cinq écritures du
module est la bonne (§ 2).
