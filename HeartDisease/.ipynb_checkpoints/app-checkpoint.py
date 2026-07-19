import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('model.pkl')

st.title("Heart Disease Prediction App")
st.write("Enter the following details to predict heart disease:")

bmi = st.number_input(
    "Enter BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

smoking = st.selectbox(
    "Do you smoke?",
    ["No", "Yes"]
)

stroke = st.selectbox(
    "Have you ever had a stroke?",
    ["No", "Yes"]
)

diabetic = st.selectbox(
    "Are you diabetic?",
    ["No", "Yes"]
)

physical_activity = st.selectbox(
    "Do you do regular physical activity?",
    ["No", "Yes"]
)

diff_walking = st.selectbox(
    "Do you have difficulty walking?",
    ["No", "Yes"]
)

smoking = 1 if smoking == "Yes" else 0
stroke = 1 if stroke == "Yes" else 0
diabetic = 1 if diabetic == "Yes" else 0
physical_activity = 1 if physical_activity == "Yes" else 0
diff_walking = 1 if diff_walking == "Yes" else 0

if st.button("Predict"):
    prediction = model.predict([[
        bmi,
        smoking,
        stroke,
        diabetic,
        physical_activity,
        diff_walking
    ]])

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")