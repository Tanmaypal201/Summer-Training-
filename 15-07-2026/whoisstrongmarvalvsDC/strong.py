import pandas as pd
import numpy as np
import streamlit as st
import joblib
import streamlit as st

model = joblib.load('IwillMakeit.pkl')

st.set_page_config(page_title="Character Battle Predictor", page_icon="⚔️")

st.title("⚔️ Fictional Character Battle Predictor")
character_map = {
    "Wonder Woman": 0,
    "Iron Man": 1,
    "Spider-Man": 2,
    "Flash": 3,
    "Thor": 4,
    "Batman": 5,
    "Superman": 6,
    "Captain America": 7
}

universe_map = {
    "DC Comics": 0,
    "Marvel": 1
}

ability_map = {
    "Telekinesis": 0,
    "Invisibility": 1,
    "Super Strength": 2,
    "Flight": 3
}

weakness_map = {
    "Kryptonite": 0,
    "Magic": 1,
    "Wooden Stake": 2,
    "Silver": 3
}
character = st.selectbox(
    "Character",
    list(character_map.keys())
)

universe = st.selectbox(
    "Universe",
    list(universe_map.keys())
)

strength = st.slider(
    "Strength",
    min_value=1,
    max_value=100,
    value=50
)

speed = st.slider(
    "Speed",
    min_value=1,
    max_value=100,
    value=50
)

intelligence = st.slider(
    "Intelligence",
    min_value=1,
    max_value=100,
    value=50
)

ability = st.selectbox(
    "Special Ability",
    list(ability_map.keys())
)

weakness = st.selectbox(
    "Weakness",
    list(weakness_map.keys())
)


if st.button("Predict Battle Outcome"):

    data = pd.DataFrame({
        "Character":[character_map[character]],
        "Universe":[universe_map[universe]],
        "Strength":[strength],
        "Speed":[speed],
        "Intelligence":[intelligence],
        "SpecialAbilities":[ability_map[ability]],
        "Weaknesses":[weakness_map[weakness]]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("🏆 Battle Result : WIN")
    else:
        st.error("❌ Battle Result : LOSE")