import pandas as pd
import warnings
from src.content import GOAL_MAP
from src.data_manager import initialize_dataset, train_model, log_recommendation, view_logs, clear_logs
from src.health_metrics import calculate_bmi, show_bmi, show_water_intake, show_calorie_estimate
from src.input_helpers import get_user_profile
from src.recommender import show_recommendation

warnings.filterwarnings("ignore")

def run_recommendation_flow(model) -> None:
    print("\nGreat! Let's learn a little about you first.\n")

    age, weight, height_m, gender, goal = get_user_profile()

    print("\n" + "=" * 50)
    print("  Your Health Snapshot")
    print("=" * 50)
    show_bmi(weight, height_m)
    show_water_intake(weight)
    show_calorie_estimate(age, weight, height_m, goal, gender)
    print("=" * 50)

    goal_code = GOAL_MAP[goal]
    user_input = pd.DataFrame([[age, weight, goal_code]], columns=['age', 'weight_kg', 'goal_code'])
    prediction = model.predict(user_input)[0]

    show_recommendation(prediction, goal, gender)

    diet_summary = "Deficit" if goal == 'weight loss' else "Surplus"
    bmi = calculate_bmi(weight, height_m)
    log_recommendation(age, weight, height_m, gender, goal, prediction, diet_summary, bmi)
    print("\n Your recommendation has been saved! Keep up the great work!\n")


def main() -> None:
    print("==========================================")
    print("      AI Fitness & Diet Suggester         ")
    print("==========================================")

    initialize_dataset()

    model = train_model()
    if model is None:
        print("Sorry, we ran into a problem loading the fitness model. Please try restarting the app.")
        return

    while True:
        print("\nWhat would you like to do?")
        print("  1.   Get a personalized fitness & diet recommendation")
        print("  2.   View my past recommendations")
        print("  3.   Clear all logs")
        print("  4.   Exit")

        try:
            choice = input("\nYour choice (1, 2, 3, or 4): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nShutting down system. Goodbye!")
            break

        if choice == '1':
            run_recommendation_flow(model)
        elif choice == '2':
            view_logs()
        elif choice == '3':
            clear_logs()
        elif choice == '4':
            print("Shutting down system. Goodbye!")
            break
        else:
            print("Hmm, that's not a valid option. Please type 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
