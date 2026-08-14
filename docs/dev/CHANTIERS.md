> **Statut : registre vivant.** Ce fichier ne contient que des pistes
> **ouvertes**. Un chantier livré en sort et devient une entrée de
> `CHANGELOG.md`, à la racine du dépôt, qui renvoie au document
> expliquant le détail. Les sections portent des titres et non des
> numéros : le registre bouge, un numéro ne se cite pas durablement.

# CHANTIERS : pistes ouvertes (mise à jour 2026-08-14)

## Aucun concept de facette ne porte de définition (2026-08-14)

Mesuré sur `docs/card.ttl` avant de le montrer à quiconque : les 573
concepts ont tous un `skos:prefLabel` dans les deux langues et aucun
n'est orphelin, mais **les concepts qui portent l'arbre n'ont qu'une
étiquette**. `basses eaux`, `débit de base`, `saisonnalité`, `par saison`
n'ont ni `skos:definition` ni `skos:scopeNote`. Côté variables, 257 sur
444 ont une définition, et c'est délibéré : une fiche ne remplit sa
`description` que si son `name` ne dit pas déjà tout.

Ce qui manque tient en une quarantaine d'entrées, dans `topics.yaml` :
4 grandeurs, 11 phénomènes, 5 aspects, 18 statistiques, 6 fenêtres,
3 formes, 2 finalités. Le fichier ne porte aujourd'hui que `en` et `fr`,
donc c'est un champ de plus et une phrase par entrée, relue.

**Pourquoi ça presse un peu** : `QUESTIONS_THEIA.md` leur signale que
`Summer period` et `Winter period` ne portent aucune définition chez eux.
Leur envoyer cette remarque avec un vocabulaire dont aucun phénomène
n'est défini serait une invitation à la retourner. Ce n'est pas un
blocage, c'est une question de tenue.

## Nom PyPI de card (PEP 541)

Le nom `card` sur PyPI est occupé par une réservation VIDE : mesuré le
2026-08-05, la release unique de 2019 ne contient aucun module Python et
`pip install card` n'installe rien. C'est le motif le plus solide de
PEP 541, celui du projet invalide.

**En attente d'action de l'utilisateur.** Les preuves, les trois textes
à envoyer et les dates d'envoi vivent dans `PLAN_PYPI.md`, qui est le
seul endroit qui les porte.

Ne rien publier sur PyPI tant que la demande n'est pas tranchée :
`card-stase` reste le nom de repli du `pyproject.toml`, et l'import est
`card` dans tous les cas.

## Le kwarg `relative` de `delta` est déductible (2026-08-13)

Mesuré pendant le chantier `relative` : le kwarg `relative` passé à la
fonction `delta` dans un `process` et le champ `meta.global.relative`
expriment **la même propriété**, l'un du côté du calcul, l'autre du côté
de la déclaration. Ils s'accordaient déjà 77 fois sur 82 avant
correction, et les 5 écarts se sont tous révélés être des erreurs.

Le kwarg pourrait donc être déduit du `relative` de la variable de BASE
que le `delta` consomme, au lieu d'être écrit une seconde fois. Même
raisonnement que le retrait d'`operator` : une valeur écrite deux fois
finit par diverger, et la fiche seule ne peut pas dire laquelle a raison.

Ce qu'il faudrait regarder avant : le `delta` de `card.functions` est une
fonction publique dont `relative` est un paramètre légitime ; le déduire
côté fiche ne doit pas retirer à quelqu'un qui appelle la fonction
directement la possibilité de le choisir. La piste porte donc sur le
LOADER (remplir le kwarg depuis la déclaration quand la fiche ne l'écrit
pas), pas sur la signature.

Rien ne presse : depuis la correction, le linter tient déjà les deux
d'accord par l'unité.

## Signalement amont des fiches R cassées

Des fiches plantent dans le paquet R lui-même, donc sans référence
croisée possible. Le signalement en amont est devenu actionnable le
2026-07-22, la cause étant diagnostiquée : **lesquelles, et pourquoi, se
lisent dans `ORIGINE_R.md`** (deux familles, dont l'une est un
`summarise` que dplyr a durci sous des fiches qui fonctionnaient).

Ce qui reste à faire, et qui n'est écrit qu'ici :

- correctif probable côté EXstat pour la première famille : basculer
  l'appel de `summarise` vers `reframe` quand la fonction rend un
  vecteur ; la seconde famille est à creuser séparément, sa cause n'est
  pas établie ;
- le diagnostic vaut pour la version de R installée ici : le rejouer sur
  l'environnement de l'utilisateur avant d'ouvrir le signalement.

## Référence R gelée : deux pistes optionnelles

La référence croisée est dans le dépôt depuis le 2026-08-05
(`ORIGINE_R.md`). Deux choses restent possibles, aucune nécessaire.

- **La porter de 206 à 217 fiches.** Onze fiches ne tournent plus dans le
  paquet R avec dplyr >= 1.1, donc la référence gelée ne les couvre pas.
  Les récupérer demande un R d'époque, image rocker ou snapshot Posit
  daté. Ne redeviendra jamais plus facile qu'aujourd'hui, et se périme un
  peu plus chaque année.
- **Câbler `run_py_corpus.py` en CI.** Devenu possible maintenant que la
  référence est versionnée, mais demande de refabriquer les 18 Mo
  d'entrée à chaque exécution. Bonus, pas un manque : la garde de
  non-régression est `test_py_golden.py`, et elle tourne déjà.

## Références externes : la bibliographie, et les notations officielles

Deux choses distinctes, longtemps confondues ici, et elles n'ont pas le
même lieu.

**La bibliographie** ancre une fiche standardisée sur son article :
identifiants climdex/ETCCDI (RCXA1 ↔ RX1day, RCXA5 ↔ RX5day,
dtCDDA ↔ CDD, dtCWDA ↔ CWD...). **À retravailler avec le système de
biblio scientifique existant de l'utilisateur** (ne pas inventer un
format de citation avant d'avoir vu le sien).

**La notation officielle du SCHAPI est alignée depuis le 2026-08-14**,
pour quinze variables et une grandeur d'entrée. Comment c'est fait, ce
qui est écarté et pourquoi, et les deux correspondances laissées de côté
faute d'une décision de leur part : `PLAN_THESAURUS.md`, sections « La
notation officielle française » et « Ce qui reste ouvert ». Rien n'est
recopié ici.

Une règle qui vaut pour toute extension, en revanche, parce qu'elle est
propre à ce chantier : **rien ne se dérive**, la table s'écrit à la
main. Décoder un nom de variable serait le piège d'`operator` en pire,
les deux grammaires descendant du même Oberlin 1992 et se ressemblant
assez pour qu'une correspondance fausse passe inaperçue.

## Lint temps réel sous Emacs

Objectif : valider les YAML pendant l'édition. Deux voies :
- générer un **JSON Schema** des fiches (depuis schema.py) et brancher
  `yaml-language-server` (paquet Emacs `lsp-mode` ou `eglot`), la voie
  standard, autocomplétion incluse ;
- ou un checker flycheck maison qui appelle
  `python -m card.schema <fichier>` (déjà supporté en CLI, plus simple
  mais sans autocomplétion).

## Deux réserves laissées dans des descriptions (2026-08-03)

Le chantier des descriptions est livré (cf. `CHANGELOG.md`). Deux points
n'ont pas pu être tranchés faute d'information :

- `CR` et `CRS_season` s'appellent « coefficient correctif » sans que la
  fiche ni le code ne disent comment appliquer la correction. Leur
  description s'arrête donc au fait, le rapport simulé sur observé.
- Celle d'`a-FDC` lit la pente comme une mesure de variabilité du régime,
  ce qui est la lecture usuelle mais reste une lecture.

## Si une moyenne de pluie devient une SORTIE (veille)

`RA-mean` règle trois colonnes intermédiaires, et c'est proportionné.
Mais Oberlin n'a pas de case pour la moyenne temporelle d'une pluie :
pour lui ce n'est pas une variate, la position 3 vide valant « totale »
(cf. `NOMENCLATURE.md`). Le jour où une telle moyenne devient une
sortie publiée, il faudra un jeton de position 3 plutôt qu'un suffixe de
variante, donc une extension du système et non un contournement.

## Deux fonctions circulaires sans usage

`circular_ratio` et `circular_difference` ne sont employées par aucune
fiche (mesuré le 2026-08-03). Ce sont des portages de R, donc la question
est une question de PARITÉ, pas de ménage : les retirer romprait la
correspondance avec `CARD`/`EXstat`, les garder laisse deux fonctions
qu'aucun test de fiche n'exerce. À trancher avec le sort du portage.

Leur voisine `difference_longest_run`, elle, a été retirée le 2026-08-03 :
créée par symétrie le 2026-07-31, aucune fiche ne l'a jamais employée
(cf. `RENAMING.md`).

## `meta.sampling_period` : prose d'un côté, littéral Python de l'autre

Une partie du corpus écrit une phrase (« Mois du maximum des débits
mensuels »), une autre un littéral brut (`['01-09', '31-08']`) que la
figure doit reformater pour le rendre lisible. Même famille de problème
que `method` avant sa refonte : un champ qui porte deux formes sans règle.
Repéré pendant le chantier `method`, pas traité.

## Une donnée de FONCTION complète les métadonnées affichées d'une fiche (2026-08-12)

Gêne exprimée par l'utilisateur, non tranchée. Elle est réelle et voici
sa mesure exacte.

La figure d'une fiche tire toutes ses **phrases** du `method` de la
fiche : plus aucune docstring de fonction n'y entre, c'était l'objet du
chantier `method`. Mais elle dessine aussi un **grain**, les lignes
marquées `◦` (« Une valeur par jour », « Une seule valeur, répétée sur
toute la chronique »), et celui-là se calcule depuis `time_step` et
`keep` du process.

Dans un cas, ces deux champs ne suffisent pas : `time_step: none` avec
`keep: all`, qui recouvre deux comportements opposés. `render.decoupe`
consulte alors `is_transform`, attribut posé **sur la fonction Python**
dans `card/functions/`. C'est le seul endroit du paquet qui le lise.

Mesuré le 2026-08-12 : **124 process sur 504, dans 91 fiches**. Deux
exemples, dont les YAML sont identiques à cet endroit :

```
VCN10 P1        time_step: none, keep: all, rollmean_center
                → « Une valeur par jour »
n-VCN10-5_H P3  time_step: none, keep: all, return_level
                → « Une seule valeur, répétée sur toute la chronique »
```

**Pourquoi il existe** : la version précédente devinait, en cherchant le
préfixe `nan` et deux noms écrits en dur dont `quantile`. Le renommage
`compute_Qp` → `exceedance_quantile` a laissé la chaîne derrière lui et
six figures ont annoncé « une valeur par jour » pour un seuil unique.
`is_transform` est la déclaration minimale qui a remplacé cette
devinette.

**Pourquoi ça gêne quand même** : une fiche doit être autoportante, et
là une ligne de sa figure dépend de code hors de la fiche.

Les trois sorties possibles, aucune satisfaisante en l'état :

- **la fiche le déclare** : il faudrait le redire à chaque process, pour
  une propriété inhérente à la fonction et identique partout où elle est
  appelée. C'est de la duplication, et elle peut se contredire ;
- **la figure renonce à la ligne** : on perd une information que le
  lecteur utilise, et qui est juste ;
- **une troisième voie reste à trouver**, par exemple faire porter la
  nature de la sortie par le `func` de la fiche plutôt que par la
  fonction, ou la déduire de la chaîne de colonnes déclarée.

**Ce qui est déjà tranché** : c'est une propriété d'**affichage**, pas de
sens. Elle ne peut donc pas fonder un alignement sémantique, et
`PLAN_SITE_SKOS.md` l'écarte explicitement de l'export SKOS.

## Raffiner `method` par étape, en plus de la classification (2026-08-12)

La facette `statistic` classe la variable par son opération TERMINALE,
une valeur par variable produite. Elle répond au besoin de familles et à
`hasStatisticalModifier` d'I-ADOPT, qui est facultatif et peut être
unique.

Elle ne dit rien de la **chaîne** : `VCN10` est un minimum d'une moyenne
mobile de dix jours, et seule la première moitié est classée. Le besoin
est réel mais **différent** : la chaîne ne permettrait pas la
classification globale d'une variable, et la classification ne permet pas
de décrire la chaîne. Aucune des deux ne remplace l'autre.

Si on la veut un jour, sa place est identifiée : `method` est indexé par
process et par colonne produite, soit **856 entrées** dans le corpus, et
c'est exactement la granularité où une opération vaut un mot. Deux formes
possibles :

- un bloc parallèle indexé comme `method`, que le linter vérifierait de
  la même façon qu'il vérifie déjà la correspondance des clés ;
- ou l'entrée de `method` qui devient une table,
  `{statistic: mean, text: "..."}`, plus juste mais imposant une
  migration de format sur les 856 entrées, alors que `method` vient
  d'être refondu (`archive/PLAN_METHOD.md`).

Le vocabulaire, lui, serait le même : celui de la facette `statistic`.
Donc rien de ce travail n'est perdu si on s'y met plus tard.

**Devenu un prérequis le 2026-08-13, et pas seulement un confort.** Le
thésaurus sait maintenant dire qu'une statistique porte sa fenêtre
(« minimum sur l'année hydrologique »), et le vocabulaire CPM sait
chaîner une mesure statistique à une autre, ce qui écrirait « minimum
annuel d'une moyenne sur 10 jours » d'un seul tenant. Ce qui manque pour
le faire est exactement cette piste : la statistique de l'étape
INTERMÉDIAIRE. La deviner voudrait dire lire un nom de fonction, c'est
le piège d'`operator`. Détail et forme visée : `PLAN_SITE_SKOS.md`,
section « Deux choses arrêtées en chemin ».

## Revue de code du package (lisibilité, dé-boîte-noire)

Crainte utilisateur : code trop compliqué ou alambiqué par endroits.
À son initiative, mais aides possibles : un `ARCHITECTURE.md` qui
explique le pipeline en langage simple (loader, stase, compactage), et
une passe de simplification ciblée sur `extraction.py`, qui concentre la
complexité (kwargs-colonnes, colonnes creuses, fan-out).

## Documentation utilisateur étendue

- README : section « développer sa fiche » faite (copy_cards puis
  extract(path=...) puis `python -m card.schema`) ; à étoffer d'un
  exemple complet de fiche commentée ligne à ligne ?
- Pages : tutoriel pas-à-pas avec données réelles.

## Export SKOS et site de documentation

Le besoin s'est concrétisé le 2026-08-11 : ces deux pistes sont sorties du
registre et ont leur propre plan. **Les deux sont livrées en 0.12.0**, et
il en reste deux publications, chacune dans son document :

- `PLAN_SITE_SKOS.md` : ce qui a été construit, l'audit des vocabulaires
  qui reste la référence du modèle, et les trois bascules du jour où le
  site part en ligne ;
- `PLAN_THESAURUS.md` : la question restée ouverte, à côté de
  Theia/OZCAR ou dedans, avec la mesure de leur thésaurus et ce qu'il
  faut leur demander.

Ne rien noter ici de ce qui les regarde.

Ce qui restait écrit ici et qui n'est pas dans le plan, parce que ça
concerne le service et non le corpus : card-api pourrait exposer un
`GET /v1/concepts` renvoyant vers les URIs des concepts. C'est un renvoi,
pas une source : la vérité reste dans `src/card/topics.yaml` et dans les
blocs `classification` des fiches.

## Unités machine-lisibles (UCUM) (différé)

Les unités sont des chaînes LaTeX-ish (`m^{3}.s^{-1}`, `hm^{3}`, `jour de
l'année`, `sans unité`). Lisibles pour un humain, mais pas
interopérables : un client ne peut pas convertir ni comparer sans parser.
Piste : ajouter un code **UCUM** (`m3/s`, `Cel`, `mm`…) à côté de chaque
unité, dans `inputs.yaml` pour les entrées et dans un registre pour les
sorties, exposé tel quel par card-api. Amélioration FAIR-Interopérabilité,
sans urgence (même famille que l'export SKOS). Noté depuis la revue FAIR
de card-api du 2026-07-24.

## Tendance des régimes mensuels et saisonniers (limite structurelle)

`card.trend` ne s'applique qu'aux fiches `output: series` (une valeur par
année). `QM` (régime mensuel, `curve`) et `QSA_season` (agrégat saisonnier)
ne sont donc pas tendançables, alors qu'une tendance du régime mensuel
aurait du sens. Ce n'est pas un bug : ces fiches collapsent ou indexent le
temps autrement que par année, ce que le modèle série-annuelle de stase ne
couvre pas. Piste future : une variante `output: series` par mois/saison
(le fan-out `_month`/`_season` existe déjà côté valeurs), ou un mode trend
qui accepte un axe sous-annuel. Noté à la revue card-api du 2026-07-24, à
ne pas traiter maintenant.

## Ce que HydroPortail calcule et que card n'a pas (inventaire 2026-08-14)

Relevé en alignant card sur la notation officielle du SCHAPI, en lisant
leurs quatre documents, leur aide en ligne, la nomenclature Sandre 513 et
la fiche de statistiques d'une station réelle. C'est un inventaire de
CORPUS : chaque ligne est une fiche possible, aucune n'est décidée.
L'intérêt du repère est que le SCHAPI fixe en partie la pratique
française, donc une absence ici est une absence que des utilisateurs
verront. Ce qui a été relevé dans LEUR documentation est ailleurs :
`RETOURS_SCHAPI.md`.

**Sept absences qui ont un sens hydrologique clair.**

- **QCNn** (`QiXnJ-N` chez eux, code Sandre `QCN`) : le plus petit
  maximum de n débits consécutifs, seuil au-dessous duquel les débits
  sont restés n jours. Seuil d'étiage, et c'est une procédure HYDRO 2
  historique.
- **QCXn** (`QiNnJ-X`, Sandre `QCX`) : le symétrique en crue, le plus
  grand minimum de n débits consécutifs.
- **QME**, débit moyen d'étiage (Sandre) : le débit du mois dont la
  moyenne inter-annuelle est la plus faible. card a la courbe `QM`, donc
  les douze valeurs, mais ne publie pas son minimum.
- **DCE**, débit caractéristique d'étiage : le débit journalier non
  atteint 10 jours par an. Notion réglementaire, très citée.
- **DCC**, débit caractéristique de crue : dépassé 10 jours par an.
- **DCn**, débit caractéristique de durée n mois (1, 3, 6, 9) : égalé ou
  dépassé pendant n mois de l'année.
- **Durées cumulées ou maximales sous ou sur un seuil**, avec ajustement
  et période de retour (`dc()`, `dx()`), qu'ils annoncent comme leur
  nouveauté en hautes eaux. card a des durées, mais attachées à des
  définitions hydrologiques fixes, jamais à un seuil libre. Même famille
  que la piste « durées cumulées de dépassement » plus bas.

Les trois premières sont des variables au sens de card. Les trois
suivantes sont la même idée à une paramétrisation près : `DCE` et `DCC`
sont des quantiles sur chronique entière, comme `Q10`, `Q50` et `Q90`,
mais exprimés en jours par an. Les créer serait moins un ajout qu'une
extension de la famille `Q<p>` vers leurs valeurs usuelles.

**Deux différences de déclinaison, pas des absences.**

- Leur fiche de station porte `Q3J-N (VCN3)` pour **chacun des douze
  mois**. card décline `VCN3` par saison (`_summer`, `_winter`), pas par
  mois. Les deux se défendent ; le fan-out mensuel existe déjà côté
  valeurs.
- `DCNn` et `DCXn` sont des débits journaliers de **rang** n dans
  l'année. card a `Q90A`, `Q95A`, `Q99A`, la même idée par fréquence.

**Hors périmètre assumé, à ne pas compter comme un manque.** Toute la
famille instantanée (`QIX`, `QIN`, `QIXJ`, `QINJ`, et le `Q-X (CRUCAL)`
instantané) : card part de chroniques journalières. Les hauteurs, pour la
même raison. Et les ajustements de lois de distribution, qui sont leur
métier : card produit l'échantillon, `stase` fait les niveaux de retour
là où une fiche le demande.

**Ce que card a et qu'ils n'ont pas**, pour que le tableau soit
équilibré : débit de base et séparation d'hydrogramme, dates et volumes
d'étiage, durées de crue, précipitations, températures,
évapotranspiration, tendances, performance de modèle et sensibilité
climatique. Le recouvrement est étroit, et il est entier du côté des
basses et hautes eaux de débit.

## Fiches futures

- **Rc** (vrai coefficient de ruissellement adimensionnel) :
  86,4 × ΣQ/ΣR / S, avec la surface S en colonne constante d'entrée
  (déjà au registre inputs.yaml) ;
- **durées cumulées de dépassement** (jours/an, famille DC d'Oberlin,
  préfixe dt) si le besoin se confirme ;
- fiches personnelles de l'utilisateur (en local via copy_cards puis
  contribution).

### Complétion de symétrie restante (inventaire 2026-07-18)

Trous relevés lors de l'inventaire familles x déclinaisons, non créés
pour l'instant (décision : se limiter au lot climatologique
mean-QSA_season, mean-TMA_month, mean-RMA_month, ETPSA_season,
ETPMA_month et aux cases isolées median-centerLF, median-tVCX3,
median-tVCX10, faits le 2026-07-18). À reprendre si le besoin se
confirme :

- **delta saisonniers des caractéristiques d'étiage** (10 fiches) :
  delta-{dtLF, vLF, centerLF, startLF, endLF}\_{summer, winter}\_H,
  modèle direct delta-allLF_summer_H / delta-allLF_winter_H (les
  séries saisonnières correspondantes existent déjà) ;
- **compagnons de niveaux de retour** (4 fiches) : delta-VCN30-2_H et
  delta-QMNA-5_H (modèle delta-VCN10-5_H), n-VCN30-2_H et n-QMNA-5_H
  (modèle n-VCN10-5_H) ;
- **maxima saisonniers de précipitations** : RCXSA1_season,
  RCXSA5_season (modèle RSA_season + RCXA1/RCXA5) ;
- **coefficient d'écoulement mensuel** : CRM_month (modèle CRS_season) ;
- **miroirs basses eaux des fréquences fQ** : fQ90A, fQ95A, fQ99A
  (temps passé sous le quantile) + deltas ; opérateur inversé par
  rapport à fQ01A, pas une pure déclinaison ;
- absences uniformes assumées, à rediscuter seulement si un usage les
  demande : aucun median- saisonnier, aucune variante saisonnière côté
  hautes eaux (VCX*_summer...), ratios annuels uniquement, famille
  alpha- limitée au trio MAKAHO (QA, QJXA, VCN10).

## Palettes : questions ouvertes (2026-07-18)

État : les fiches à grandeur non ambiguë sont toutes équipées (héritage
de la fiche mère ; voir RENAMING.md 2026-07-18 pour l'orientation ETP).
Quatre palettes sémantiques en usage : marron vers vert (quantités
d'eau), bleu vers rouge (température), violet vers orange (dates et
durées de crue), vert vers marron (durées et volumes d'étiage, ETP :
assèchement).

- **Scores de performance et indices sans unité** (KGE, NSE et
  variantes, Bias, STD_ratio, epsilon_R/T, RAT_*, QR_ratio, RA_ratio,
  BFI-LH/Wal et leurs deltas, BFM, a-FDC) : laissés sans palette
  volontairement. Si on les équipe un jour, il faudra une palette
  divergente centrée sur la valeur de référence (1 pour KGE/NSE, 0 pour
  les deltas de BFI), décision non prise.
- **dtFlood** : partage la palette violet vers orange avec les dates, et
  non la palette d'assèchement de dtLF/dtBF. Examiné le 2026-07-18 et
  conservé : une durée de crue représente un risque (dégâts), pas un
  assèchement, et une crue plus longue n'est pas « plus d'eau » ; la
  dynamique diffère de celle des étiages. Si on veut un jour distinguer
  le risque de crue des dates par une palette dédiée, c'est une
  décision à part.
