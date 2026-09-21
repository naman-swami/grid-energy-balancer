import argparse
import json
import os
from models.ace_frequency_model import GridFrequencyBalancer

def main():
    parser = argparse.ArgumentParser(description="Grid Energy Balancer CLI")
    parser.add_argument("--demo", action="store_true", help="Balance sample microgrid scenario")
    args = parser.parse_args()

    data_file = os.path.join(os.path.dirname(__file__), "fixtures", "grid_scenarios", "ieee_microgrid.json")

    if args.demo:
        with open(data_file, "r") as f:
            d = json.load(f)

        res = GridFrequencyBalancer.calculate_ace_and_dispatch(
            actual_freq=d["current_frequency_hz"],
            nominal_freq=d["nominal_frequency_hz"],
            actual_tie_mw=d["tie_line_actual_flow_mw"],
            scheduled_tie_mw=d["tie_line_scheduled_flow_mw"],
            frequency_bias_b=d["frequency_bias_mw_per_01hz"],
            bess_capacity_mwh=d["bess_available_capacity_mwh"]
        )

        print("=== SMART GRID FREQUENCY & ACE BALANCING REPORT ===\n")
        print(f"Microgrid Zone: {d['grid_id']}")
        print(f"System Frequency: {d['current_frequency_hz']} Hz (Deviation: {res['frequency_deviation_hz']} Hz)")
        print(f"Tie-line Flow: {d['tie_line_actual_flow_mw']} MW (Scheduled: {d['tie_line_scheduled_flow_mw']} MW)")
        print(f"Area Control Error (ACE): {res['area_control_error_mw']} MW")
        print(f"Stability Assessment: {res['grid_stability_tier']}")
        print(f"Automated Action: {res['dispatch_action']} ({res['bess_dispatch_mw']} MW)\n")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
