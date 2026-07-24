# Journal des modifications

Évolutions notables de `card` : les fiches du recueil comme la
bibliothèque. Format inspiré de [Keep a
Changelog](https://keepachangelog.com/fr/1.1.0/).

**Numérotation.** SemVer avec la convention du 0.x : tant que le premier
chiffre vaut 0, un changement incompatible incrémente le deuxième, le
reste incrémente le troisième. Les numéros servent à la publication ; au
quotidien, c'est le commit qui identifie un état (cf. ci-dessous).

Ne pas confondre avec la version d'une **fiche** (champ `version:` de son
YAML) : la fiche versionne une définition, le paquet versionne le code et
le corpus. Une fiche passe au majeur quand ses **sorties** changent, au
mineur pour sa méthode ou sa description, au patch pour le reste ; sa
version voyage dans les métadonnées de sortie, si bien qu'un résultat dit
avec quelle définition il a été calculé.

Le paquet n'est pas encore publié sur PyPI (installation depuis GitHub,
nom en attente d'une demande PEP 541). Le moteur `stase` tient son propre
journal.

Chaque entrée dit ce qui a changé et renvoie au document qui l'explique.
Rien n'est recopié ici : une information recopiée finit par mentir à un
des deux endroits.

## Versions, en quatre phrases

1. **Au quotidien, on ne touche à aucun numéro.** La production suit
   `main` : une correction de fiche part en ligne au prochain
   `make update`, sans négociation.
2. **Ce qui trace, c'est le commit, et c'est automatique.** Chaque
   réponse du service dit le commit exact de card et de stase qui l'a
   produite, son identifiant pérenne Software Heritage
   (`swh:1:rev:<commit>`, qui résout puisque les trois dépôts y sont
   archivés depuis le 2026-07-22), et chaque variable porte la version de
   sa fiche. Rien à faire, rien à oublier.
3. **Publier une version reste rare, et tient en une commande.**
   `python scripts/set_version.py 0.3.0` accorde `pyproject.toml`,
   `CITATION.cff` et `codemeta.json`, les trois seuls endroits où le
   numéro est écrit. Ne jamais les éditer à la main :
   `tests/test_citation.py` refuse le désaccord.
4. **Le seul geste manuel régulier, c'est ce fichier.** Un changement
   qui mérite d'être retenu s'écrit sous `## Non publié`.

## Non publié

### Modifié

- **Le corpus est rangé par régime observé.** L'arborescence passe de
  `cards/<domaine>/<forme>/` à
  `cards/<domaine>/<phénomène>/<forme>/` : les 226 fiches sont
  déplacées sous leur phénomène (ou `purpose` à défaut). Fini le dossier
  `flow/scalar/` de 112 fiches : 22 dossiers feuilles de 1 à 85, qu'on
  parcourt par type d'étude (`flow/low-flows/`, `precipitation/heavy-rain/`…).
  Le linter contrôle désormais `chemin == (domaine, phénomène|purpose,
  forme)`. Le **catalogue** suit : rangé domaine → phénomène, avec un
  sommaire cliquable et une colonne *forme*. Aucun calcul touché, que des
  déplacements et des métadonnées. Prérequis livré juste avant : toute
  fiche a un phénomène (voir plus bas). Détail : `docs/dev/TOPICS.md`.

- **Le régime médian se sigle `D`, plus le préfixe `median-`.**
  `median-QJ` et `median-QJC5` deviennent **`QJD`** et **`QJDC10`**. Le
  préfixe `median-`/`mean-` désigne une réduction d'une série à un
  scalaire (`median-tVCN10` = médiane de la série `tVCN10`) ; l'appliquer
  à un régime, qui produit une courbe et dont la médiane est
  *intrinsèque* au calcul, était incohérent avec les 24 autres fiches
  préfixées. La médiane rejoint donc `N` (min) et `X` (max) comme
  **statistique d'ordre en position 3** : `N`/`D`/`X` = min/médiane/max,
  la moyenne restant implicite, `Pq` pour les autres percentiles. Le
  sigle `D` est libre car CARD ne réserve pas les durées cumulées
  d'Oberlin (`DC`) : les débits caractéristiques passent par la courbe
  `FDC`. `QJD` : calcul inchangé, seuls id et nom de colonne changent.
  `QJDC10` : au passage sa fenêtre de lissage passe de 5 à 10 jours,
  harmonisée sur `QJC10` (les valeurs changent, cf. RENAMING.md). Parité
  R sur le nom, plus la fenêtre pour `QJDC10`. Conception : NOMENCLATURE
  §3–§4–§6, trace RENAMING.md et ORIGINE_R.md.

### Ajouté

- **La clé du vocabulaire devient un slug neutre.** Dans `topics.yaml`,
  un concept s'identifiait par son libellé **anglais**, le français
  n'étant qu'une propriété : l'anglais faisait office d'identité, et le
  nom des dossiers se *dérivait* de sa formulation (reformuler un libellé
  aurait déplacé des fiches). La clé est désormais un slug déclaré
  (`low-flows: {en: low flows, fr: basses eaux}`) : il identifie le
  concept, nomme le dossier, et fournira l'URI d'un futur export SKOS où
  `en` et `fr` sont deux étiquettes **à égalité**. Le linter retrouve un
  concept par son étiquette, dans n'importe quelle langue.
  `card.vocabulary()` rend `{facette: {slug: {en, fr, ...}}}`. Aucun
  dossier déplacé (les slugs déclarés valent les noms existants), aucune
  fiche modifiée. Détail : `docs/dev/TOPICS.md`.

- **`card.figure`, `card.vocabulary` et `card.info(quiet=True)`**, pour
  servir card ailleurs qu'un terminal. `info` imprimait la figure et
  retournait le dict : parfait pour un humain, inutilisable pour un
  programme, qui veut soit la figure en **chaîne**, soit le dict **sans
  rien imprimer** (un service web n'a pas de terminal et voyait la figure
  partir dans ses logs à chaque requête, calculée pour rien).
  `card.figure(nom)` rend la chaîne sans imprimer, `card.info(quiet=True)`
  rend le seul dict, et `card.info(nom)` ne change pas d'un iota.
  `card.vocabulary()` expose la liste fermée des valeurs de facette
  (fr/en), c'est-à-dire les filtres valides de `list_cards` : un client
  peut les proposer au lieu de les deviner. Demandé par la revue FAIR de
  card-api, qui sert désormais la figure et le vocabulaire.

- **Toute variate a désormais un phénomène** (23 fiches complétées).
  Les cumuls de pluie (`RA`, `RMA`, `RSA`…), les températures moyennes
  (`TA`, `TMA`, `TSA`) et l'évapotranspiration (`ETPA`…) semblaient
  « sans régime » ; en réalité leur magnitude moyenne est un phénomène à
  part entière, pendant de « moyennes eaux » côté débit. Trois phénomènes
  ajoutés à `topics.yaml` : `mean precipitation` / précipitations
  moyennes, `mean temperatures` / températures moyennes,
  `evaporative demand` / demande évaporative. Les fractions liquide/solide
  (`RA_ratio`, `RAl_ratio`) rejoignent `neige` ; `CR`/`CRS_season` (rapport
  simulé/observé des précipitations) deviennent `purpose: model
  performance`, comme `Bias`. Renverse une décision antérieure de
  `TOPICS.md` (« mean ne devient pas un phénomène »), pour permettre de
  ranger le corpus par régime observé. Métadonnée seule, valeurs
  inchangées, patch de version sur les 23. Détail : `docs/dev/TOPICS.md`.

- **`QJ`, le régime journalier moyen brut, complète la famille.** Il
  existait comme intermédiaire de `QJC10` mais pas comme fiche : le
  régime moyen non lissé n'était pas extractible seul, alors que sa
  variante médiane (`QJD`) l'était. La famille est désormais complète et
  symétrique : `QJ`/`QJD` non lissés (moyen/médian), `QJC10`/`QJDC10`
  lissés sur 10 jours. `QJ` reçoit la période facultative comme `QJD`. La
  moyenne reste implicite (aucun préfixe, NOMENCLATURE §4).

- **La période facultative gagne `QJC10` et le régime médian.** `QJC10`
  (régime moyen lissé) et `QJDC10` (régime médian lissé) reçoivent
  `period_start`/`period_end` en entrées facultatives, comme `QJD` et
  `QM` : leur P1 passe par `over_period`. Sans période, le résultat est
  inchangé (vérifié à 3·10⁻¹⁵ près sur `QJC10`, fiche protégée). Les deux
  fiches lissées ne diffèrent plus que par moyenne/médiane, mêmes fenêtre
  (10 j) et seuils de lacunes.

- **`card.info` dessine la fiche au lieu d'en lister les champs.** Une
  fiche contient tout ce qu'il faut pour comprendre son calcul, mais
  aplati en liste cela se lit mal. La figure montre la chaîne des étapes,
  les fonctions et leurs réglages, la fenêtre d'échantillonnage sur douze
  mois, et ce qui est produit. Le dict retourné ne change pas : c'est lui
  que consomme le code appelant.

  Trois principes. La figure suit la **forme de sortie**, déjà une
  facette de la classification : une série montre son axe de temps, un
  changement la frise des deux fenêtres qu'il compare, une courbe l'axe
  qui l'indexe. Un kwarg qui nomme une colonne est une **référence**, pas
  un réglage, et s'affiche comme telle. Une **enveloppe se déplie** :
  `over_period` cacherait que la fiche calcule une médiane.

  Généré depuis le YAML, jamais écrit à la main ; un test vérifie que les
  225 fiches du corpus se rendent sans exception.

- **La figure parle les deux langues.** La prose de la figure (pas de
  temps, fenêtre, lacunes, forme de sortie) était française en dur :
  `info(lang="en")` échouait en silence et retombait sur l'ancienne liste
  de champs. Elle passe par une table de traduction, et les 225 fiches se
  rendent désormais dans les deux langues, dates comprises (MM-DD en
  anglais, DD-MM en français, comme les métadonnées). Le défaut par
  défaut reste `lang="fr"` : aucun appelant n'est touché.

### Modifié

- **La figure nomme les variables par leur identifiant**, celui des
  colonnes produites, et non par leur nom traduit : une fiche annonçait
  « 2 sorties : CDC_p, CDC_Q » là où les données portent `FDC_p` et
  `FDC_Q`. Le nom traduit reste affiché entre parenthèses. La prose se
  traduit, les identifiants non.
- **Un symbole, un rôle** dans la figure : le point médian sépare des
  informations sur une même ligne (et signe les unités), une puce ouvre
  un item de liste. Le même caractère servait aux deux.
- **L'identifiant pérenne s'affiche en URL** cliquable vers l'archive
  Software Heritage, au lieu du `swh:1:cnt:` nu que personne ne savait où
  porter. Il ne résout qu'après le passage suivant de SWH sur le dépôt :
  une fiche modifiée depuis la dernière visite renvoie une 404 en
  attendant.
- **Une fonction à seuil se lit par sa condition.** `where='<='` et
  `lim=upLim` s'affichaient en réglages séparés, suivis d'une glose qui
  énumérait les valeurs possibles de `where` alors que la fiche en avait
  choisi une : `apply_threshold` se lit maintenant `VC10 <= upLim, plus
  long épisode, premier jour`. Une glose répétée à l'identique dans un
  même process ne s'affiche plus qu'une fois.
- **Chaque sortie dit de quelle fonction elle vient** dès qu'un process
  en produit plusieurs : `allLF` alignait cinq appels puis cinq noms, à
  charge du lecteur de les apparier.
- **La figure ne dit plus que ce que la fiche détermine.** Elle annonçait
  l'axe d'une courbe, deviné de la présence de « FDC » dans un nom de
  variable, et une granularité de lignes déduite du pas de temps. Mesure
  faite par extraction réelle, `time_step: none` rend une ligne pour
  `BFM`, 365 pour `QJC10` et 1000 pour `FDC` : cela dépend de ce que la
  fonction retourne, pas de la fiche. L'axe n'est plus annoncé du tout,
  la granularité l'est pour les six couples (pas de temps, compress)
  vérifiés un par un, et les colonnes démultipliées par `compress` sont
  nommées (`QMA_month` déclare `QMA` et produit `QMA_jan … QMA_dec`).
- `card.load_card` accepte un **nom de fiche** et pas seulement un chemin :
  `card.load_card("QA")` rend la fiche telle qu'écrite, les deux langues
  et tous les processus, là où `card.info` en dessine une lecture et
  retourne un dict aplati d'une seule langue.

### Retiré

- Le mode `compact` du rendu, qui masquait les descriptions de fonctions.
  Seule la fonction interne l'exposait, `card.info` ne le passait jamais :
  personne ne pouvait s'en servir.

### Corrigé

- **`QM` était classée `series`, c'est un régime donc une `curve`.** Le
  débit moyen mensuel collapse les années par mois civil : 12 valeurs
  indexées par mois, une courbe, comme le régime journalier `QJC10`. Elle
  passe en `courbe` et rejoint `flow/curve/` (version 1.2, valeur
  inchangée, seule l'étiquette de forme change).
- **`Bias_season` était classée `series`, elle produit des scalaires.**
  Elle rend 4 biais saisonniers (`Bias_DJF..SON`), un par saison, une
  valeur par série : un critère de performance, pas un régime ni une
  série temporelle. Elle passe en `scalaire` et rejoint `flow/scalar/`
  (version 1.1, valeur inchangée).
- **`BFM` était classée `output: curve`, elle produit un scalaire.** Sa
  fonction rend `(max - min) / max` des débits de base agrégés, soit une
  seule valeur par série ; l'extraction donne une ligne et une colonne.
  La classification passe à `scalaire`, la fiche quitte `flow/curve/`
  pour `flow/scalar/` (le linter impose chemin == classification), et la
  version passe à 1.1. La valeur calculée ne change pas, seule
  l'étiquette de forme qui voyage dans les métadonnées de sortie. Repéré
  en mesurant la sortie réelle pendant la reprise de `card.info`.
- **Le régime médian lissé (désormais `QJDC10`) était deux fiches en
  une.** Il sortait le régime médian brut **et** sa version lissée, alors
  que le régime brut a déjà sa fiche autonome (`QJD`). Il passe de
  `keep: all` à `keep: [QJDC10]`, comme `QJC10` le fait déjà, et ne
  produit plus que sa colonne (une sortie retirée). Parité R volontairement
  rompue (le golden R garde les deux colonnes). Détail :
  `docs/dev/RENAMING.md` et `docs/dev/ORIGINE_R.md`.

### Corrigé

- **La figure annonçait l'unité et la description de la première sortie
  comme celles de la fiche entière.** `allLF` se disait « jour de l'année »
  alors qu'elle produit aussi une durée et un volume ; `QSA_season`
  affichait « Mois de décembre, janvier et février », qui ne décrit que
  DJF. L'unité monte en facette si elle vaut pour toutes les sorties et
  descend par sortie sinon ; la description ne s'affiche que si elle est
  commune.
- La figure datait ses fenêtres en MM-DD y compris en français, où les
  métadonnées écrivent DD-MM depuis toujours.
- Un titre long était tronqué (`[...]`) au lieu d'être replié sur une
  seconde ligne, ce qui perdait la moitié du nom des fiches `delta-`.
- Une valeur réduite puis diffusée sur toute la série (un seuil comme
  `upLim`) s'annonçait « transforme la série sans l'agréger, une valeur
  par jour », ce qui donnait à croire qu'elle variait chaque jour.

### Modifié

- **Douze fiches à horizon fixe disparaissent, sans en créer aucune.**
  La période devient une entrée **facultative** de `QM`, `FDC` et
  `QJD` (alors nommée `median-QJ`), qui existaient déjà : sans bornes elles calculent sur
  toute la chronique comme avant, avec bornes elles restreignent. Le
  vocabulaire parle de période et non d'horizon, ces fiches servant aussi
  bien une fenêtre observée qu'une projection. Vérifié des deux côtés :
  identique aux fiches de base sans période, identique aux douze fiches à
  horizon figé avec période.
- Étape intermédiaire de la même journée, remplacée par la fusion : `QM_H0..H3`,
  `FDC_H0..H3` et `median-QJ_H0..H3` figeaient leur période dans le
  fichier. Elles sont remplacées par `QM_H`, `FDC_H` et `median-QJ_H`,
  qui reçoivent `horizon_start` et `horizon_end` en colonnes d'entrée et
  se déclinent par suffixe, comme les fiches delta depuis le 2026-07-21.
  L'appelant choisit ses horizons, autant qu'il veut, et plus aucune date
  ne vit dans le corpus. À période égale, le résultat est identique à
  l'ancien, vérifié valeur par valeur sur les trois familles et sur les
  quatre horizons, soit 16 sorties sur 16. Détail : `docs/dev/RENAMING.md`.
- Le vocabulaire de ces trois fiches parle de **période**, non
  d'horizon : elles calculent un régime mensuel ou une courbe des débits
  classés sur n'importe quelle fenêtre, observée comprise, et « horizon »
  n'y désignait qu'un cas particulier. Leurs colonnes d'entrée deviennent
  `period_start` et `period_end`, et leur forme générique se lit « sur la
  période étudiée ». Les 59 fiches `delta-` gardent « horizon », qui y est
  exact puisqu'elles comparent une référence à une projection.
- Famille FDC : les deux coordonnées de la courbe deviennent deux
  variables déclarées, avec chacune son unité (sans unité pour les
  probabilités, m³/s pour les quantiles). Une seule ligne de métadonnées
  décrivait jusqu'ici les deux colonnes, ce qui empêchait de rattacher
  `FDC_Q_H1` à son horizon sous suffixe. Le `name` reste unique, la règle
  des coordonnées d'un même objet étant conservée.

### Ajouté

- `over_period(X, func, dates, period_start, period_end)` : restreint un
  calcul à une sous-période puis délègue. Nécessaire parce que `nanmean`
  et `nanmedian` sont des fonctions numpy, auxquelles on ne peut pas
  ajouter de paramètres. Une borne absente laisse son côté ouvert.
  `_const_date` et `_subset_period`, jusque-là dupliqués dans deux
  modules, y sont rassemblés.

### Corrigé

- `card.info()` affichait le placeholder brut (`{suffix.name}`) au lieu
  de la forme générique, là où le catalogue la résout depuis toujours.
  Défaut préexistant, visible sur les 62 fiches à placeholder.
- **Les cinq fiches FDC plantaient depuis l'origine du portage.**
  `fdc_probabilities` ne déclare aucune colonne d'entrée, or le moteur
  affecte d'office la première colonne numérique à une telle fonction :
  la valeur se liait au paramètre `n` et l'appel échouait. Trois des cinq
  masquaient le défaut par une période hors données, donc sans calcul.
  Aucun test ne les couvrait, et le corpus de validation les excluait
  puisqu'elles plantent aussi dans le paquet R.

- **14 fiches d'horizon annonçaient le mauvais horizon.** Le chantier du
  2026-07-21 les a rendues mono-sortie, l'horizon étant choisi par
  l'appelant, mais leur `name` était resté une **liste de trois**
  libellés, un par horizon. Seul le premier pouvant être publié, elles
  annonçaient « l'horizon proche » quelle que soit la période demandée :
  un résultat calculé sur 2071-2100 était étiqueté futur proche. Leur
  `method` utilisait déjà correctement le placeholder. Les libellés sont
  repliés en un seul, mot pour mot, avec `{suffix.name}` à la place du
  mot d'horizon. Aucune valeur calculée ne change, vérifié sur les 14.
  Concernées : delta-Q90A, Q95A, Q99A, QMNA, QNA, VCN10-5, VCN10, VCN30,
  VCN3, centerLF, dtLF, startLF, tVCN10, vLF.
- Le linter ne pouvait pas voir ce défaut : il ne vérifiait la longueur
  des métadonnées en liste que pour les fiches à sorties multiples. Une
  métadonnée en liste sur une variable unique est désormais refusée,
  puisque seul son premier élément serait publié.
- Les `method` de 53 variables portaient un retour à la ligne au milieu
  d'une phrase, artefact d'un repli de confort dans le YAML que le bloc
  littéral `|` conserve. Replié à la lecture, donc réglé aussi pour les
  fiches à venir.

### Modifié

- `card.extract(metadata_only=True, suffix=[...])` ignorait le suffixe en
  silence. Il le signale désormais : sans données, le nombre de sorties
  suffixées ne peut pas être connu, la règle de fan-out de stase étant
  conditionnelle.

- `copy_cards` ne numérote plus les fichiers par défaut. Le linter exige
  que l'identifiant d'une fiche soit aussi son nom de fichier : une copie
  nommée `001_VCN10.yaml` échouait donc au premier contrôle, et le
  parcours « copier un modèle puis valider » se contredisait de bout en
  bout. `numbered=True` reste disponible pour ordonner un dossier de
  travail.

### Corrigé

- CI en échec depuis le 2026-07-21 : un import `pytest` devenu orphelin
  dans `tests/test_loader.py` faisait échouer `ruff`, donc le job de
  lint, donc un mail d'échec à chaque push. La routine de vérification
  ignorait `ruff`, elle est corrigée dans CLAUDE.md.

### Ajouté

- **Chaque fiche porte son identifiant pérenne**, colonne `swhid` des
  métadonnées. Le SWHID de contenu d'un fichier est son hash de blob
  git : il se calcule donc localement, sans réseau ni dépôt, et désigne
  la **définition** exacte employée, indépendamment du dépôt et de la
  révision d'où elle vient. Un résultat archivé permet ainsi de
  retrouver la fiche telle qu'elle était, en ouvrant
  `https://archive.softwareheritage.org/swh:1:cnt:...`. Vérifié de bout
  en bout : la fiche est bien récupérable depuis l'archive.

### Modifié

- `script_path` publie le chemin dans le corpus (`flow/series/QA.yaml`)
  et non plus le chemin absolu sur la machine, qui n'apprenait rien à
  personne et exposait l'arborescence du serveur.

## 0.2.0 (2026-07-22)

### Ajouté

- La **version d'une fiche** atteint enfin les métadonnées de sortie,
  comme une colonne `version`. Un résultat dit désormais avec quelle
  définition il a été calculé, ce qui est la condition pour qu'un export
  soit reproductible et citable. Le champ existait dans les 237 fiches et
  la règle d'incrémentation était tenue depuis des semaines, mais
  `load_card` ne lisait pas le champ : il n'atteignait ni les
  métadonnées, ni le service web, ni personne.
- Le linter contrôle ce champ, ce qu'il ne faisait pas du tout : présence,
  format `majeur.mineur[.patch]`, et chaîne citée. Sans guillemets, YAML
  lit `1.10` comme le nombre `1.1`, et deux versions distinctes se
  confondent silencieusement.

### Modifié

- Dépendance montée à `stase>=0.5.0`, la version qui apporte le rôle
  `param_cols` dont les fiches `_H` dépendent depuis le 2026-07-21. La
  contrainte précédente était satisfaite par une version qui n'avait pas
  la fonctionnalité.
- Documentation de développement restructurée : un rôle par fichier, un
  bandeau de statut en tête, les documents d'époque rangés dans
  `docs/dev/archive/` au lieu d'être supprimés. Ce qui est daté vit ici,
  ce qui fait autorité vit dans une normative, ce qui est mort vit dans
  l'archive.
- `docs/dev/VALIDATION_R.md` renommé `docs/dev/ORIGINE_R.md` : rôle
  identique au fichier de ce nom dans stase (origine R, validation
  croisée, divergences assumées).

### Corrigé

- Affirmations démenties par le code : les clés `dataEX`/`metaEX` étaient
  présentées comme des alias vivants alors qu'elles sont purgées depuis
  le 2026-07-16, et le caractère relatif comme passant par le paramètre
  `meta=` de stase, retiré en stase 0.4.0.
- Décompte des fiches recopié dans trois documents et faux dans les
  trois. `scripts/generate_catalog.py` resynchronise désormais celui de
  `docs/index.md`, la dérive ne peut plus revenir.
- `n-VCN10-5_H` portait la version « 1.1.0 » quand les 236 autres fiches
  écrivent « 1.1 ». Sans contrôle du format, personne ne pouvait le voir.

## 2026-07-21

### Ajouté

- Les 59 fiches `_H` reçoivent leurs bornes d'horizon comme colonnes
  d'entrée fournies par l'appelant, au lieu d'un `$H` écrit en dur dans
  la fiche. `delta` prend quatre bornes (`ref_start`, `ref_end`,
  `horizon_start`, `horizon_end`) ; `return_level` et `apply_threshold`
  gagnent `period_start` et `period_end`. Sorties inchangées, vérifié à
  l'exact sur les 59 fiches. Débloque les horizons par degré de
  réchauffement, dont les bornes varient d'une série à l'autre.
- Goldens Python pour les 12 fiches qui divergent volontairement de R.
  Elles sortent de la comparaison à R, qui ne pouvait que produire un
  écart permanent, et sont jugées contre leur propre sortie de référence.
  Le corpus distingue maintenant une divergence attendue d'une
  régression.

### Corrigé

- Cause des 4 divergences VCN restées longtemps non rattachées :
  convention de moyenne mobile à **fenêtre paire**. `rollmean_center`
  suit pandas (`center=True`), R (RcppRoll) centre une position à côté.
  Le décalage d'un jour ne change pas le minimum annuel mais bascule
  celui d'une fenêtre saisonnière quand il tombe au bord.

Détail : `docs/dev/RENAMING.md` (2026-07-21), `docs/dev/ORIGINE_R.md`,
`tests/data/known_divergences.yaml`.

## 2026-07-20

### Ajouté

- Suffixes de scénario : `card.extract(..., suffix=["DOE", "DCR"])`
  applique une même fiche à plusieurs variantes d'une entrée en un seul
  appel, sur des colonnes `Q_lim_DOE`/`Q_lim_DCR`, ou `obs`/`sim` sur
  n'importe quelle fiche. Le fan-out des valeurs est fait par stase au
  niveau colonne ; card n'ajoute que les métadonnées, si bien qu'aucun
  placeholder ne peut changer un calcul. Une variable suffixée est une
  autre variable, donc une autre ligne de `meta`, plus une colonne
  `suffix`.
- `card.trend` suit les suffixes tout seul, en lisant cette colonne.
- Fiches `rp-` (période de retour d'un seuil réglementaire), qui sont le
  cas d'usage d'origine du mécanisme.

### Modifié

- La dépendance à stase, jusque-là sans contrainte, est épinglée à
  `>= 0.4.0` : c'est la version qui rend le moteur agnostique de card
  (retrait de son paramètre `meta=`) et lève l'ambiguïté d'unité de ses
  colonnes de tendance.
- Empaquetage : `inputs.yaml` et `topics.yaml` embarqués dans la
  distribution, ils manquaient à l'installation.

Détail : docstring de `src/card/suffix.py`, `docs/dev/RENAMING.md`
(deux entrées du 2026-07-20).

## 2026-07-18

### Ajouté

- 8 fiches comblant les trous relevés à l'inventaire familles x
  déclinaisons (lot climatologique saisonnier et mensuel, cases isolées
  `median-`).

### Corrigé

- Sommes de l'évapotranspiration rendues strictes : une année entièrement
  lacunaire est une lacune, pas un cumul nul.
- Sorties `mean-RSA_*` et orientation de plusieurs palettes.
- `return_period` : le paramètre était un seuil et non une période de
  retour, avec une correction sur `p0`. Fiches `rp-` renommées en
  conséquence.

Détail : `docs/dev/RENAMING.md` (2026-07-18).

## 2026-07-17

### Ajouté

- Le linter refuse les noms d'agrégation ambigus face aux valeurs
  manquantes : `sum` ou `mean` nus, qui ne disent pas ce qu'ils font
  d'une lacune, alors que le corpus dépend de cette réponse.

## 2026-07-16

### Ajouté

- Classification à facettes dans chaque fiche : bloc `classification`
  bilingue (`domain`, `phenomenon`, `aspect` aligné sur la typologie IHA,
  `season`, `output`, `purpose`), adossé au vocabulaire de contrôle
  `topics.yaml`, avec appariement français/anglais vérifié par le linter.
  L'arborescence `cards/<domain>/<output>/` doit refléter la
  classification, le linter l'impose. `list_cards` filtre par facette
  dans les deux langues.
- `inputs.yaml` : unités et définitions des variables d'entrée,
  invariants centralisés hors des fiches.
- `card.trend` : analyse de tendance consciente des fiches. Refuse
  explicitement les fiches qui ne sont pas `output: series`, traduit
  leurs métadonnées en `relative={variable: bool}` pour le moteur, et
  prend AR1 par défaut, les étiages étant autocorrélés.
- `card.extract(sampling_period="preferred"|"MM-DD")` : impose une
  fenêtre annuelle commune, pour comparer des stations entre elles. Les
  fenêtres partielles font partie de la définition d'une variable et ne
  sont jamais écrasées. La convention adaptative par phénomène (étiages
  `nanmax` et 01-01, crues `nanmin` et 09-01) devient un invariant
  vérifié par le linter.

### Retiré

- Les clés héritées `dataEX` et `metaEX` : `card.extract` renvoie
  `{"data", "meta"}`, et rien d'autre. La sortie d'une extraction est de
  la donnée comme une autre.
- Le champ `topic`, remplacé par la classification à facettes.

Détail : `docs/dev/TOPICS.md`.

## 2026-07-15

### Modifié

- Audit des métadonnées appliqué en quatre lots : `name`, `description`,
  `method` et `unit` alignés sur le bloc `process` réellement exécuté.
  Règle érigée à cette occasion : la fonction fait foi, une métadonnée ne
  ment jamais sur ce que calcule la fiche.
- Renommages de sorties, parité R rompue volontairement et fiches
  concernées passées en v2.0 : `STD` en `STD_ratio` (c'est le alpha du
  KGE, pas un écart-type), `Rc` en `QR_ratio` (le coefficient n'était pas
  adimensionnel), `median-finLF` en `median-endLF`.
- 48 champs `method` vides remplis, fiche `QJC10` réparée.

### Ajouté

- Guide de nommage écrit et arbitré (`docs/dev/NOMENCLATURE.md`) : le
  système du corpus consolidé par Oberlin, la grammaire des identifiants
  et sept règles de rédaction des métadonnées.
- 11 fiches comblant des manques évidents du catalogue (déclinaisons
  saisonnières des basses eaux, critère BFI-LH).

Détail : `docs/dev/archive/AUDIT_FICHES.md`, `docs/dev/NOMENCLATURE.md`,
`docs/dev/RENAMING.md`.

## 2026-07-12

Première version du paquet, port Python du paquet R
[CARD](https://github.com/lou-heraut/CARD).

### Ajouté

- 215 fiches YAML, les fonctions hydrologiques portées de R, le chargeur
  de fiches et l'extraction, cette dernière déléguée au moteur
  [stase](https://github.com/lou-heraut/stase).
- API pythonique : `card.extract`, `card.list_cards`, `card.info`,
  `card.copy_cards`. Les noms du R restent valides en alias.
- Linter sans dépendance (`python -m card.schema`), suite pytest adossée
  à des goldens figés depuis la validation R, catalogue généré
  (`docs/CARDS.md`) et page GitHub Pages.

### Modifié

- Résolution des fonctions par espace de noms (`card.functions` puis
  numpy) : les fiches appellent directement `nanmean`, `nanargmax`, le
  registre-table de R disparaît, comme le kwarg `{skipna: true}`.
- Renommage des fonctions hydro et des clés de fiche, table validée
  fonction par fonction (`get_deltaX` en `delta`, `get_Xn` en
  `return_level`, `to_normalise` en `relative`).
- Licence GPL-3 pour tout le dépôt, en-têtes de copyright repris des
  fichiers R d'origine.

Validation croisée : 552 comparaisons identiques à R sur le corpus
complet, tolérance 1e-6.

Détail : `docs/dev/archive/ROADMAP.md`, `docs/dev/RENAMING.md`,
`docs/dev/ORIGINE_R.md`.
