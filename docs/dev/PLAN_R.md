> **Statut : plan, en cours.** Comment un utilisateur R accède au corpus
> card sans qu'aucun moteur ne soit écrit deux fois, et ce que
> deviennent les paquets R historiques. Le chantier 2 est **fait**
> (`card4r` existe et tourne), les autres non. Ce qui est **décidé**, ce
> qui est **écarté** et ce qui reste **ouvert** sont distingués exprès.
> Sans rapport avec `NETTOYAGE.md`, procédure d'hygiène documentaire.
> **À supprimer une fois déroulé**, en répartissant son reste : ce qui
> concerne le front R ira dans `card4r`, ce qui concerne la référence
> gelée dans `ORIGINE_R.md`.

# Plan : l'écosystème R après le port Python

## Pourquoi ce fichier

Le sujet traverse quatre dépôts, dont deux qui doivent rester sans
fichiers IA. Il ne tient pas dans `CHANTIERS.md`, registre des pistes
ouvertes du seul corpus card.

## Le point de départ

Le port Python est validé sur le corpus entier (`ORIGINE_R.md`). Le
paquet R historique fonctionne : 206 fiches sur 217 tournent avec le R
installé ici, les 11 autres ont une cause diagnostiquée et écrite. Il
n'est pas cassé, il n'est pas en train de pourrir.

Ce qui a changé, c'est qu'il existe un utilisateur réel du paquet R
(D. Dorchies, G-EAU) dont le besoin est explicite : **utilisation en
local, sur données custom, en R**.

## Ce qui est décidé

1. **Rien ne quitte `lou-heraut/`.** Pas de transfert vers une
   organisation, pas de r-universe.
2. **Un corpus, un moteur.** Le corpus YAML de card est la source unique.
   Aucun re-port de stase ou de card vers R.
3. **`card4r`** : paquet R mince qui appelle card via reticulate. Dépôt
   et paquet portent le même nom.
4. **CARD-R reste du R pur**, sans fichiers IA, historique intact.
5. **`CARD` et `EXstat` passent `superseded`**, badge `lifecycle` et
   README explicite. L'archivage GitHub vient plus tard.
6. **`card4py` abandonné**, `card-stase` reste le nom de repli PyPI.
7. **PyPI mis de côté** pour l'instant.

## Ce qui est écarté, et pourquoi

Consigné pour ne pas y revenir.

- **Déménager CARD et EXstat vers `inrae/` + r-universe.** r-universe
  n'est pas le CRAN, et le paquet ne se lègue pas.
- **Un second moteur R maintenu par un tiers.** Même avec un corpus YAML
  unique, il reste une réimplémentation de chaque fonction hydro avec la
  même sémantique au flottant près. Une GitHub Action synchronise des
  déclarations, jamais des sémantiques.
- **Ajouter à `card-api` un endpoint qui accepte une série envoyée par
  l'appelant.** Ce serait la solution la moins chère en apparence, et
  elle servirait R, Julia et Matlab d'un coup. Elle est écartée pour le
  besoin visé : une donnée de recherche non publiée ne part pas sur un
  serveur, et le calcul local doit marcher sans réseau. La question du
  service reste ouverte pour d'autres usages, elle ne répond pas à
  celui-ci.
- **Renommer le paquet R historique.** Tranché : non (cf. chantier 1).
- **Honorer la signature de `CARD_extraction()` dans `card4r`.** Comparé
  le 2026-08-05 : `expand_overwrite`, `rmNApct`, `rm_duplicates` et `dev`
  n'ont aucun équivalent Python, ils ont disparu au portage. Les accepter
  pour les ignorer serait un mensonge d'API. `card4r` expose donc des
  noms neufs et le README donne la table de correspondance.

## Les chantiers

### 1. Réparer `Package:` dans le DESCRIPTION de CARD-R — FAIT le 2026-08-05

`Package: CARD-R` (commit `2f68ad6`) était refusé par `R CMD build` : un
nom de paquet R n'accepte que lettres, chiffres et points. Le paquet
historique n'était donc plus installable proprement. `Package: CARD`
remis, **dépôt qui reste `CARD-R`**, `Title` qui décrit le paquet au lieu
de répéter son nom. Vérifié : le build passe.

### 2. `card4r` — FAIT le 2026-08-05, version 0.1.0

**La règle de conception qui décide du coût : ce qui traverse le pont,
c'est de la donnée.** Un data.frame entre, des data.frames plus les
métadonnées sortent. Le front couvre `card_extract`, `card_trend`,
`card_list`, `card_info`, et **jamais** `card.functions` ni l'écriture
d'une fiche en R. Le jour où on voudrait faire traverser une fonction R,
le pont devient ingérable : c'est la différence entre un week-end et un
an.

Trois mesures ont décidé de la forme, et deux ont **simplifié** le
paquet par rapport à ce qui était prévu :

- **`py_require()` provisionne Python tout seul** (reticulate >= 1.41),
  uv et interpréteur compris, sur une machine qui n'avait ni l'un ni
  l'autre. La promesse « tu n'as rien à faire » tient donc, et la limite
  à documenter n'est plus « il faut installer Python » mais « il faut du
  réseau une fois ». `RETICULATE_PYTHON` reste la porte de sortie hors
  ligne, et card4r ne déclare alors rien pour ne pas avertir dans le vide.
- **reticulate convertit déjà data.frame vers pandas et retour**, sans
  colle. Ne restaient que les dates : une `Date` part en `POSIXct` UTC,
  ce qui arrive nativement en `datetime64` ; au retour les horodatages
  sont relus en UTC avant de redevenir des `Date`, sans quoi un minuit du
  1er janvier devient le 31 décembre précédent.
- **Les valeurs coïncident avec celles du paquet R historique à 1,8e-15**,
  la précision machine, sur QA et VCN10. Le test tourne avec la suite du
  paquet et se saute si `CARD` n'est pas installé.

`R CMD check` : Status OK, sans warning ni note. Distribution par
`install_github`. Le CRAN reste possible plus tard, c'est un chantier en
soi.

**Ce qu'il reste à faire pour card4r** : le dépôt n'est pas encore poussé
sur GitHub, et les deux refs épinglées (`CARD_REF`, `STASE_REF` dans
`R/zzz.R`) devront monter à chaque version de card qui compte pour un
utilisateur R.

### 3. Badges `superseded` et README de CARD et EXstat

`superseded` (lifecycle) dit : remplacé, plus recommandé, correctifs
critiques seulement, ne disparaît pas. **Ce n'est pas l'archivage
GitHub**, qui met en lecture seule et interdit tout, y compris à soi-même.

Le README doit dire pourquoi, et il peut désormais dire **où aller** :
`card4r` existe, et la bascule ne change pas les valeurs, ce qui est
mesuré. La matière du « pourquoi » est dans le mail du 2026-08-04 : 200
fiches à migrer à la main impossibles à tenir, BDOH qui est un projet
Python, MAKAHO bloqué par Shiny.

**Séquençage : badge d'abord, archivage en dernier.** La condition
posée, « ne pas déclarer CARD mort avant que card4r existe », est
maintenant levée : card4r existe et est vérifié contre lui.

### 4. Geler les sorties de référence R

**Prérequis de l'archivage seulement**, pas une urgence tant qu'un R qui
tourne existe. `Rscript run_R_corpus.R` (~10 min) continue de régénérer
la référence aussi longtemps que le paquet R est installable.

Le jour où CARD est archivé, on garde le code mais on perd le rejouable :
il faudrait reconstituer un R avec le dplyr d'avant la 1.1.

Ce qui serait gelé : `tests/data/R_corpus/` (206 fichiers, 5,8 Mo
compressés) et `tests/data/R_out/`, en retirant leurs lignes du
`.gitignore`. Les valeurs complètes, pas un condensé : une empreinte
dirait qu'il y a divergence, jamais laquelle, et c'est exactement la
question qu'on pose à une référence.

**Le trou à boucher en même temps** : rien ne relie la référence gelée à
l'entrée qui l'a produite. Committer le md5 de `test_data.csv` à côté de
`R_corpus/` et refuser la comparaison s'il ne correspond pas (32 octets,
attrape l'erreur) suffit ; committer les 18 Mo d'entrée est défendable
mais paie cher une question déjà réglée par `make_test_data.py`, qui
refabrique l'entrée depuis une graine fixe.

## Ce qui reste ouvert

- **Pousser `card4r` sur GitHub**, et décider s'il rejoint la carte des
  rôles de `NETTOYAGE.md` comme quatrième dépôt (fait) et s'il reçoit un
  `CLAUDE.md` (non fait, à décider).
- **Les ~50 fonctions hydro exportées par CARD** : `card4r` ne les
  republie pas, et c'est écrit dans son README. À rouvrir seulement si un
  utilisateur les appelle vraiment hors machinerie de fiches.
- **Récupérer les 11 fiches manquantes avant le gel ?** Il faut un R avec
  un dplyr d'avant la 1.1 (snapshot Posit PM ou image rocker) pour porter
  la référence de 206 à 217 fiches. Optionnel, et ne redeviendra jamais
  plus facile qu'aujourd'hui.
- **Câbler `run_py_corpus.py` en CI** une fois la référence dans git ?
  Bonus, demande de fabriquer les 18 Mo d'entrée à chaque exécution.
  Décision séparée du gel.

## Faits mesurés

Pour ne pas re-mesurer.

**2026-08-05, avant `card4r`** : `card.extract` est agnostique de la
source (vérifié sur un DataFrame synthétique) ; `card-api` ne sait
calculer que sur Hub'Eau, aucun endpoint n'accepte de série en entrée ;
CARD-R contient un second corpus, 217 fiches écrites en scripts R sous
`inst/__all__/`, plus ~50 fonctions hydro exportées, ce qui n'est pas une
copie du corpus YAML mais une autre écriture du même contenu.

**Noms PyPI** : `card` est squatté (release 0.0.1 de 2019) ; `stase` et
`card-stase` sont libres. Mis de côté par décision.

**2026-08-05, en construisant `card4r`** : R 4.5.2, reticulate 1.46,
`CARD` 2.0.0 et `EXstat` 3.0.0 installés et fonctionnels. Provisionnement
`py_require()` réussi depuis une machine sans Python déclaré ni uv, sur
le réseau INRAE, sans configuration de proxy. Pont data.frame vers pandas
sans colle. Écart maximal avec le paquet R historique : 1,8e-15 sur QA,
8,9e-16 sur VCN10.

**Tailles** (le point qui inquiétait, et qui ne tient pas) :

| | brut | compressé, ce que git stocke |
|---|---|---|
| `tests/data/R_corpus/` (206 fichiers) | 20 Mo | 5,8 Mo |
| `tests/data/test_data.csv` (l'entrée) | 18 Mo | 5,2 Mo |
| `.git` du dépôt aujourd'hui | 23 Mo | |

Une référence gelée n'est jamais réécrite : un blob par fichier, payé une
fois. C'est le bon cas pour git, à deux ordres de grandeur des limites
GitHub.
