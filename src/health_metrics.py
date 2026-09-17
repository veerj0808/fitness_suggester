from src.content import BMI_NOTES

def calculate_bmi(weight_kg: float, height_m: float) -> float:
    #Standard BMI formula: weight (kg) / height (m)^2.
    return round(weight_kg / (height_m ** 2), 1)

def get_bmi_category(bmi: float) -> str:
    """Return a plain-English label for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def show_bmi(weight_kg: float, height_m: float) -> None:
    bmi = calculate_bmi(weight_kg, height_m)
    category = get_bmi_category(bmi)
    print(f"\n  BMI: {bmi}  ({category})")
    print(f"  Note: {BMI_NOTES[category]}")

def calculate_water_intake(weight_kg: float) -> float:
    #Rough daily water-intake guideline: 35 ml per kg of body weight.
    return round((weight_kg * 35) / 1000, 1)

def show_water_intake(weight_kg: float) -> None:
    liters = calculate_water_intake(weight_kg)
    print(f"\n  Daily water intake target: {liters} liters")
    print("  Tip: Spread it across the day — don't try to drink it all at once!")

def calculate_tdee(age: int, weight_kg: float, height_m: float, goal: str, gender: str):
    gender_constant = 5 if gender == 'male' else -161
    bmr = (10 * weight_kg) + (6.25 * height_m * 100) - (5 * age) + gender_constant
    tdee = round(bmr * 1.55)

    if goal == 'weight loss':
        target = tdee - 500  # ~0.5 kg loss per week
        label = "Caloric Deficit Target"
    else:
        target = tdee + 300  # lean bulk
        label = "Caloric Surplus Target"

    return tdee, target, label

def show_calorie_estimate(age: int, weight_kg: float, height_m: float, goal: str, gender: str) -> None:
    tdee, target, label = calculate_tdee(age, weight_kg, height_m, goal, gender)
    print(f"\n  Estimated maintenance calories: ~{tdee} kcal/day")
    print(f"  {label}: ~{target} kcal/day")
