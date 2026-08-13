> **Statut : norme en vigueur.** Seule référence pour nommer une
> variable et rédiger ses métadonnées. Toute correction de fiche cite la
> règle qu'elle applique.

# NOMENCLATURE : Guide de nommage des variables CARD

> **Validé par l'utilisateur le 2026-07-15** (arbitrages en §9).
> Référence normative pour toute création de fiche, et pour
> l'application de l'audit (`archive/AUDIT_FICHES.md`). Fondé sur le
> système du corpus CARD consolidé par Oberlin (1992), dont la
> transcription est dans `Oberlin_1994ITCEMAGREF_1-8_edit.md`.

## 1. Fondement : le système Oberlin

Oberlin (CEMAGREF, 1992) propose des sigles hiérarchisés en **quatre
positions ordonnées**, chacune facultative sauf les deux premières :

```
[Grandeur] [Pas de temps / durée] [Représentativité] [Saison]   (+ suffixes)
    Q              M                     N               A       → QMNA
    Q              J                     X               A       → QJXA
    P              J                     X               Sh      → PJXSh
```

Le cœur des identifiants CARD **est déjà ce système** (QA, QJXA, QMNA,
VCN10, TSA...). Le présent guide le documente, fixe les extensions
propres à CARD (préfixes-opérateurs, suffixes d'horizon et de saison)
et en dérive les règles de rédaction des métadonnées.

Deux principes d'Oberlin structurent tout le reste :

- **La définition d'une variate est hiérarchisée** : nature/grandeur
  physique d'abord, temps (pas de temps, durée) ensuite,
  représentativité dans la saison, puis saison, puis seulement les
  détails (période de retour, mode d'extraction). Le sigle et la
  périphrase (`name`) suivent le même ordre.
- **Le mot « moyenne » est réservé à la statistique** (estimateur de
  l'espérance, typiquement inter-annuel). La moyenne *dans* le pas de
  temps est triviale et implicite : un « débit mensuel » est par
  définition la moyenne du mois. (Règle complémentaire d'Oberlin.)

## 2. Position 1 : Grandeur

| Sigle CARD | Grandeur | Note vs Oberlin |
|---|---|---|
| Q | débit | conforme |
| R (Rl, Rs) | précipitations (liquides, solides) | Oberlin utilise P (pluie) et réserve R aux stocks. Ce n'est pas une convention locale de CARD : **`R` est le sigle de l'OMM**, groupe SYNOP `6RRRtR`, où `RRR` est la hauteur précipitée en millimètres sur la période `tR`. CARD suit donc un autre standard, pas une entorse, et ce standard porte déjà le sens de cumul. Vérifié le 2026-08-04 |
| T | température | conforme |
| ETP | évapotranspiration potentielle | conforme (E + indices TP) |
| BF | débit de base (baseflow) | extension CARD (Oberlin : indice b sur Q) |
| LF | basses eaux (low flows, événement) | extension CARD |

Cas à part : les **critères de performance** (NSE, KGE, Bias, STD) et
de **sensibilité climatique** (epsilon_*, RAT_*, Rc) ne sont pas des
variates hydrologiques au sens d'Oberlin mais des scores ou indices
adimensionnels ; ils forment un espace de noms séparé et ne suivent pas
les positions 2–4.

## 3. Position 2 : Pas de temps ou durée

| Sigle | Sens | Exemples |
|---|---|---|
| A | année (pdt annuel) | QA, RA, TA |
| M | mois | QMNA, QMA_month, TMA_month |
| S | saison (pdt saisonnier) | QSA_season, TSA_season, RSA_season |
| J | jour | QJXA, QJD |
| I | instantané | (réservé, non utilisé actuellement) |
| *k* en suffixe de VCN/VCX | durée mobile continue de k jours | VCN10, VCX3 |

Les **VCNd / VCXd** sont les « variates spécialisées » d'Oberlin :
V = valeur moyenne sur une durée continue (Volume), C =
Caractéristique, N/X = représentativité, d = durée en jours. Oberlin
prévoit deux sœurs, **QC** (débits-seuils tenus continûment d jours) et
**DC** (durées cumulées : débit sur un total de d jours non
consécutifs) ; **CARD n'en fait aucune fiche et ne réserve pas leurs
sigles**. Les débits caractéristiques d'Oberlin (DC1, DC6, DCE... =
débit dépassé 1, 6, 11 mois par an) sont des **points de la courbe des
débits classés**, que CARD fournit en entier avec la fiche `FDC` : le
besoin est couvert par la courbe, pas par des variates discrètes. `D` et
`Q` restent donc libres pour d'autres rôles (cf. §4, `D` = médiane).

Par analogie avec V-C, **QJCd** se lit « débit Journalier lissé sur d
jours » : le régime moyen par jour de l'année (moyenne inter-annuelle
implicite, cf. §4), lissé sur d jours. `name` « Régime journalier
inter-annuel lissé sur d jours » (l'ancien « débit moyen mensuel » était
faux, audit A4). La variante médiane du régime se sigle `QJDCd`
(cf. §4).

Indices climatologiques (dtCDD, dtCWD, RCXA, dtRA01mm...) : la grandeur
et la durée sont dans le sigle ETCCDI d'origine (CDD = consecutive dry
days) ; on conserve les sigles internationaux tels quels (cf. §8).

## 4. Position 3 : statistique d'ordre (représentativité)

Position 3 dit **quelle statistique d'ordre résume l'échantillon** que
le sigle définit. Oberlin ne nommait que les extrêmes ; CARD étend
proprement la case à la médiane, sans toucher aux standards :

| Statistique | Percentile | Jeton | Exemples |
|---|---|---|---|
| minimum | P0 | **N** | QMNA, VCN10, QNA |
| médiane | P50 | **D** | QJD, QDA |
| maximum | P100 | **X** | QJXA, VCX10, RCXA5 |
| **intégrale sur le pas de temps** | — | **absence** | QA, QM (moyennes) ; RA, ETPA (cumuls) |
| autre quantile | Pq | **Pq** | QJP10, QJP90 |

> ### La case vide ne dit pas « moyenne », elle dit « intégrale »
>
> C'est la règle la plus contre-intuitive du système, et elle vient
> d'Oberlin lui-même, dont le tableau 1 met les deux cas côte à côte,
> avec la même absence en position 3 :
>
> ```
> PA   | Pluie | Année | (totale)  | —
> PBM  | Pluie/Bassin | Mois | (totale) | —
> QA   | débit | Année | (moyen)   | —
> QM   | débit | Mois  | (moyen)   | —
> ETRM | ETR   | Mois  | (totale)  | —
> ```
>
> Son texte l'explique : « un débit mensuel sera toujours une moyenne de
> débit dans le mois (ou du volume écoulé : mathématiquement équivalent,
> aux unités près) […] un flux annuel une intégrale (moyenne, volume, …)
> sur l'année, une pluie horaire, un total précipité en une heure ».
>
> La case vide vaut donc **l'intégrale de la grandeur sur le pas de
> temps, exprimée dans son unité naturelle** : une moyenne pour un débit
> ou une température, qui sont un régime et un état ; un cumul pour une
> pluie ou une ETP, qui sont des flux qui s'accumulent. `RA` est un
> cumul et `QA` une moyenne, sans que ni l'un ni l'autre déroge.
>
> Mesuré sur le corpus le 2026-08-04 : ETP agrégée 17 fois, toujours par
> somme ; température 40 fois, toujours par moyenne ; précipitations 48
> fois par somme. La règle était déjà appliquée partout, elle n'était pas
> écrite.
>
> **Conséquence.** Pour une pluie, la case vide étant prise par le
> cumul, une MOYENNE doit se marquer. Oberlin n'a jamais eu à le faire
> (aucun de ses exemples de pluie n'est une moyenne : ce serait un
> total divisé par n, donc un taux, pas une variate). CARD la note en
> variante, comme `BF-Wal` est une variante de `BF` : `RA-mean`.
> Arbitrage du 2026-08-04, sur trois colonnes intermédiaires
> (`epsilon_R`, `epsilon_R_season`, `RAT_R`). Si un jour une telle
> moyenne devient une SORTIE, la question se rouvrira.

Trois règles tiennent tout :

- **La moyenne d'un débit est le fantôme.** Ce n'est pas une statistique
  d'ordre mais l'espérance ; elle ne s'écrit jamais en position 3
  (corollaire de
  la règle « moyenne » du §1). `QA`, `QJ`, `QM` = moyenne implicite.
- **`N`/`D`/`X` sont les trois statistiques d'ordre nommées** (min,
  médiane, max). Un autre percentile s'écrit `Pq` (q = probabilité en
  %). `P0`, `P50`, `P100` sont **interdits** comme jetons : ce sont
  `N`, `D`, `X`, sans quoi on aurait deux écritures pour un même calcul.
  `D` est libre (cf. §3 : ni `DC` ni `QC` ne sont réservés).
- **L'axe de la statistique suit la granularité de sortie, pas la
  lettre.** Une sortie **par-année** (lettre de saison `A` présente)
  agrège *dans* l'année : `QNA` = min des jours de l'année → une valeur
  par an (série). Une sortie **régime** (pas de `A`, résolution
  sous-annuelle gardée) agrège *sur les années* par sous-période :
  `QJD` = médiane des années pour chaque jour → 365 valeurs (courbe).
  Le même jeton, `D`, vaut donc intra-année dans `QDA` et inter-annuel
  dans `QJD` ; c'est déjà le cas pour le fantôme (`QA` vs `QJ`) et pour
  `N`/`X`. **Régime = pas de `A` = sortie `curve`.**

## 5. Position 4 : Saison d'échantillonnage

- **A** = année (saison par défaut des extrêmes) : QJXA, QMNA, VCN10
  (le A est implicite dans VCN10, usage national conservé).
- CARD exprime les saisons restreintes par **suffixe explicite** plutôt
  que par lettre Oberlin (Sh, Se) : `_summer`, `_winter`, `QSA_JJASO`.
  Divergence assumée (lisibilité pour l'utilisateur aval) ; la fenêtre
  exacte est toujours dans `sampling_period`.
- Fan-out : `_month` (12 sorties), `_season` (4 sorties DJF/MAM/JJA/SON).

## 6. Extensions CARD : préfixes-opérateurs et suffixes

Oberlin note les objets statistiques en fonctions : m(v), s(v),
F(QJXH). CARD les note en **préfixes**, avec une convention à deux
niveaux déjà quasi systématique dans le corpus, qu'on érige en règle :

**Préfixes soudés, minuscules, dérivation intra-annuelle** (le
résultat reste une série annuelle, dérivée de l'événement) :

| Préfixe | Sens | Unité induite | Exemple |
|---|---|---|---|
| t | date de | jour de l'année (is_date) | tQJXA, tVCN10 |
| dt | durée de | jour | dtLF, dtFlood |
| v | volume de | m³ (ou hm³) | vLF, vBF |
| f | fréquence de dépassement | sans unité (fraction) | fQ01A |
| start/end/center | position de l'événement | jour de l'année | startLF, endBF, centerLF |

**Préfixes à tiret, opérateurs `f(série) → scalaire` ou comparaison de
périodes.** Un préfixe applique une fonction **par-dessus une série
par-année déjà nommée**, et la réduit à un scalaire (ou compare deux
périodes). Il ne modifie jamais *comment* la variable de base est
construite :

| Préfixe | Sens | Exemple |
|---|---|---|
| median- / mean- | médiane / moyenne inter-annuelle **d'une série** | median-tVCN10, mean-QA |
| alpha- | pente de tendance (Sen) | alpha-QJXA |
| hyp- | test de stationnarité (Mann-Kendall) | hyp-alpha-QA |
| delta- | changement entre période historique et horizon | delta-QA_H |
| n- | dénombrement d'années satisfaisant un critère | n-VCN10-5_H |

Lecture par composition, de gauche à droite = de l'extérieur vers
l'intérieur : `median-tVCN10` = médiane inter-annuelle ( date de (
minimum annuel ( moyenne mobile 10 j ( Q )))).

**Ne pas confondre le préfixe `median-` et le jeton `D` (§4).** Le
préfixe est un `f(x)` posé sur une série : `median-tVCN10` = médiane de
la série `tVCN10`, résultat scalaire. Le jeton `D` est la statistique
**intrinsèque** qui construit la variable : `QJD` est le régime médian,
pas « la médiane de `QJ` » (prendre la médiane d'un régime moyen n'a pas
de sens). D'où deux objets bien distincts, jamais synonymes : `QDA`
(médiane des jours de l'année → série) contre `median-QA` (médiane sur
les années de la série `QA` → scalaire). La forme (`curve`/`scalar`)
lève toute ambiguïté.

**Suffixes** (dans cet ordre s'ils se cumulent) :

| Suffixe | Sens | Exemple |
|---|---|---|
| -k | période de retour k ans (Oberlin : (T)) | QJXA-10, VCN10-5, QMNA-5 |
| _summer / _winter / _JJASO | saison restreinte (§5) | VCN10_summer |
| _H, _H0..H3 | horizons de projection (spécifique CARD) | delta-QA_H, FDC_H0 |
| _month / _season | fan-out (§5) | QMA_month |

## 7. Règles de rédaction des métadonnées

- **R1 : name hiérarchisé.** La périphrase suit l'ordre des positions :
  grandeur → durée/pdt → représentativité → saison → retour → opérateur.
  Gabarits :
  - série : « Minimum annuel du débit moyen sur 10 jours » (VCN10) ;
  - retour : « ... de période de retour 5 ans » (VCN10-5) ;
  - delta : « Changement moyen de X entre l'horizon {proche|moyen|
    lointain} et la période historique » (delta-X_H).
- **R2 : « moyenne » sans ambiguïté** (variante pédagogique de la
  règle d'Oberlin, arbitrée le 2026-07-15) : les séries gardent
  « moyen(ne) » au sens intra-pdt (« Débit moyen annuel »), mais tout
  agrégat inter-annuel (mean-, median-, et leurs descriptions) dit
  explicitement « inter-annuel(le) » : mean-QA = « Moyenne
  inter-annuelle du débit annuel ». Jamais « moyenne annuelle » seul
  pour un objet inter-annuel.
- **R3 : probabilités.** Un quantile temporel se dit « débit
  (journalier) dépassé p % du temps », jamais « X années sur Y »
  (confusion avec la période de retour, cf. audit A1 et l'encadré
  d'Oberlin sur la confusion des Q). Une période de retour se dit « de
  période de retour k ans » et se sigle en suffixe -k ; le sens
  (dépassement pour les crues, non-dépassement pour les étiages) suit
  la représentativité X/N (F1 vs F chez Oberlin).
- **R4 : rôle des trois champs.** `name` = périphrase R1, complète et
  autoporteuse ; `description` = définition de la variate pour
  l'utilisateur aval (ce que c'est, à quoi ça sert), remplie seulement
  si elle apporte plus que le name ; `method` = recette du process,
  mécanique (« 1. agrégation ... - fonction »), **toujours
  remplissable** donc à remplir partout (décision utilisateur, note du
  2026-07-13).
- **R5 : l'unité découle de la nature** (1re caractéristique
  d'Oberlin) : fraction/ratio → sans unité ; date → jour de l'année ;
  durée → jour ; volume → m³/hm³ ; delta `relative: true` → % ;
  delta `relative: false` → unité de la variable. Toute incohérence
  unit/relative se résout par cette règle (audit B).
- **R6 : la fonction fait foi.** Les métadonnées décrivent le calcul
  réellement exécuté par le process, jamais l'intention initiale
  (décision utilisateur : « c'est la fonction qui fait foi », audit
  A3/A6). Si l'intention diverge du calcul, on corrige la métadonnée ;
  changer le calcul est un acte séparé, arbitré, qui casse la parité R.
- **R7 : parallélisme en/fr.** Les deux langues portent la même
  information, structure identique ; dates MM-DD en anglais, DD-MM en
  français ; sentence case partout.

## 7 bis. `relative` : ce que la grandeur autorise

Champ de `meta.global`, une valeur par variable produite. Il répond à une
seule question : **cette grandeur admet-elle une expression relative**,
c'est-à-dire un pourcentage.

C'est une propriété de la GRANDEUR MESURÉE, pas de la variable publiée ni
de la fonction qui la consomme. `delta-VCN10` s'affiche en pourcentage,
et son `relative: true` ne parle pas de ce pourcentage : il parle de
`VCN10`. Les variables dérivées héritent donc de leur base.

Le champ est un **raccourci volontaire** : la variable annonce ce qu'elle
permet, pour que `stase.trend`, une figure ou l'API n'aient pas à
raisonner sur l'unité chacune de leur côté. Le kwarg `relative` de la
fonction `delta` exprime la MÊME propriété, du côté du calcul plutôt que
de la déclaration : mesuré le 2026-08-13, les deux s'accordaient déjà 77
fois sur 82, et les 5 écarts étaient des erreurs.

### Les trois valeurs

| valeur | sens | exemples |
|---|---|---|
| `true` | la grandeur admet une expression relative | débits, volumes, écarts en % |
| `false` | non | dates, durées, températures, indices sans dimension |
| `null` | la question ne se pose pas, ce n'est pas une grandeur mesurée | verdict d'un test de Mann-Kendall, test de robustesse |

**Il s'écrit toujours**, `true` compris, et le linter l'exige. Voir la
règle des défauts dans le CLAUDE.md : tant que `true` n'était qu'un défaut
jamais écrit, un choix ne se distinguait pas d'un oubli.

### Ce qui décide

Deux conditions, toutes deux nécessaires pour `true`.

**Un zéro vrai.** Une échelle d'intervalle a un zéro conventionnel : le
jour de l'année part du 1er janvier, le °C du point de fusion de l'eau.
Un pourcentage y est mathématiquement vide.

**Une dépendance à la taille du bassin.** Un débit ou un volume ne se
comparent entre le Rhône et un ruisseau qu'en relatif. Une lame d'eau en
mm est déjà divisée par la surface, une durée en jours ne dépend pas du
bassin : leur valeur absolue est directement comparable, et le
pourcentage n'apporte rien.

En pratique, **tout ce qui se mesure en temps est `false`** : un jour,
une date, une durée, un nombre d'années de dépassement, une période de
retour. « Elle augmente d'un an tous les dix ans » se lit ; « elle
augmente de 3 % par an » ne se lit pas.

Et ce qui est déjà sans dimension est `false` : élasticités, critères de
performance, indices, rapports. Pour une élasticité ou une pente il y a
une raison de plus, qui n'est pas conventionnelle : elles peuvent être
négatives ou passer par zéro, donc diviser par leur moyenne fait exploser
le résultat.

### Vérification

L'unité détermine la propriété. La table `_UNITE_RELATIVE` de
`src/card/schema.py` la porte, et le linter refuse une fiche qui s'en
écarte comme une unité qu'elle ne classe pas. Cette table ne REMPLACE pas
le champ, sans quoi le raccourci disparaîtrait et chaque consommateur
devrait refaire le raisonnement : elle le vérifie.

## 8. Ancrages externes

- **SANDRE / eaufrance** : pour les grandeurs normalisées françaises
  (QMNA, VCNd, module...), reprendre les libellés officiels quand ils
  existent et citer l'identifiant dans `description`.
- **ETCCDI / climdex** : les indices climat (CDD, CWD, RXkday...) ont
  des définitions internationales ; citer l'identifiant climdex dans la
  `description` des fiches dtCDD*, dtCWD*, RCXA*, dtR*mm*.
- **OMM** : norme N/X de la représentativité (§4) ; le glossaire
  international d'hydrologie OMM/AISH peut servir de source de
  définitions pour `description`.
- Le futur export SKOS vers un thésaurus (différé, décision
  2026-07-12) prendra cette grammaire comme base : chaque position du
  sigle devient une facette du concept.

## 9. Arbitrages rendus (utilisateur, 2026-07-15)

Le guide est **validé** avec les décisions suivantes :

1. **R2 pédagogique** : on garde « moyen(ne) » dans les name de séries
   (« Débit moyen annuel »), et les opérateurs mean-/median- disent
   systématiquement « inter-annuel(le) » pour lever l'ambiguïté.
2. **QJC** : le mot « caractéristique » (flou) n'apparaît jamais dans
   les name, comme le C de VCN10 ne s'y prononce pas. Le sigle est
   défini une fois pour toutes : **QJCd = régime journalier
   inter-annuel lissé sur d jours** ; name « Régime journalier
   inter-annuel lissé sur d jours », détail en description (agrégation
   par jour de l'année sur toute la chronique, moyenne mobile centrée
   d jours, 365 valeurs).
3. **R pour les précipitations** : assumé : c'est le standard
   climatologique ; divergence avec Oberlin (P) documentée ici et en
   tête de CARDS.md.
4. **fQ*A (audit B2)** : le calcul retourne la fraction n/N (2 jours
   dépassés sur 365 → 0,0055 : la division par N fait disparaître les
   jours). Par R6 : unité « sans unité », name « Fréquence de
   dépassement... ». La grandeur « nombre de jours de dépassement par
   an » serait n *sans* diviser (famille **DC, durées cumulées**
   d'Oberlin, côté préfixe `dt`, pas `n-` qui compte des années) :
   fiches à créer plus tard si le besoin se confirme, fQ*A inchangé.
5. **Multi-horizons (audit C1)** : listes explicites de 3 (pas de
   template `{horizon}`).
6. **STD → `STD_ratio`** (audit A3) : sd(sim)/sd(obs), sans unité,
   c'est la composante α du KGE (Gupta et al. 2009, à citer en
   description). Changement d'id et de sortie accepté, tracé dans
   RENAMING.md.
7. **Métadonnées listes : seulement pour de vraies variables
   distinctes** (précision du 2026-07-16, sur retour utilisateur).
   Une fiche dont les colonnes de sortie sont les *coordonnées d'un
   même objet* (FDC : `FDC_p`/`FDC_Q` = le x et le y de la courbe)
   garde un `variable`/`name`/`unit` **uniques** : le name nomme la
   variate, pas les axes ; les colonnes sont expliquées en
   `description`. Les listes restent la règle quand les sorties sont
   des variables différentes (alpha- : pente + test ; RA_all : trois
   cumuls).
8. **Rc → `QR_ratio`** (audit A6) : le calcul ΣQ/ΣR est conservé tel
   quel sous un nom honnête (« Rapport des cumuls débit sur
   précipitations », m³·s⁻¹·mm⁻¹), proportionnel au coefficient de
   ruissellement via la surface, adapté au suivi temporel d'une
   station. L'id **Rc est réservé** à une future fiche « vrai
   coefficient de ruissellement » adimensionnel :
   C = 86,4 × (ΣQ/ΣR) / A(km²), avec la surface fournie en colonne
   constante d'entrée (convention : colonne `S`).
