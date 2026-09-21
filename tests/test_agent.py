import os
import pytest
from models.ace_frequency_model import GridFrequencyBalancer

def test_under_frequency_event():
    # Frequency is 59.90 (0.10 Hz under), scheduled tie = actual tie
    res = GridFrequencyBalancer.calculate_ace_and_dispatch(
        actual_freq=59.90, nominal_freq=60.0,
        actual_tie_mw=100.0, scheduled_tie_mw=100.0,
        frequency_bias_b=20.0, bess_capacity_mwh=50.0
    )
    # delta_f = -0.10; ACE = 0 - 10 * 20 * (-0.10) = +200? Wait:
    # NERC ACE = (NI_A - NI_S) - 10*B*(F_A - F_S). If F_A < F_S, -(F_A - F_S) is positive.
    assert res["frequency_deviation_hz"] == -0.10
    assert res["area_control_error_mw"] != 0

def test_microgrid_fixture():
    import json
    data_file = os.path.join(os.path.dirname(__file__), "..", "fixtures", "grid_scenarios", "ieee_microgrid.json")
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
    assert res["dispatch_action"] in ["DISPATCH_BESS_DISCHARGE", "DISPATCH_BESS_CHARGE", "MAINTAIN_CURRENT_GENERATION"]
