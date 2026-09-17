"""
content.py — Static reference content used by the recommender.

Keeping this text separate from the program logic (data-manager,
health-metrics, CLI) makes the project easier to navigate and lets
you extend the plans/tips without touching any actual logic.
"""

# Maps a user-typed goal string to the numeric code the ML model
# was trained on.
GOAL_MAP = {
    'weight loss': 0,
    'muscle gain': 1,
}

WORKOUT_ROUTINES = {
    'Cardio': """
    Weekly Cardio & Endurance Plan:
    - Monday: 30 min steady-state jogging or brisk walking.
    - Tuesday: 20 min cycling or swimming.
    - Wednesday: Active rest (light stretching or 15 min walk).
    - Thursday: 30 min interval running (1 min fast, 2 min slow).
    - Friday: 45 min brisk walk or hiking.
    - Weekend: Rest or recreational sports.
    """,
    'Weightlifting': """
    Weekly Muscle Gain (Push/Pull/Legs) Plan:
    - Monday: Push Day (Bench press, overhead press, triceps extensions).
    - Tuesday: Pull Day (Barbell rows, pull-ups/lat pulldowns, bicep curls).
    - Wednesday: Rest and recovery.
    - Thursday: Leg Day (Squats, lunges, Romanian deadlifts, calf raises).
    - Friday: Full Body or weak-point focus (light weight, high reps).
    - Weekend: Rest and light walking.
    """,
    'Yoga': """
    Weekly Flexibility & Core (Yoga) Plan:
    - Monday: 45 min Vinyasa flow (full body mobility).
    - Tuesday: 30 min core-focused Pilates or Yoga.
    - Wednesday: Rest.
    - Thursday: 45 min Hatha Yoga (focusing on holding poses).
    - Friday: 30 min Restorative or Yin Yoga for deep stretching.
    - Weekend: Active rest.
    """,
    'HIIT': """
    Weekly High-Intensity Interval Training (HIIT) Plan:
    - Monday: 20 min Bodyweight HIIT (30s work, 30s rest: burpees, squats).
    - Tuesday: Active recovery (light stretching or walking).
    - Wednesday: 25 min Dumbbell HIIT or Kettlebell swings.
    - Thursday: Rest.
    - Friday: 20 min Sprint intervals (on a track, bike, or treadmill).
    - Weekend: Rest.
    """,
}

DIET_PLANS = {
    'weight loss': """
    Nutrition Plan: Caloric Deficit & High Satiety Focus
    - Breakfast: Oatmeal with berries or a 3-egg-white spinach omelet.
    - Lunch: Grilled chicken salad with a light vinaigrette.
    - Snack: Greek yogurt or a small handful of almonds.
    - Dinner: Baked salmon or tofu with roasted asparagus and a small portion of quinoa.
    - Hydration: Minimum 3 liters of water daily. Replace sugary drinks with black coffee or green tea.
    """,
    'muscle gain': """
    Nutrition Plan: Caloric Surplus & High Protein Focus
    - Breakfast: 3 scrambled whole eggs, 2 slices of whole-wheat toast, and a protein shake.
    - Lunch: Large portion of chicken breast, brown rice, and steamed broccoli.
    - Snack: Peanut butter on rice cakes or a bowl of cottage cheese.
    - Dinner: Lean steak or ground turkey, sweet potato, and mixed vegetables.
    - Post-Workout: Whey protein isolate and a banana.
    """,
}

# One short tip per workout type, per gender, shown at the end of the plan.
GENDER_WORKOUT_TIPS = {
    'male': {
        'Cardio': 'Focus on maintaining a strong pace. Track your heart rate to stay in the fat-burn zone (60-70% max HR).',
        'Weightlifting': 'Progressive overload is key — try to add small weight or an extra rep each week.',
        'Yoga': "Don't skip the strength-focused poses like Warrior and Chair — they build functional muscle.",
        'HIIT': 'Push hard on the work intervals. Your recovery will improve fast with consistency.',
    },
    'female': {
        'Cardio': 'Mix in incline walking — it targets glutes and burns more calories than flat jogging.',
        'Weightlifting': "Don't fear heavier weights. Lifting heavy won't bulk you up — it'll tone and strengthen.",
        'Yoga': 'Hip-opening poses like Pigeon and Lizard are especially beneficial. Prioritise them.',
        'HIIT': 'Lower-body focused HIIT (glute bridges, jump squats) will complement your goals well.',
    },
}

BMI_NOTES = {
    "Underweight":   "Consider increasing calorie intake with nutrient-dense foods.",
    "Normal weight": "Great foundation to work with! Focus on your goal.",
    "Overweight":    "A mix of cardio and strength work will help a lot.",
    "Obese":         "Start with low-impact exercise and consult a doctor if unsure.",
}
