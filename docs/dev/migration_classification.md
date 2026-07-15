# Migration `topic` → `classification` — table de relecture (2026-07-16)

Labels anglais (les blocs fr reçoivent les paires du vocabulaire).
`—` = pas de ligne. Les `?` marquent un cas non projeté automatiquement.

| id | topic actuel (en) | domain | tags | aspect | season | output | purpose |
|---|---|---|---|---|---|---|---|
| ETPA | Evapotranspiration, Average, Intensity | Evapotranspiration | [] | Magnitude | Annual | Series | — |
| BFI-LH | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Scalar | — |
| BFI-Wal | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Scalar | — |
| BFM | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Curve | — |
| delta-BFI-LH_H | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Scalar | — |
| delta-BFI-Wal_H | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Scalar | — |
| delta-centerBF_H | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| delta-dtBF_H | Flow, Baseflow, Duration | Flow | [Baseflow] | Duration | Annual | Scalar | — |
| delta-endBF_H | Flow, Base Flow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| delta-startBF_H | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| delta-vBF_H | Flow, Baseflow, Intensity | Flow | [Baseflow] | Magnitude | Annual | Scalar | — |
| median-centerBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| median-dtBF | Flow, Baseflow, Duration | Flow | [Baseflow] | Duration | Annual | Scalar | — |
| median-endBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| median-startBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Scalar | — |
| median-vBF | Flow, Baseflow, Intensity | Flow | [Baseflow] | Magnitude | Annual | Scalar | — |
| BF-LH | Flow, Base Flow, Intensity | Flow | [Baseflow] | Magnitude | Record | Scalar | — |
| centerBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Series | — |
| dtBF | Flow, Baseflow, Duration | Flow | [Baseflow] | Duration | Annual | Series | — |
| endBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Series | — |
| startBF | Flow, Baseflow, Seasonality | Flow | [Baseflow] | Timing | Annual | Series | — |
| vBF | Flow, Baseflow, Intensity | Flow | [Baseflow] | Magnitude | Annual | Series | — |
| Q10 | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Record | Scalar | — |
| QJXA-10 | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| alpha-QJXA | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-Q01A_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-Q05A_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-Q10A_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-QJXA-10_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-QJXA_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-VCX10_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-VCX3_H | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Scalar | — |
| delta-dtFlood_H | Flow, High Flows, Duration | Flow | [High flows] | Duration | Annual | Scalar | — |
| delta-fQ01A_H | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Scalar | — |
| delta-fQ05A_H | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Scalar | — |
| delta-fQ10A_H | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Scalar | — |
| delta-tQJXA_H | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Scalar | — |
| delta-tVCX10_H | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Scalar | — |
| delta-tVCX3_H | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Scalar | — |
| median-dtFlood | Flow, High Flows, Duration | Flow | [High flows] | Duration | Annual | Scalar | — |
| median-tQJXA | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Scalar | — |
| n-QJXA-10_H | Flow, High Flows, Occurrence | Flow | [High flows] | Frequency | Annual | Scalar | — |
| Q01A | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| Q05A | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| Q10A | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| QJXA | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| VCX10 | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| VCX3 | Flow, High Flows, Intensity | Flow | [High flows] | Magnitude | Annual | Series | — |
| dtFlood | Flow, High Flows, Duration | Flow | [High flows] | Duration | Annual | Series | — |
| fQ01A | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Series | — |
| fQ05A | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Series | — |
| fQ10A | Flow, High Flows, Frequency | Flow | [High flows] | Frequency | Annual | Series | — |
| tQJXA | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Series | — |
| tVCX10 | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Series | — |
| tVCX3 | Flow, High Flows, Seasonality | Flow | [High flows] | Timing | Annual | Series | — |
| Q90 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Record | Scalar | — |
| QMNA-5 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | By month | Scalar | — |
| VCN10-5 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| VCN30-2 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| alpha-VCN10 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-Q90A_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-Q95A_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-Q99A_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-QMNA_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | By month | Scalar | — |
| delta-QNA_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-VCN10-5_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-VCN10_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-VCN30_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-VCN3_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| delta-allLF_H | Flow, Low Flows, Seasonality (×15) | Flow | [Low flows] | Timing | Annual | Scalar | — |
| delta-centerLF_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| delta-dtLF_H | Flow, Low Flows, Duration | Flow | [Low flows] | Duration | Annual | Scalar | — |
| delta-endLF_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| delta-startLF_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| delta-tVCN10_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| delta-vLF_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| median-allLF | Flow, Low Flows, Seasonality (×5) | Flow | [Low flows] | Timing | Annual | Scalar | — |
| median-dtLF | Flow, Low Flows, Duration | Flow | [Low flows] | Duration | Annual | Scalar | — |
| median-endLF | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| median-startLF | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| median-tVCN10 | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Scalar | — |
| median-vLF | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Scalar | — |
| n-VCN10-5_H | Flow, Low Flows, Occurrence | Flow | [Low flows] | Frequency | Annual | Scalar | — |
| Q90A | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| Q95A | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| Q99A | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| QMNA | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | By month | Series | — |
| QNA | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| VCN10 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| VCN3 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| VCN30 | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| allLF | Flow, Low Flows, Seasonality (×5) | Flow | [Low flows] | Timing | Annual | Series | — |
| centerLF | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Series | — |
| dtLF | Flow, Low Flows, Duration | Flow | [Low flows] | Duration | Annual | Series | — |
| endLF | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Series | — |
| startLF | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Series | — |
| tVCN10 | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Annual | Series | — |
| vLF | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Annual | Series | — |
| delta-QMNA_summer_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Scalar | — |
| delta-QNA_summer_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Scalar | — |
| delta-VCN10_summer_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Scalar | — |
| delta-VCN30_summer_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Scalar | — |
| delta-VCN3_summer_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Scalar | — |
| delta-allLF_summer_H | Flow, Low Flows, Seasonality (×15) | Flow | [Low flows] | Timing | Summer | Scalar | — |
| delta-tVCN10_summer_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Summer | Scalar | — |
| QMNA_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| QNA_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| VCN10_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| VCN30_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| VCN3_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| allLF_summer | Flow, Low Flows, Seasonality (×5) | Flow | [Low flows] | Timing | Summer | Series | — |
| centerLF_summer | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Summer | Series | — |
| dtLF_summer | Flow, Low Flows, Duration | Flow | [Low flows] | Duration | Summer | Series | — |
| endLF_summer | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Summer | Series | — |
| startLF_summer | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Summer | Series | — |
| tVCN10_summer | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Summer | Series | — |
| vLF_summer | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Summer | Series | — |
| delta-QMNA_winter_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Scalar | — |
| delta-QNA_winter_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Scalar | — |
| delta-VCN10_winter_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Scalar | — |
| delta-VCN30_winter_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Scalar | — |
| delta-VCN3_winter_H | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Scalar | — |
| delta-allLF_winter_H | Flow, Low Flows, Seasonality (×15) | Flow | [Low flows] | Timing | Winter | Scalar | — |
| delta-tVCN10_winter_H | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Winter | Scalar | — |
| QMNA_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| QNA_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| VCN10_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| VCN30_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| VCN3_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| allLF_winter | Flow, Low Flows, Seasonality (×5) | Flow | [Low flows] | Timing | Winter | Series | — |
| centerLF_winter | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Winter | Series | — |
| dtLF_winter | Flow, Low Flows, Duration | Flow | [Low flows] | Duration | Winter | Series | — |
| endLF_winter | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Winter | Series | — |
| startLF_winter | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Winter | Series | — |
| tVCN10_winter | Flow, Low Flows, Seasonality | Flow | [Low flows] | Timing | Winter | Series | — |
| vLF_winter | Flow, Low Flows, Intensity | Flow | [Low flows] | Magnitude | Winter | Series | — |
| Q50 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Scalar | — |
| a-FDC | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Scalar | — |
| alpha-QA | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| delta-Q25A_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| delta-Q50A_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| delta-Q75A_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| delta-QA_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| delta-QMA_month_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Scalar | — |
| delta-QSA_season_H | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By season | Scalar | — |
| mean-QA | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Scalar | — |
| FDC | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| FDC_H0 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| FDC_H1 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| FDC_H2 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| FDC_H3 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| Q25A | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Series | — |
| Q50A | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Series | — |
| Q75A | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Series | — |
| QA | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Annual | Series | — |
| QJC10 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| QM | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QMA_month | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QM_H0 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QM_H1 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QM_H2 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QM_H3 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By month | Series | — |
| QSA_JJASO | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Summer | Series | — |
| QSA_season | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | By season | Series | — |
| median-QJ | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| median-QJC5 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| median-QJ_H0 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| median-QJ_H1 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| median-QJ_H2 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| median-QJ_H3 | Flow, Mean Flows, Intensity | Flow | [Mean flows] | Magnitude | Record | Curve | — |
| Bias | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| Bias_season | Flow, Performance | Flow | [] | — | Record | Series | Model performance |
| KGE | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| KGEsqrt | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| NSE | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| NSEinv | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| NSElog | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| NSEsqrt | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| STD_ratio | Flow, Performance | Flow | [] | — | Record | Scalar | Model performance |
| CR | Precipitations, Moderate, Parameterization | Precipitation | [] | Magnitude | Annual | Scalar | — |
| CRS_season | Precipitations, Moderate, Parameterization | Precipitation | [] | Magnitude | By season | Scalar | — |
| RA | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | Annual | Series | — |
| RA_all | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | Annual | Series | — |
| RA_ratio | Precipitations, Moderate, Ratio | Precipitation | [] | Magnitude | Annual | Scalar | — |
| RAl | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | Annual | Series | — |
| RAl_ratio | Precipitations, Moderate, Ratio | Precipitation | [] | Magnitude | Annual | Series | — |
| RAs | Precipitations, Moderate, Intensity | Precipitation | [Snow] | Magnitude | Annual | Series | — |
| RAs_ratio | Precipitations, Moderate, Ratio | Precipitation | [Snow] | Magnitude | Annual | Series | — |
| RCXA1 | Precipitations, Heavy, Intensity | Precipitation | [Heavy rain] | Magnitude | Annual | Series | — |
| RCXA5 | Precipitations, Heavy, Intensity | Precipitation | [Heavy rain] | Magnitude | Annual | Series | — |
| RMA_month | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | By month | Series | — |
| RMAl_month | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | By month | Series | — |
| RMAs_month | Precipitations, Moderate, Intensity | Precipitation | [Snow] | Magnitude | By month | Series | — |
| RSA_season | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | By season | Series | — |
| RSAl_season | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | By season | Series | — |
| RSAs_season | Precipitations, Moderate, Intensity | Precipitation | [Snow] | Magnitude | By season | Series | — |
| dtCDDA | Precipitations, Dry Period, Duration | Precipitation | [Dry spells] | Duration | Annual | Series | — |
| dtCDDMA_month | Precipitations, Dry Period, Duration | Precipitation | [Dry spells] | Duration | By month | Series | — |
| dtCDDSA_season | Precipitations, Dry Period, Duration | Precipitation | [Dry spells] | Duration | By season | Series | — |
| dtCWDA | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | Annual | Series | — |
| dtCWDMA_month | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | By month | Series | — |
| dtCWDSA_season | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | By season | Series | — |
| dtRA01mm | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | Annual | Series | — |
| dtRA20mm | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | Annual | Series | — |
| dtRA50mm | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | Annual | Series | — |
| dtRMA01mm_month | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | By month | Series | — |
| dtRMA20mm_month | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | By month | Series | — |
| dtRMA50mm_month | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | By month | Series | — |
| dtRSA01mm_season | Precipitations, Low, Duration | Precipitation | [Wet days] | Duration | By season | Series | — |
| dtRSA20mm_season | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | By season | Series | — |
| dtRSA50mm_season | Precipitations, Heavy, Duration | Precipitation | [Heavy rain] | Duration | By season | Series | — |
| mean-RA | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | Annual | Scalar | — |
| mean-RSA_season | Precipitations, Moderate, Intensity | Precipitation | [] | Magnitude | By season | Scalar | — |
| QR_ratio | Flow / Precipitations, Sensitivity to Climate Variability | [Flow, Precipitation] | [] | — | Record | Scalar | Climate sensitivity |
| RAT_ET0 | Flow / Evapotranspiration, Sensitivity to Climate Variability | [Flow, Evapotranspiration] | [] | — | Annual | Scalar | Climate sensitivity |
| RAT_R | Flow / Precipitations, Sensitivity to Climate Variability | [Flow, Precipitation] | [] | — | Annual | Scalar | Climate sensitivity |
| RAT_T | Flow / Temperature, Sensitivity to Climate Variability | [Flow, Temperature] | [] | — | Annual | Scalar | Climate sensitivity |
| epsilon_R | Flow / Precipitations, Sensitivity to Climate Variability | [Flow, Precipitation] | [] | — | Annual | Scalar | Climate sensitivity |
| epsilon_R_season | Flow / Precipitations, Sensitivity to Climate Variability | [Flow, Precipitation] | [] | — | By season | Scalar | Climate sensitivity |
| epsilon_T | Flow / Temperature, Sensitivity to Climate Variability | [Flow, Temperature] | [] | — | Annual | Scalar | Climate sensitivity |
| epsilon_T_season | Flow / Temperature, Sensitivity to Climate Variability | [Flow, Temperature] | [] | — | By season | Scalar | Climate sensitivity |
| TA | Temperature, Average, Intensity | Temperature | [] | Magnitude | Annual | Series | — |
| TMA_month | Temperature, Average, Intensity | Temperature | [] | Magnitude | By month | Series | — |
| TSA_season | Temperature, Mean, Intensity | Temperature | [] | Magnitude | By season | Series | — |
| mean-TA | Temperature, Average, Intensity | Temperature | [] | Magnitude | Annual | Scalar | — |
| mean-TSA_season | Temperature, Average, Intensity | Temperature | [] | Magnitude | By season | Scalar | — |
