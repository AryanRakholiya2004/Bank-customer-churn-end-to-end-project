import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle

model = load_model("deep_model.h5")

st.title("Deep Learning Predictor")
inputs = []

credit_score = st.number_input("Credit Score", value=777.0,max_value=1000.0)
geography = st.selectbox("Geography", ["France", "Germany", "Spain"])
gender = st.radio("Gender",["Male","Female"])
age = st.number_input("Age", value=18, min_value=18, max_value=100)
tenure = st.number_input("Tenure (in Years)", value=3, min_value=0, max_value=10)
balance = st.number_input("Balance", value=50000.0)
num_of_products = st.number_input("Number of Products", value=1, min_value=1, max_value=10)
is_active_member = st.radio("Is Active Member", ["Yes", "No"])
has_credit_card = st.radio("Has Credit Card", ["Yes", "No"])
estimated_salary = st.number_input("Estimated Salary", value=50000.0)

inputs.append(credit_score)
inputs.append(geography)
inputs.append(gender)
inputs.append(age)
inputs.append(tenure)
inputs.append(balance)
inputs.append(num_of_products)
inputs.append(is_active_member)
inputs.append(has_credit_card)
inputs.append(estimated_salary)

# Load the preprocessor
with open("preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)
    print(type(preprocessor))
    print(type(preprocessor))
    print(type(preprocessor))
    print(type(preprocessor))

# Transform the inputs
inputs = np.array([inputs])  # Convert to 2D array
print(inputs)
import pandas as pd

# Convert inputs to a DataFrame with appropriate column names
input_columns = ["Credit Score", "Geography", "Gender", "Age", "Tenure", "Balance", 
                 "Number of Products", "Is Active Member", "Has Credit Card", "Estimated Salary"]
inputs_df = pd.DataFrame(inputs, columns=input_columns)
print(inputs_df)

# Transform the inputs
inputs = preprocessor.transform(inputs_df)

print(inputs)

if st.button("Predict"):
    prediction = model.predict(inputs)
    st.success(f"Prediction: {prediction[0][0]:.4f}")
