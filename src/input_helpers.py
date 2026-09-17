MIN_AGE, MAX_AGE = 1, 120
MIN_WEIGHT_KG, MAX_WEIGHT_KG = 20.0, 300.0
MIN_HEIGHT_CM, MAX_HEIGHT_CM = 50.0, 250.0

def ask_for_age() -> int:
    while True:
        try:
            age = int(input(f"How old are you? ({MIN_AGE}-{MAX_AGE}, e.g., 21): "))
            if MIN_AGE <= age <= MAX_AGE:
                return age
            print(f"Please enter an age between {MIN_AGE} and {MAX_AGE}.")
        except ValueError:
            print("Please enter a whole number for age.")

def ask_for_weight() -> float:
    while True:
        try:
            weight = float(input(f"What's your current weight in kg? ({MIN_WEIGHT_KG:.0f}-{MAX_WEIGHT_KG:.0f}, e.g., 75.5): "))
            if MIN_WEIGHT_KG <= weight <= MAX_WEIGHT_KG:
                return weight
            print(f"Please enter a weight between {MIN_WEIGHT_KG:.0f} and {MAX_WEIGHT_KG:.0f} kg.")
        except ValueError:
            print("Please enter a number for weight (e.g., 70 or 68.5).")

def ask_for_height() -> float:
    """Prompt for height in cm, return it converted to metres."""
    while True:
        try:
            height_cm = float(input(f"What's your height in cm? ({MIN_HEIGHT_CM:.0f}-{MAX_HEIGHT_CM:.0f}, e.g., 175): "))
            if MIN_HEIGHT_CM <= height_cm <= MAX_HEIGHT_CM:
                return height_cm / 100  # store as metres for BMI/TDEE formulas
            print(f"Please enter a height between {MIN_HEIGHT_CM:.0f} and {MAX_HEIGHT_CM:.0f} cm.")
        except ValueError:
            print("Please enter a number for height (e.g., 170).")

def ask_for_goal() -> str:
    while True:
        goal = input("What's your main goal? Type 'weight loss' or 'muscle gain': ").strip().lower()
        if goal in ('weight loss', 'muscle gain'):
            return goal
        print("Please type exactly 'weight loss' or 'muscle gain'.")

def ask_for_gender() -> str:
    while True:
        gender = input("What's your gender? Type 'male' or 'female': ").strip().lower()
        if gender in ('male', 'female'):
            return gender
        print("Please type 'male' or 'female'.")

def get_user_profile():
    age = ask_for_age()
    weight = ask_for_weight()
    height_m = ask_for_height()
    gender = ask_for_gender()
    goal = ask_for_goal()
    return age, weight, height_m, gender, goal
