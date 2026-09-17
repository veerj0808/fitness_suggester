"""
test_health_metrics.py — sanity checks for the pure calculation functions.

These don't need pytest: run directly with

    python3 tests/test_health_metrics.py

or, if pytest is installed:

    pytest tests/
"""

import os
import sys

# Make the project root importable when this file is run directly
# (e.g. `python3 tests/test_health_metrics.py` from anywhere).
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.health_metrics import calculate_bmi, get_bmi_category, calculate_water_intake, calculate_tdee


def test_calculate_bmi():
    # 70 kg at 1.75 m -> 70 / (1.75**2) = 22.9
    assert calculate_bmi(70, 1.75) == 22.9


def test_bmi_category_boundaries():
    assert get_bmi_category(18.4) == "Underweight"
    assert get_bmi_category(18.5) == "Normal weight"
    assert get_bmi_category(24.9) == "Normal weight"
    assert get_bmi_category(25.0) == "Overweight"
    assert get_bmi_category(29.9) == "Overweight"
    assert get_bmi_category(30.0) == "Obese"


def test_water_intake():
    # 80 kg * 35 ml/kg = 2800 ml = 2.8 L
    assert calculate_water_intake(80) == 2.8


def test_tdee_weight_loss_is_lower_than_maintenance():
    tdee, target, label = calculate_tdee(age=25, weight_kg=70, height_m=1.75, goal='weight loss', gender='male')
    assert target == tdee - 500
    assert label == "Caloric Deficit Target"


def test_tdee_muscle_gain_is_higher_than_maintenance():
    tdee, target, label = calculate_tdee(age=25, weight_kg=70, height_m=1.75, goal='muscle gain', gender='female')
    assert target == tdee + 300
    assert label == "Caloric Surplus Target"


def run_all():
    tests = [obj for name, obj in globals().items() if name.startswith('test_') and callable(obj)]
    passed = 0
    for test in tests:
        test()
        passed += 1
        print(f"  PASS  {test.__name__}")
    print(f"\n{passed}/{len(tests)} tests passed.")


if __name__ == "__main__":
    run_all()
