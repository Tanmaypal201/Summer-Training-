import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('decision_perfect.pkl')

import streamlit as st

st.title("🔥 Calories Burned Prediction")

age = st.slider("Age", min_value=10, max_value=80, value=25)
gender = st.selectbox(
    "Gender",
    options=[0, 1],
    format_func=lambda x: "Male" if x == 1 else "Female"
)
weight = st.number_input(
    "Weight (kg)",
    min_value=30.0,
    max_value=200.0,
    value=70.0,
    step=0.5
)
height = st.number_input(
    "Height (m)",
    min_value=1.0,
    max_value=2.5,
    value=1.70,
    step=0.01
)
max_bpm = st.slider(
    "Maximum BPM",
    min_value=100,
    max_value=220,
    value=180
)

avg_bpm = st.slider(
    "Average BPM",
    min_value=60,
    max_value=200,
    value=130
)

resting_bpm = st.slider(
    "Resting BPM",
    min_value=40,
    max_value=120,
    value=70
)
session_duration = st.number_input(
    "Session Duration (hours)",
    min_value=0.5,
    max_value=5.0,
    value=1.0,
    step=0.1
)
workout_type = st.selectbox(
    "Workout Type",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Yoga",
        2: "HIIT",
        3: "Cardio",
        4: "Strength"
    }[x]
)
fat_percentage = st.slider(
    "Fat Percentage",
    min_value=5.0,
    max_value=50.0,
    value=20.0,
    step=0.1
)

water_intake = st.number_input(
    "Water Intake (liters)",
    min_value=0.5,
    max_value=10.0,
    value=2.5,
    step=0.1
)

workout_frequency = st.slider(
    "Workout Frequency (days/week)",
    min_value=1,
    max_value=7,
    value=4
)

experience_level = st.selectbox(
    "Experience Level",
    options=[1, 2, 3],
    format_func=lambda x: {
        1: "Beginner",
        2: "Intermediate",
        3: "Advanced"
    }[x]
)
bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=50.0,
    value=22.0,
    step=0.1
)

input_data = pd.DataFrame({
    "Age": [age],
    "Gender": [gender],
    "Weight (kg)": [weight],
    "Height (m)": [height],
    "Max_BPM": [max_bpm],
    "Avg_BPM": [avg_bpm],
    "Resting_BPM": [resting_bpm],
    "Session_Duration (hours)": [session_duration],
    "Workout_Type": [workout_type],
    "Fat_Percentage": [fat_percentage],
    "Water_Intake (liters)": [water_intake],
    "Workout_Frequency (days/week)": [workout_frequency],
    "Experience_Level": [experience_level],
    "BMI": [bmi]
})

if st.button("Predict Calories Burned"):
    prediction = model.predict(input_data)
    st.success(f"🔥 Estimated Calories Burned: {prediction[0]:.2f} kcal")