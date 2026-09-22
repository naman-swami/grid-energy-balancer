# Power Grid Reliability Standards & Fast Frequency Regulation

## 1. NERC Reliability Standards Compliance
Grid Energy Balancer implements real-time power system frequency regulation under **North American Electric Reliability Corporation (NERC)** mandatory reliability standards:
- **NERC BAL-001-2 (Real-Time Frequency Support)**: Ensures balancing authorities maintain Area Control Error (ACE) within statistical compliance bounds ($	ext{CPS1}$ and $	ext{BAAL}$).
- **NERC BAL-002-3 (Disturbance Control Standard)**: Requires complete recovery of Area Control Error to zero or its pre-disturbance value within **15 minutes** following a reportable contingency event.
- **NERC BAL-003-2 (Frequency Response & Frequency Bias Setting)**: Mandates annual calibration of the frequency bias setting ($B$) to match natural governor and load damping responses.

---

## 2. Mathematical Formulation of Area Control Error (ACE)
The balancing algorithm evaluates real-time tie-line flow deviations and grid frequency offsets at 4-second SCADA intervals:

$$ACE = (I_A - I_S) - 10 B (F_A - F_S) - I_{ME}$$

Where:
- $I_A$: Actual net interchange tie-line power flow ($	ext{MW}$).
- $I_S$: Scheduled net interchange power flow ($	ext{MW}$).
- $B$: Frequency bias coefficient of the balancing authority ($	ext{MW} / 0.1	ext{ Hz}$), typically negative.
- $F_A$: Actual instantaneous grid frequency ($	ext{Hz}$).
- $F_S$: Scheduled reference frequency ($60.00	ext{ Hz}$ in WECC/Eastern Interconnections).
- $I_{ME}$: Meter error correction factor.

---

## 3. Battery Energy Storage System (BESS) Fast Dispatch Control
When renewable intermittency causes steep frequency excursions ($|\Delta f| > 0.05	ext{ Hz}$):
1. **Governor Deadband**: Inverter dispatch remains inactive within the $\pm 0.036	ext{ Hz}$ deadband ($59.964 - 60.036	ext{ Hz}$) to prevent unnecessary battery cycling.
2. **Fast Frequency Response (FFR)**: Inverters inject active power ($P$) within **500 milliseconds** of crossing the excursion threshold.
3. **Droop Curve**:
   $$P_{\text{dispatch}} = -\frac{1}{\text{Droop \%}} \times \frac{\Delta f}{f_{\text{nom}}} \times P_{\text{rated}}$$
   Using standard $4.0\%$ droop characteristic on $100\text{ MW} / 400\text{ MWh}$ lithium iron phosphate (LFP) installations.

---

## 4. Under-Frequency Load Shedding (UFLS) Coordination
If frequency drops below $59.50	ext{ Hz}$ despite full BESS discharge:
- Stage 1 UFLS: Shed $10\%$ of non-critical feeder load at $59.30\text{ Hz}$ with $0.1\text{s}$ time delay.
- Stage 2 UFLS: Shed additional $15\%$ feeder load at $59.00\text{ Hz}$.
