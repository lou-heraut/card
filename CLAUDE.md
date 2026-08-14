# CLAUDE.md : card

## Contexte

`card` est le package Python du recueil de fiches hydroclimatiques
CARD : chaque fiche YAML décrit comment extraire une variable (débit,
précipitation, température...) de séries journalières. Exécution par le
moteur [`stase`](../../EXstat_project/stase/). Ports Python des
packages R `CARD`/`EXstat` ; les repos R (`../CARD-R/`,
`EXstat_project/EXstat/`) sont en maintenance, référence de validation
uniquement, sans fichiers IA. Port validé R↔Python sur le corpus entier ;
la mesure, sa date et les divergences résiduelles sont dans
`docs/dev/ORIGINE_R.md`.

Où lire quoi. Un rôle par fichier, chacun l'annonce dans un bandeau de
statut en tête ; ne jamais recopier d'un fichier à l'autre, renvoyer.
- `CHANGELOG.md` (racine) : ce qui a changé, quand, et où lire le détail.
- docs/dev/, normes en vigueur : `NOMENCLATURE.md` (nommage, règles
  R1-R7, Oberlin), `TOPICS.md` (classification à facettes),
  `RENAMING.md` (noms R vers Python, et sorties modifiées
  volontairement), `ORIGINE_R.md` (origine, validation croisée,
  divergences assumées).
- docs/dev/`CHANTIERS.md` : pistes ouvertes seulement.
- docs/dev/archive/ : documents d'époque, non maintenus (`ROADMAP.md`,
  `AUDIT_FICHES.md`, `PLAN_METHOD.md`, `PLAN_R.md`). On y va pour
  comprendre POURQUOI une décision a été prise, jamais pour savoir où en
  est le corpus.
- docs/dev/`NETTOYAGE.md` : la procédure du ménage documentaire de
  l'écosystème, à rejouer quand il le faut ; sa section « Campagne en
  cours » est le seul endroit qui dise où en est chaque phase, et elle
  dit aujourd'hui qu'aucune n'est ouverte.
- docs/dev/`PLAN_PYPI.md` : réclamation du nom `card` sur PyPI, preuves
  et dates d'envoi.
- docs/dev/`PLAN_SITE_SKOS.md` : le site de documentation et l'export
  SKOS, **construits et livrés en 0.12.0**, publication exceptée. Reste
  la référence du MODÈLE : l'audit des vocabulaires (ce que SKOS,
  I-ADOPT, CPM, CF, QUDT et OWL-Time savent dire, et ce que card publie
  avec chacun) n'est écrit que là. Porte aussi les trois bascules du jour
  de la publication du site.
- docs/dev/`PLAN_THESAURUS.md` : la forme du vocabulaire, close depuis le
  2026-08-14, et pourquoi elle est celle-là. Porte la mesure de LEUR
  thésaurus faite sur le graphe entier, le point de jonction unique,
  l'alignement HydroPortail, et **la liste de ce qui reste ouvert, en fin
  de document et à un seul endroit**. **Rien n'est publié** tant que
  Theia n'a pas répondu.
- docs/dev/`QUESTIONS_THEIA.md` : ce qu'on leur demande, et rien
  d'autre. Brouillon, rien n'est envoyé, et **rien n'attend leur
  réponse** : aucune des questions ne bloque le reste.
- docs/dev/`RETOURS_SCHAPI.md` : même rôle pour le SCHAPI, ce qu'on a
  relevé dans leur documentation et dans leur outil en alignant card sur
  la notation officielle. Brouillon, rien n'est envoyé, rien n'en dépend.
- **Écosystème R** : le front vit dans `../card4r/` (paquet mince qui
  APPELLE card, ne le réimplémente pas) ; les paquets historiques
  `../CARD-R/` et `../../EXstat_project/EXstat/` sont `superseded` et
  restent **sans fichiers IA**. Pourquoi ces choix : `archive/PLAN_R.md`.

## Structure

```
src/card/
  cards/<domain>/<phenomenon>/<output>/   # les fiches, rangées par régime :
                             #   flow|precipitation|temperature|evapotranspiration
                             #   / low-flows|high-flows|… / series|scalar|curve ;
                             #   le linter impose chemin == classification
                             #   (domaine / phénomène-ou-purpose / forme)
  functions/     # fonctions hydro portées de R. Docstring en ANGLAIS
                 #   avec sections NumPy, comme le reste de l'API et
                 #   comme stase : ses lecteurs sont `help()`, qui ouvre
                 #   le fichier, et la documentation des fonctions du
                 #   site. Elle décrit la FONCTION, pas ce qu'une fiche
                 #   en fait : la figure ne la lit plus, elle lit le
                 #   `method` de la fiche.
                 #   Une fonction TRANSFORME (une valeur par pas de temps)
                 #   ou RÉDUIT, jamais les deux : `is_transform = True` se
                 #   déclare à côté d'elle pour le premier cas, l'absence
                 #   vaut le second.
                 #   Tout cela est MESURÉ par tests/test_nature_fonctions.py
                 #   et tests/test_render.py : rien à retenir, ils le disent.
  method.py      # le `method` d'une fiche : colonnes qu'un process produit
                 #   (clé de func, suffixée par saison/mois si `compress`),
                 #   grain temporel de chaque colonne, et assemblage de la
                 #   forme publiée en remontant la chaîne de dépendances
                 #   que la fiche DÉCLARE. Ne fabrique jamais une phrase.
  loader.py      # YAML -> processus ($Hx, tuples func, défauts)
  extraction.py  # card.extract -> {data, meta} (chaîne P1..Pn via stase)
  suffix.py      # suffixes de scénario : vocabulaire {clé: enregistrement},
                 #   placeholders {suffix.<champ>}, défauts de fiche
  trend.py       # card.trend : stase.trend fiche-conscient (refus explicite
                 #   des fiches non `output: series` ; traduit les fiches en
                 #   relative={variable: bool}, dérive suffix= de meta)
  management.py  # list_cards (filtres par facette : slug OU libellé fr/en),
                 #   info (imprime la figure ; quiet=True pour le seul dict),
                 #   copy_cards
  render.py      # figure() : la fiche DESSINÉE, rendue en chaîne, sans
                 #   rien imprimer (c'est ce que sert card-api). Sa
                 #   doctrine est dans son propre docstring de module ; ce
                 #   qu'il faut savoir avant d'y toucher : rien ne s'y
                 #   déduit d'un NOM de fonction, et ce que fait une
                 #   étape se lit dans le `method` de la FICHE, jamais
                 #   dans la docstring de la fonction, qui ne peut dire
                 #   que du général.
  schema.py      # linter : python -m card.schema ; vocabulary() public
  topics.yaml    # vocabulaire de contrôle : la CLÉ est un slug neutre,
                 #   `en` et `fr` sont deux étiquettes à égalité ; le slug
                 #   nomme aussi le dossier (cf. docs/dev/TOPICS.md)
  inputs.yaml    # unités/définitions des variables d'entrée (invariants)
  alignments.yaml # ce que les fiches ne peuvent PAS dire : correspondances
                 #   vers les vocabulaires externes (Theia/OZCAR, QUDT, CF,
                 #   et les DEUX notations officielles françaises sous
                 #   `notations:`, celle du SCHAPI et celle du Sandre ; un
                 #   registre de plus ne demande aucun code, et une valeur
                 #   peut être une liste parce qu'ils écrivent eux-mêmes
                 #   la même variable de plusieurs façons), familles de
                 #   contrainte propres à
                 #   card, table des paramètres de process qui sont
                 #   sémantiques, et les quatre racines thématiques
                 #   (`topics:`), leur note de portée et leur
                 #   `broadMatch`. Rien de dérivable.
tests/           # pytest (goldens R, loader, lint, suffixes, UX, rendu)
                 #   pas de décompte ici : il périme, cf. README
scripts/generate_catalog.py   # QUATRE sorties, relancer après toute modif :
                              #   docs/CARDS.md et CARDS.fr.md (GitHub),
                              #   docs/catalogue.md (le site, une entrée par
                              #   VARIABLE), docs/cards/*.md (une page par
                              #   fiche, portant sa figure) et le décompte
                              #   du README
scripts/generate_skos.py      # docs/card.ttl : le corpus en SKOS, I-ADOPT,
                              #   CPM, QUDT, OWL-Time et ISO 25964. Base
                              #   d'URI PROVISOIRE et fausse : rien n'est
                              #   publié, cf. PLAN_THESAURUS.md. L'arbre va
                              #   de la grandeur au phénomène puis à la
                              #   variable ; une FAMILLE n'est pas dans cette
                              #   chaîne, c'est un `isothes:ThesaurusArray`,
                              #   et son libellé de nœud vient de deux tables
                              #   ÉCRITES qu'une facette nouvelle oblige à
                              #   compléter (la génération échoue sinon).
scripts/arbre_skos.py         # `make arbre` : le .ttl en arbre, lisible.
                              #   Un Turtle sort dans l'ordre des URIs, où la
                              #   hiérarchie est invisible : c'est la seule
                              #   façon de juger la forme du vocabulaire.
                              #   Ne vérifie rien, c'est une paire de lunettes.
mkdocs.yml                    # le site : `make serve` en local,
docs/assets/                  #   .github/workflows/site.yml en ligne.
                              #   theme.css porte l'identité (celle de la
                              #   page /docs de card-api), catalogue.css et
                              #   .js le catalogue. Le déclenchement est
                              #   MANUEL tant que la publication n'est pas
                              #   tranchée.
scripts/verifie_alignements.py # résout les URIs externes, sur le réseau,
                              #   donc hors de la suite de tests
scripts/analyse_classification.py  # santé des facettes : redondance,
                              #   pouvoir de résolution, colonnes dérivées.
                              #   À lancer AVANT d'ajouter, retirer ou
                              #   fusionner une facette ; ses chiffres ne
                              #   sont recopiés nulle part, ils bougent.
```

Env : venv `.python_env/` ; `tests/conftest.py` rend card, stase et
`scripts/` importables. **Vérifs après toute modif** (ce que lance le CI,
dans cet ordre) : `pytest`, `python -m card.schema`, `ruff check src tests
scripts`, soit `make check`. Le `Makefile` est le bloc-notes des
commandes de base, `make` seul les liste ; il ne décide rien, il évite de
retenir, donc rien de ce qui est écrit ailleurs n'y est recopié. Le catalogue n'est plus à retenir : si une fiche a bougé,
`tests/test_catalogue.py` échoue et réclame `scripts/generate_catalog.py`
en le nommant. Même chose pour `docs/card.ttl` et
`tests/test_skos.py`, avec une dépendance de plus : le fichier porte la
version du PAQUET, donc il se régénère APRÈS `set_version.py`, jamais
avant. Le test le dit s'il est oublié. Oublier ruff
casse le CI en silence et envoie un mail d'échec à l'utilisateur à chaque
push, ce qui est arrivé du 2026-07-21 au 2026-07-22.

## Format d'une fiche

```yaml
id: QA                      # = nom de fichier ; grammaire NOMENCLATURE.md
version: "2.0"              # bump majeur si les SORTIES changent,
                            # mineur si method/description, patch sinon
authors: ["Louis Héraut (INRAE, UR RiverLy)"]
date: "2026-04-30"

meta:
  en:
    variable: QA            # listes si plusieurs sorties distinctes
    unit: "m^{3}.s^{-1}"
    name: Annual mean daily discharge      # cf. « Les trois champs humains »
    description: ""                        # vide si le name porte déjà tout
    method:                                # une phrase par colonne produite
      P1:
        QA: "annual aggregation [09-01, 08-31] - mean"
    sampling_period: ["09-01", "08-31"]     # MM-DD en en, DD-MM en fr
    classification:         # labels MINUSCULES, validés contre topics.yaml
      domain: flow          #   (liste si plusieurs grandeurs)
      phenomenon: mean flows  # scalaire/liste/absent, jamais forcé
      aspect: magnitude     # IHA ; interdit si purpose présent
      statistic: mean       # l'opération TERMINALE, orthogonale à aspect
                            #   (VCN10 et tVCN10 sont tous deux `minimum`) ;
                            #   absente si la sortie vient d'un filtre
      season: annual        # annual|summer|winter|by season|by month|record
      output: series        # series|scalar|curve, doit matcher le dossier
      # purpose: model performance | climate sensitivity (optionnel)
  fr:
    ...                     # mêmes champs, labels français appariés
  global:                   # zone neutre non traduite
    input_vars: Q           # doit exister dans inputs.yaml
    preferred_sampling_period: "09-01"
    palette: [...]

process:
  P1:
    func:
      QA: [nanmean, "Q"]    # [fonction, *colonnes, kwargs?, is_date?]
    sampling_period: "09-01"
    max_na_pct: 3
    max_na_years: 10
```

### Les trois champs humains, et leurs trois niveaux

`name`, `description` et `method` s'adressent à des personnes, pas à une
machine. Ce sont trois niveaux de détail sur la même variable, et **ils
ont le droit de se recouvrir** : deux textes qui disent le même fait à
deux niveaux ne sont pas un doublon, c'est le service rendu.

- **`name`** : court et général, parfois vernaculaire. « Durée des crues ».
- **`description`** : plus long, scientifiquement clair sur ce qu'EST la
  variable produite. Ne se remplit que si le `name` ne porte pas déjà
  toute l'information : « Minimum annuel du débit journalier » se suffit,
  « Début des écoulements lents » appelle « Date à laquelle 10 % du cumul
  annuel du débit de base sont atteints ». Mesuré le 2026-08-03, c'est
  déjà le rôle qu'elle tient dans le corpus.
- **`method`** : le process d'agrégation, étape par étape, avec la
  nomenclature et les paramètres précis. Une phrase par colonne produite.

> **La règle « ne jamais recopier ce qui vit ailleurs » ne s'applique
> PAS entre ces trois-là.** Elle vise les VALEURS qui dérivent (versions,
> décomptes, plafonds), et les champs machine. `sampling_period` est du
> langage machine ; qu'une description dise « Mois de décembre, janvier
> et février » n'est donc pas une redite à supprimer, c'est la même chose
> dite à un lecteur. Erreur commise trois fois pendant le chantier
> `method` d'août 2026, corrigée trois fois par l'utilisateur.

Règles clés (détail : NOMENCLATURE.md) :
- **func** : résolution card.functions puis numpy (nanmean, nanargmax,
  delta, return_level, apply_threshold...) ; kwarg dont la valeur est
  une variable amont ({lim: upLim}) résolu dynamiquement ; littéraux
  positionnels permis ; `true` final = is_date.
- **sampling_period adaptatif** : `{type: adaptive, func: [nanmax, "Q"]}`.
  Convention PAR PHÉNOMÈNE (linter) : low flows = nanmax + preferred
  01-01 ; high flows = nanmin + preferred 09-01 ; toute fiche adaptative
  doit déclarer un preferred_sampling_period. À l'exécution,
  `card.extract(..., sampling_period="preferred"|"MM-DD")` écrase les
  fenêtres ANNUELLES (protocole MAKAHO = "preferred") ; les fenêtres
  partielles [début, fin] font partie de la définition, jamais écrasées.
- **horizons** : déclarés dans meta.global.horizons, référencés `$H0..$H3`.
- **défauts à omettre** : dans meta.global, is_date false,
  is_experimental false, source/palette/preferred null, input_vars "X" ;
  dans process, sampling_period/period/max_na_* null, seasons
  [DJF,MAM,JJA,SON], keep null, compress/expand false. Exception : un
  kwarg explicite dans la source reste explicite.
  **Quatre champs font exception et s'écrivent TOUJOURS**, y compris pour
  leur défaut, et le linter les exige. La règle qui les sépare du reste :
  on omet un défaut qui veut dire « rien de particulier » ; on écrit un
  défaut qui est un CHOIX, sans quoi son absence se lit comme un oubli.
  Une fiche est de la donnée : elle porte ce qu'elle affirme sans qu'on
  ait à connaître un défaut de code.
  - `time_step`, le cœur de l'agrégation, un choix parmi sept valeurs ;
  - `is_date`, de quel axe parle la variable (`true` ssi `aspect: timing`) ;
  - `relative`, ce que la GRANDEUR autorise, cf. NOMENCLATURE §7 bis ;
  - `max_na_pct` **et seulement sur un process qui range du JOURNALIER
    dans des cases**, avec `max_na_years` **une fois par fiche**, parce
    que c'est un critère sur la chronique et non sur un pas de temps.

  La règle n'est donc pas « écrire partout » mais **« écrire partout où ça
  a un sens, et n'être silencieux nulle part où ça en a un »**. Sur un
  process qui divise deux séries déjà annuelles, un pourcentage de jours
  manquants ne veut rien dire, et l'écrire serait du bruit. Un seuil
  DÉLIBÉRÉMENT absent s'écrit `null` : `QJ` range par jour calendaire,
  donc une case contient des années et non des jours, et la valeur 3 y
  écarterait un jour dès qu'une seule année manque.

  Ce que le silence a coûté, deux fois : une ligne perdue dans la fiche R
  de `RMAs_month` a fait annoncer douze variables comme relatives, seules
  de leur famille ; et `dtFlood` calculait son maximum annuel sur une
  année même privée de la moitié de ses jours, quand la fiche jumelle
  `dtLF` écartait la même année. Les deux corrigés le 2026-08-13, et
  aucun n'était visible fiche par fiche.
- **multi-sorties** : métadonnées en listes si les sorties sont des
  variables distinctes ; name UNIQUE si ce sont les coordonnées d'un même
  objet (FDC_p/FDC_Q = une courbe).
- La moyenne intra-pas-de-temps est implicite ; « inter-annuel(le) »
  toujours explicite pour mean-/median-. Quantiles temporels : « dépassé
  p % du temps », jamais « X années sur Y ».

> ## À NE JAMAIS FAIRE
>
> - **`note.txt` (et tout fichier de notes de l'utilisateur) : NE PAS
>   L'OUVRIR.** Ni Read, ni `cat`, ni `grep`, ni au détour d'un `git add`.
>   C'est son brouillon personnel : pas de lecture, pas de résumé, pas de
>   « au passage j'ai vu que ». Il n'entre dans aucune tâche sans une
>   demande explicite de sa part, fichier par fichier. Un en-tête qui dit
>   de ne pas lire est un ordre, pas une mise en garde à évaluer.
> - **Pas de `git add -A` ni de `git add .`** : stager nommément les
>   fichiers que l'on a soi-même modifiés. Ce qui traîne dans l'arbre de
>   travail appartient à l'utilisateur.
> - **Ne JAMAIS signaler un fichier non suivi.** Un fichier non suivi est
>   à l'utilisateur : brouillon, essai, sortie jetable. Il a le droit d'en
>   avoir, il n'a pas à s'en justifier, et le lui rappeler est une
>   nuisance. Pas de « au passage, j'ai vu que », pas de « je n'y touche
>   pas », pas de récapitulatif en fin de réponse. On n'en parle que s'il
>   en parle le premier. Le répertoire `bac/` est ignoré par git : c'est
>   là qu'on lui propose de déposer ce qu'il veut faire disparaître du
>   `git status`, une fois, sans y revenir.

### Trois acquis à ne pas reperdre

Ils changent la façon d'écrire une fiche, et rien dans le YAML ne les
rappelle :

- **`method` est indexé par process et par colonne produite**, une phrase
  par colonne, clés non traduites, et le linter tient plusieurs règles
  dessus (correspondance avec `process`, chaîne lisible sans les clés,
  moitié gauche confrontée au calcul, nombres écrits vérifiés). La figure
  lit ce champ. Conception : docstring de `src/card/method.py`, raisons dans
  `docs/dev/archive/PLAN_METHOD.md`.
- **suffixes de scénario** : le fan-out des valeurs est fait par stase au
  niveau colonne, card n'ajoute que les métadonnées, donc aucun
  placeholder ne peut changer un calcul. Une variable suffixée est une
  autre variable, donc une autre ligne de `meta` et une colonne
  `suffix`. Conception : docstring de `src/card/suffix.py`.
- **paramètres externes en colonnes d'entrée** : seuils réglementaires et
  bornes d'horizon arrivent comme des colonnes (rôle `param_cols` côté
  stase), une fiche ne fige plus ni un seuil ni une date. Conception :
  docstring de l'extraction de stase.

## Règles de travail

- Lire la fiche complète avant modification ; la fonction fait foi (les
  métadonnées décrivent le calcul réel).
- Modifications de masse par batch (~10), récap avec niveau de confiance,
  attendre le go. Corrections auto uniquement à confiance élevée
  (grammaire, casse, cohérence) ; réécriture scientifique = validation.
- Noms de fonctions/paramètres : RENAMING.md fait foi, tout nouveau
  renommage validé par l'utilisateur.
- **Docstring d'une fonction PUBLIQUE ou d'une fonction hydro** : elles
  suivent la MÊME règle depuis le 2026-08-11, **anglais et sections
  NumPy**, comme dans stase. C'est de la documentation, pas un
  commentaire, et elle nourrira la documentation des fonctions du site.
  Mesuré deux fois : `tests/test_docstrings.py` pour ce que
  `card.__all__` annonce, `tests/test_render.py` pour les fonctions que
  les fiches emploient. La machinerie interne, elle, écrit dans la
  langue qu'elle veut : elle s'adresse à qui ouvre le fichier.
  **Le balisage du corps est du MARKDOWN**, en revanche, et pour tout le
  paquet : un accent grave SIMPLE pour du code, aucun rôle `:func:`. Le
  style NumPy est né pour Sphinx et sa syntaxe en ligne est du reST, que
  le site ne lit pas : il découpe les sections NumPy puis rend le corps
  en Markdown. Un renvoi s'écrit donc `card.list_cards`, sans lien, la
  syntaxe de lien de mkdocstrings laissant ses crochets dans `help()`.
  Mesuré par `tests/test_docstrings.py`, et la même règle vaut dans
  stase.
- **Version d'une fiche** (champ `version:` de son YAML) : majeur si ses
  SORTIES changent (+ trace RENAMING.md, parité R rompue documentée,
  goldens re-figés), mineur pour method/description, patch sinon. Elle
  part dans les métadonnées de sortie.
- **Chaînage à ne pas rater**, rappelé ici exprès : une modif notable se
  note sous `## Non publié` du CHANGELOG ; **écrire l'entrée qui CLÔT un
  chantier, c'est le moment où l'on se demande s'il faut couper une
  version** (`scripts/set_version.py --etat` donne les faits, la règle
  est la cinquième phrase du CHANGELOG) ; publier se fait par
  `scripts/set_version.py`, jamais à la main ; un changement de moteur
  nécessaire à card impose de remonter `stase>=` dans le pyproject.
  Détail : « Versions et citation » plus bas.
- Pas de PDF ni de `*~` sous git.
- **Jamais de fenêtre de choix à cocher** (outil de question à options).
  Elle coupe la conversation au lieu de la nourrir. Une décision à
  prendre s'expose dans la réponse, en prose : le constat, les options,
  celle qu'on recommande et pourquoi. L'utilisateur répond dans le fil,
  ou dit qu'il ne sait pas et on en discute.
- Pas de tiret quadratin (—) dans la prose (docs, messages, commentaires,
  réponses) : reformuler (deux points, parenthèses, phrases séparées).
  Perçu comme un marqueur de texte IA, rebute des utilisateurices.
- **Aucun nombre écrit à la main s'il vit ailleurs.** Nombre de fiches, de
  variables, de tests, de fonctions : la phrase reste, la valeur bouge, et
  la doc ment sans que rien ne rougisse. Le SEUL décompte du dépôt est
  celui du README entre les marqueurs `<!-- cards:count -->`, tenu par
  `scripts/generate_catalog.py`. Partout ailleurs on dit la RÈGLE, pas la
  valeur, ou on renvoie à la commande qui la donne. Constaté le
  2026-07-30 : le README annonçait « 105 tests » pour 126 réels, dans la
  ligne juste au-dessus de la commande qui affiche le vrai chiffre. Même
  règle dans card-api, même raison.
- **Une chaîne de caractères qui nomme une fonction est un lien que rien
  ne vérifie.** Ni l'import, ni le linter, ni les tests ne suivent un nom
  de fonction écrit en dur dans une liste (`if nom in ("quantile", ...)`).
  `RENAMING.md` acte les renommages, il ne sait pas qui les cite en
  toutes lettres. Préférer une propriété DÉCLARÉE à côté de la fonction
  (`is_transform`) et un test qui refuse une fonction du corpus non
  classée. Constaté le 2026-07-30 : `compute_Qp` renommé
  `exceedance_quantile`, la liste restée en arrière, six figures
  annonçant « une valeur par jour » pour un seuil unique, suite verte.

## Versions et citation

Doctrine complète : « Versions, en cinq phrases », en tête de
`CHANGELOG.md`. Ce qu'il ne faut pas rater :

- **Au quotidien : rien.** La production suit `main`, le service publie
  le commit et le SWHID de card et de stase dans chaque réponse. Le seul
  geste régulier est l'entrée `## Non publié` du CHANGELOG. **Le
  proposer soi-même**, l'utilisateur ne le demandera pas.
- **Quand couper une version** : une rupture de SORTIES se publie le jour
  où elle est livrée, le reste attend la fin du chantier en cours, jamais
  le calendrier. Critères exacts : cinquième phrase du CHANGELOG.
  `python scripts/set_version.py --etat` donne les faits (dernier tag,
  commits depuis, entrées non publiées). **Le proposer soi-même** aussi :
  l'utilisateur ne le demandera pas, il l'a dit explicitement le
  2026-08-05.
- **Publier une version** : `python scripts/set_version.py 0.3.0` accorde
  tous les fichiers qui portent le numéro. Ne JAMAIS y écrire un numéro à
  la main : `tests/test_citation.py` refuse le désaccord. Puis section de
  CHANGELOG, commit, `git tag -a vX.Y.Z`, `git push --tags`.
- **SWHID** : `swh:1:rev:<hash du commit>` EST l'identifiant Software
  Heritage d'une révision git, calculable sans aucun appel d'API. Il ne
  résout que si le dépôt est archivé : fait le 2026-07-22 pour les trois,
  et SWH revisite tout seul ensuite. Rien à refaire par version.
- **Ne pas confondre** avec la version d'une FICHE (champ `version:` de
  son YAML, majeur si ses SORTIES changent) : elle voyage dans les
  métadonnées de sortie, une par variable, à côté de la colonne `swhid`
  qui identifie le FICHIER de fiche (`swh:1:cnt:` + son hash de blob
  git, calculé à la lecture). Trois niveaux de traçabilité, donc : la
  définition (swhid de fiche), le corpus (commit de card), le moteur
  (commit de stase).


## État

Cette section ne porte aucun état, et c'est volontaire : un état recopié
ici ne peut que retarder sur le dépôt. Elle dit seulement où le lire.

- **Ce qui a été livré, et quand** : `CHANGELOG.md`.
- **Ce qui reste ouvert**, y compris ce qui attend une action de
  l'utilisateur et le prochain chantier proposé :
  `docs/dev/CHANTIERS.md`.
- **Où en est le ménage documentaire** : la section « Campagne en cours »
  de `docs/dev/NETTOYAGE.md`.

Écosystème : le moteur vit dans `../../EXstat_project/stase/`, le service
web dans `../card-api/`. Chacun a son CLAUDE.md, ses chantiers et son
journal. Ne rien consigner ici de ce qui les regarde, et réciproquement.
