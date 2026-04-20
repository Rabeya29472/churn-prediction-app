import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("churn_model.pkl")

st.set_page_config(page_title="Customer Churn App", page_icon="📊", layout="centered")

st.title(" Customer Churn Prediction App")
st.write("Fill in customer details to predict churn risk.")

st.markdown("---")



age = st.slider("Age", 18, 100, 30)

gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0   # keep consistent with your training

tenure = st.number_input("Tenure (months)", min_value=0, value=1)

monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)

contract = st.selectbox("Contract Type", ["Month-to-Month", "One-Year", "Two-Year"])

internet = st.selectbox("Internet Service", ["Fiber Optic", "DSL", "None"])

total_charges = st.number_input("Total Charges", min_value=0.0, value=100.0)

tech_support = st.selectbox("Tech Support", ["Yes", "No"])
tech_support = 1 if tech_support == "Yes" else 0

# --------- ENCODING ---------

contract_map = {
    "Month-to-Month": [1, 0, 0],
    "One-Year": [0, 1, 0],
    "Two-Year": [0, 0, 1]
}

internet_map = {
    "Fiber Optic": 1,
    "DSL": 0,
    "None": 2
}

contract_encoded = contract_map[contract]
internet_encoded = internet_map[internet]



input_data = np.array([[
    age,
    gender,
    tenure,
    monthly_charges,
    internet_encoded,
    total_charges,
    tech_support,
    *contract_encoded
]])

if st.button("🔮 Predict Churn"):
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error(" This customer is likely to CHURN")
        st.markdown(" Suggestion: Offer discount or retention plan")
    else:
        st.success(" This customer is likely to STAY")
        st.markdown(" Good customer retention risk")

st.markdown("---")
st.caption("Built with Streamlit | Churn Prediction Model")
