"""Namespace des fonctions hydro référencées par les fiches YAML.

Les fiches référencent directement des noms Python réels : d'abord ce
namespace (fonctions hydro spécifiques), puis numpy en repli (nanmean,
nanargmax...). Voir card.extraction.resolve(). La table de correspondance
avec les anciens noms R est dans docs/dev/RENAMING.md.
"""

from .aggregation import (  # noqa: F401
    circular_difference,
    circular_median,
    circular_ratio,
    difference,
    nansum_strict,
    ratio,
    rollmean_center,
    rollsum_center,
)
from .baseflow import (  # noqa: F401
    BFI,
    BFM,
    baseflow,
    quickflow,
    snowmelt_duration,
    snowmelt_timing,
    snowmelt_volume,
)
from .climate import elasticity, runoff_coefficient  # noqa: F401
from .fdc import (  # noqa: F401
    exceedance_frequency,
    exceedance_quantile,
    fdc_probabilities,
    fdc_quantiles,
    fdc_slope,
)
from .performance import (  # noqa: F401
    KGE,
    KGE_sqrt,
    NSE,
    NSE_inverse,
    NSE_log,
    NSE_sqrt,
    RAT,
    bias,
    std_ratio,
)
from .return_period import return_level  # noqa: F401
from .seasonal import delta  # noqa: F401
from .threshold import apply_threshold, deficit_volume  # noqa: F401
from .trend import (  # noqa: F401
    mannkendall_pvalue,
    mannkendall_slope,
    mannkendall_test,
)
