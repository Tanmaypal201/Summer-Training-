import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

st.title("🏠 House Price Prediction")

df = pd.read_csv("HouseVSPrice.csv")
df.isnull().sum()
X = df[['House_Size_sqft']]
Y = df['House_Price_Lakhs']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, Y_train)   

house_size = st.number_input(
    "Enter House Size (sq ft)",
    min_value=500,
    max_value=10000
)

if st.button("Predict"):
    prediction = model.predict([[house_size]])
    st.subheader(" Prediction Result")
    st.write(f"House Size : {house_size} sq ft")
    st.write(f"Predicted Price : ₹{prediction[0]:.2f} Lakhs")
    st.success("Prediction Completed Successfully ✅")