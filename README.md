# Grid Energy Balancer & Frequency Regulation Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![SmartGrid](https://img.shields.io/badge/Domain-Power_Systems_Smart_Grid-blue.svg)](docs/ferc_nerc_reliability_standards.md)
[![Standard](https://img.shields.io/badge/Standard-NERC_BAL--001-orange.svg)](docs/ferc_nerc_reliability_standards.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

An automated power system grid frequency and Area Control Error (ACE) balancing engine optimizing battery energy storage system (BESS) dispatch during renewable solar intermittency.

```
                    ┌─────────────────────────┐
                    │ Grid Telemetry Feeds    │
                    │ (Frequency & Tie Flow)  │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ models/ace_frequency    │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  NERC ACE Equation  │         │  Stability Warning  │
      │  (MW Imbalance)     │         │ (Under/Over Freq)   │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Fast BESS Dispatch Plan │
                    │ (MW Charge / Discharge) │
                    └─────────────────────────┘
```

## Features

- **NERC BAL-001 Compliance**: Implements the official Area Control Error (ACE) formulation.
- **Fast-Frequency BESS Dispatch**: Automatically issues MW charge/discharge commands to mitigate sub-60Hz excursions.
- **Microgrid Benchmarking**: Comes pre-loaded with intermittent solar microgrid scenarios.

## Directory Structure

```
grid-energy-balancer/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint power system provenance
├── models/
│   └── ace_frequency_model.py       # Area Control Error balancing engine
├── fixtures/
│   └── grid_scenarios/
│       └── ieee_microgrid.json      # Microgrid benchmark telemetry
├── docs/
│   └── ferc_nerc_reliability_standards.md # NERC reliability standards
├── tests/
│   └── test_agent.py                # Power balancing test suite
├── main.py                          # Smart grid balancing CLI
└── requirements.txt
```

## Quick Start

```bash
# Run grid balancing tests
pytest tests/ -v

# Balance sample microgrid telemetry
python main.py --demo
```
