# Problem Statement

People starting a fitness journey are often given generic, one-size-fits-all
workout advice that ignores who they actually are — their age, weight,
build, and specific goal. Weight loss and muscle gain call for different
training and nutrition strategies, and advice that doesn't account for that
difference is not very useful. Without access to a coach or trainer, most
people fall back on searching online, where recommendations are inconsistent
and rarely tailored to the individual.

## Scope

This project is a command-line application that:

- Collects a short personal profile (age, weight, height, gender, fitness goal)
- Predicts a suitable workout type using a K-Nearest Neighbours (KNN)
  classifier trained on a small labelled dataset
- Computes a health snapshot (BMI, daily water intake target, estimated
  calorie needs) using standard formulas
- Returns a full weekly workout routine and a goal-based diet plan
- Logs every recommendation to a CSV file so a user can review their history

It is scoped as a single-user, offline, CLI tool — it does not cover
multi-user accounts, a persistent database, or a graphical interface.

## Target Users

- Beginners starting a fitness routine without access to a personal trainer
- Anyone who wants a quick, personalized starting point for workout and diet
  choices based on simple, explainable inputs

## High-Level Features

- ML-based workout type recommendation (Cardio / Weightlifting / Yoga / HIIT)
- Goal-based diet plan (calorie deficit for weight loss, surplus for muscle gain)
- BMI, water intake, and TDEE (calorie) calculation
- Gender-specific coaching tips
- Input validation on every field, with sane real-world ranges
- Session history logging, viewing, and clearing via CSV
