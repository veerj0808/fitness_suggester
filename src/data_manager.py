"""
data_manager.py — dataset bootstrap, ML model training, and CSV logging.

FIX vs. the original script: file paths were bare filenames
('fitness_dataset.csv'), so the program only worked if you happened
to run it from inside the folder that held the CSVs. Paths here are
built from the project root, so `python3 main.py` works from any
directory, and the dataset/logs live in clearly separate data/ and
logs/ folders instead of the project root.
"""

import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(PROJECT_ROOT, 'data')
LOGS_DIR = os.path.join(PROJECT_ROOT, 'logs')

DATA_FILE = os.path.join(DATA_DIR, 'fitness_dataset.csv')
LOG_FILE = os.path.join(LOGS_DIR, 'user_recommendation_logs.csv')


def initialize_dataset() -> None:
    """Create a starter dataset if one doesn't exist yet."""
    if os.path.exists(DATA_FILE):
        return

    os.makedirs(DATA_DIR, exist_ok=True)
    print("Setting things up for the first time — this will only take a moment!")

    data = {
        'age': [18, 22, 25, 30, 45, 50, 20, 23, 35, 40, 28, 55],
        'weight_kg': [60, 85, 70, 95, 65, 90, 55, 100, 80, 75, 68, 88],
        'goal_code': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
        'workout_type': [
            'Cardio', 'Weightlifting', 'Cardio', 'Weightlifting',
            'Yoga', 'Weightlifting', 'Cardio', 'Weightlifting',
            'HIIT', 'Weightlifting', 'Cardio', 'Yoga',
        ],
    }

    pd.DataFrame(data).to_csv(DATA_FILE, index=False)
    print("All set! Let's get started.\n")


def train_model():
    """Load the dataset and train a KNN classifier to predict workout type."""
    try:
        df = pd.read_csv(DATA_FILE)
        X = df[['age', 'weight_kg', 'goal_code']]
        y = df['workout_type']

        model = KNeighborsClassifier(n_neighbors=3)
        model.fit(X, y)
        return model

    except Exception as e:
        print(f"Oops! Something went wrong while loading the fitness model: {e}")
        return None


def log_recommendation(age, weight, height_m, gender, goal, workout, diet_type, bmi) -> None:
    os.makedirs(LOGS_DIR, exist_ok=True)

    entry = pd.DataFrame({
        'Age': [age],
        'Weight_kg': [weight],
        'Height_m': [height_m],
        'BMI': [bmi],
        'Gender': [gender.title()],
        'Goal': [goal.title()],
        'Recommended_Workout': [workout],
        'Diet_Focus': [diet_type],
    })

    write_header = not os.path.exists(LOG_FILE)
    entry.to_csv(LOG_FILE, mode='a', header=write_header, index=False)


def view_logs() -> None:
    if not os.path.exists(LOG_FILE):
        print("\nNo previous logs found. Generate a recommendation first.\n")
        return

    print("\n Here's a look at your past recommendations:\n")
    logs = pd.read_csv(LOG_FILE)
    print(logs.to_string(index=False))
    print("\n(That's all of them so far!)\n")


def clear_logs() -> None:
    if not os.path.exists(LOG_FILE):
        print("\nThere are no logs to clear.\n")
        return

    confirm = input("Are you sure you want to delete all logs? This can't be undone. (yes/no): ").strip().lower()
    if confirm == 'yes':
        os.remove(LOG_FILE)
        print("Logs cleared successfully.\n")
    else:
        print("No changes made.\n")
