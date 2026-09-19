# Explainability — grid-energy-balancer

## Decision Reasoning
GridZen determines energy dispatch schedules by solving linear programming optimizations balancing battery cycle degradation costs against wholesale electricity price arbitrage and demand-charge tariffs.

## Data Sources and Inputs Used
SCADA microgrid telemetry, ISO/RTO day-ahead and real-time locational marginal prices (LMP), NOAA weather forecast APIs, and watt-time carbon intensity feeds.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, grid-energy-balancer assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, grid-energy-balancer will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, grid-energy-balancer explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
grid-energy-balancer actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Physical Grid Infrastructure: Cannot physically repair downed high-voltage transmission lines or blown transformer coils.
- Regulatory Utility Tariffs: Cannot renegotiate fixed monopoly utility interconnection agreements unilaterally.
- Battery Chemistry Physics: Cannot alter the thermal chemistry limits or physical safety constraints of lithium battery cells.
- Nuclear/Hydro Dispatch: Does not control regional sovereign baseload nuclear generation facilities.

## Uncertainty Quantification Approach
When weather forecasts diverge regarding cloud cover timing, GridZen maintains a conservative spinning-reserve energy buffer in the BESS and avoids deep battery discharges until generation certainty stabilizes.
