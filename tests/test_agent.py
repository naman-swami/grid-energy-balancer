import pytest
from src.grid_engine import GridEnergyEngine

def test_peak_shaving_discharge():
    engine = GridEnergyEngine(battery_capacity_mwh=20.0, max_charge_rate_mw=5.0)
    res = engine.calculate_dispatch(current_soc_pct=80.0, demand_mw=18.0, peak_threshold_mw=15.0, lmp_price_per_mwh=100.0)
    assert res["action"] == "DISCHARGE"
    assert res["dispatch_mw"] == 3.0
    assert res["curtailed_peak_mw"] == 15.0

def test_cheap_power_charge():
    engine = GridEnergyEngine(battery_capacity_mwh=20.0, max_charge_rate_mw=5.0)
    res = engine.calculate_dispatch(current_soc_pct=40.0, demand_mw=10.0, peak_threshold_mw=15.0, lmp_price_per_mwh=15.0)
    assert res["action"] == "CHARGE"
    assert res["dispatch_mw"] > 0
