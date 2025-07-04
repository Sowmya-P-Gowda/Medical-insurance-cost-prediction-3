# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1n97MF5Ln52bjMCqox_YYIlm0Nph4FRz8
"""

import streamlit as st
import numpy as np
import pickle

# Set up page
st.set_page_config(page_title="Medical Insurance Cost Predictor", layout="centered")

st.title("💰 Medical Insurance Cost Predictor")
st.subheader("Enter User Details")

# Input fields
age = st.slider("Age", 18, 100, 30)
sex_input = st.radio("Sex", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0, step=0.1)
children = st.slider("Number of Children", 0, 5, 1)
smoker_input = st.selectbox("Smoker", ["No", "Yes"])
region_input = st.selectbox("Region", ['Southeast', 'Southwest', 'Northeast', 'Northwest'])

# Encode inputs
sex = 0 if sex_input == "Male" else 1
smoker = 1 if smoker_input == "Yes" else 0
region_dict = {'Southeast': 0, 'Southwest': 1, 'Northeast': 2, 'Northwest': 3}
region = region_dict[region_input]

# Feature engineering
obese_smoker = int(bmi >= 30 and smoker == 1)

# Encode bmi_category
if bmi < 18.5:
    bmi_category = 3  # Underweight
elif bmi < 25:
    bmi_category = 2  # Normal
elif bmi < 30:
    bmi_category = 0  # Overweight
else:
    bmi_category = 1  # Obese

# Final feature array in same order as training
user_input = np.array([[age, sex, bmi, children, smoker, region, obese_smoker, bmi_category]])

# Load model
with open("random_forest_model (4).pkl", "rb") as file:
    model = pickle.load(file)

# Prediction
if st.button("Predict Insurance Cost"):
    prediction = model.predict(user_input)[0]
    st.success(f"💡 Estimated Medical Insurance Cost: ₹{round(prediction, 2)}")
