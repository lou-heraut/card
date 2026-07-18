# CHANTIERS — pistes ouvertes (mise à jour 2026-07-18)

Registre des chantiers non commencés ou différés. Un chantier terminé
sort de ce fichier (l'historique est dans git).

Sorti le 2026-07-18 : « card-api : suivi des jobs, identité et RGPD »
(jetons hachés affichés une fois, préfixe pseudonyme dans le journal
et sur les jobs, GET /v1/jobs par clé, tickets 64 bits, mention RGPD
dans le template d'issue ; clés conservées tant qu'actives, effacées
à la révocation).

## 2. Références bibliographiques externes dans les fiches

Ancrer les fiches standardisées sur leurs références : identifiants
climdex/ETCCDI (RCXA1 ↔ RX1day, RCXA5 ↔ RX5day, dtCDDA ↔ CDD,
dtCWDA ↔ CWD...), libellés SANDRE/eaufrance (QMNA, VCNd, module).
**À retravailler avec le système de biblio scientifique existant de
l'utilisateur** (ne pas inventer un format de citation avant d'avoir
vu le sien).

## 3. Lint temps réel sous Emacs

Objectif : valider les YAML pendant l'édition. Deux voies :
- générer un **JSON Schema** des fiches (depuis schema.py) et brancher
  `yaml-language-server` (paquet Emacs `lsp-mode` ou `eglot`) — la voie
  standard, autocomplétion incluse ;
- ou un checker flycheck maison qui appelle
  `python -m card.schema <fichier>` (déjà supporté en CLI, plus simple
  mais sans autocomplétion).

## 4. Revue de code du package (lisibilité, dé-boîte-noire)

Crainte utilisateur : code trop compliqué/alambiqué par endroits.
À son initiative, mais aides possibles : un `docs/dev/ARCHITECTURE.md`
qui explique le pipeline en langage simple (loader → stase →
compactage), et une passe de simplification ciblée (/simplify) sur
extraction.py qui concentre la complexité (kwargs-colonnes, sparse,
fan-out).

## 5. Documentation utilisateur étendue

- README : section « développer sa fiche » faite (copy_cards →
  extract(path=...) → python -m card.schema) ; à étoffer d'un exemple
  complet de fiche commentée ligne à ligne ?
- Pages : tutoriel pas-à-pas avec données réelles (lié au chantier 1 ?).

## 6. Export SKOS / thésaurus (différé de longue date)

La classification (docs/dev/TOPICS.md) fournit désormais les concepts
et les paires en/fr — chaque facette devient un concept scheme.
Réévaluer quand le besoin Skosmos se concrétise.

## 7. Fiches futures

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

## 8. Palettes : questions ouvertes (2026-07-18)

État : les fiches à grandeur non ambiguë sont toutes équipées (héritage
de la fiche mère ; voir RENAMING.md 2026-07-18 pour l'orientation ETP).
Quatre palettes sémantiques en usage : marron→vert (quantités d'eau),
bleu→rouge (température), violet→orange (dates et durées de crue),
vert→marron (durées/volumes d'étiage, ETP : assèchement).

- **Scores de performance et indices sans unité** (KGE, NSE et
  variantes, Bias, STD_ratio, epsilon_R/T, RAT_*, QR_ratio, RA_ratio,
  BFI-LH/Wal et leurs deltas, BFM, a-FDC) : laissés sans palette
  volontairement. Si on les équipe un jour, il faudra une palette
  divergente centrée sur la valeur de référence (1 pour KGE/NSE, 0 pour
  les deltas de BFI), décision non prise.
- **dtFlood** : partage la palette violet→orange avec les dates, et non
  la palette d'assèchement de dtLF/dtBF. Examiné le 2026-07-18 et
  conservé : une durée de crue représente un risque (dégâts), pas un
  assèchement, et une crue plus longue n'est pas « plus d'eau » ; la
  dynamique diffère de celle des étiages. Si on veut un jour distinguer
  le risque de crue des dates par une palette dédiée, c'est une
  décision à part.

## 9. Multi-seuils réglementaires : remise à plat suffix/renommage

Contexte à relire ENTIER avant toute reprise (épisode du 2026-07-18,
implémentation faite puis RETIRÉE le même jour à la demande de
l'utilisateur, pour être reconçue posément).

**Objectif sous-jacent.** Les fiches rp-VCN10, rp-VCN30, rp-QMNA
(créées et conservées, fonctionnelles) donnent la période de retour
d'UN débit seuil réglementaire par station, passé en colonne constante
Q_lim. Dans la pratique une station a PLUSIEURS seuils (DOE, DCR,
alerte, alerte renforcée...) et on veut toutes les périodes de retour
en un appel, avec des noms de sortie déterministes (sinon chacun
relance l'extraction par seuil et renomme à sa façon, exactement ce
qu'un corpus normalisé doit empêcher). La valeur d'un seuil étant
propre à chaque station, elle ne peut pas vivre dans l'id d'une fiche
(contrairement au « 5 » de VCN10-5, constante du corpus) : le nom de
sortie doit venir d'un suffixe dérivé des données ou d'un mécanisme
d'appel.

**Ce qui a été tenté puis retiré.** Un « fan-out » dans card.extract :
plusieurs colonnes associées à la même variable d'entrée via le
paramètre rename= existant (rename={"Q_DOE": "Q_lim", "Q_DCR":
"Q_lim"}) exécutaient les fiches une fois par colonne avec sorties et
métadonnées suffixées d'après la colonne source (rp-VCN10_DOE...).
Ça fonctionnait (aller-retour exact, card.trend enchaînait dessus,
test d'intégration vert) mais c'était conçu SANS avoir inventorié le
mécanisme suffix historique : risque de réinvention et de double
grammaire. Retiré de extraction.py, du README, des tests et de
RENAMING.md ; récupérable dans l'historique de conversation ou
réimplémentable, mais pas avant l'inventaire ci-dessous.

**Inventaire à faire avant de reconcevoir** (personne ne se fie à sa
mémoire, la mienne comme celle de l'utilisateur) :
- R EXstat, process_extraction : paramètre suffix= documenté
  (EXstat_project/EXstat/R/process_extraction.R, @param suffix
  vers les lignes 68-69, exemple vers 202-212) : funct=list(QA=mean) +
  funct_args=list("Q") + suffix=c("obs","sim") lit Q_obs et Q_sim et
  sort QA_obs, QA_sim ; le suffixe s'applique à TOUTES les colonnes
  référencées, plus expand= pour éclater par suffixe.
- stase : au grep du 2026-07-18, suffix= n'existe QUE dans stase.trend
  (retrait des suffixes pour regrouper les extrêmes et consulter meta,
  porté de process_trend R). PAS trouvé dans stase.process_extraction.
  MAIS l'utilisateur se souvient d'un suffix implémenté et testé côté
  stase pour déployer un calcul sur plusieurs colonnes proches :
  vérifier l'historique git de stase et d'EXstat avant de conclure.
- Suffixes structurels existants à ne pas percuter : compress
  (_DJF, _jan...), horizons (_H1..), saisons de fiches (_summer...).

**Contraintes dégagées pour la conception :**
- le suffix= R suffixe toutes les colonnes référencées ; le cas
  multi-seuils ne fait varier QUE Q_lim pendant que Q reste fixe, et
  les colonnes réelles s'appellent Q_DOE (pas Q_lim_DOE) : le
  mécanisme R ne couvre donc pas ce cas tel quel ;
- il faut UNE seule grammaire cohérente entre l'extraction (ajout de
  suffixes) et stase.trend (retrait de suffixes), pas deux
  vocabulaires ;
- l'idée d'associer les colonnes de seuils à la variable d'entrée via
  rename= plaisait en surface à l'utilisateur ; la piste « porter
  suffix= dans stase.process_extraction pour la parité R puis faire
  déléguer card » est l'alternative à évaluer ;
- sorties NaN quand le seuil est hors du support de la loi (validé) ;
  une seule variable en fan-out par appel si ce mécanisme revient
  (pas de produit cartésien).
