# The toolbox cards draw from

A card does not compute anything by itself: it **declares** a chain of
operations, and names them. This page documents the operations it can
name. They are not all hydrological, and some are plain statistics, but
they have one thing in common: a card calls them, you do not. The
functions *you* call are in [Python functions](functions.md).

They are documented here because reading a variable definition means
knowing what `baseflow(method="Wal")` does exactly, and that should not
require opening the package.

Each one either **transforms** a series, one value per time step, or
**reduces** it to one value per period. Never both: the distinction is
declared next to the function and measured by the test suite, because a
figure that gets it wrong describes the wrong thing.

Beyond these, a card can also name any `numpy` function, `nanmean` and
`nanargmax` among them.

## Baseflow and low flows

::: card.functions.baseflow
::: card.functions.quickflow
::: card.functions.BFI
::: card.functions.BFM
::: card.functions.deficit_volume

## Moving windows and periods

::: card.functions.rollmean_center
::: card.functions.rollsum_center
::: card.functions.over_period
::: card.functions.nansum_strict

## Thresholds and exceedance

::: card.functions.apply_threshold
::: card.functions.exceedance_frequency
::: card.functions.exceedance_quantile
::: card.functions.ratio_longest_run

## Flow duration curve

::: card.functions.fdc_probabilities
::: card.functions.fdc_quantiles
::: card.functions.fdc_slope

## Extreme values

::: card.functions.return_level
::: card.functions.return_period

## Snow

::: card.functions.snowmelt_timing
::: card.functions.snowmelt_duration
::: card.functions.snowmelt_volume

## Change, trend and dates

::: card.functions.delta
::: card.functions.difference
::: card.functions.ratio
::: card.functions.mannkendall_test
::: card.functions.mannkendall_slope
::: card.functions.mannkendall_pvalue
::: card.functions.circular_median
::: card.functions.circular_difference
::: card.functions.circular_ratio

## Model performance

::: card.functions.KGE
::: card.functions.KGE_sqrt
::: card.functions.NSE
::: card.functions.NSE_log
::: card.functions.NSE_sqrt
::: card.functions.NSE_inverse
::: card.functions.bias
::: card.functions.std_ratio
::: card.functions.RAT

## Climate sensitivity

::: card.functions.elasticity
::: card.functions.runoff_coefficient
