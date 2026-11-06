> **Statut : repères en vigueur.** Les choix du dépôt qui ne se
> déduisent ni du code ni d'une norme, chacun avec sa date et sa raison :
> on les suit tant qu'ils servent, et leur raison dit quand l'un d'eux ne
> tient plus. Les règles de nommage et de classification ont leurs normes
> (`dev/nomenclature.md`, `dev/topics.md`), les divergences avec le R
> leur fichier (`dev/r-origin.md`), et les consignes de travail le
> `CLAUDE.md`. Créé le 2026-11-06.

# Décisions de card

## Les principes documentaires (arbitrés le 2026-07-22)

Repris de la procédure de ménage de juillet
(`dev/plans/2026-07-21_cleanup.md`) à sa retraite, parce qu'ils valent
au-delà d'elle et pour les quatre dépôts de l'écosystème.

1. **Une VALEUR, un seul endroit.** Un nombre, un décompte, une
   affirmation vérifiable : les autres fichiers RENVOIENT, ne recopient
   pas, sinon l'un des deux finira faux. En revanche un **rappel de
   procédure** gagne à être répété là où on travaille : il ne peut pas
   mentir, et sa redondance est précisément ce qui évite l'oubli. Doubler
   une consigne, oui ; doubler un numéro de version, jamais.
2. **Git ne suffit pas.** Arbitré après s'être fait piéger sur la
   divergence de rolling, retrouvée à la main faute d'être écrite quelque
   part. Un document terminé reste en place avec un bandeau de statut, il
   ne se supprime pas, et chaque paquet tient un `CHANGELOG.md` qui dit ce
   qui a changé, quand, et où lire le détail. Depuis le 2026-11-06, la
   date dans le nom range les plans terminés : il n'y a plus de dossier
   d'archive.
3. **Pas de nom maison.** On utilise les noms attendus d'un dépôt
   (README, LICENSE, AUTHORS, CHANGELOG, CITATION.cff, ROADMAP) plutôt
   que d'inventer HISTORIQUE ou JOURNAL, qui obligent à deviner. Un
   bandeau de statut en tête de chaque document dit son rôle et sa
   validité.
4. **Sobre et exécuté.** Un README d'usage suit le parcours « pourquoi,
   quoi, comment », et chaque exemple y a été EXÉCUTÉ, jamais seulement
   écrit (Python puis R en parallèle quand les deux existent).

Deux règles de méthode, nées de la même campagne :

- **Aucune valeur dérivée dans un tableau d'inventaire.** Constaté le
  2026-08-04 : une colonne « lignes » avait dérivé sur chacune de ses
  lignes en deux semaines. `wc -l` la donne quand elle sert.
- **Trois questions tranchent une redondance supposée** : qui DÉFINIT
  cette information ? qui la RECOPIE ? est-elle encore VRAIE ? Et toute
  trouvaille se vérifie dans le code avant d'être écrite : une redondance
  supposée est souvent la même chose dite à deux niveaux de détail.

## La forme générique des fiches à placeholder est voulue (2026-07-21)

Précisé par l'utilisateur. La forme PAR DÉFAUT d'une fiche à suffixe
(placeholders résolus par `suffix_default`) est voulue générique : c'est
la métadonnée publique qu'exporte `card.extract(metadata_only=True)`, une
fiche volontairement non spécifique. Le mécanisme de suffixe est
précisément ce qui CLARIFIE les placeholders avec le contexte, quand
l'appelant fournit ses données de paramétrage externes. « target
horizon » par défaut n'est donc PAS un bug, c'est la forme générique
assumée.

Le travail n'est pas de figer du contexte dans la fiche, mais de
VÉRIFIER la cohérence : que chaque `{suffix.X}` forme une phrase lisible
en anglais et en français, en générique comme avec des enregistrements
riches. Mesuré le 2026-07-21 sur `delta-QA_H` et sur toutes les fiches à
placeholder : aucune accolade résiduelle, aucun mot double. Un
`suffixes:` par défaut ne se déciderait que si des exemples rendus
montraient le générique incohérent, pas par principe.

## Une fiche n'est silencieuse nulle part où ça a un sens (2026-08-13)

La règle d'écriture est dans le `CLAUDE.md` (quatre champs s'écrivent
toujours, un seuil délibérément absent s'écrit `null`). Ce qui l'a fait
naître :

Ce que le silence a coûté, deux fois : une ligne perdue dans la fiche R
de `RMAs_month` a fait annoncer douze variables comme relatives, seules
de leur famille ; et `dtFlood` calculait son maximum annuel sur une
année même privée de la moitié de ses jours, quand la fiche jumelle
`dtLF` écartait la même année. Les deux corrigés le 2026-08-13, et
aucun n'était visible fiche par fiche.
