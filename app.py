import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("📊 Customer Churn Prediction App")
st.write("Enter customer details below to predict churn probability.")

# Example input fields (you can adjust according to your model features)
gender = st.selectbox("Gender", ["Male", "Female"])
senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0, max_value=200, value=70)
total_charges = tenure * monthly_charges

# Convert categorical inputs to numeric
gender_val = 1 if gender == "Male" else 0
senior_val = 1 if senior_citizen == "Yes" else 0
partner_val = 1 if partner == "Yes" else 0
dependents_val = 1 if dependents == "Yes" else 0

# Final feature array (⚠️ adjust order/features to match your model training)
features = np.array([[gender_val, senior_val, partner_val, dependents_val, tenure, monthly_charges, total_charges]])

if st.button("🔮 Predict"):
    prediction = model.predict_proba(features)[0][1]  # probability of churn
    st.success(f"Churn Probability: **{prediction:.2f}**")
