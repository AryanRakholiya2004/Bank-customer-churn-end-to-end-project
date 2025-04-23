import streamlit as st
import pandas as pd
import joblib
import os

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

# Load the trained machine learning model
model_path = os.path.join(base_dir, "artifacts", "model.pkl")
with open(model_path, "rb") as f:
    model = joblib.load(f)
    print('=x='*50)
    print(model)
    print(type(model))
    print('=x='*50)

# Load the preprocessor
preprocessor_path = os.path.join(base_dir, "artifacts", "preprocessor.pkl")
with open(preprocessor_path, "rb") as f:
    preprocessor = joblib.load(f)
    print('=x='*50)
    print(preprocessor)
    print(type(preprocessor))
    print('=x='*50)

# Streamlit app title
st.title("Customer Churn Prediction")
st.subheader("Decision Tree Classifier - Predict whether a customer will churn or not")

# Input fields for user data
credit_score = st.number_input("Credit Score", value=777.0, max_value=1000.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.radio("Gender", ["Male", "Female"])
age = st.number_input("Age", value=18, min_value=18, max_value=100)
tenure = st.number_input("Tenure (in Years)", value=3, min_value=0, max_value=10)
balance = st.number_input("Balance", value=50000.0)
num_of_products = st.number_input("Number of Products", value=1, min_value=1, max_value=10)
is_active_member = st.radio("Is Active Member", ["Yes", "No"])
has_credit_card = st.radio("Has Credit Card", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", value=50000.0)

# Collect inputs into a list
inputs = [
    credit_score,
    geography,
    gender,
    age,
    tenure,
    balance,
    num_of_products,
    is_active_member,
    has_credit_card,
    estimated_salary,
]

# Convert inputs to a DataFrame with appropriate column names
input_columns = [
    "CreditScore",
    "Geography",
    "Gender",
    "Age",
    "Tenure",
    "Balance",
    "NumOfProducts",
    "isActiveMember",
    "HasCrCard",
    "EstimatedSalary",
]
# Convert inputs to a DataFrame with appropriate column names
inputs_df = pd.DataFrame([inputs], columns=input_columns)

# Handle categorical variables
inputs_df["Geography"] = inputs_df["Geography"].astype(str)
inputs_df["Gender"] = inputs_df["Gender"].astype(str)
inputs_df["isActiveMember"] = inputs_df["isActiveMember"].map({"Yes": 1, "No": 0})
inputs_df["HasCrCard"] = inputs_df["HasCrCard"].map({"Yes": 1, "No": 0})

# Transform the inputs using the preprocessor
try:
    transformed_inputs = preprocessor.transform(inputs_df)
except Exception as e:
    st.error(f"Error in preprocessing inputs: {e}")
    st.stop()

# Predict button
if st.button("Predict"):
    try:
        # Make prediction
        prediction = model.predict(transformed_inputs)
        # Map prediction to classification outcome
        outcome = "Churned" if prediction[0] == 1 else "Not Churned"
        st.success(f"Prediction: {outcome}")
    except Exception as e:
        st.error(f"Error in making prediction: {e}")
