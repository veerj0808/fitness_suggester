"""
recommender.py — formats and prints the workout + diet recommendation.
"""

from src.content import WORKOUT_ROUTINES, DIET_PLANS, GENDER_WORKOUT_TIPS


def show_recommendation(prediction: str, goal: str, gender: str) -> None:
    """Print the recommended workout and diet plan in a readable format."""
    print("\n Crunching the numbers... Here's what we recommend for you!")

    print(f"\n Your Recommended Workout Style: {prediction}")
    print("-" * 50)
    print(WORKOUT_ROUTINES.get(prediction, "No detailed plan available for this workout type yet."))

    tip = GENDER_WORKOUT_TIPS.get(gender, {}).get(prediction)
    if tip:
        print(f"  Tip for you: {tip}")

    print(f"\n Your Nutrition Approach: {goal.title()}")
    print("-" * 50)
    print(DIET_PLANS.get(goal, "No detailed diet plan available."))
    print("-" * 50)
