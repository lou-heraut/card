> **Statut : norme en vigueur.** Seule référence pour nommer une
> variable et rédiger ses métadonnées. Toute correction de fiche cite la
> règle qu'elle applique.

# NOMENCLATURE — Guide de nommage des variables CARD

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

## 2. Position 1 — Grandeur

| Sigle CARD | Grandeur | Note vs Oberlin |
|---|---|---|
| Q | débit | conforme |
| R (Rl, Rs) | précipitations (liquides, solides) | **divergence assumée** : Oberlin utilise P (pluie) et réserve R aux stocks/réservoirs. CARD garde R (convention historique du corpus), à documenter en tête de CARDS.md |
| T | température | conforme |
| ETP | évapotranspiration potentielle | conforme (E + indices TP) |
| BF | débit de base (baseflow) | extension CARD (Oberlin : indice b sur Q) |
| LF | basses eaux (low flows, événement) | extension CARD |

Cas à part : les **critères de performance** (NSE, KGE, Bias, STD) et
de **sensibilité climatique** (epsilon_*, RAT_*, Rc) ne sont pas des
variates hydrologiques au sens d'Oberlin mais des scores ou indices
adimensionnels ; ils forment un espace de noms séparé et ne suivent pas
les positions 2–4.

## 3. Position 2 — Pas de temps ou durée

| Sigle | Sens | Exemples |
|---|---|---|
| A | année (pdt annuel) | QA, RA, TA |
| M | mois | QMNA, QMA_month, TMA_month |
| S | saison (pdt saisonnier) | QSA_season, TSA_season, RSA_season |
| J | jour | QJXA, median-QJ |
| I | instantané | (réservé, non utilisé actuellement) |
| *k* en suffixe de VCN/VCX | durée mobile continue de k jours | VCN10, VCX3 |

Les **VCNd / VCXd** sont les « variates spécialisées » d'Oberlin :
V = valeur moyenne sur une durée continue (Volume), C =
Caractéristique, N/X = représentativité, d = durée en jours. Même
famille : DC (durées cumulées) et QC (débits-seuils), disponibles si
besoin futur.

Par analogie, **QJC** (QJC10, median-QJC5) se lit « débit Journalier
Caractéristique » : le régime inter-annuel par jour de l'année, lissé
sur d jours. ⚠️ Interprétation à confirmer par l'utilisateur — si c'est
bien cela, le `name` de QJC10 (« débit moyen mensuel... », faux, cf.
audit A4) devient « Régime journalier inter-annuel lissé sur 10 jours ».

Indices climatologiques (dtCDD, dtCWD, RCXA, dtRA01mm...) : la grandeur
et la durée sont dans le sigle ETCCDI d'origine (CDD = consecutive dry
days) ; on conserve les sigles internationaux tels quels (cf. §8).

## 4. Position 3 — Représentativité

Norme OMM reprise par Oberlin, seuls deux cas existent :

- **X** = maXimal(e) — QJXA, VCX10, RCXA5
- **N** = miNimal(e) — QMNA, VCN10, QNA

**Absence de lettre = intégrale/moyenne triviale sur le pas de temps**
(QA, QM, RA). C'est le corollaire de la règle « moyenne » : ne jamais
écrire de lettre ni de mot pour la moyenne intra-pdt.

## 5. Position 4 — Saison d'échantillonnage

- **A** = année (saison par défaut des extrêmes) : QJXA, QMNA, VCN10
  (le A est implicite dans VCN10 — usage national conservé).
- CARD exprime les saisons restreintes par **suffixe explicite** plutôt
  que par lettre Oberlin (Sh, Se) : `_summer`, `_winter`, `QSA_JJASO`.
  Divergence assumée (lisibilité pour l'utilisateur aval) ; la fenêtre
  exacte est toujours dans `sampling_period`.
- Fan-out : `_month` (12 sorties), `_season` (4 sorties DJF/MAM/JJA/SON).

## 6. Extensions CARD — préfixes-opérateurs et suffixes

Oberlin note les objets statistiques en fonctions : m(v), s(v),
F(QJXH). CARD les note en **préfixes**, avec une convention à deux
niveaux déjà quasi systématique dans le corpus, qu'on érige en règle :

**Préfixes soudés, minuscules — dérivation intra-annuelle** (le
résultat reste une série annuelle, dérivée de l'événement) :

| Préfixe | Sens | Unité induite | Exemple |
|---|---|---|---|
| t | date de | jour de l'année (is_date) | tQJXA, tVCN10 |
| dt | durée de | jour | dtLF, dtFlood |
| v | volume de | m³ (ou hm³) | vLF, vBF |
| f | fréquence de dépassement | sans unité (fraction) | fQ01A |
| start/end/center | position de l'événement | jour de l'année | startLF, endBF, centerLF |

**Préfixes à tiret — opérateurs inter-annuels ou inter-périodes** (le
résultat réduit la série annuelle à un scalaire ou compare des
périodes) :

| Préfixe | Sens | Exemple |
|---|---|---|
| median- / mean- | médiane / moyenne inter-annuelle | median-tVCN10, mean-QA |
| alpha- | pente de tendance (Sen) | alpha-QJXA |
| hyp- | test de stationnarité (Mann-Kendall) | hyp-alpha-QA |
| delta- | changement entre période historique et horizon | delta-QA_H |
| n- | dénombrement d'années satisfaisant un critère | n-VCN10-5_H |

Lecture par composition, de gauche à droite = de l'extérieur vers
l'intérieur : `median-tVCN10` = médiane inter-annuelle ( date de (
minimum annuel ( moyenne mobile 10 j ( Q )))).

**Suffixes** (dans cet ordre s'ils se cumulent) :

| Suffixe | Sens | Exemple |
|---|---|---|
| -k | période de retour k ans (Oberlin : (T)) | QJXA-10, VCN10-5, QMNA-5 |
| _summer / _winter / _JJASO | saison restreinte (§5) | VCN10_summer |
| _H, _H0..H3 | horizons de projection (spécifique CARD) | delta-QA_H, FDC_H0 |
| _month / _season | fan-out (§5) | QMA_month |

## 7. Règles de rédaction des métadonnées

- **R1 — name hiérarchisé.** La périphrase suit l'ordre des positions :
  grandeur → durée/pdt → représentativité → saison → retour → opérateur.
  Gabarits :
  - série : « Minimum annuel du débit moyen sur 10 jours » (VCN10) ;
  - retour : « ... de période de retour 5 ans » (VCN10-5) ;
  - delta : « Changement moyen de X entre l'horizon {proche|moyen|
    lointain} et la période historique » (delta-X_H).
- **R2 — « moyenne » sans ambiguïté** (variante pédagogique de la
  règle d'Oberlin, arbitrée le 2026-07-15) : les séries gardent
  « moyen(ne) » au sens intra-pdt (« Débit moyen annuel »), mais tout
  agrégat inter-annuel (mean-, median-, et leurs descriptions) dit
  explicitement « inter-annuel(le) » : mean-QA = « Moyenne
  inter-annuelle du débit annuel ». Jamais « moyenne annuelle » seul
  pour un objet inter-annuel.
- **R3 — probabilités.** Un quantile temporel se dit « débit
  (journalier) dépassé p % du temps » — jamais « X années sur Y »
  (confusion avec la période de retour, cf. audit A1 et l'encadré
  d'Oberlin sur la confusion des Q). Une période de retour se dit « de
  période de retour k ans » et se sigle en suffixe -k ; le sens
  (dépassement pour les crues, non-dépassement pour les étiages) suit
  la représentativité X/N (F1 vs F chez Oberlin).
- **R4 — rôle des trois champs.** `name` = périphrase R1, complète et
  autoporteuse ; `description` = définition de la variate pour
  l'utilisateur aval (ce que c'est, à quoi ça sert) — remplie seulement
  si elle apporte plus que le name ; `method` = recette du process,
  mécanique (« 1. agrégation ... - fonction »), **toujours
  remplissable** donc à remplir partout (décision utilisateur, note du
  2026-07-13).
- **R5 — l'unité découle de la nature** (1re caractéristique
  d'Oberlin) : fraction/ratio → sans unité ; date → jour de l'année ;
  durée → jour ; volume → m³/hm³ ; delta `relative: true` → % ;
  delta `relative: false` → unité de la variable. Toute incohérence
  unit/relative se résout par cette règle (audit B).
- **R6 — la fonction fait foi.** Les métadonnées décrivent le calcul
  réellement exécuté par le process, jamais l'intention initiale
  (décision utilisateur : « c'est la fonction qui fait foi », audit
  A3/A6). Si l'intention diverge du calcul, on corrige la métadonnée ;
  changer le calcul est un acte séparé, arbitré, qui casse la parité R.
- **R7 — parallélisme en/fr.** Les deux langues portent la même
  information, structure identique ; dates MM-DD en anglais, DD-MM en
  français ; sentence case partout.

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
   les name — comme le C de VCN10 ne s'y prononce pas. Le sigle est
   défini une fois pour toutes : **QJCd = régime journalier
   inter-annuel lissé sur d jours** ; name « Régime journalier
   inter-annuel lissé sur d jours », détail en description (agrégation
   par jour de l'année sur toute la chronique, moyenne mobile centrée
   d jours, 365 valeurs).
3. **R pour les précipitations** : assumé — c'est le standard
   climatologique ; divergence avec Oberlin (P) documentée ici et en
   tête de CARDS.md.
4. **fQ*A (audit B2)** : le calcul retourne la fraction n/N (2 jours
   dépassés sur 365 → 0,0055 : la division par N fait disparaître les
   jours). Par R6 : unité « sans unité », name « Fréquence de
   dépassement... ». La grandeur « nombre de jours de dépassement par
   an » serait n *sans* diviser (famille **DC — durées cumulées**
   d'Oberlin, côté préfixe `dt`, pas `n-` qui compte des années) :
   fiches à créer plus tard si le besoin se confirme, fQ*A inchangé.
5. **Multi-horizons (audit C1)** : listes explicites de 3 (pas de
   template `{horizon}`).
6. **STD → `STD_ratio`** (audit A3) : sd(sim)/sd(obs), sans unité —
   c'est la composante α du KGE (Gupta et al. 2009, à citer en
   description). Changement d'id et de sortie accepté, tracé dans
   RENAMING.md.
7. **Métadonnées listes : seulement pour de vraies variables
   distinctes** (précision du 2026-07-16, sur retour utilisateur).
   Une fiche dont les colonnes de sortie sont les *coordonnées d'un
   même objet* (FDC : `FDC_p`/`FDC_Q` = le x et le y de la courbe)
   garde un `variable`/`name`/`unit` **uniques** — le name nomme la
   variate, pas les axes ; les colonnes sont expliquées en
   `description`. Les listes restent la règle quand les sorties sont
   des variables différentes (alpha- : pente + test ; RA_all : trois
   cumuls).
8. **Rc → `QR_ratio`** (audit A6) : le calcul ΣQ/ΣR est conservé tel
   quel sous un nom honnête (« Rapport des cumuls débit sur
   précipitations », m³·s⁻¹·mm⁻¹), proportionnel au coefficient de
   ruissellement via la surface — adapté au suivi temporel d'une
   station. L'id **Rc est réservé** à une future fiche « vrai
   coefficient de ruissellement » adimensionnel :
   C = 86,4 × (ΣQ/ΣR) / A(km²), avec la surface fournie en colonne
   constante d'entrée (convention : colonne `S`).
