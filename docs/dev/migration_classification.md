# Migration `topic` → `classification` — table de relecture (2026-07-16, v2)

Labels anglais minuscules (les blocs fr reçoivent les paires du
vocabulaire). `—` = pas de ligne. « chemin » = destination physique
`cards/<domain premier>/<output>/`.

| id | topic actuel (en) | domain | phenomenon | aspect | season | output | purpose | chemin |
|---|---|---|---|---|---|---|---|---|
| ETPA | Evapotranspiration, Average, Intensity | evapotranspiration | — | magnitude | annual | series | — | evapotranspiration/series/ |
| BFI-LH | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | scalar | — | flow/scalar/ |
| BFI-Wal | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | scalar | — | flow/scalar/ |
| BFM | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | curve | — | flow/curve/ |
| delta-BFI-LH_H | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | scalar | — | flow/scalar/ |
| delta-BFI-Wal_H | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | scalar | — | flow/scalar/ |
| delta-centerBF_H | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| delta-dtBF_H | Flow, Baseflow, Duration | flow | baseflow | duration | annual | scalar | — | flow/scalar/ |
| delta-endBF_H | Flow, Base Flow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| delta-startBF_H | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| delta-vBF_H | Flow, Baseflow, Intensity | flow | baseflow | magnitude | annual | scalar | — | flow/scalar/ |
| median-centerBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| median-dtBF | Flow, Baseflow, Duration | flow | baseflow | duration | annual | scalar | — | flow/scalar/ |
| median-endBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| median-startBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | scalar | — | flow/scalar/ |
| median-vBF | Flow, Baseflow, Intensity | flow | baseflow | magnitude | annual | scalar | — | flow/scalar/ |
| BF-LH | Flow, Base Flow, Intensity | flow | baseflow | magnitude | record | scalar | — | flow/scalar/ |
| centerBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | series | — | flow/series/ |
| dtBF | Flow, Baseflow, Duration | flow | baseflow | duration | annual | series | — | flow/series/ |
| endBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | series | — | flow/series/ |
| startBF | Flow, Baseflow, Seasonality | flow | baseflow | timing | annual | series | — | flow/series/ |
| vBF | Flow, Baseflow, Intensity | flow | baseflow | magnitude | annual | series | — | flow/series/ |
| Q10 | Flow, High Flows, Intensity | flow | high flows | magnitude | record | scalar | — | flow/scalar/ |
| QJXA-10 | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| alpha-QJXA | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q01A_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q05A_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q10A_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-QJXA-10_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-QJXA_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCX10_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCX3_H | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-dtFlood_H | Flow, High Flows, Duration | flow | high flows | duration | annual | scalar | — | flow/scalar/ |
| delta-fQ01A_H | Flow, High Flows, Frequency | flow | high flows | frequency | annual | scalar | — | flow/scalar/ |
| delta-fQ05A_H | Flow, High Flows, Frequency | flow | high flows | frequency | annual | scalar | — | flow/scalar/ |
| delta-fQ10A_H | Flow, High Flows, Frequency | flow | high flows | frequency | annual | scalar | — | flow/scalar/ |
| delta-tQJXA_H | Flow, High Flows, Seasonality | flow | high flows | timing | annual | scalar | — | flow/scalar/ |
| delta-tVCX10_H | Flow, High Flows, Seasonality | flow | high flows | timing | annual | scalar | — | flow/scalar/ |
| delta-tVCX3_H | Flow, High Flows, Seasonality | flow | high flows | timing | annual | scalar | — | flow/scalar/ |
| median-dtFlood | Flow, High Flows, Duration | flow | high flows | duration | annual | scalar | — | flow/scalar/ |
| median-tQJXA | Flow, High Flows, Seasonality | flow | high flows | timing | annual | scalar | — | flow/scalar/ |
| n-QJXA-10_H | Flow, High Flows, Occurrence | flow | high flows | frequency | annual | scalar | — | flow/scalar/ |
| Q01A | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| Q05A | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| Q10A | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| QJXA | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| VCX10 | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| VCX3 | Flow, High Flows, Intensity | flow | high flows | magnitude | annual | series | — | flow/series/ |
| dtFlood | Flow, High Flows, Duration | flow | high flows | duration | annual | series | — | flow/series/ |
| fQ01A | Flow, High Flows, Frequency | flow | high flows | frequency | annual | series | — | flow/series/ |
| fQ05A | Flow, High Flows, Frequency | flow | high flows | frequency | annual | series | — | flow/series/ |
| fQ10A | Flow, High Flows, Frequency | flow | high flows | frequency | annual | series | — | flow/series/ |
| tQJXA | Flow, High Flows, Seasonality | flow | high flows | timing | annual | series | — | flow/series/ |
| tVCX10 | Flow, High Flows, Seasonality | flow | high flows | timing | annual | series | — | flow/series/ |
| tVCX3 | Flow, High Flows, Seasonality | flow | high flows | timing | annual | series | — | flow/series/ |
| Q90 | Flow, Low Flows, Intensity | flow | low flows | magnitude | record | scalar | — | flow/scalar/ |
| QMNA-5 | Flow, Low Flows, Intensity | flow | low flows | magnitude | by month | scalar | — | flow/scalar/ |
| VCN10-5 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| VCN30-2 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| alpha-VCN10 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q90A_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q95A_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q99A_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-QMNA_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | by month | scalar | — | flow/scalar/ |
| delta-QNA_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCN10-5_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCN10_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCN30_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-VCN3_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-allLF_H | Flow, Low Flows, Seasonality (×15) | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| delta-centerLF_H | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| delta-dtLF_H | Flow, Low Flows, Duration | flow | low flows | duration | annual | scalar | — | flow/scalar/ |
| delta-endLF_H | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| delta-startLF_H | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| delta-tVCN10_H | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| delta-vLF_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| median-allLF | Flow, Low Flows, Seasonality (×5) | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| median-dtLF | Flow, Low Flows, Duration | flow | low flows | duration | annual | scalar | — | flow/scalar/ |
| median-endLF | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| median-startLF | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| median-tVCN10 | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | scalar | — | flow/scalar/ |
| median-vLF | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | scalar | — | flow/scalar/ |
| n-VCN10-5_H | Flow, Low Flows, Occurrence | flow | low flows | frequency | annual | scalar | — | flow/scalar/ |
| Q90A | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| Q95A | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| Q99A | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| QMNA | Flow, Low Flows, Intensity | flow | low flows | magnitude | by month | series | — | flow/series/ |
| QNA | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| VCN10 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| VCN3 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| VCN30 | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| allLF | Flow, Low Flows, Seasonality (×5) | flow | low flows | timing | annual | series | — | flow/series/ |
| centerLF | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | series | — | flow/series/ |
| dtLF | Flow, Low Flows, Duration | flow | low flows | duration | annual | series | — | flow/series/ |
| endLF | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | series | — | flow/series/ |
| startLF | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | series | — | flow/series/ |
| tVCN10 | Flow, Low Flows, Seasonality | flow | low flows | timing | annual | series | — | flow/series/ |
| vLF | Flow, Low Flows, Intensity | flow | low flows | magnitude | annual | series | — | flow/series/ |
| delta-QMNA_summer_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | scalar | — | flow/scalar/ |
| delta-QNA_summer_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | scalar | — | flow/scalar/ |
| delta-VCN10_summer_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | scalar | — | flow/scalar/ |
| delta-VCN30_summer_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | scalar | — | flow/scalar/ |
| delta-VCN3_summer_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | scalar | — | flow/scalar/ |
| delta-allLF_summer_H | Flow, Low Flows, Seasonality (×15) | flow | low flows | timing | summer | scalar | — | flow/scalar/ |
| delta-tVCN10_summer_H | Flow, Low Flows, Seasonality | flow | low flows | timing | summer | scalar | — | flow/scalar/ |
| QMNA_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| QNA_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| VCN10_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| VCN30_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| VCN3_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| allLF_summer | Flow, Low Flows, Seasonality (×5) | flow | low flows | timing | summer | series | — | flow/series/ |
| centerLF_summer | Flow, Low Flows, Seasonality | flow | low flows | timing | summer | series | — | flow/series/ |
| dtLF_summer | Flow, Low Flows, Duration | flow | low flows | duration | summer | series | — | flow/series/ |
| endLF_summer | Flow, Low Flows, Seasonality | flow | low flows | timing | summer | series | — | flow/series/ |
| startLF_summer | Flow, Low Flows, Seasonality | flow | low flows | timing | summer | series | — | flow/series/ |
| tVCN10_summer | Flow, Low Flows, Seasonality | flow | low flows | timing | summer | series | — | flow/series/ |
| vLF_summer | Flow, Low Flows, Intensity | flow | low flows | magnitude | summer | series | — | flow/series/ |
| delta-QMNA_winter_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | scalar | — | flow/scalar/ |
| delta-QNA_winter_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | scalar | — | flow/scalar/ |
| delta-VCN10_winter_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | scalar | — | flow/scalar/ |
| delta-VCN30_winter_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | scalar | — | flow/scalar/ |
| delta-VCN3_winter_H | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | scalar | — | flow/scalar/ |
| delta-allLF_winter_H | Flow, Low Flows, Seasonality (×15) | flow | low flows | timing | winter | scalar | — | flow/scalar/ |
| delta-tVCN10_winter_H | Flow, Low Flows, Seasonality | flow | low flows | timing | winter | scalar | — | flow/scalar/ |
| QMNA_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| QNA_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| VCN10_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| VCN30_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| VCN3_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| allLF_winter | Flow, Low Flows, Seasonality (×5) | flow | low flows | timing | winter | series | — | flow/series/ |
| centerLF_winter | Flow, Low Flows, Seasonality | flow | low flows | timing | winter | series | — | flow/series/ |
| dtLF_winter | Flow, Low Flows, Duration | flow | low flows | duration | winter | series | — | flow/series/ |
| endLF_winter | Flow, Low Flows, Seasonality | flow | low flows | timing | winter | series | — | flow/series/ |
| startLF_winter | Flow, Low Flows, Seasonality | flow | low flows | timing | winter | series | — | flow/series/ |
| tVCN10_winter | Flow, Low Flows, Seasonality | flow | low flows | timing | winter | series | — | flow/series/ |
| vLF_winter | Flow, Low Flows, Intensity | flow | low flows | magnitude | winter | series | — | flow/series/ |
| Q50 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | scalar | — | flow/scalar/ |
| a-FDC | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | scalar | — | flow/scalar/ |
| alpha-QA | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q25A_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q50A_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-Q75A_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-QA_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| delta-QMA_month_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | scalar | — | flow/scalar/ |
| delta-QSA_season_H | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by season | scalar | — | flow/scalar/ |
| mean-QA | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | scalar | — | flow/scalar/ |
| FDC | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| FDC_H0 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| FDC_H1 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| FDC_H2 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| FDC_H3 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| Q25A | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | series | — | flow/series/ |
| Q50A | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | series | — | flow/series/ |
| Q75A | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | series | — | flow/series/ |
| QA | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | annual | series | — | flow/series/ |
| QJC10 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| QM | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QMA_month | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QM_H0 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QM_H1 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QM_H2 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QM_H3 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by month | series | — | flow/series/ |
| QSA_JJASO | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | summer | series | — | flow/series/ |
| QSA_season | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | by season | series | — | flow/series/ |
| median-QJ | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| median-QJC5 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| median-QJ_H0 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| median-QJ_H1 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| median-QJ_H2 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| median-QJ_H3 | Flow, Mean Flows, Intensity | flow | mean flows | magnitude | record | curve | — | flow/curve/ |
| Bias | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| Bias_season | Flow, Performance | flow | — | — | record | series | model performance | flow/series/ |
| KGE | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| KGEsqrt | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| NSE | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| NSEinv | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| NSElog | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| NSEsqrt | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| STD_ratio | Flow, Performance | flow | — | — | record | scalar | model performance | flow/scalar/ |
| CR | Precipitations, Moderate, Parameterization | precipitation | — | magnitude | annual | scalar | — | precipitation/scalar/ |
| CRS_season | Precipitations, Moderate, Parameterization | precipitation | — | magnitude | by season | scalar | — | precipitation/scalar/ |
| RA | Precipitations, Moderate, Intensity | precipitation | — | magnitude | annual | series | — | precipitation/series/ |
| RA_all | Precipitations, Moderate, Intensity | precipitation | — | magnitude | annual | series | — | precipitation/series/ |
| RA_ratio | Precipitations, Moderate, Ratio | precipitation | — | magnitude | annual | scalar | — | precipitation/scalar/ |
| RAl | Precipitations, Moderate, Intensity | precipitation | — | magnitude | annual | series | — | precipitation/series/ |
| RAl_ratio | Precipitations, Moderate, Ratio | precipitation | — | magnitude | annual | series | — | precipitation/series/ |
| RAs | Precipitations, Moderate, Intensity | precipitation | snow | magnitude | annual | series | — | precipitation/series/ |
| RAs_ratio | Precipitations, Moderate, Ratio | precipitation | snow | magnitude | annual | series | — | precipitation/series/ |
| RCXA1 | Precipitations, Heavy, Intensity | precipitation | heavy rain | magnitude | annual | series | — | precipitation/series/ |
| RCXA5 | Precipitations, Heavy, Intensity | precipitation | heavy rain | magnitude | annual | series | — | precipitation/series/ |
| RMA_month | Precipitations, Moderate, Intensity | precipitation | — | magnitude | by month | series | — | precipitation/series/ |
| RMAl_month | Precipitations, Moderate, Intensity | precipitation | — | magnitude | by month | series | — | precipitation/series/ |
| RMAs_month | Precipitations, Moderate, Intensity | precipitation | snow | magnitude | by month | series | — | precipitation/series/ |
| RSA_season | Precipitations, Moderate, Intensity | precipitation | — | magnitude | by season | series | — | precipitation/series/ |
| RSAl_season | Precipitations, Moderate, Intensity | precipitation | — | magnitude | by season | series | — | precipitation/series/ |
| RSAs_season | Precipitations, Moderate, Intensity | precipitation | snow | magnitude | by season | series | — | precipitation/series/ |
| dtCDDA | Precipitations, Dry Period, Duration | precipitation | dry spells | duration | annual | series | — | precipitation/series/ |
| dtCDDMA_month | Precipitations, Dry Period, Duration | precipitation | dry spells | duration | by month | series | — | precipitation/series/ |
| dtCDDSA_season | Precipitations, Dry Period, Duration | precipitation | dry spells | duration | by season | series | — | precipitation/series/ |
| dtCWDA | Precipitations, Low, Duration | precipitation | wet days | duration | annual | series | — | precipitation/series/ |
| dtCWDMA_month | Precipitations, Low, Duration | precipitation | wet days | duration | by month | series | — | precipitation/series/ |
| dtCWDSA_season | Precipitations, Low, Duration | precipitation | wet days | duration | by season | series | — | precipitation/series/ |
| dtRA01mm | Precipitations, Low, Duration | precipitation | wet days | duration | annual | series | — | precipitation/series/ |
| dtRA20mm | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | annual | series | — | precipitation/series/ |
| dtRA50mm | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | annual | series | — | precipitation/series/ |
| dtRMA01mm_month | Precipitations, Low, Duration | precipitation | wet days | duration | by month | series | — | precipitation/series/ |
| dtRMA20mm_month | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | by month | series | — | precipitation/series/ |
| dtRMA50mm_month | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | by month | series | — | precipitation/series/ |
| dtRSA01mm_season | Precipitations, Low, Duration | precipitation | wet days | duration | by season | series | — | precipitation/series/ |
| dtRSA20mm_season | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | by season | series | — | precipitation/series/ |
| dtRSA50mm_season | Precipitations, Heavy, Duration | precipitation | heavy rain | duration | by season | series | — | precipitation/series/ |
| mean-RA | Precipitations, Moderate, Intensity | precipitation | — | magnitude | annual | scalar | — | precipitation/scalar/ |
| mean-RSA_season | Precipitations, Moderate, Intensity | precipitation | — | magnitude | by season | scalar | — | precipitation/scalar/ |
| QR_ratio | Flow / Precipitations, Sensitivity to Climate Variability | [flow, precipitation] | — | — | record | scalar | climate sensitivity | flow/scalar/ |
| RAT_ET0 | Flow / Evapotranspiration, Sensitivity to Climate Variability | [flow, evapotranspiration] | — | — | annual | scalar | climate sensitivity | flow/scalar/ |
| RAT_R | Flow / Precipitations, Sensitivity to Climate Variability | [flow, precipitation] | — | — | annual | scalar | climate sensitivity | flow/scalar/ |
| RAT_T | Flow / Temperature, Sensitivity to Climate Variability | [flow, temperature] | — | — | annual | scalar | climate sensitivity | flow/scalar/ |
| epsilon_R | Flow / Precipitations, Sensitivity to Climate Variability | [flow, precipitation] | — | — | annual | scalar | climate sensitivity | flow/scalar/ |
| epsilon_R_season | Flow / Precipitations, Sensitivity to Climate Variability | [flow, precipitation] | — | — | by season | scalar | climate sensitivity | flow/scalar/ |
| epsilon_T | Flow / Temperature, Sensitivity to Climate Variability | [flow, temperature] | — | — | annual | scalar | climate sensitivity | flow/scalar/ |
| epsilon_T_season | Flow / Temperature, Sensitivity to Climate Variability | [flow, temperature] | — | — | by season | scalar | climate sensitivity | flow/scalar/ |
| TA | Temperature, Average, Intensity | temperature | — | magnitude | annual | series | — | temperature/series/ |
| TMA_month | Temperature, Average, Intensity | temperature | — | magnitude | by month | series | — | temperature/series/ |
| TSA_season | Temperature, Mean, Intensity | temperature | — | magnitude | by season | series | — | temperature/series/ |
| mean-TA | Temperature, Average, Intensity | temperature | — | magnitude | annual | scalar | — | temperature/scalar/ |
| mean-TSA_season | Temperature, Average, Intensity | temperature | — | magnitude | by season | scalar | — | temperature/scalar/ |

## Répartition physique cible

| dossier | fiches |
|---|---|
| cards/evapotranspiration/series/ | 1 |
| cards/flow/curve/ | 13 |
| cards/flow/scalar/ | 103 |
| cards/flow/series/ | 70 |
| cards/precipitation/scalar/ | 5 |
| cards/precipitation/series/ | 29 |
| cards/temperature/scalar/ | 2 |
| cards/temperature/series/ | 3 |
