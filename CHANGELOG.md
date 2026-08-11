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

## Versions, en cinq phrases

1. **Au quotidien, on ne touche à aucun numéro.** La production suit
   `main` : une correction de fiche part en ligne au prochain
   `make update`, sans négociation.
2. **Ce qui trace, c'est le commit, et c'est automatique.** Chaque
   réponse du service dit le commit exact de card et de stase qui l'a
   produite, son identifiant pérenne Software Heritage
   (`swh:1:rev:<commit>`, qui résout puisque les trois dépôts y sont
   archivés depuis le 2026-07-22), et chaque variable porte la version de
   sa fiche. Rien à faire, rien à oublier.
3. **Publier une version tient en une commande.**
   `python scripts/set_version.py 0.3.0` accorde tous les fichiers où le
   numéro est écrit (son docstring en tient la liste). Ne jamais les
   éditer à la main : `tests/test_citation.py` refuse le désaccord.
4. **Le seul geste manuel régulier, c'est ce fichier.** Un changement
   qui mérite d'être retenu s'écrit sous `## Non publié`.
5. **Quand couper ? Sur du contenu, jamais sur un calendrier.** Trois cas
   suffisent, et ils se tranchent sans rien mesurer :
   - une entrée qui change les **sorties** du corpus (les valeurs d'une
     fiche, le nom d'une colonne, une signature publique) se publie le
     jour où elle est livrée : sans numéro, personne ne peut désigner la
     rupture ni s'y arrêter ;
   - sinon, on coupe **à la fin d'un chantier**, au moment précis où l'on
     écrit l'entrée qui le clôt, si « Non publié » porte au moins une
     chose qu'un lecteur extérieur remarquerait ;
   - jamais au milieu d'un chantier, et jamais parce que du temps a
     passé.

   `python scripts/set_version.py --etat` dit où on en est sans avoir à y
   penser : dernier tag, commits depuis, entrées non publiées. Ce que
   coûte l'oubli est mesuré : le 2026-08-05, le paquet était encore en
   0.2.0 avec quatre-vingt-treize commits derrière lui, si bien que
   `CITATION.cff` faisait citer un logiciel qui n'était plus celui qui
   tournait, et que « Non publié » pesait près de quatre fois toutes les
   versions publiées réunies.

## Non publié

Rien depuis la 0.5.2.

## 0.5.2 (2026-08-11)

### Modifié

- **Les fonctions hydro se documentent comme le reste, et un module
  disparaît (2026-08-11).** Leurs docstrings s'écrivaient en deux blocs
  `en:` et `fr:`, convention propre à card, lue par un module dédié,
  `card/docstring.py`. Mesuré ce jour : **ce module n'était appelé par
  aucun code de production**, seulement par des tests. La figure a cessé
  de lire les docstrings de fonctions quand `method` a pris le relais,
  et rien d'autre ne les consommait, ni dans card, ni dans card-api.

  Les blocs français avaient donc un lecteur humain et aucun lecteur
  machine. Or ce qu'un hydrologue francophone doit savoir d'une
  **variable** vit dans la fiche (`meta.fr`), qui reste bilingue et
  publiée dans le catalogue ; une docstring décrit une **fonction**, et
  son destinataire est celui qui code.

  Les 42 fonctions publiques de `functions/` passent donc à l'anglais
  avec sections NumPy, la règle posée la veille pour l'API. `docstring.py`
  est **supprimé**, et les trois tests qui tenaient la convention
  bilingue deviennent un seul, qui applique aux fonctions du corpus la
  règle de `tests/test_docstrings.py`. Une convention, un module et deux
  tests en moins, pour une norme unique dans les deux paquets.

  Aucun comportement ne bouge, aucune fiche n'est touchée.

## 0.5.1 (2026-08-11)

### Modifié

- **L'API publique se documente en anglais, en sections NumPy
  (2026-08-11).** `help(card.extract)` répondait en français, en prose
  libre, alors que le README, le catalogue, le site et la publication
  scientifique sont en anglais. Le lecteur changeait donc de langue au
  moment précis où il passait de la promesse à l'usage. Les treize noms
  de `__all__` sont convertis, soit 1 132 mots sur neuf docstrings
  uniques : `extract`, `trend`, `list_cards`, `info`, `figure`,
  `copy_cards`, `load_card`, `vocabulary`, `provenance`, et les quatre
  alias hérités du R. Aucun comportement ne bouge.

  **Les sections ne sont pas une coquetterie de forme.** Un paragraphe
  libre oblige le lecteur à chercher le sens de `sampling_period` dans
  une phrase, et aucun générateur de documentation ne sait le rendre en
  tableau. stase écrivait déjà ainsi une partie de son API : c'est
  désormais la règle des deux côtés.

  **Deux familles de docstrings ne sont PAS touchées**, et c'est
  délibéré. Celles de `functions/` restent bilingues `en:`/`fr:` comme
  une fiche : elles décrivent une méthode hydrologique à des
  hydrologues, pas une API à des développeurs, et leur convention est
  déjà mesurée par `test_render.py`. Celles de la machinerie interne
  écrivent dans la langue qu'elles veulent : elles s'adressent à qui
  ouvre le fichier.

  `tests/test_docstrings.py` mesure les deux règles au lieu de compter
  sur la mémoire, et le CLAUDE.md les énonce. Même fichier et mêmes
  règles dans stase (0.6.3) : les deux paquets s'installent et se lisent
  ensemble, une norme qui s'arrêterait à la frontière de l'un ne
  servirait à rien.

## 0.5.0 (2026-08-11)

### Ajouté

- **Ce qu'on liste, on peut enfin le calculer.** `list_cards()` et
  `extract` rendent une colonne `card` : le nom de la FICHE qui produit
  la variable de la ligne, c'est-à-dire ce qu'`extract(cards=...)`
  attend. L'enchaînement le plus naturel du paquet, lister une famille
  puis la calculer, échouait :

  ```python
  temp = card.list_cards(domain="temperature")
  card.extract(data, cards=temp["variable_en"])   # FileNotFoundError
  card.extract(data, cards=temp["card"].unique()) # désormais
  ```

  `list_cards` rend une ligne par VARIABLE, ce qui est juste quand on
  cherche une variable, mais le fan-out par mois ou par saison sépare les
  deux noms : `mean-TMA_jan` est une variable de la fiche
  `mean-TMA_month`. Mesuré le 2026-08-11 : **343 des 472 variables
  listées, soit 73 %, ne portent pas le nom de leur fiche**. Le seul
  recours était de le reconstruire depuis `script_path`, donc de faire
  dépendre du code utilisateur d'une convention d'arborescence.

  **C'est une parité rétablie, pas une nouveauté** : le CSV du paquet R
  portait `CARD_name` en première colonne, où elle valait `variable_en`
  sur ses 565 lignes sans exception, une fiche R sortant une variable et
  une seule. Elle a été droppée au portage comme une redondance, et le
  fan-out l'a rendue nécessaire après coup. Détail et réserves de
  compatibilité : `RENAMING.md`.

  Trouvé en portant sur card4r la vignette écrite en 2025 pour le paquet
  R, qui fait exactement ce geste.

## 0.4.1 (2026-08-11)

### Modifié

- **Le README ne compte plus les fiches par facette (2026-08-11).** Les
  exemples de `list_cards()` annonçaient « 114 variables », « 267 »,
  « 83 » : trois nombres écrits à la main sur un corpus qui bouge, dans
  un dépôt dont la règle dit que le SEUL décompte est celui des marqueurs
  `<!-- cards:count -->`. Ils étaient encore exacts, ce qui est le
  propre du piège. Les commentaires disent maintenant ce que la facette
  SÉLECTIONNE, qui est ce que le lecteur a besoin de comprendre. Même
  correction dans le README de card4r, qui les avait recopiés.

- **Le README est réorganisé et tourne sur des données réelles
  (2026-08-06).** Quatorze sections à plat deviennent trois parties à
  deux niveaux : comment on s'en sert, ce qu'est une fiche, et le reste.
  « Cards that need a parameter » passe de cinq blocs de code à deux : sa
  place venait du chantier qui l'avait précédée, pas de son importance.
  « Finding your variable » remonte juste après le premier essai, avec la
  grammaire des noms, puisque c'est la question qu'on se pose une fois
  que ça marche.

  Les exemples tournent désormais sur **l'Yzeron à Craponne**, bassin
  périurbain suivi depuis 1970, chargé depuis Hub'Eau en sept lignes sans
  clé ni dépendance. Du gamma aléatoire prouvait que le code tourne ;
  -12,8 % sur le module entre 1970-1999 et 2000-2022, et des étiages en
  baisse de 1,1 % par an, montrent ce que la collection sert à voir.
  Toutes les sorties affichées sont celles que le code produit.

  La fiche `QA` est montrée en YAML, avec le partage `meta` écrit pour
  des humains et `process` qui s'exécute, juste avant « écrivez la
  vôtre ». `res["meta"]` est affichée au lieu d'être seulement annoncée.

- **Le plan R est déroulé, il rejoint les archives (2026-08-06).** Ses
  quatre chantiers sont sortis : le `Package:` de CARD-R réparé, `card4r`
  écrit et publié, les badges `superseded` posés, la référence R gelée.
  Seul l'archivage GitHub des paquets historiques est écarté, une
  conversation y étant ouverte. Ce qui restait de vivant est ré-hébergé
  avant le déplacement, comme la recette l'exige : deux pistes
  optionnelles sur la référence gelée passent dans `CHANTIERS.md`, le
  reste vit déjà dans `ORIGINE_R.md` et dans le dépôt `card4r`.

  La réclamation du nom PyPI a désormais son propre plan,
  `PLAN_PYPI.md` : le courriel au propriétaire et l'issue publique sont
  partis le 2026-08-06, la demande PEP 541 peut suivre à partir du
  2026-09-06. Les dates n'ont pas d'autre endroit où vivre.

- **La campagne de nettoyage est close (2026-07-21 au 2026-08-05).** Ses
  six phases sont cochées : carte des rôles et redondances corrigées,
  historiques archivés sous bandeau, CLAUDE.md élagués, README à exemples
  exécutés, métadonnées à placeholder relues, landing tranchée,
  conventions et renvois croisés appliqués aux quatre dépôts.
  `NETTOYAGE.md` redevient une procédure dormante, sans campagne ouverte,
  et le chantier sort de `CHANTIERS.md` comme son bandeau l'exige. Le
  signal qu'il en faudra une autre est écrit là-bas : un renvoi qui ne
  mène plus où il dit, un décompte écrit à la main, un document qui
  annonce un état que son dépôt contredit.

- **Le catalogue s'adresse enfin à un humain qui cherche une variable
  (2026-08-05).** Il affichait `m^{3}.s^{-1}` là où `card.info` écrit
  déjà `m³·s⁻¹` : même donnée, joliment rendue dans la figure et brute
  dans le catalogue. Il répétait le nom de la fiche dans une colonne
  « variable(s) » qui n'apprend quelque chose que pour les rares fiches
  multi-sorties. Et il ne disait nulle part que les identifiants sont un
  SYSTÈME, alors que c'est ce qui transforme 226 noms opaques en noms
  qu'on prédit.

  Désormais : unités lisibles (la fonction de la figure est réemployée,
  pas réécrite), sept colonnes au lieu de neuf avec les facettes
  regroupées, colonne « variables » remplie seulement quand elle
  distingue, et le décodage d'un nom en tête de fichier. Le catalogue est
  publié dans les **deux langues** du corpus, `CARDS.md` et
  `CARDS.fr.md`, qui se renvoient l'une à l'autre : n'en publier qu'une
  jetait la moitié de ce que les fiches portent. La garde de fraîcheur
  couvre les deux.

  `docs/index.md` devient une page d'aiguillage : ce que card calcule en
  trois lignes, les deux catalogues mis en avant, le décodage d'un nom,
  et trois portes selon qu'on vient de Python, de R ou du web. Rien du
  README n'y est recopié, ni installation ni exemples ni citation : deux
  vitrines divergent, un aiguillage ne peut pas mentir.

- **« au regard de » disait mal ce que la fiche calcule (2026-08-05).**
  Les trois fiches `rp-` annonçaient une période de retour « au regard
  des minimums annuels », tournure administrative qui reste vague : une
  période de retour se calcule DANS une distribution, et c'est ce que la
  phrase dit désormais, « dans la distribution des minimums annuels »,
  avec le même resserrement côté anglais (`with respect to` devient `in
  the distribution of`). Version mineure des trois fiches : le texte
  humain change, aucune valeur ne bouge.

  Le README dit maintenant où atterrit le nom d'une variante, qui diffère
  selon la famille : un groupe nominal avec son article pour les fiches à
  période (« over the observed period 1976-2005 »), un adjectif sans
  article pour les fiches à horizon (« the near future horizon »). Rien
  ne le disait, et la seule façon de l'apprendre était d'essayer.

- **Le corpus a un front R, et les docs de card le disent (2026-08-05).**
  `card4r` est un quatrième dépôt, paquet R mince qui **appelle** card
  par reticulate au lieu de le réimplémenter : un `data.frame` entre, des
  `data.frame` et leurs métadonnées sortent. Rien ne change dans card, ni
  dans le corpus, ni dans une sortie ; c'est pour cela que cette entrée
  ne coupe pas de version. Ce qui change ici : `PLAN_R.md` est repris
  avec ce qui a été mesuré en le construisant, la carte des rôles de
  `NETTOYAGE.md` couvre le quatrième dépôt pour que le cloisonnement ne
  se relâche pas, et le CLAUDE.md dit où vit le front R et lesquels des
  dépôts R restent sans fichiers IA.

### Corrigé

- **Le README annonçait un commit qui était faux dès le commit suivant
  (2026-08-11).** La section « What a result says about itself » montrait
  la table `meta` avec de vrais `card_commit` et `stase_commit`, relevés
  au moment où l'exemple a été joué. C'est le seul endroit de
  l'écosystème où un commit était écrit à la main, et c'était dans la
  section qui explique justement qu'un commit ne ment jamais, contrairement
  à un numéro de version. Il n'y avait pas de garde possible : la 0.4.0 a
  posé qu'une copie de travail modifiée ne publie AUCUN commit, si bien
  qu'un test comparant le README à la valeur réelle échouerait pendant
  tout le travail, et que la valeur juste est vide la moitié du temps.
  Les deux colonnes sont donc élidées comme le `swh:1:cnt:` qui les
  jouxte déjà, et comme le chemin de l'interpréteur l'est chez card4r :
  un `…` dit « valeur longue, coupée ici », ce qu'elle est. Ce que le
  lecteur devait apprendre, la prose sous le bloc le dit. Même correction
  dans le README de card4r, qui écrivait en plus les quarante caractères
  entiers.

  Ce qui reste écrit en dur, et pourquoi : les `swh:1:cnt:` identifient
  le FICHIER de fiche, ne bougent que si le YAML bouge, et celui de la
  figure `VCN10` est un lien qui résout pour de vrai.

- **`list_cards` affichait des gabarits, pas des phrases (2026-08-06).**
  La fonction de découverte du corpus rendait « between the
  {suffix.name} horizon » sur les 83 fiches `delta-`, c'est-à-dire une
  accolade brute à l'endroit exact où quelqu'un cherche une variable.
  `info()` résolvait déjà le placeholder avec le défaut de la fiche, le
  catalogue aussi, et un commentaire du code disait « jamais l'accolade,
  comme le catalogue » : `list_cards` avait simplement été oubliée en
  passant par un constructeur de métadonnées qui ne résout pas.
  L'invariant est désormais tenu sur les **quatre** surfaces qui
  s'adressent à un humain, vérifiées une à une : `extract(metadata_only)`,
  `list_cards()`, `figure()` et le dict de `info()`. `load_card()` garde
  l'accolade, et c'est voulu : il rend la fiche telle qu'elle est écrite.
  Trouvé en écrivant les exemples du README sur données réelles.

- **Le paquet n'emportait aucune description : sa page PyPI aurait été
  vide (2026-08-06).** `pyproject.toml` ne déclarait pas de champ
  `readme`, si bien que la roue construite ne portait que 678 caractères
  de métadonnées et un résumé d'une ligne. Or **la page pypi.org d'un
  paquet EST son README** : c'est la landing du monde Python, elle vient
  gratuitement avec la publication, et card l'aurait affichée aussi vide
  que celle du squat qu'on lui reproche. Trouvé en préparant la demande
  PEP 541, avant de publier quoi que ce soit.

  Les liens du README passent en absolu dans la foulée, PyPI ne résolvant
  aucun chemin relatif : sept liens seraient morts et l'image d'en-tête
  absente. Les catalogues et les normes pointent vers le site, qui les
  rend ; le CHANGELOG et la licence vers GitHub, leur seul endroit.
  Vérifié par `twine check` (les deux artefacts passent) et en
  interrogeant chaque URL.

## 0.4.0 (2026-08-05)

### Ajouté

- **Un résultat dit enfin avec quel LOGICIEL il a été calculé.** Trois
  niveaux de traçabilité étaient annoncés (la définition, le corpus, le
  moteur) mais un seul sortait de card employé seul : la fiche. Un
  résultat calculé dans un carnet avait donc une provenance logicielle
  vide, quand la même requête passée au service était parfaitement
  tracée. `meta` porte désormais `card_version`, `card_commit`,
  `stase_version` et `stase_commit`, mêmes noms que les champs de
  card-api, et `card.provenance()` les donne sans lancer de calcul. Les
  colonnes voyagent avec un export : un CSV posé dans un dossier dit
  seul avec quoi il a été produit. Détail des sorties : `RENAMING.md`.

  **Le commit, pas seulement le numéro.** Un numéro ne désigne un état
  unique que le jour où il est coupé, et dans une installation éditable
  il est figé au dernier `pip install -e` : mesuré ce jour, cet
  environnement annonçait 0.1.0 pour des dépôts en 0.3.1 et 0.6.1. Le
  commit, lui, désigne toujours un état et un seul, et `swh:1:rev:` +
  commit en est l'identifiant Software Heritage citable.

  **Rien à inventer, la norme le fournit** : une installation
  `pip install git+…@ref` enregistre son commit dans un `direct_url.json`
  (PEP 610), lisible à l'exécution. Les quatre modes d'installation ont
  été mesurés le 2026-08-05 : installation git (commit fourni), archive
  (non, d'où le passage par l'environnement que card-api renseigne),
  éditable (git répond), copie sans installation (git aussi). Un paquet
  peut lire la provenance d'un autre, si bien que `stase` n'a rien eu à
  implémenter : savoir comment on a été installé n'est pas le métier
  d'un moteur d'agrégation.

  **Une copie de travail modifiée ne publie pas de commit.** Le code qui
  tourne est alors le commit plus les modifications en cours : on
  n'annonce un commit que s'il est exactement vrai, et la colonne vide
  dit « ce résultat vient d'un code en cours d'édition, ne le cite pas ».
  Les fichiers non suivis par git ne comptent pas. Conception et ordre de
  résolution : docstring de `src/card/provenance.py`.

## 0.3.1 (2026-08-05)

### Corrigé

- **La contrainte `stase>=` mentait, pour la deuxième fois.** card
  déclarait `stase>=0.5.0` alors que son test de tendance lit `df["h"]`
  et que son README documente la colonne `h` : ce nom n'existe que
  depuis stase 0.6.0, publiée le jour même, le moteur rendant `H`
  auparavant. Installé avec un stase 0.5.0, card aurait donc produit `H`
  en documentant `h`. La contrainte passe à `stase>=0.6.0`. Même défaut
  qu'avec `param_cols` en juillet, et même remède : la règle de
  numérotation de stase le dit maintenant explicitement, une rupture du
  moteur se publie le jour où elle est livrée et card remonte sa
  contrainte dans la foulée.

## 0.3.0 (2026-08-05)

Première version coupée depuis le 2026-07-22. Elle contient la refonte
du champ `method`, les descriptions des fiches, les suffixes de scénario,
les paramètres externes en colonnes d'entrée, et six fiches dont les
valeurs ont changé : c'est une rupture, d'où le deuxième chiffre.

### Ajouté

- **Une règle dit enfin QUAND couper une version (2026-08-05).** Le
  paquet est resté en 0.2.0 pendant quatre-vingt-treize commits, non par
  négligence mais parce que rien ne déclenchait la question : `CITATION.cff`
  faisait donc citer un logiciel qui n'était plus celui qui tournait, et
  « Non publié » pesait près de quatre fois toutes les versions publiées
  réunies. La règle tient en trois cas (cinquième phrase de ce fichier) et
  s'accroche au seul geste qu'on fait toujours en terminant un chantier :
  écrire l'entrée qui le clôt. `scripts/set_version.py --etat` pose les
  faits sous les yeux à ce moment-là (dernier tag, commits depuis, entrées
  non publiées) sans rien décider, parce que le jugement reste humain.
  Les vingt-deux blocs `###` empilés sous « Non publié » sont par ailleurs
  regroupés en un par type, ce que le fichier annonçait déjà mais ne
  tenait plus.

- **La fraîcheur du catalogue est mesurée, plus consignée (2026-08-05).**
  `docs/CARDS.md` et le décompte du README entre les balises
  `<!-- cards:count -->` sortent tous deux de
  `scripts/generate_catalog.py`, mais rien ne vérifiait qu'ils étaient à
  jour : leur exactitude reposait sur une consigne écrite à deux endroits,
  donc sur la mémoire de qui touche une fiche, alors que tout le reste du
  dépôt est tenu par un test (`test_citation.py` pour les versions,
  `test_nature_fonctions.py` pour les fonctions). Le rendu du catalogue
  est désormais séparé de son écriture (`render()` ne touche à rien), ce
  qui permet à `tests/test_catalogue.py` de régénérer en mémoire et de
  confronter aux fichiers versionnés. Une fiche ajoutée sans régénération
  fait rougir la suite, en local comme en CI, et le message nomme la
  commande qui répare. Vérifié sur les trois cas qu'il doit attraper :
  catalogue périmé, décompte faux, balises disparues. Aucune étape de CI
  en plus, `pytest` y passait déjà.

- **Le linter confronte `method` au `process` (2026-08-03).** Sept
  règles : une phrase par colonne réellement produite, aucune phrase
  orpheline, les mêmes clés dans les deux langues, un nom cité présenté
  par la phrase qui le produit, et la moitié gauche confrontée à ce que
  le process calcule. Cette dernière est le seul contrôle croisé qui
  existe sur `method`, et il n'existe que parce que la phrase est ÉCRITE.
  Le pas de temps ne suffit pas à conclure : `RAl_ratio` P2 divise deux
  séries déjà annuelles et n'agrège rien, là où `dtFlood` P3 agrège
  vraiment parce que son entrée a été rediffusée sur la grille
  journalière par un `keep: all` amont. En lisant ce détail, les 504
  étapes du corpus s'accordent sans une exception. Le contrôle a servi
  aussitôt : `QM` annonçait « agrégation mensuelle par année » pour un
  `time_step: month`.

- **`tests/test_py_golden.py` : les fiches qui divergent volontairement du
  R sont enfin tenues par la CI (2026-07-31).** `tests/data/py_golden/`
  fige la sortie Python des fiches dont la parité R est rompue sciemment,
  seules fiches qu'aucun golden R ne peut juger. Ces fichiers n'étaient
  lus que par `tests/run_py_corpus.py`, un script que la CI ne lance pas :
  ils ne gardaient rien. Constaté en cherchant ce qui protégeait les
  fiches `fQ*` après le changement de dénominateur, réponse : rien. Les
  dix-huit fiches concernées sont maintenant vérifiées par `pytest`, dont
  les six `fQ*` dont le golden est posé à cette occasion, et un test
  refuse qu'un golden existe sans motif déclaré dans
  `known_divergences.yaml` ou l'inverse. Éprouvé en remettant l'ancien
  dénominateur : les six rougissent.

- **`tests/test_nature_fonctions.py` : la nature d'une fonction est
  désormais MESURÉE, plus déclarée sur parole (2026-07-30).** Sept tests
  appellent chaque fonction avec les arguments que le corpus lui passe
  vraiment, sur une chronique de synthèse, et comparent la longueur de la
  sortie à celle de l'entrée. Le test central ne demande pas à
  `decoupe()` d'où elle tient son verdict, il demande si son verdict est
  vrai : c'est le seul qui aurait rougi le jour du renommage. Aucune
  liste de noms à tenir à jour ; les sept fonctions qu'on ne peut pas
  appeler hors du moteur, leurs arguments désignant des colonnes, sont
  classées à la main dans `HORS_MESURE` avec leur raison, et un test
  refuse que cette liste garde une fonction devenue mesurable. Éprouvé
  par quatre mutations, chacune vue rouge sur le test attendu : le bug
  d'origine réintroduit, une déclaration oubliée, une déclaration fausse,
  et `decoupe()` ignorant la déclaration.

  Deux trouvailles du test lui-même. `ratio` et `difference` n'avaient pas
  de nature définissable, leur drapeau `first` en faisant deux fonctions :
  résolu par la scission, voir plus bas. `return_level` a été classée à la
  main après lecture, elle ajuste une loi et rend une valeur.

- **Les docstrings des fonctions hydro sont bilingues, et se lisent comme
  une fiche (2026-08-01).** Les gloses de la figure viennent des
  docstrings, écrites en français, et s'affichaient telles quelles dans
  la figure anglaise : c'était le dernier morceau de la figure à ne pas
  passer par la table `_T`. Une docstring porte désormais un bloc `en:`
  puis un bloc `fr:`, à égalité et dans cet ordre, plus ce qui n'a pas de
  langue en dehors des blocs : c'est le découpage de `meta.en` /
  `meta.fr` / `meta.global` d'une fiche, appliqué au code, avec les mêmes
  codes ISO 639-1 en minuscules. Un marqueur en marge ouvre un bloc, les
  lignes indentées le continuent, une ligne revenue en marge sans
  marqueur est une note hors langue (parité R, dates, renvois internes),
  qu'on ne traduit pas sous peine d'entretenir deux versions d'un même
  fait daté.

  Aucun standard Python n'existe pour cela, vérifié : `gettext` ne sait
  pas envelopper un `__doc__`, qui doit rester un littéral, et
  `sphinx-intl` traduit à la construction de la documentation, quand le
  lecteur est ici une figure rendue à l'exécution. Le choix suit donc la
  doctrine du dépôt, celle des métadonnées bilingues qui vivent dans la
  fiche : une traduction rangée ailleurs dérive de son original sans que
  personne ne le voie. Elle n'entre pas non plus dans `_T`, indexée sur
  des concepts et non sur des noms de fonctions, qui redeviendrait la
  table distante dont `render.py` s'est débarrassé deux fois cette
  semaine.

  40 fonctions récrites, description **complète** dans les deux langues
  et non un résumé anglais greffé sur un corps français. `help()` rend la
  fonction bilingue au passage. Quatre tests, éprouvés par mutation : un
  bloc absent, un bloc recopié de l'autre langue, `glose()` ignorant la
  langue demandée, et la continuation par indentation désactivée.

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

- `over_period(X, func, dates, period_start, period_end)` : restreint un
  calcul à une sous-période puis délègue. Nécessaire parce que `nanmean`
  et `nanmedian` sont des fonctions numpy, auxquelles on ne peut pas
  ajouter de paramètres. Une borne absente laisse son côté ouvert.
  `_const_date` et `_subset_period`, jusque-là dupliqués dans deux
  modules, y sont rassemblés.

  **La voie plus élégante a été écartée par la mesure**, et c'est à
  retenir avant de la reproposer : une fonction `mask_period` rendant la
  série avec des NaN hors fenêtre, suivie des agrégations habituelles
  inchangées, marche mais **les NaN du masque comptent comme des
  lacunes**. Mesuré le 2026-07-22, une agrégation mensuelle avec
  `max_na_pct=3` sur une série masquée à 20 ans sur 51 rend 0 mois sur
  12 au lieu de 12. Les fiches concernées n'employaient pas ce seuil et
  n'en auraient pas souffert, mais toute fiche future en aurait hérité
  en silence. Restreindre DANS la fonction d'agrégation laisse au
  contraire la restriction invisible au comptage des lacunes.

- **Chaque fiche porte son identifiant pérenne**, colonne `swhid` des
  métadonnées. Le SWHID de contenu d'un fichier est son hash de blob
  git : il se calcule donc localement, sans réseau ni dépôt, et désigne
  la **définition** exacte employée, indépendamment du dépôt et de la
  révision d'où elle vient. Un résultat archivé permet ainsi de
  retrouver la fiche telle qu'elle était, en ouvrant
  `https://archive.softwareheritage.org/swh:1:cnt:...`. Vérifié de bout
  en bout : la fiche est bien récupérable depuis l'archive.

### Modifié

- **La section « État » du CLAUDE.md ne porte plus d'état (2026-08-05).**
  Elle affirmait « tout est commité et poussé », phrase qui redevient
  fausse à la première édition, et redisait le décompte du corpus, les
  chantiers en attente et le prochain proposé, tous écrits ailleurs. Elle
  ne dit plus que **où** lire chaque chose. Les trois acquis qu'elle
  portait (indexation de `method`, suffixes de scénario, paramètres
  externes en colonnes) ne sont pas un état mais de la doctrine
  d'écriture : ils rejoignent « Format d'une fiche », la section dont
  c'est le rôle. C'était la raison pour laquelle « État » regonflait à
  chaque chantier malgré la consigne de ne pas le faire.

  Deux nombres écrits à la main sont partis avec : les onze fiches R
  cassées, que `CHANTIERS.md` redisait alors qu'`ORIGINE_R.md` les
  énumère et les diagnostique (le registre ne garde que l'action qui
  reste à faire), et les « huit règles » du linter de `method`, qui vit
  dans le code. La cohérence des fiches à placeholder est datée plutôt
  que comptée, et le corpus validé contre R est dit « d'alors », pour
  qu'on ne lise plus 215 comme la taille du corpus d'aujourd'hui.

- **`PLAN_nettoyage.md` devient `NETTOYAGE.md`, une procédure et non plus
  un plan (2026-08-05).** Le document décrivait un ménage à faire une
  fois puis à supprimer ; il décrit maintenant comment on nettoie, et se
  rejoue quand il le faut. Son seul statut d'avancement est la section
  « Campagne en cours » : le document lui-même, `CHANTIERS.md` et
  `CLAUDE.md` en donnaient chacun une version, et les trois se
  contredisaient (l'un annonçait « phases 0 à 2 faites » quand la
  checklist en cochait quatre de plus), ce qu'interdit son propre
  principe 1. Les trois autres endroits renvoient désormais sans rien
  redire.

  Dans la foulée, ce qui était du constat de campagne est devenu de la
  procédure : les sept redondances relevées le 2026-07-22, toutes
  corrigées et re-vérifiées dans les trois dépôts le 2026-08-05, ne se
  lisent plus comme du travail à faire mais comme les cinq formes que
  prend une redondance, à rechercher au prochain passage. La carte
  « fichier -> rôle exclusif » couvre à nouveau tout `docs/dev/` et dit
  qu'un document s'y inscrit en même temps qu'il est écrit, faute de quoi
  elle cesse d'être un inventaire. Un renvoi mort trouvé au passage dans
  `src/card/suffix.py`, vers un « CHANTIERS.md §9 » disparu avec
  l'abandon des numéros de section : les trois règles qu'il citait sont
  dans la docstring elle-même.

- **Passe sur les documents de développement (2026-08-04).** Le README
  montrait, sous « Lire une fiche », une figure `card.info` d'avant la
  refonte : mauvais cadre, phrases qui n'existent plus, et jusqu'à la
  version et au SWHID de VCN10 qui avaient bougé. Elle est régénérée
  depuis la sortie réelle, et le paragraphe qui la commente dit les
  signes d'aujourd'hui.

  Deux chantiers livrés étaient restés dans `CHANTIERS.md`, qui
  n'accueille que des pistes ouvertes : la conversion des douze fiches à
  horizon figé et les entrées facultatives, sorties toutes deux le
  2026-07-27. Ce qu'ils portaient encore d'utile, la fausse piste
  `mask_period` écartée par la mesure, remonte à l'entrée `over_period`
  de cette date-là plutôt que de disparaître avec eux.

  `PLAN_nettoyage.md` tenait une colonne « lignes » recopiée à la main
  pour vingt-quatre fichiers, qui avait dérivé sur chacun d'eux en deux
  semaines, ce que son propre principe 1 interdit. Elle est retirée, les
  chemins sont ceux d'après la phase 1, et les cartes de stase et de
  card-api sont complétées. `TOPICS.md` annonçait « 22 dossiers feuilles
  de 1 à 85 fiches » pour un maximum réel de 46, et sa liste numérotée
  sautait de 5 à 7 pour reprendre le 6 après le 11.

- **Le numéro de version du README est désormais tenu (2026-08-04).** Le
  modèle de citation portait « version 0.2.0 » sans que rien ne le
  surveille : `scripts/set_version.py` l'écrit maintenant, et
  `tests/test_citation.py` refuse le désaccord, comme pour les quatre
  autres emplacements. Au passage, la date de publication ne bouge plus
  qu'avec la version : `set_version.py` sans argument redatait
  `CITATION.cff` et `codemeta.json` d'aujourd'hui alors qu'il ne fait que
  propager un numéro inchangé.

- **La figure d'une fiche se lit sans qu'on ait à deviner (2026-08-04).**
  Le rendu ASCII est repris de bout en bout. L'identité tient dans un
  cadre de largeur fixe, titre aligné à droite. Ce qui classe la fiche
  s'écrit en étiquettes alignées (`phénomène ─ moyennes eaux`) plutôt
  qu'en phrases, valeurs en minuscules puisque ce sont des mots-clés du
  vocabulaire de classification. Chaque sortie s'ouvre par un losange,
  identifiant puis libellé traduit collés (`◇ QMA_jan (QMA_janv)`), et
  reprend en dessous les seules étiquettes qui varient d'une sortie à
  l'autre. Le process devient un arbre vertical centré sous les valeurs :
  un trait par étape, le geste sous un coude, les réglages sur un rang
  décalé, la frise des mois là où la fenêtre d'échantillonnage se joue.
  Une description commune à toutes les sorties remonte sous le titre, y
  compris pour une fiche multi-sorties, où elle n'était plus affichée du
  tout : `FDC` taisait la phrase qui dit de quoi elle parle.

  Rien de tout cela ne touche une fiche ni une sortie de calcul : c'est
  l'affichage de `card.info`, et le corps de réponse de `card-api`.

- **Trois noms de fonctions écrits en dur dans la figure (2026-08-04).**
  `render.py` prévient dans son propre docstring qu'un nom de fonction
  cité en toutes lettres est un lien que rien ne vérifie ; il en gardait
  trois. Ils se déduisent de l'appel (`threshold=`, `func=`), ce qui
  ferme un trou : `exceedance_frequency` et `return_period` manquaient à
  la liste, et neuf fiches annonçaient « d'après lowLim » là où la
  condition est un franchissement. Dix entrées du dictionnaire de
  traduction laissées sans appelant par la refonte sont retirées.

- **`method` porte désormais une phrase par colonne produite
  (2026-08-03).** Le champ était une chaîne numérotée, sans lien machine
  avec le process qu'il décrit : rien ne pouvait y demander « la phrase
  de P4 », si bien que la figure se rabattait sur la docstring de la
  fonction, qui ne parle que du général. `method` est maintenant indexé
  par process puis par colonne produite, la colonne étant la clé de
  `func` suffixée par saison ou par mois quand le process porte
  `compress`. Les clés ne sont pas traduites, ce sont les identifiants
  des colonnes de sortie. Le linter refuse un process sans phrase, une
  phrase sans colonne, et des clés différentes entre les deux langues.

  **La sortie ne change pas de forme** : `method_fr` et `method_en`
  restent les étapes numérotées, assemblées par `card/method.py` en
  suivant la chaîne de dépendances que la fiche déclare. Rien n'est
  déduit d'un paramètre de process, seules des phrases écrites dans le
  YAML sont mises bout à bout.

  Vérifié en comparant la publication des 472 lignes de méta avant et
  après, dans les deux langues : 378 étapes changent, toutes dans cinq
  catégories déclarées à l'avance (renvois anaphoriques remplacés par le
  nom de colonne que la fiche déclare, incises `(série des X)` retirées
  puisque la clé nomme la colonne, `agrégation mensuelle` uniformisée en
  `agrégation mensuelle par année`, deux capitales corrigées, phrases
  composées des fiches d'élasticité rendues à leur colonne). Tout le
  reste revient à l'octet. Conception et suite des lots :
  `docs/dev/archive/PLAN_METHOD.md`.

- **La chaîne publiée se lit maintenant sans les clés (2026-08-03).** Les
  clés de `method` lèvent l'ambiguïté machine, mais la valeur publiée ne
  les montre pas : un lecteur reçoit des phrases numérotées, et « sous
  upLim » à l'étape 4 ne se lit que si une étape antérieure a écrit
  `upLim`. Or les incises `(série des X)` retirées à la migration étaient
  précisément ce qui présentait ces noms, à trois orthographes près.
  Mesure faite, 80 références pendaient sur 34 fiches.

  La prose du process qui produit une colonne la nomme donc, dès qu'une
  étape ultérieure la cite, sous une orthographe unique et identique dans
  les deux langues : le nom entre parenthèses en fin de phrase, dispositif
  que le corpus employait déjà (`… sur la période historique (QJXA-10)`).
  Une phrase qui se présente dit aussi sur quoi elle opère, un « minimum »
  nu ne se lisant pas dans une chaîne : l'opérande est lu dans le `func`,
  jamais choisi. Le linter tient la règle, et le test l'éprouve en
  cassant la chaîne. Deux divergences fr/en sont tombées au passage, dont
  l'anglais de `median-dtFlood` qui gardait trois formulations propres.

- **La figure ne répète plus ce que la fiche vient de dire
  (2026-08-03).** `exceedance_quantile(Q)   p=0.01` surmonté de
  « quantile à la probabilité de dépassement de 1 % » disait deux fois la
  même chose : un réglage que la phrase énonce déjà ne s'affiche plus, et
  le corpus passe de trente-trois réglages bruts à quatorze, ceux que
  rien d'autre ne dit. Un nom unique pour plusieurs sorties redevient le
  titre de la fiche, la FDC ayant deux colonnes mais une seule courbe.
  Et la description ne semble plus continuer le bloc de sortie.

- **La figure affiche la phrase de la fiche, plus la docstring de la
  fonction (2026-08-03).** C'est le geste qui a ouvert le chantier : sous
  `apply_threshold(dQ)   dQ >= lowLim, select=dQXA, durée`, `dtFlood`
  ajoutait « Analyse des épisodes où X franchit un seuil lim », et lit
  désormais sa propre phrase, « nombre de jours où dQ dépasse lowLim ».
  Une glose est attachée à une FONCTION, donc elle ne peut dire que du
  général : `apply_threshold` mesure une durée de crue ici et date un
  début d'étiage ailleurs. Seule la moitié droite s'affiche, la maille
  d'agrégation étant déjà dessinée. `render.py` perd cent lignes et une
  indirection ; les docstrings bilingues passent à `card/docstring.py`,
  en attendant le rendu de fonction qui les publiera entières.

- **Les noms de colonnes intermédiaires ont été inventoriés et corrigés
  (2026-08-04).** 113 noms, 384 emplois, confrontés à deux questions : un
  nom désigne-t-il toujours le même calcul, un calcul porte-t-il toujours
  le même nom ? Trente-quatre fiches portaient un suffixe de saison que
  leur calcul n'a pas (`VC10_summer` est une moyenne mobile sans fenêtre,
  donc `VC10` ; la saison n'arrive qu'à l'étape suivante). Deux nommaient
  `QA`/`TA` un agrégat saisonnier, que `QSA_season` nomme `QSA`. `BFM`
  nommait `BF` ce que ses voisines nomment `BF-Wal`.

  Et `RA` désignait un cumul ici, une moyenne là. La règle est venue de
  la source primaire : le tableau 1 d'Oberlin met `PA | Pluie | Année |
  (totale)` en face de `QA | débit | Année | (moyen)`, avec la même
  absence en position 3. La case vide dit « intégrale sur le pas de
  temps, dans l'unité naturelle de la grandeur », donc moyenne pour un
  débit, cumul pour une pluie. `RA` = cumul est conforme, et les trois
  moyennes deviennent `RA-mean`, en variante comme `BF-Wal` l'est de
  `BF`. `NOMENCLATURE.md` porte la règle, et corrige au passage la
  présentation du `R`, qui n'est pas une convention locale mais le sigle
  de l'OMM (groupe SYNOP `6RRRtR`).

  Aucune sortie n'est modifiée, ce que la comparaison par hachage des
  données des 39 fiches, avant et après, a vérifié.

- **Le rôle de `name`, `description` et `method` est écrit, et vingt
  définitions manquantes sont comblées (2026-08-03).** Trois champs à
  destination de personnes, trois niveaux de détail sur la même variable,
  et ils ont le droit de se recouvrir : `name` court et général,
  `description` scientifiquement claire sur ce qu'EST la variable,
  `method` le process d'agrégation étape par étape. La règle « ne jamais
  recopier ce qui vit ailleurs » ne s'applique pas entre eux, elle vise
  les valeurs qui dérivent et les champs machine.

  Mesure faite avant d'écrire : le champ `description` tenait déjà ce
  rôle dans la grande majorité des fiches qui en avaient une, et les
  fiches sans n'étaient pas autant de manques. Vingt seulement en
  manquaient vraiment, celles dont le nom emploie un terme qui ne se
  définit pas tout seul. Quatre n'en manquaient pas mais en avaient une
  fausse : `BFI-LH` et `BFI-Wal`, avec leurs dérivées d'horizon,
  portaient la même description mot pour mot alors que la méthode de
  séparation est exactement ce qui les distingue.

- **Les moitiés droites de `method` ont été relues sous la charte
  (2026-08-03).** Quatre erreurs de fond en sont sorties, qu'aucun test
  ne pouvait voir puisqu'elles portaient sur de la prose :
  `delta-VCX10_H` annonçait en anglais une moyenne mobile sur 3 jours
  pour un `k: 10` ; les trois fiches `rp-*` étiquetaient « minimum » une
  colonne calculée par `nanmean` ; les fiches `alpha-*` annonçaient une
  pente de Sen filtrée sur la significativité du test de Mann-Kendall,
  filtrage que `mannkendall_slope` ne fait pas et ne doit pas faire, la
  pente devant toujours être donnée et interprétée avec le test.

  Le reste est de l'uniformisation : « inter-annuel(le) » rendu
  explicite pour `mean-` et `median-` comme la règle du CLAUDE.md le
  demandait déjà, une phrase par colonne là où quinze fiches en gardaient
  une qui les énumérait toutes, une seule formulation par geste, et la
  forme nominale pour les trente-huit étapes qui disaient encore « le
  maximum de VCN10 EST PRIS comme seuil ».

  Ce qui n'a **pas** changé, et c'est un arbitrage : les notes brèves du
  type « calcul du NSE » restent. `method` donne à voir les étapes du
  process, la complétude est portée par `name` et `description`. Le vrai
  manque est là, une fiche sur deux n'ayant pas de description
  (CHANTIERS).

- **Le drapeau `first` de `ratio` et `difference` est scindé en deux
  fonctions (2026-07-31).** Il ne réglait pas un détail, il changeait ce
  que la fonction produit : `ratio(a, b)` rend une valeur par pas de
  temps, `ratio(a, b, first=True)` en rend UNE, celle du plus long
  palier. Deux fonctions dans une, donc une nature indéfinissable, donc
  une figure incapable d'annoncer ce que produit une étape. Arbitrage de
  l'utilisateur : une fonction ne peut avoir qu'une seule de ces deux
  natures, et cette nature vit dans la fonction, jamais dans la fiche qui
  pourrait la déclarer fausse. D'où **`ratio_longest_run`** et
  **`difference_longest_run`**, et `is_transform` désormais posé sur les
  quatre fonctions arithmétiques, `circular_ratio` et
  `circular_difference` comprises. Trois fiches employaient le drapeau,
  toutes pour le même seuil de crue : `dtFlood`, `median-dtFlood`,
  `delta-dtFlood_H`, version mineure montée. **Aucune valeur ne change**,
  vérifié par extraction avant et après sur le jeu de test. Le test de
  nature devient total, sans exception : un nouveau test refuse qu'une
  fonction change de nature d'un appel à l'autre, et il a été vu rouge en
  réintroduisant le drapeau. Détail : `docs/dev/RENAMING.md`.

- **`exceedance_frequency` ne compte plus les lacunes au dénominateur
  (2026-07-30).** Le numérateur les écartait déjà, le dénominateur les
  comptait par parité R : la fréquence rendue valait la vraie fréquence
  multipliée par la part de données présentes, une année à 3 % de lacunes
  rendant une fréquence 3 % trop basse. Un jour manquant est un jour dont
  on ne sait rien, pas un jour de non-dépassement. Trois raisons de
  rompre : l'estimateur `n / N_observé` est le seul non biaisé sous
  données manquantes aléatoires ; `exceedance_quantile`, dans le même
  fichier, écarte les lacunes des deux côtés, si bien que les fiches
  `fQ*`, qui tirent leur seuil de l'une et leur fréquence de l'autre, se
  contredisaient au milieu ; et la complétude des chroniques Hub'Eau
  s'améliorant avec le temps, ce biais était corrélé au temps et se
  lisait comme une tendance à la hausse. Une série entièrement absente
  rend NaN au lieu de 0, qui se lisait comme « aucun dépassement
  observé ». Six fiches touchées (`fQ01A`, `fQ05A`, `fQ10A` et leurs
  `delta-*_H`), toutes plafonnées à 3 % de lacunes, ce qui borne l'écart.
  Rupture de parité R assumée, avec sa réserve (les lacunes des fiches de
  hautes eaux ne sont probablement pas aléatoires) :
  `docs/dev/ORIGINE_R.md`.

- **La seconde liste de noms en dur de `render.py` disparaît à son tour
  (2026-07-30).** `glose()` décidait de museler une explication d'après
  le NOM de la fonction (`startswith("nan")`, plus `ratio` et
  `difference`). Elle regarde désormais à QUI appartient la fonction :
  une docstring que card n'a pas écrite est de l'anglais de référence
  numpy, sans rapport avec ce que la fiche calcule. Le silence éditorial,
  lui, se déclare à côté de la fonction (`glose_inutile`), donc un
  renommage l'emporte avec lui. Aucune figure ne change. Le préfixe
  muselait au passage `nansum_strict`, qui est de card et a sa propre
  prose : elle reste invisible pour l'autre raison, sa première phrase
  dépassant le seuil de 120 caractères, ouvert dans
  `docs/dev/CHANTIERS.md`.

- **Cinq docstrings parlaient au lecteur du code, pas au lecteur d'une
  fiche (2026-07-30).** La première phrase d'une docstring est reprise
  telle quelle dans la figure par `glose()` : `center=True`, « type 7 R =
  défaut numpy » et « convention du pipeline is_date » y arrivaient
  intacts. Première phrase recentrée sur ce que la fonction calcule,
  détails d'implémentation descendus d'un paragraphe, rien supprimé, pour
  `rollmean_center`, `rollsum_center`, `exceedance_quantile`,
  `exceedance_frequency` et `snowmelt_timing`. Cette dernière décrivait un
  paramètre `p` absent de sa signature. Aucun calcul modifié, diff des 452
  figures limité aux cinq gloses.

- **`card.trend()` rend `h` et non plus `H` (2026-07-28),** en suivant
  stase. La majuscule était le dernier reste du portage R au milieu de
  `level`, `p`, `a`, `b`, `period_start` : dans le même dictionnaire de
  sortie, `P`, `STAT` et `TREND` avaient déjà été mis en minuscules. Le
  détail et l'arbitrage sont dans le CHANGELOG de stase.

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

- `script_path` publie le chemin dans le corpus (`flow/series/QA.yaml`)
  et non plus le chemin absolu sur la machine, qui n'apprenait rien à
  personne et exposait l'arborescence du serveur.

### Retiré

- **`difference_longest_run` (2026-08-03).** Créée par symétrie le
  2026-07-31, aucune fiche ne l'a jamais employée. Sa jumelle
  `ratio_longest_run` reste : trois fiches s'en servent, et un drapeau
  qui change la cardinalité du retour rend le pas de temps d'un process
  indécidable à la lecture. Trace dans `RENAMING.md`.

- Le mode `compact` du rendu, qui masquait les descriptions de fonctions.
  Seule la fonction interne l'exposait, `card.info` ne le passait jamais :
  personne ne pouvait s'en servir.

### Corrigé

- **Personne ne pouvait installer card en suivant le README.** La ligne
  `pip install "card @ git+…"` échouait : pip confronte le nom demandé
  aux métadonnées du dépôt, qui annoncent `card-stase`, et renonce
  (« inconsistent name »). Il se rabattait alors sur PyPI, où `card` est
  la release 0.0.1 d'un squat. La commande nomme maintenant
  `card-stase`, et le README dit les trois choses qu'un lecteur ne peut
  pas deviner : l'ordre des deux lignes compte (`stase` n'étant publié
  nulle part, card installé seul ne résout pas son moteur), le nom
  d'import reste `card`, et une variante par archives du dépôt installe
  les deux sans git sur la machine. Les trois formes vérifiées dans des
  environnements neufs, extraction d'une fiche comprise.

- **La CI était rouge depuis le 2026-07-31, et le disait par mail à
  chaque poussée.** `tests/test_py_golden.py`, arrivé ce jour-là pour que
  la suite lise enfin les golden Python, lit `tests/data/test_data.csv`.
  Ce fichier pèse dix-huit mégaoctets, il est hors git à juste titre
  (`.gitignore`) puisqu'il est entièrement dérivable, mais **rien ne le
  fabriquait ailleurs que sur une machine qui l'avait déjà** : dix-huit
  `FileNotFoundError` sur le runner, et le même mur pour quiconque clone
  le dépôt. `tests/conftest.py` le génère maintenant quand il manque, ce
  qui répare la CI et le clone frais d'un seul geste. Vérifié en
  supprimant le fichier local puis en rejouant la suite : il revient à
  l'octet près (même md5), et les dix-huit fiches retrouvent leur golden.

  Leçon de méthode : une suite verte en local ne dit rien tant qu'elle
  n'a pas tourné sur un arbre qui ne contient QUE ce que git suit.

- **Six figures annonçaient l'inverse de ce qu'elles calculaient
  (2026-07-30).** `fQ01A`, `fQ05A`, `fQ10A` et leurs `delta-*_H`
  affichaient « transforme la série sans l'agréger, une valeur par jour »
  sous un `exceedance_quantile` qui réduit toute la chronique à un seuil
  unique. `decoupe()` de `render.py` devinait la nature d'une fonction
  d'après son nom, en cherchant le préfixe `nan` et deux noms écrits en
  dur, dont `quantile` : le renommage `compute_Qp` vers
  `exceedance_quantile` (RENAMING.md) avait laissé la chaîne derrière
  lui. La nature se lit désormais dans `is_transform`, propriété déclarée
  à côté de la fonction, qui existait déjà et que personne ne lisait. Le
  défaut est « réduit », transformer étant le cas rare et délibéré.
  Vérifié par capture des 452 figures du corpus (226 fiches, deux
  langues) avant et après : seules les six fiches annoncées changent,
  d'une ligne chacune. La suite de tests était verte avant comme après,
  d'où le test de garde ouvert dans `docs/dev/CHANTIERS.md`.

- **La figure taisait les arguments positionnels littéraux
  (2026-08-01).** `render.appel` n'affichait que les colonnes :
  `[ratio_longest_run, "dQXA", 2]` se rendait `ratio_longest_run(dQXA)`,
  et rien ne disait que le seuil de crue de `dtFlood` vaut la **moitié**
  du maximum annuel d'écoulement rapide. L'information la plus utile de
  la ligne était celle qui manquait. Trois fiches concernées, une ligne
  chacune. Un entier s'affiche sans décimale, sinon la fiche semble
  annoncer une précision qu'elle n'a pas.

- **Sept fonctions n'expliquaient rien, ou expliquaient un moignon, dans
  les figures (2026-07-31).** `glose()` coupait la docstring au premier
  point suivi d'une espace : `RAT` n'affichait plus que son sigle, coupé
  après « (Nicolle et al », et `circular_median` finissait sur « , ex ».
  Le découpeur connaît maintenant les abréviations courantes, plutôt que
  d'obliger le code à écrire sans « et al. » pour ménager son afficheur.
  Quatre autres rendaient une glose vide, leur première phrase dépassant
  le seuil de 120 caractères : c'étaient des paragraphes déguisés en
  phrases (`return_level` en faisait 186), raccourcis sans rien perdre,
  le détail descendant d'un cran. `RAT` et `circular_median` ont eu le
  même traitement une fois le découpeur réparé. **Plus aucune fonction de
  card employée par le corpus ne reste muette**, sauf celles qui le
  déclarent, et un test le vérifie. `BFM` gagne au passage l'exemple que
  la troncature lui mangeait.

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

- CI en échec depuis le 2026-07-21 : un import `pytest` devenu orphelin
  dans `tests/test_loader.py` faisait échouer `ruff`, donc le job de
  lint, donc un mail d'échec à chaque push. La routine de vérification
  ignorait `ruff`, elle est corrigée dans CLAUDE.md.

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
