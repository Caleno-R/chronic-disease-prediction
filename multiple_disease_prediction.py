# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 09:17:06 2022

@author: Caleno
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
        
    selected = option_menu('Multiple  Chronic Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           
                           icons = ['activity', 'heart', 'person'],
                           
                           default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Patient Diabetes Prediction System')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value = 0)
    
    with col2:
        Glucose = st.number_input('Glucose Level in mg/dL', min_value = 0)

    with col3:
        BloodPressure = st.number_input('Blood Pressure Value in mmHg', min_value = 0)

    with col1:
        SkinThickness = st.number_input('Skin Thickness Value in mm', min_value = 0)

    with col2:
        Insulin = st.number_input('Insulin Level in mcU/mL', min_value =0)

    with col3:
        BMI = st.number_input('BMI Value in kg/m2', min_value = 0.00)

    with col1:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function Value', min_value = 0.000)

    with col2:
        Age = st.number_input('Age of the Person', min_value = 0)
    
    #code for prediction
    diab_diagnosis = ''
    
    #creating prediction Button
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies,Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis = 'This patient is diabetic'
            
        else:
            diab_diagnosis = 'The patient is not diabetic'
    
    st.success(diab_diagnosis)
        
    
# Heart Disease Prediction Page    
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title(' Patient Heart Disease Prediction System')
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.number_input('Age', min_value = 0, max_value = 95)
    
    with col2:
        sex = st.number_input('sex (1 = male; 0 = female)', min_value = 0, max_value = 1)

    with col1:
        cp = st.number_input('Chest Pain Types (4 values)', min_value = 0, max_value = 4)

    with col2:
        trestbps = st.number_input('Resting Blood Pressure', min_value = 0, max_value = 300)

    with col1:
        chol = st.number_input('Serum Cholestoral in mg/dl', min_value =0, max_value = 570)

    with col2:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', min_value = 0, max_value = 1)

    with col1:
        restecg = st.number_input('Resting Electrocardiographic Results (values 0,1,2)', min_value = 0, max_value = 2)

    with col2:
        thalach = st.number_input('Maximum Heart Rate Achieved', min_value = 0, max_value = 300)
        
    with col1:
        exang = st.number_input('Exercise Induced Angina (1 = yes; 0 = no)', min_value = 0, max_value = 1)

    with col2:
        oldpeak = st.number_input('ST depression induced by exercise relative to rest', min_value = 0, max_value = 7)
        
    with col1:
        slope = st.number_input('Peak exercise ST segment Slope', min_value = 0, max_value = 2)
        
    with col2:
        ca = st.number_input('Major vessels colored by flourosopy (0-3)', min_value = 0, max_value = 4)
        
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect', min_value = 0, max_value = 5)
    
    #code for prediction
    heart_diagnosis = ''
    
    #creating prediction Button
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The person has a heart disease'
            
        else:
            heart_diagnosis = 'The person does not have any heart disease'
    
    st.success(heart_diagnosis)
        
        
# Parkinson's Prediction Page
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Patient Parkinsons Disease Prediction System')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        fo = st.number_input('Average vocal fundamental frequency (Hz)', min_value = 0.0, format="%.3f")
    
    with col2:
        fhi = st.number_input('Maximum vocal fundamental frequency (Hz)', min_value = 0.0, format="%.3f")

    with col3:
        flo = st.number_input('Minimum vocal fundamental frequency (Hz)', min_value = 0.0, format="%.3f")

    with col1:
        Jitter_percent = st.number_input('Measure of variation in fundamental frequency MDVP:Jitter(%)', min_value = 0.0, format="%.5f")

    with col2:
        Jitter_Abs = st.number_input('Measure of variation in fundamental frequency MDVP:Jitter(Abs)', min_value = 0.0, format="%.5f")

    with col3:
        RAP = st.number_input(' Measure of variation in fundamental frequency MDVP:RAP', min_value = 0.0, format="%.5f")

    with col1:
        PPQ = st.number_input('Measure of variation in fundamental frequency MDVP:PPQ', min_value = 0.0, format="%.5f")

    with col2:
        DDP = st.number_input('Measure of variation in fundamental frequency Jitter:DDP', min_value = 0.0, format="%.5f")
        
    with col3:
        Shimmer = st.number_input('Measure of variation in amplitude MDVP:Shimmer', min_value = 0.0, format="%.5f")

    with col1:
        Shimmer_dB = st.number_input('Measure of variation in amplitudeMDVP:Shimmer(dB)', min_value = 0.0, format="%.5f")
        
    with col2:
        APQ3 = st.number_input('Measure of variation in amplitude Shimmer:APQ3', min_value = 0.0, format="%.5f")
        
    with col3:
        APQ5 = st.number_input('Measure of variation in amplitude Shimmer:APQ5', min_value = 0.0, format="%.5f")
        
    with col1:
        APQ = st.number_input('Measure of variation in amplitude Shimmer:APQ', min_value = 0.0, format="%.5f")        
        
    with col2:
        DDA = st.number_input('Measure of variation in amplitude Shimmer:DDA', min_value = 0.0, format="%.5f")        
        
    with col3:
        NHR = st.number_input('Measure of ratio of noise to tonal components in the voiceNHR', min_value = 0.0, format="%.5f")
        
    with col1:
        HNR = st.number_input('Measure of ratio of noise to tonal components in the voiceHNR', min_value = 0.0, format="%.3f")
        
    with col2:
        RPDE = st.number_input('Nonlinear dynamical complexity measure (RPDE)', min_value = 0.0, format="%.6f")
        
    with col3:
        DFA = st.number_input('Signal fractal scaling exponent DFA', min_value = 0.0, format="%.6f")
        
    with col1:
        spread1 = st.number_input('Nonlinear measure of fundamental frequency variation (spread1)', min_value = 0.0, format="%.6f")

    with col2:
        spread2 = st.number_input('Nonlinear measure of fundamental frequency variation (spread2)',  min_value = 0.0, format="%.6f")
        
    with col3:
        D2 = st.number_input('Nonlinear dynamical complexity measure (D2)', min_value = 0.0, format="%.6f")
        
    with col1:
        PPE = st.number_input('Nonlinear measure of fundamental frequency variation (PPE)', min_value = 0.0, format="%.6f")
        
    #code for prediction
    parkinsons_diagnosis = ''
    
    #creating prediction Button
   
    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
    
    st.success(parkinsons_diagnosis)
        
            
    
    

    
