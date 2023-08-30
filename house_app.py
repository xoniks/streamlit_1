import streamlit as st 
import pandas as pd
import numpy as np
import pickle 
from sklearn.linear_model import LogisticRegression

st.title('Real Estate Price Predictor')

st.sidebar.header("Upload Pre-trained Model")
model_upload = st.sidebar.file_uploader("Upload a Pickle Model File", type=["pkl","sav"])


model = None
if model_upload is not None:
    with model_upload as file:
        model = pickle.load(file)

def get_user_input():
    avg_income = st.sidebar.number_input('Avg. Area Income')
    avg_age = st.sidebar.number_input('Avg. Area house age')
    avg_rooms = st.sidebar.number_input('Avg. Number of Rooms')
    avg_bedrooms = st.sidebar.number_input('Avg. Number of Bedrooms')
    area_population = st.sidebar.number_input('Area Population')
    return np.array([avg_income,avg_age,avg_rooms,avg_bedrooms,area_population]).reshape(1,-1)

if model is not None:
    st.subheader("Make a Prediction")
    user_input = get_user_input()
    if st.button("Predict Price"):
        predicted_price = model.predict(user_input)[0]
        st.subheader(f"Predicted house price: ${predicted_price:,.2f}")

if model is None:
    st.warning('Please upload a pre-trained model before prediction')