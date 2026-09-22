# Grid Frequency Regulation & BESS Balancer

> **Transmission System Operator (TSO) Control Loop for Grid Reliability**  
> Operationalizing NERC BAL-001 Real-Time Area Control Error (ACE) and Battery Storage Dispatch.

---

### NERC Reliability & ACE Dynamics

To maintain grid nominal frequency ($60.00\text{ Hz}$ in North America, $50.00\text{ Hz}$ in ENTSO-E), the engine continuously computes the Area Control Error:

$$ACE = (I_A - I_S) - 10 B (F_A - F_S)$$

Where:
- $I_A - I_S$: Real-time tie-line power flow deviation from schedule ($	ext{MW}$).
- $B$: Frequency bias setting ($	ext{MW}/0.1	ext{ Hz}$).
- $F_A - F_S$: Measured instantaneous frequency deviation from nominal ($	ext{Hz}$).

---

### Real-Time Inverter & BESS Fast Dispatch

When solar PV or wind generation suddenly drops, the engine dispatches Battery Energy Storage Systems (BESS) within a 4-second sub-cycle response:

```
[60.00 Hz Nominal] ──────────────────────────────────────────
                       \
                        \  PV Generation Cloud Ramp (-35 MW)
                         \
[59.82 Hz Trigger] ───────▼──────────────────────────────────
                          [BESS INJECTION: +35 MW in 3.2s]
                           ─────────────────────────────────► Recover to 59.98 Hz
```

---

### SCADA Simulation & Telemetry

```bash
# Balance IEEE microgrid scenario from fixtures/grid_scenarios/
python balance.py --demo

# Run power system control loop unit tests
pytest tests/ -v
```

Operating reserve rules, spinning reserve metrics, and frequency deadbands are governed by [GRID_RELIABILITY.md](GRID_RELIABILITY.md).
