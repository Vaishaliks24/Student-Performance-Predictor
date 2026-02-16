import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt

# Load model safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "student_model.pkl")
model = joblib.load(MODEL_PATH)

st.title("🎓 Student Performance Predictor")

# ---- INPUT FIELDS ----

age = st.number_input("Age", 15, 25, 17)
G1 = st.number_input("G1 (First Period Grade)", 0, 20, 10)
G2 = st.number_input("G2 (Second Period Grade)", 0, 20, 10)
studytime = st.slider("Study Time (1-4)", 1, 4, 2)
absences = st.number_input("Absences", 0, 100, 5)
failures = st.slider("Past Failures (0-3)", 0, 3, 0)

if st.button("Predict"):

    input_df = pd.DataFrame({
        "age": [age],
        "G1": [G1],
        "G2": [G2],
        "studytime": [studytime],
        "absences": [absences],
        "failures": [failures]
    })

    prediction = model.predict(input_df)

    st.success(f"Predicted Final Grade (G3): {prediction[0]:.2f}")

importances = model.named_steps['regressor'].feature_importances_
features = model.feature_names_in_

plt.bar(features, importances)
plt.xticks(rotation=45)
st.pyplot(plt)