import streamlit as st
import joblib

# Load model
model = joblib.load(r"C:\Users\nurpe\Downloads\Bazlakunova_test_tasks_with_comments\Bazlakunova_test-tasks_3.1\best_m.pkl")

def predict_problems(overdues_max, overdues_mean, overdues_sum, n_loan_types, Age, gender, loan_year, loan_months):
    input_ = [[overdues_max, overdues_mean, overdues_sum, n_loan_types, Age, gender, loan_year, loan_months]]
    outcome = model.predict(input_)
    return outcome[0]

st.title("Credit Scoring")

# User input
overdues_max = st.number_input("Enter maximum overdues:", step=1)
overdues_mean = st.number_input("Enter mean overdues:", step=1)
overdues_sum = st.number_input("Enter sum overdues:", step=1)
n_loan_types = st.number_input("Enter number of loan types:", step=1)
Age = st.number_input("Enter age:", step=1)
gender = st.number_input("Enter gender (0=Male, 1=Female):", step=1)
loan_year = st.number_input("Enter loan year:", step=1)
loan_months = st.number_input("Enter loan months:", step=1)

if st.button("Predict customer credit rate type"):
    outcome = predict_problems(overdues_max, overdues_mean, overdues_sum, n_loan_types, Age, gender, loan_year, loan_months)
    mapp = {0:'Normal', 1:'Problematic'}
    st.write(f"Customer most likely is {mapp.get(outcome)}")
