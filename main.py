import json
import argparse
from src.grid_engine import GridEnergyEngine

def main():
    parser = argparse.ArgumentParser(description="Grid Energy Balancer CLI")
    parser.add_argument("--demo", action="store_true", help="Run simulated microgrid battery dispatch optimization")
    args = parser.parse_args()

    engine = GridEnergyEngine(battery_capacity_mwh=25.0, max_charge_rate_mw=5.0)
    # 18 MW demand exceeding 15 MW threshold, with LMP price at $320/MWh
    report = engine.calculate_dispatch(current_soc_pct=85.0, demand_mw=18.5, peak_threshold_mw=15.0, lmp_price_per_mwh=320.0)
    print("="*60)
    print(" GRIDZEN MICROGRID BESS DISPATCH AUDIT REPORT")
    print("="*60)
    print(json.dumps(report, indent=2))
    print("="*60)

if __name__ == "__main__":
    main()
