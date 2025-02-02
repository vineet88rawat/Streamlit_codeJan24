import streamlit as st
import pandas as pd
import requests
import json

# Define the API URL
api_url = 'https://your-api-url/predict'

# Define the function to get predictions from the API
def get_prediction(data):
    response = requests.post(api_url, json=data)
    prediction = response.json().get('prediction')
    return prediction

# Title
st.title('Insurance Price Prediction App')

# Input fields
age = st.number_input('Age', min_value=18, max_value=100, value=30)
any_transplants = st.selectbox('Any Transplants', options=[0, 1])
weight = st.number_input('Weight', min_value=30.0, max_value=200.0, value=70.0)
any_chronic_diseases = st.selectbox('Any Chronic Diseases', options=[0, 1])
history_of_cancer_in_family = st.selectbox('History of Cancer in Family', options=[0, 1])
number_of_major_surgeries = st.number_input('Number of Major Surgeries', min_value=0, max_value=10, value=0)
bmi = st.number_input('BMI', min_value=10.0, max_value=50.0, value=25.0)
blood_pressure_problems = st.selectbox('Blood Pressure Problems', options=[0, 1])
blood_pressure_problems_0 = st.selectbox('Blood Pressure Problems_0', options=[0, 1])
diabetes_0 = st.selectbox('Diabetes_0', options=[0, 1])
diabetes = st.selectbox('Diabetes', options=[0, 1])
diabetes_1 = st.selectbox('Diabetes_1', options=[0, 1])
height = st.number_input('Height', min_value=100.0, max_value=250.0, value=170.0)
known_allergies = st.selectbox('Known Allergies', options=[0, 1])

# Collect the inputs into a dictionary
input_data = {
    'Age': age,
    'AnyTransplants': any_transplants,
    'Weight': weight,
    'AnyChronicDiseases': any_chronic_diseases,
    'HistoryOfCancerInFamily': history_of_cancer_in_family,
    'NumberOfMajorSurgeries': number_of_major_surgeries,
    'BMI': bmi,
    'BloodPressureProblems': blood_pressure_problems,
    'BloodPressureProblems_0': blood_pressure_problems_0,
    'Diabetes_0': diabetes_0,
    'Diabetes': diabetes,
    'Diabetes_1': diabetes_1,
    'Height': height,
    'KnownAllergies': known_allergies
}

# Prediction
if st.button('Predict'):
    prediction = get_prediction(input_data)
    st.success(f'The estimated insurance price is: ${prediction:.2f}')

# Run the app
if __name__ == '__main__':
    st.run()
