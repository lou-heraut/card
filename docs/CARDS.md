# Catalogue des fiches CARD

226 fiches, 602 variables. Généré par `scripts/generate_catalog.py`, ne pas éditer à la main.

Chaque fiche s'exécute via `card.extract(data, cards=[...])` ; la colonne *entrées* indique les colonnes que `data` doit contenir (cf. `rename=` pour la correspondance). Détail d'une fiche : `card.info("nom")`.

## Evapotranspiration

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [ETPA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Evapotranspiration/ETPA.yaml) | ETPA | Cumul annuel de l'évapotranspiration potentielle | mm | ETP |  |

## Flow / Baseflow / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [BFI-LH](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/BFI-LH.yaml) | BFI-LH | Indice de débit de base (Lyne et Hollick) | without unit | Q |  |
| [BFI-Wal](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/BFI-Wal.yaml) | BFI-Wal | Indice de débit de base (Wallingford) | without unit | Q |  |
| [BFM](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/BFM.yaml) | BFM | Magnitude du débit de base | without unit | Q |  |
| [delta-BFI-LH_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-BFI-LH_H.yaml) | delta-BFI-LH_H1, delta-BFI-LH_H2, delta-BFI-LH_H3 | Changement moyen de l'indice de débit de base entre l'horizon proche et la période historique (Lyne et Hollick) | without unit | Q |  |
| [delta-BFI-Wal_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-BFI-Wal_H.yaml) | delta-BFI-Wal_H1, delta-BFI-Wal_H2, delta-BFI-Wal_H3 | Changement moyen de l'indice de débit de base entre l'horizon proche et la période historique (Wallingford) | without unit | Q |  |
| [delta-centerBF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-centerBF_H.yaml) | delta-centerBF_H1, delta-centerBF_H2, delta-centerBF_H3 | Changement moyen du centre des écoulements lents entre l'horizon proche et la période historique | day | Q |  |
| [delta-dtBF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-dtBF_H.yaml) | delta-dtBF_H1, delta-dtBF_H2, delta-dtBF_H3 | Changement moyen de la durée des écoulements lents entre l'horizon proche et la période historique | day | Q |  |
| [delta-endBF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-endBF_H.yaml) | delta-endBF_H1, delta-endBF_H2, delta-endBF_H3 | Changement moyen de la fin des écoulements lents entre l'horizon proche et la période historique | day | Q |  |
| [delta-startBF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-startBF_H.yaml) | delta-startBF_H1, delta-startBF_H2, delta-startBF_H3 | Changement moyen du début des écoulements lents entre l'horizon proche et la période historique | day | Q |  |
| [delta-vBF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/delta-vBF_H.yaml) | delta-vBF_H1, delta-vBF_H2, delta-vBF_H3 | Changement moyen du volume annuel généré par le débit de base entre l'horizon proche et la période historique | % | Q |  |
| [median-centerBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/median-centerBF.yaml) | median-centerBF | Médiane inter-annuelle du centre des écoulements lents | yearday | Q |  |
| [median-dtBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/median-dtBF.yaml) | median-dtBF | Médiane inter-annuelle de la durée des écoulements lents | day | Q |  |
| [median-endBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/median-endBF.yaml) | median-endBF | Médiane inter-annuelle de la fin des écoulements lents | yearday | Q |  |
| [median-startBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/median-startBF.yaml) | median-startBF | Médiane inter-annuelle du début des écoulements lents | yearday | Q |  |
| [median-vBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/criteria/median-vBF.yaml) | median-vBF | Médiane inter-annuelle du volume annuel généré par les écoulements lents | hm^{3} | Q |  |

## Flow / Baseflow / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [BF-LH](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/BF-LH.yaml) | BF-LH | Débit de base (Lyne et Hollick) | m^{3}.s^{-1} | Q |  |
| [centerBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/centerBF.yaml) | centerBF | Centre des écoulements lents | yearday | Q |  |
| [dtBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/dtBF.yaml) | dtBF | Durée des écoulements lents | day | Q |  |
| [endBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/endBF.yaml) | endBF | Fin des écoulements lents | yearday | Q |  |
| [startBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/startBF.yaml) | startBF | Début des écoulements lents | yearday | Q |  |
| [vBF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Baseflow/serie/vBF.yaml) | vBF | Volume annuel généré par le débit de base | hm^{3} | Q |  |

## Flow / High Flows / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Q10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/Q10.yaml) | Q10 | Débit journalier dépassé 10 % du temps (chronique entière) | m^{3}.s^{-1} | Q |  |
| [QJXA-10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/QJXA-10.yaml) | QJXA-10 | Débit journalier maximal annuel de période de retour 10 ans | m^{3}.s^{-1} | Q |  |
| [alpha-QJXA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/alpha-QJXA.yaml) | alpha-QJXA, hyp-alpha-QJXA | Pente de Sen de la série des débits journaliers maximaux annuels (QJXA) | m^{3}.s^{-1}.year^{-1} | Q |  |
| [delta-Q01A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-Q01A_H.yaml) | delta-Q01A_H1, delta-Q01A_H2, delta-Q01A_H3 | Changement moyen du débit journalier dépassé 1 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q05A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-Q05A_H.yaml) | delta-Q05A_H1, delta-Q05A_H2, delta-Q05A_H3 | Changement moyen du débit journalier dépassé 5 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q10A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-Q10A_H.yaml) | delta-Q10A_H1, delta-Q10A_H2, delta-Q10A_H3 | Changement moyen du débit journalier dépassé 10 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-QJXA-10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-QJXA-10_H.yaml) | delta-QJXA-10_H1, delta-QJXA-10_H2, delta-QJXA-10_H3 | Changement du débit journalier maximal annuel de période de retour 10 ans entre l'horizon proche et la période historique | % | Q |  |
| [delta-QJXA_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-QJXA_H.yaml) | delta-QJXA_H1, delta-QJXA_H2, delta-QJXA_H3 | Changement moyen du débit journalier maximal annuel entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCX10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-VCX10_H.yaml) | delta-VCX10_H1, delta-VCX10_H2, delta-VCX10_H3 | Changement moyen du maximum annuel de la moyenne mobile sur 10 jours des débits journaliers entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCX3_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-VCX3_H.yaml) | delta-VCX3_H1, delta-VCX3_H2, delta-VCX3_H3 | Changement moyen du maximum annuel de la moyenne mobile sur 3 jours des débits journaliers entre l'horizon proche et la période historique | % | Q |  |
| [delta-dtFlood_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-dtFlood_H.yaml) | delta-dtFlood_H1, delta-dtFlood_H2, delta-dtFlood_H3 | Changement moyen de la durée des crues entre l'horizon proche et la période historique | day | Q |  |
| [delta-fQ01A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-fQ01A_H.yaml) | delta-fQ01A_H1, delta-fQ01A_H2, delta-fQ01A_H3 | Changement moyen de la fréquence annuelle de dépassement du Q01 entre l'horizon proche et la période historique | without unit | Q |  |
| [delta-fQ05A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-fQ05A_H.yaml) | delta-fQ05A_H1, delta-fQ05A_H2, delta-fQ05A_H3 | Changement moyen de la fréquence annuelle de dépassement du Q05 entre l'horizon proche et la période historique | without unit | Q |  |
| [delta-fQ10A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-fQ10A_H.yaml) | delta-fQ10A_H1, delta-fQ10A_H2, delta-fQ10A_H3 | Changement moyen de la fréquence annuelle de dépassement du Q10 entre l'horizon proche et la période historique | without unit | Q |  |
| [delta-tQJXA_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-tQJXA_H.yaml) | delta-tQJXA_H1, delta-tQJXA_H2, delta-tQJXA_H3 | Changement moyen de la date du débit journalier maximal annuel entre l'horizon proche et la période historique | day | Q |  |
| [delta-tVCX10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-tVCX10_H.yaml) | delta-tVCX10_H1, delta-tVCX10_H2, delta-tVCX10_H3 | Changement moyen de la date du maximum annuel de la moyenne sur 10 jours du débit journalier entre l'horizon proche et la période historique | day | Q |  |
| [delta-tVCX3_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/delta-tVCX3_H.yaml) | delta-tVCX3_H1, delta-tVCX3_H2, delta-tVCX3_H3 | Changement moyen de la date du maximum annuel de la moyenne sur 3 jours du débit journalier entre l'horizon proche et la période historique | day | Q |  |
| [median-dtFlood](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/median-dtFlood.yaml) | median-dtFlood | Médiane inter-annuelle de la durée des crues | day | Q |  |
| [median-tQJXA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/median-tQJXA.yaml) | median-tQJXA | Médiane inter-annuelle des dates du débit journalier maximal annuel | yearday | Q |  |
| [n-QJXA-10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/criteria/n-QJXA-10_H.yaml) | n-QJXA-10_H1, n-QJXA-10_H2, n-QJXA-10_H3 | Nombre d'années de l'horizon proche où le QJXA est supérieur au QJXA-10 de la période historique | without unit | Q |  |

## Flow / High Flows / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Q01A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/Q01A.yaml) | Q01A | Débit journalier dépassé 1 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [Q05A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/Q05A.yaml) | Q05A | Débit journalier dépassé 5 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [Q10A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/Q10A.yaml) | Q10A | Débit journalier dépassé 10 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [QJXA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/QJXA.yaml) | QJXA | Débit journalier maximal annuel | m^{3}.s^{-1} | Q |  |
| [VCX10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/VCX10.yaml) | VCX10 | Maximum annuel de la moyenne mobile sur 10 jours des débits journaliers | m^{3}.s^{-1} | Q |  |
| [VCX3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/VCX3.yaml) | VCX3 | Maximum annuel de la moyenne mobile sur 3 jours des débits journaliers | m^{3}.s^{-1} | Q |  |
| [dtFlood](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/dtFlood.yaml) | dtFlood | Durée des crues | day | Q |  |
| [fQ01A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/fQ01A.yaml) | fQ01A | Fréquence annuelle de dépassement du Q01 | without unit | Q |  |
| [fQ05A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/fQ05A.yaml) | fQ05A | Fréquence annuelle de dépassement du Q05 | without unit | Q |  |
| [fQ10A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/fQ10A.yaml) | fQ10A | Fréquence annuelle de dépassement du Q10 | without unit | Q |  |
| [tQJXA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/tQJXA.yaml) | tQJXA | Date du débit journalier maximal annuel | yearday | Q |  |
| [tVCX10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/tVCX10.yaml) | tVCX10 | Date du maximum annuel de la moyenne sur 10 jours du débit journalier | yearday | Q |  |
| [tVCX3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/High_Flows/serie/tVCX3.yaml) | tVCX3 | Date du maximum annuel de la moyenne sur 3 jours du débit journalier | yearday | Q |  |

## Flow / Low Flows / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Q90](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/Q90.yaml) | Q90 | Débit journalier dépassé 90 % du temps (chronique entière) | m^{3}.s^{-1} | Q |  |
| [QMNA-5](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/QMNA-5.yaml) | QMNA-5 | Minimum annuel des débits mensuels de période de retour 5 ans | m^{3}.s^{-1} | Q |  |
| [VCN10-5](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/VCN10-5.yaml) | VCN10-5 | Minimum annuel de la moyenne sur 10 jours du débit journalier VCN10 de période de retour 5 ans | m^{3}.s^{-1} | Q |  |
| [VCN30-2](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/VCN30-2.yaml) | VCN30-2 | Minimum annuel de la moyenne sur 30 jours du débit journalier de période de retour 2 ans | m^{3}.s^{-1} | Q |  |
| [alpha-VCN10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/alpha-VCN10.yaml) | alpha-VCN10, hyp-alpha-VCN10 | Pente de Sen de la série des minimums annuels des débits moyens sur 10 jours (VCN10) | m^{3}.s^{-1}.year^{-1} | Q |  |
| [delta-Q90A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-Q90A_H.yaml) | delta-Q90A_H1, delta-Q90A_H2, delta-Q90A_H3 | Changement moyen du débit journalier dépassé 90 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q95A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-Q95A_H.yaml) | delta-Q95A_H1, delta-Q95A_H2, delta-Q95A_H3 | Changement moyen du débit journalier dépassé 95 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q99A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-Q99A_H.yaml) | delta-Q99A_H1, delta-Q99A_H2, delta-Q99A_H3 | Changement moyen du débit journalier dépassé 99 % du temps de l'année entre l'horizon proche et la période historique | % | Q |  |
| [delta-QMNA_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-QMNA_H.yaml) | delta-QMNA_H1, delta-QMNA_H2, delta-QMNA_H3 | Changement moyen du minimum annuel des débits mensuels entre l'horizon proche et la période historique | % | Q |  |
| [delta-QNA_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-QNA_H.yaml) | delta-QNA_H1, delta-QNA_H2, delta-QNA_H3 | Changement moyen du minimum annuel du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN10-5_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-VCN10-5_H.yaml) | delta-VCN10-5_H1, delta-VCN10-5_H2, delta-VCN10-5_H3 | Changement du minimum annuel de la moyenne sur 10 jours du débit journalier VCN10 de période de retour 5 ans entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-VCN10_H.yaml) | delta-VCN10_H1, delta-VCN10_H2, delta-VCN10_H3 | Changement moyen du minimum annuel de la moyenne sur 10 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN30_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-VCN30_H.yaml) | delta-VCN30_H1, delta-VCN30_H2, delta-VCN30_H3 | Changement moyen du minimum annuel de la moyenne sur 30 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN3_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-VCN3_H.yaml) | delta-VCN3_H1, delta-VCN3_H2, delta-VCN3_H3 | Changement moyen du minimum annuel de la moyenne sur 3 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-allLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-allLF_H.yaml) | delta-startLF_H1, delta-startLF_H2, delta-startLF_H3, delta-centerLF_H1, delta-centerLF_H2, delta-centerLF_H3, delta-endLF_H1, delta-endLF_H2, delta-endLF_H3, delta-dtLF_H1, delta-dtLF_H2, delta-dtLF_H3, delta-vLF_H1, delta-vLF_H2, delta-vLF_H3 | Changement moyen du début des basses eaux entre l'horizon proche et la période historique | day | Q |  |
| [delta-centerLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-centerLF_H.yaml) | delta-centerLF_H1, delta-centerLF_H2, delta-centerLF_H3 | Changement moyen du centre des basses eaux entre l'horizon proche et la période historique | day | Q |  |
| [delta-dtLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-dtLF_H.yaml) | delta-dtLF_H1, delta-dtLF_H2, delta-dtLF_H3 | Changement moyen de la durée des basses eaux entre l'horizon proche et la période historique | day | Q |  |
| [delta-endLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-endLF_H.yaml) | delta-endLF_H1, delta-endLF_H2, delta-endLF_H3 | Changement moyen de la fin des basses eaux entre l'horizon proche et la période historique | day | Q |  |
| [delta-startLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-startLF_H.yaml) | delta-startLF_H1, delta-startLF_H2, delta-startLF_H3 | Changement moyen du début des basses eaux entre l'horizon proche et la période historique | day | Q |  |
| [delta-tVCN10_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-tVCN10_H.yaml) | delta-tVCN10_H1, delta-tVCN10_H2, delta-tVCN10_H3 | Changement moyen de la date du minimum annuel des débits moyens sur 10 jours entre l'horizon proche et la période historique | day | Q |  |
| [delta-vLF_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/delta-vLF_H.yaml) | delta-vLF_H1, delta-vLF_H2, delta-vLF_H3 | Changement moyen du volume de déficit des basses eaux entre l'horizon proche et la période historique | % | Q |  |
| [median-allLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-allLF.yaml) | median-startLF, median-centerLF, median-endLF, median-dtLF, median-vLF | Médiane inter-annuelle du début des basses eaux | yearday | Q |  |
| [median-dtLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-dtLF.yaml) | median-dtLF | Médiane inter-annuelle de la durée des basses eaux | day | Q |  |
| [median-endLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-endLF.yaml) | median-endLF | Médiane inter-annuelle de la fin des basses eaux | yearday | Q |  |
| [median-startLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-startLF.yaml) | median-startLF | Médiane inter-annuelle du début des basses eaux | yearday | Q |  |
| [median-tVCN10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-tVCN10.yaml) | median-tVCN10 | Médiane inter-annuelle des dates du minimum annuel des débits moyens sur 10 jours | yearday | Q |  |
| [median-vLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/median-vLF.yaml) | median-vLF | Médiane inter-annuelle des volumes de déficit des basses eaux | hm^{3} | Q |  |
| [n-VCN10-5_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/criteria/n-VCN10-5_H.yaml) | n-VCN10-5_H1, n-VCN10-5_H2, n-VCN10-5_H3 | Nombre d'années de l'horizon proche où le VCN10 est inférieur ou égal au VCN10-5 de la période historique | without unit | Q |  |

## Flow / Low Flows / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Q90A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/Q90A.yaml) | Q90A | Débit journalier dépassé 90 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [Q95A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/Q95A.yaml) | Q95A | Débit journalier dépassé 95 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [Q99A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/Q99A.yaml) | Q99A | Débit journalier dépassé 99 % du temps de l'année | m^{3}.s^{-1} | Q |  |
| [QMNA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/QMNA.yaml) | QMNA | Minimum annuel des débits mensuels | m^{3}.s^{-1} | Q |  |
| [QNA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/QNA.yaml) | QNA | Minimum annuel du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/VCN10.yaml) | VCN10 | Minimum annuel de la moyenne sur 10 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/VCN3.yaml) | VCN3 | Minimum annuel de la moyenne sur 3 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN30](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/VCN30.yaml) | VCN30 | Minimum annuel de la moyenne sur 30 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [allLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/allLF.yaml) | startLF, centerLF, endLF, dtLF, vLF | Début des basses eaux | yearday | Q |  |
| [centerLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/centerLF.yaml) | centerLF | Centre des basses eaux | yearday | Q |  |
| [dtLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/dtLF.yaml) | dtLF | Durée des basses eaux | day | Q |  |
| [endLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/endLF.yaml) | endLF | Fin des basses eaux | yearday | Q |  |
| [startLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/startLF.yaml) | startLF | Début des basses eaux | yearday | Q |  |
| [tVCN10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/tVCN10.yaml) | tVCN10 | Date du minimum annuel des débits moyens sur 10 jours | yearday | Q |  |
| [vLF](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows/serie/vLF.yaml) | vLF | Volume de déficit des basses eaux | hm^{3} | Q |  |

## Flow / Low Flows Summer / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [delta-QMNA_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-QMNA_summer_H.yaml) | delta-QMNA_summer_H1, delta-QMNA_summer_H2, delta-QMNA_summer_H3 | Changement moyen du minimum estival des débits mensuels entre l'horizon proche et la période historique | % | Q |  |
| [delta-QNA_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-QNA_summer_H.yaml) | delta-QNA_summer_H1, delta-QNA_summer_H2, delta-QNA_summer_H3 | Changement moyen du minimum estival du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN10_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-VCN10_summer_H.yaml) | delta-VCN10_summer_H1, delta-VCN10_summer_H2, delta-VCN10_summer_H3 | Changement moyen du minimum estival de la moyenne sur 10 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN30_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-VCN30_summer_H.yaml) | delta-VCN30_summer_H1, delta-VCN30_summer_H2, delta-VCN30_summer_H3 | Changement moyen du minimum estival de la moyenne sur 30 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN3_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-VCN3_summer_H.yaml) | delta-VCN3_summer_H1, delta-VCN3_summer_H2, delta-VCN3_summer_H3 | Changement moyen du minimum estival de la moyenne sur 3 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-allLF_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-allLF_summer_H.yaml) | delta-startLF_summer_H1, delta-startLF_summer_H2, delta-startLF_summer_H3, delta-centerLF_summer_H1, delta-centerLF_summer_H2, delta-centerLF_summer_H3, delta-endLF_summer_H1, delta-endLF_summer_H2, delta-endLF_summer_H3, delta-dtLF_summer_H1, delta-dtLF_summer_H2, delta-dtLF_summer_H3, delta-vLF_summer_H1, delta-vLF_summer_H2, delta-vLF_summer_H3 | Changement moyen du début des basses eaux estivales entre l'horizon proche et la période historique | day | Q |  |
| [delta-tVCN10_summer_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/criteria/delta-tVCN10_summer_H.yaml) | delta-tVCN10_summer_H1, delta-tVCN10_summer_H2, delta-tVCN10_summer_H3 | Changement moyen de la date du minimum estival des débits moyens sur 10 jours entre l'horizon proche et la période historique | day | Q |  |

## Flow / Low Flows Summer / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [QMNA_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/QMNA_summer.yaml) | QMNA_summer | Minimum estival des débits mensuels | m^{3}.s^{-1} | Q |  |
| [QNA_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/QNA_summer.yaml) | QNA_summer | Minimum estival du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN10_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/VCN10_summer.yaml) | VCN10_summer | Minimum estival de la moyenne sur 10 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN30_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/VCN30_summer.yaml) | VCN30_summer | Minimum estival de la moyenne sur 30 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN3_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/VCN3_summer.yaml) | VCN3_summer | Minimum estival de la moyenne sur 3 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [allLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/allLF_summer.yaml) | startLF_summer, centerLF_summer, endLF_summer, dtLF_summer, vLF_summer | Début des basses eaux estivales | yearday | Q |  |
| [centerLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/centerLF_summer.yaml) | centerLF_summer | Centre des basses eaux estivales | yearday | Q |  |
| [dtLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/dtLF_summer.yaml) | dtLF_summer | Durée des basses eaux estivales | day | Q |  |
| [endLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/endLF_summer.yaml) | endLF_summer | Fin des basses eaux estivales | yearday | Q |  |
| [startLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/startLF_summer.yaml) | startLF_summer | Début des basses eaux estivales | yearday | Q |  |
| [tVCN10_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/tVCN10_summer.yaml) | tVCN10_summer | Date du minimum estival des débits moyens sur 10 jours | yearday | Q |  |
| [vLF_summer](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Summer/serie/vLF_summer.yaml) | vLF_summer | Volume de déficit des basses eaux estivales | hm^{3} | Q |  |

## Flow / Low Flows Winter / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [delta-QMNA_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-QMNA_winter_H.yaml) | delta-QMNA_winter_H1, delta-QMNA_winter_H2, delta-QMNA_winter_H3 | Changement moyen du minimum hivernal des débits mensuels entre l'horizon proche et la période historique | % | Q |  |
| [delta-QNA_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-QNA_winter_H.yaml) | delta-QNA_winter_H1, delta-QNA_winter_H2, delta-QNA_winter_H3 | Changement moyen du minimum hivernal du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN10_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-VCN10_winter_H.yaml) | delta-VCN10_winter_H1, delta-VCN10_winter_H2, delta-VCN10_winter_H3 | Changement moyen du minimum hivernal de la moyenne sur 10 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN30_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-VCN30_winter_H.yaml) | delta-VCN30_winter_H1, delta-VCN30_winter_H2, delta-VCN30_winter_H3 | Changement moyen du minimum hivernal de la moyenne sur 30 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-VCN3_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-VCN3_winter_H.yaml) | delta-VCN3_winter_H1, delta-VCN3_winter_H2, delta-VCN3_winter_H3 | Changement moyen du minimum hivernal de la moyenne sur 3 jours du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-allLF_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-allLF_winter_H.yaml) | delta-startLF_winter_H1, delta-startLF_winter_H2, delta-startLF_winter_H3, delta-centerLF_winter_H1, delta-centerLF_winter_H2, delta-centerLF_winter_H3, delta-endLF_winter_H1, delta-endLF_winter_H2, delta-endLF_winter_H3, delta-dtLF_winter_H1, delta-dtLF_winter_H2, delta-dtLF_winter_H3, delta-vLF_winter_H1, delta-vLF_winter_H2, delta-vLF_winter_H3 | Changement moyen du début des basses eaux hivernales entre l'horizon proche et la période historique | day | Q |  |
| [delta-tVCN10_winter_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/criteria/delta-tVCN10_winter_H.yaml) | delta-tVCN10_winter_H1, delta-tVCN10_winter_H2, delta-tVCN10_winter_H3 | Changement moyen de la date du minimum hivernal des débits moyens sur 10 jours entre l'horizon proche et la période historique | day | Q |  |

## Flow / Low Flows Winter / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [QMNA_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/QMNA_winter.yaml) | QMNA_winter | Minimum hivernal des débits mensuels | m^{3}.s^{-1} | Q |  |
| [QNA_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/QNA_winter.yaml) | QNA_winter | Minimum hivernal du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN10_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/VCN10_winter.yaml) | VCN10_winter | Minimum hivernal de la moyenne sur 10 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN30_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/VCN30_winter.yaml) | VCN30_winter | Minimum hivernal de la moyenne sur 30 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [VCN3_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/VCN3_winter.yaml) | VCN3_winter | Minimum hivernal de la moyenne sur 3 jours du débit journalier | m^{3}.s^{-1} | Q |  |
| [allLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/allLF_winter.yaml) | startLF_winter, centerLF_winter, endLF_winter, dtLF_winter, vLF_winter | Début des basses eaux hivernales | yearday | Q |  |
| [centerLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/centerLF_winter.yaml) | centerLF_winter | Centre des basses eaux hivernales | yearday | Q |  |
| [dtLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/dtLF_winter.yaml) | dtLF_winter | Durée des basses eaux hivernales | day | Q |  |
| [endLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/endLF_winter.yaml) | endLF_winter | Fin des basses eaux hivernales | yearday | Q |  |
| [startLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/startLF_winter.yaml) | startLF_winter | Début des basses eaux hivernales | yearday | Q |  |
| [tVCN10_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/tVCN10_winter.yaml) | tVCN10_winter | Date du minimum hivernal des débits moyens sur 10 jours | yearday | Q |  |
| [vLF_winter](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Low_Flows_Winter/serie/vLF_winter.yaml) | vLF_winter | Volume de déficit des basses eaux hivernales | hm^{3} | Q |  |

## Flow / Mean Flows / criteria

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Q50](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/Q50.yaml) | Q50 | Médiane des débits journaliers (chronique entière) | m^{3}.s^{-1} | Q |  |
| [a-FDC](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/a-FDC.yaml) | a-FDC | Pente du segment entre les quantiles des débits journaliers à 33 % et 66 % de la courbe des débits classés | without unit | Q |  |
| [alpha-QA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/alpha-QA.yaml) | alpha-QA, hyp-alpha-QA | Pente de Sen de la série des débits moyens annuels | m^{3}.s^{-1}.year^{-1} | Q |  |
| [delta-Q25A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-Q25A_H.yaml) | delta-Q25A_H1, delta-Q25A_H2, delta-Q25A_H3 | Changement moyen du troisième quartile annuel des débits journaliers entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q50A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-Q50A_H.yaml) | delta-Q50A_H1, delta-Q50A_H2, delta-Q50A_H3 | Changement moyen de la médiane annuelle des débits journaliers entre l'horizon proche et la période historique | % | Q |  |
| [delta-Q75A_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-Q75A_H.yaml) | delta-Q75A_H1, delta-Q75A_H2, delta-Q75A_H3 | Changement moyen du premier quartile annuel des débits journaliers entre l'horizon proche et la période historique | % | Q |  |
| [delta-QA_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-QA_H.yaml) | delta-QA_H1, delta-QA_H2, delta-QA_H3 | Changement moyen de la moyenne annuelle du débit journalier entre l'horizon proche et la période historique | % | Q |  |
| [delta-QMA_month_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-QMA_month_H.yaml) | delta-QMA_jan_H1, delta-QMA_jan_H2, delta-QMA_jan_H3, delta-QMA_feb_H1, delta-QMA_feb_H2, delta-QMA_feb_H3, delta-QMA_mar_H1, delta-QMA_mar_H2, delta-QMA_mar_H3, delta-QMA_apr_H1, delta-QMA_apr_H2, delta-QMA_apr_H3, delta-QMA_may_H1, delta-QMA_may_H2, delta-QMA_may_H3, delta-QMA_jun_H1, delta-QMA_jun_H2, delta-QMA_jun_H3, delta-QMA_jul_H1, delta-QMA_jul_H2, delta-QMA_jul_H3, delta-QMA_aug_H1, delta-QMA_aug_H2, delta-QMA_aug_H3, delta-QMA_sep_H1, delta-QMA_sep_H2, delta-QMA_sep_H3, delta-QMA_oct_H1, delta-QMA_oct_H2, delta-QMA_oct_H3, delta-QMA_nov_H1, delta-QMA_nov_H2, delta-QMA_nov_H3, delta-QMA_dec_H1, delta-QMA_dec_H2, delta-QMA_dec_H3 | Changement moyen de la moyenne des débits journaliers de chaque janvier entre l'horizon proche et la période historique | % | Q |  |
| [delta-QSA_season_H](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/delta-QSA_season_H.yaml) | delta-QSA_DJF_H1, delta-QSA_DJF_H2, delta-QSA_DJF_H3, delta-QSA_MAM_H1, delta-QSA_MAM_H2, delta-QSA_MAM_H3, delta-QSA_JJA_H1, delta-QSA_JJA_H2, delta-QSA_JJA_H3, delta-QSA_SON_H1, delta-QSA_SON_H2, delta-QSA_SON_H3 | Changement moyen de la moyenne des débits journaliers de chaque hiver entre l'horizon proche et la période historique | % | Q |  |
| [mean-QA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/criteria/mean-QA.yaml) | mean-QA | Moyenne inter-annuelle du débit moyen annuel | m^{3}.s^{-1} | Q |  |

## Flow / Mean Flows / serie

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [FDC](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/FDC.yaml) | FDC | Courbe des débits classés | m^{3}.s^{-1} | Q |  |
| [FDC_H0](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/FDC_H0.yaml) | FDC_H0 | Courbe des débits classés de la période historique | m^{3}.s^{-1} | Q |  |
| [FDC_H1](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/FDC_H1.yaml) | FDC_H1 | Courbe des débits classés de l'horizon proche | m^{3}.s^{-1} | Q |  |
| [FDC_H2](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/FDC_H2.yaml) | FDC_H2 | Courbe des débits classés de l'horizon moyen | m^{3}.s^{-1} | Q |  |
| [FDC_H3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/FDC_H3.yaml) | FDC_H3 | Courbe des débits classés de l'horizon lointain | m^{3}.s^{-1} | Q |  |
| [Q25A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/Q25A.yaml) | Q25A | Troisième quartile annuel des débits journaliers | m^{3}.s^{-1} | Q |  |
| [Q50A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/Q50A.yaml) | Q50A | Médiane annuelle des débits journaliers | m^{3}.s^{-1} | Q |  |
| [Q75A](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/Q75A.yaml) | Q75A | Premier quartile annuel des débits journaliers | m^{3}.s^{-1} | Q |  |
| [QA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QA.yaml) | QA | Moyenne annuelle du débit journalier | m^{3}.s^{-1} | Q |  |
| [QJC10](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QJC10.yaml) | QJC10 | Régime journalier inter-annuel lissé sur 10 jours | m^{3}.s^{-1} | Q |  |
| [QM](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QM.yaml) | QM | Débit moyen mensuel | m^{3}.s^{-1} | Q |  |
| [QMA_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QMA_month.yaml) | QMA_jan, QMA_feb, QMA_mar, QMA_apr, QMA_may, QMA_jun, QMA_jul, QMA_aug, QMA_sep, QMA_oct, QMA_nov, QMA_dec | Moyenne des débits journaliers de chaque janvier | m^{3}.s^{-1} | Q |  |
| [QM_H0](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QM_H0.yaml) | QM_H0 | Débit moyen mensuel de la période historique | m^{3}.s^{-1} | Q |  |
| [QM_H1](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QM_H1.yaml) | QM_H1 | Débit moyen mensuel de l'horizon proche | m^{3}.s^{-1} | Q |  |
| [QM_H2](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QM_H2.yaml) | QM_H2 | Débit moyen mensuel de l'horizon moyen | m^{3}.s^{-1} | Q |  |
| [QM_H3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QM_H3.yaml) | QM_H3 | Débit moyen mensuel de l'horizon lointain | m^{3}.s^{-1} | Q |  |
| [QSA_JJASO](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QSA_JJASO.yaml) | QSA_JJASO | Moyenne annuelle du débit journalier de juin à octobre | m^{3}.s^{-1} | Q |  |
| [QSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/QSA_season.yaml) | QSA_DJF, QSA_MAM, QSA_JJA, QSA_SON | Moyenne des débits journaliers de chaque hiver | m^{3}.s^{-1} | Q |  |
| [median-QJ](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJ.yaml) | median-QJ | Débit médian inter-annuel | m^{3}.s^{-1} | Q |  |
| [median-QJC5](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJC5.yaml) | median-QJC5 | Régime journalier médian inter-annuel lissé sur 5 jours | m^{3}.s^{-1} | Q |  |
| [median-QJ_H0](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJ_H0.yaml) | median-QJ_H0 | Débit médian inter-annuel de la période historique | m^{3}.s^{-1} | Q |  |
| [median-QJ_H1](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJ_H1.yaml) | median-QJ_H1 | Débit médian inter-annuel de l'horizon proche | m^{3}.s^{-1} | Q |  |
| [median-QJ_H2](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJ_H2.yaml) | median-QJ_H2 | Débit médian inter-annuel de l'horizon moyen | m^{3}.s^{-1} | Q |  |
| [median-QJ_H3](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Mean_Flows/serie/median-QJ_H3.yaml) | median-QJ_H3 | Débit médian inter-annuel de l'horizon lointain | m^{3}.s^{-1} | Q |  |

## Flow / Performance

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [Bias](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/Bias.yaml) | Bias | Biais | without unit | Q_obs, Q_sim |  |
| [Bias_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/Bias_season.yaml) | Bias_DJF, Bias_MAM, Bias_JJA, Bias_SON | Biais hivernal | without unit | Q_obs, Q_sim |  |
| [KGE](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/KGE.yaml) | KGE | Coefficient de performance de Kling-Gupta | without unit | Q_obs, Q_sim |  |
| [KGEsqrt](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/KGEsqrt.yaml) | KGEsqrt | Coefficient d'efficience de Kling-Gupta de la racine carrée des données | without unit | Q_obs, Q_sim |  |
| [NSE](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/NSE.yaml) | NSE | Coefficient d'efficience de Nash-Sutcliffe | without unit | Q_obs, Q_sim |  |
| [NSEinv](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/NSEinv.yaml) | NSEinv | Coefficient d'efficience de Nash-Sutcliffe de l'inverse des données | without unit | Q_obs, Q_sim |  |
| [NSElog](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/NSElog.yaml) | NSElog | Coefficient d'efficience de Nash-Sutcliffe du logarithme des données | without unit | Q_obs, Q_sim |  |
| [NSEsqrt](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/NSEsqrt.yaml) | NSEsqrt | Coefficient d'efficience de Nash-Sutcliffe de la racine carrée des données | without unit | Q_obs, Q_sim |  |
| [STD_ratio](https://github.com/lou-heraut/card/blob/main/src/card/cards/Flow/Performance/STD_ratio.yaml) | STD_ratio | Rapport des écarts-types simulé/observé | without unit | Q_obs, Q_sim |  |

## Precipitations

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [CR](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/CR.yaml) | CR | Coefficient correctif des précipitations | without unit | R_obs, R_sim |  |
| [CRS_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/CRS_season.yaml) | CRS_DJF, CRS_MAM, CRS_JJA, CRS_SON | Coefficient correctif des précipitations hivernales | without unit | R_obs, R_sim |  |
| [RA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RA.yaml) | RA | Cumul annuel des précipitations totales | mm | R |  |
| [RA_all](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RA_all.yaml) | RA, RAl, RAs | Cumul annuel des précipitations totales | mm | R, Rl, Rs |  |
| [RA_ratio](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RA_ratio.yaml) | Rl_ratio, Rs_ratio | Rapport des précipitations liquides aux précipitations totales | without unit | R, Rl, Rs |  |
| [RAl](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RAl.yaml) | RAl | Cumul annuel des précipitations liquides | mm | Rl |  |
| [RAl_ratio](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RAl_ratio.yaml) | RAl_ratio | Ratio des précipitations annuelles liquides sur les précipitations annuelles totales | without unit | R, Rl |  |
| [RAs](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RAs.yaml) | RAs | Cumul annuel des précipitations solides | mm | Rs |  |
| [RAs_ratio](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RAs_ratio.yaml) | RAs_ratio | Ratio des précipitations annuelles solides sur les précipitations annuelles totales | without unit | R, Rs |  |
| [RCXA1](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RCXA1.yaml) | RCXA1 | Maximum annuel des précipitations journalières | mm | R |  |
| [RCXA5](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RCXA5.yaml) | RCXA5 | Maximum annuel du cumul sur 5 jours des précipitations journalières | mm | R |  |
| [RMA_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RMA_month.yaml) | RMA_jan, RMA_feb, RMA_mar, RMA_apr, RMA_may, RMA_jun, RMA_jul, RMA_aug, RMA_sep, RMA_oct, RMA_nov, RMA_dec | Cumul des précipitations journalières de chaque janvier | mm | R |  |
| [RMAl_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RMAl_month.yaml) | RMAl_jan, RMAl_feb, RMAl_mar, RMAl_apr, RMAl_may, RMAl_jun, RMAl_jul, RMAl_aug, RMAl_sep, RMAl_oct, RMAl_nov, RMAl_dec | Cumul des précipitations liquides journalières de chaque janvier | mm | Rl |  |
| [RMAs_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RMAs_month.yaml) | RMAs_jan, RMAs_feb, RMAs_mar, RMAs_apr, RMAs_may, RMAs_jun, RMAs_jul, RMAs_aug, RMAs_sep, RMAs_oct, RMAs_nov, RMAs_dec | Cumul des précipitations solides journalières de chaque janvier | mm | Rs |  |
| [RSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RSA_season.yaml) | RSA_DJF, RSA_MAM, RSA_JJA, RSA_SON | Cumul des précipitations journalières de chaque hiver | mm | R |  |
| [RSAl_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RSAl_season.yaml) | RSAl_DJF, RSAl_MAM, RSAl_JJA, RSAl_SON | Cumul des précipitations liquides journalières de chaque hiver | mm | Rl |  |
| [RSAs_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/RSAs_season.yaml) | RSAs_DJF, RSAs_MAM, RSAs_JJA, RSAs_SON | Cumul des précipitations solides journalières de chaque hiver | mm | Rs |  |
| [dtCDDA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCDDA.yaml) | dtCDDA | Nombre maximal de jours secs consécutifs dans l'année | day | R |  |
| [dtCDDMA_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCDDMA_month.yaml) | dtCDDMA_jan, dtCDDMA_feb, dtCDDMA_mar, dtCDDMA_apr, dtCDDMA_may, dtCDDMA_jun, dtCDDMA_jul, dtCDDMA_aug, dtCDDMA_sep, dtCDDMA_oct, dtCDDMA_nov, dtCDDMA_dec | Nombre maximal de jours secs consécutifs de chaque janvier | day | R |  |
| [dtCDDSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCDDSA_season.yaml) | dtCDDSA_DJF, dtCDDSA_MAM, dtCDDSA_JJA, dtCDDSA_SON | Nombre maximal de jours secs consécutifs dans l'hiver | day | R |  |
| [dtCWDA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCWDA.yaml) | dtCWDA | Nombre maximal de jours pluvieux consécutifs dans l'année | day | R |  |
| [dtCWDMA_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCWDMA_month.yaml) | dtCWDMA_jan, dtCWDMA_feb, dtCWDMA_mar, dtCWDMA_apr, dtCWDMA_may, dtCWDMA_jun, dtCWDMA_jul, dtCWDMA_aug, dtCWDMA_sep, dtCWDMA_oct, dtCWDMA_nov, dtCWDMA_dec | Nombre maximal de jours pluvieux consécutifs de chaque janvier | day | R |  |
| [dtCWDSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtCWDSA_season.yaml) | dtCWDSA_DJF, dtCWDSA_MAM, dtCWDSA_JJA, dtCWDSA_SON | Nombre maximal de jours pluvieux consécutifs dans l'hiver | day | R |  |
| [dtRA01mm](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRA01mm.yaml) | dtRA01mm | Nombre de jours pluvieux dans l'année | day | R |  |
| [dtRA20mm](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRA20mm.yaml) | dtRA20mm | Nombre de jours de forte pluie dans l'année | day | R |  |
| [dtRA50mm](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRA50mm.yaml) | dtRA50mm | Nombre de jours de pluie extrême dans l'année | day | R |  |
| [dtRMA01mm_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRMA01mm_month.yaml) | dtRMA01mm_jan, dtRMA01mm_feb, dtRMA01mm_mar, dtRMA01mm_apr, dtRMA01mm_may, dtRMA01mm_jun, dtRMA01mm_jul, dtRMA01mm_aug, dtRMA01mm_sep, dtRMA01mm_oct, dtRMA01mm_nov, dtRMA01mm_dec | Nombre de jours pluvieux de chaque janvier | day | R |  |
| [dtRMA20mm_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRMA20mm_month.yaml) | dtRMA20mm_jan, dtRMA20mm_feb, dtRMA20mm_mar, dtRMA20mm_apr, dtRMA20mm_may, dtRMA20mm_jun, dtRMA20mm_jul, dtRMA20mm_aug, dtRMA20mm_sep, dtRMA20mm_oct, dtRMA20mm_nov, dtRMA20mm_dec | Nombre de jours de forte pluie de chaque janvier | day | R |  |
| [dtRMA50mm_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRMA50mm_month.yaml) | dtRMA50mm_jan, dtRMA50mm_feb, dtRMA50mm_mar, dtRMA50mm_apr, dtRMA50mm_may, dtRMA50mm_jun, dtRMA50mm_jul, dtRMA50mm_aug, dtRMA50mm_sep, dtRMA50mm_oct, dtRMA50mm_nov, dtRMA50mm_dec | Nombre de jours de pluie extrême de chaque janvier | day | R |  |
| [dtRSA01mm_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRSA01mm_season.yaml) | dtRSA01mm_DJF, dtRSA01mm_MAM, dtRSA01mm_JJA, dtRSA01mm_SON | Nombre de jours pluvieux en hiver | day | R |  |
| [dtRSA20mm_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRSA20mm_season.yaml) | dtRSA20mm_DJF, dtRSA20mm_MAM, dtRSA20mm_JJA, dtRSA20mm_SON | Nombre de jours de forte pluie en hiver | day | R |  |
| [dtRSA50mm_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/dtRSA50mm_season.yaml) | dtRSA50mm_DJF, dtRSA50mm_MAM, dtRSA50mm_JJA, dtRSA50mm_SON | Nombre de jours de pluie extrême en hiver | day | R |  |
| [mean-RA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/mean-RA.yaml) | mean-RA | Moyenne inter-annuelle du cumul annuel des précipitations totales | mm | R |  |
| [mean-RSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Precipitations/mean-RSA_season.yaml) | mean-RA_DJF, mean-RA_MAM, mean-RA_JJA, mean-RA_SON | Moyenne inter-annuelle des précipitations totales d'hiver | mm | R |  |

## Sensitivity to Climate Variability

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [QR_ratio](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/QR_ratio.yaml) | QR_ratio | Rapport des cumuls débit sur précipitations | m^{3}.s^{-1}.mm^{-1} | Q, R |  |
| [RAT_ET0](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/RAT_ET0.yaml) | RAT_ET0 | Test de robustesse à une variation d'évapotranspiration de référence | bool | Q_obs, Q_sim, ET0_obs |  |
| [RAT_R](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/RAT_R.yaml) | RAT_R | Test de robustesse à une variation de précipitations | bool | Q_obs, Q_sim, R_obs |  |
| [RAT_T](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/RAT_T.yaml) | RAT_T | Test de robustesse à une variation de température de l'air | bool | Q_obs, Q_sim, T_obs |  |
| [epsilon_R](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/epsilon_R.yaml) | epsilon_R | Élasticité annuelle du débit aux précipitations | without unit | Q, R |  |
| [epsilon_R_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/epsilon_R_season.yaml) | epsilon_R_DJF, epsilon_R_MAM, epsilon_R_JJA, epsilon_R_SON | Élasticité hivernale du débit aux précipitations | without unit | Q, R |  |
| [epsilon_T](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/epsilon_T.yaml) | epsilon_T | Élasticité annuelle du débit aux températures de l'air | without unit | Q, T |  |
| [epsilon_T_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Sensitivity_to_Climate_Variability/epsilon_T_season.yaml) | epsilon_T_DJF, epsilon_T_MAM, epsilon_T_JJA, epsilon_T_SON | Élasticité hivernale du débit aux températures de l'air | without unit | Q, T |  |

## Temperature

| fiche | variable(s) | nom | unité | entrées | exp. |
|---|---|---|---|---|---|
| [TA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Temperature/TA.yaml) | TA | Température moyenne annuelle | °C | T |  |
| [TMA_month](https://github.com/lou-heraut/card/blob/main/src/card/cards/Temperature/TMA_month.yaml) | TMA_jan, TMA_feb, TMA_mar, TMA_apr, TMA_may, TMA_jun, TMA_jul, TMA_aug, TMA_sep, TMA_oct, TMA_nov, TMA_dec | Moyenne des températures journalières de chaque janvier | °C | T |  |
| [TSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Temperature/TSA_season.yaml) | TSA_DJF, TSA_MAM, TSA_JJA, TSA_SON | Températures hivernales annuelles | °C | T |  |
| [mean-TA](https://github.com/lou-heraut/card/blob/main/src/card/cards/Temperature/mean-TA.yaml) | mean-TA | Moyenne inter-annuelle de la température moyenne annuelle | °C | T |  |
| [mean-TSA_season](https://github.com/lou-heraut/card/blob/main/src/card/cards/Temperature/mean-TSA_season.yaml) | mean-TSA_DJF, mean-TSA_MAM, mean-TSA_JJA, mean-TSA_SON | Moyenne inter-annuelle des températures moyennes d'hiver | °C | T |  |
