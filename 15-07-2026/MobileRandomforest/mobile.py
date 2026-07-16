import pandas as pd
import numpy as np
import streamlit as st
import joblib

model = joblib.load('mobileprice.pkl')

import streamlit as st
st.title("📱 Mobile Price Prediction")
st.subheader("Enter Mobile Specifications")
ratings = st.slider("⭐ Ratings", 3.0, 5.0, 4.0, 0.1)
ram = st.slider("RAM (GB)", 2, 16, 8)
rom = st.slider("ROM (GB)", 8, 512, 128)
mobile_size = st.number_input(
    "Mobile Size (inches)",
    min_value=2.0,
    max_value=44.0,
    value=6.5,
    step=0.1
)
primary_cam = st.number_input(
    "Primary Camera (MP)",
    min_value=5,
    max_value=64,
    value=50,
    step=1
)
selfie_cam = st.number_input(
    "Selfie Camera (MP)",
    min_value=0,
    max_value=23,
    value=16,
    step=1
)
battery_power = st.number_input(
    "Battery Power (mAh)",
    min_value=1020,
    max_value=6000,
    value=5000,
    step=100
)
input_df = pd.DataFrame({
    "Ratings": [ratings],
    "RAM": [ram],
    "ROM": [rom],
    "Mobile_Size": [mobile_size],
    "Primary_Cam": [primary_cam],
    "Selfi_Cam": [selfie_cam],
    "Battery_Power": [battery_power]
})

if st.button("Predict Price 💰"):
    prediction = model.predict(input_df)

    st.success(f"Predicted Mobile Price: ₹ {prediction[0]:,.2f}")