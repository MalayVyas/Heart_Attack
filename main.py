import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb
import numpy as np
st.header("Heart Attack Prediction App")

st.write("This app is currently under maintenance, please try later")

st.text_input("Enter your Name: ", key="name")
data = pd.read_csv("heart.csv",sep=",")
# load label encoder
# encoder = LabelEncoder()
# encoder.classes_ = np.load('classes.npy', allow_pickle=True)
# load model
best_xgboost_model = xgb.XGBRegressor()
best_xgboost_model.load_model("best_model.json")

if st.checkbox('Show Training Dataframe'):
    data


input_age = st.slider('Age', 0, int(max(data["age"])), 1)

st.write("1: Male")
st.write("0: Female");

input_sex = st.slider('sex', 0, int(max(data["sex"])), 1)
st.write("cp : Chest Pain type chest pain type:")
st.write("Value 1: typical angina")
st.write("Value 2: atypical angina")
st.write("Value 3: non-anginal pain")
st.write("Value 4: asymptomatic")
input_cp = st.slider('CP', 0, int(max(data["cp"])), 1)
st.write("trtbps : resting blood pressure (in mm Hg)")
input_trtbps = st.slider('trtbps', 0, int(max(data["trtbps"])), 1)
st.write("chol : cholestoral in mg/dl fetched via BMI sensor")
input_chol = st.slider('Cholestrol', 0, int(max(data["chol"])), 1)
st.write("fbs : (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)")
input_fbs = st.slider('fbs', 0, int(max(data["fbs"])), 1)
st.write("rest_ecg : resting electrocardiographic results")
input_restecg = st.slider('restecg', 0, int(max(data["restecg"])), 1)
st.write("thalach : maximum heart rate achieved")
input_thalachh = st.slider('thalachh', 0, int(max(data["thalachh"])), 1)
input_exng = st.slider('exng', 0, int(max(data["exng"])), 1)
input_oldpeak = st.slider('oldpeak', 0.0, float(max(data["oldpeak"])), 1.0)
input_slp = st.slider('slp', 0, int(max(data["slp"])), 1)
input_caa = st.slider('caa', 0, int(max(data["caa"])), 1)
input_thall = st.slider('thall', 0, int(max(data["thall"])), 1)



if st.button('Make Prediction'):
    # input_species = encoder.transform(np.expand_dims(inp_species, -1))
    inputs = np.expand_dims(
        [input_age, input_sex, input_cp, input_trtbps, input_chol, input_fbs, input_restecg, input_thalachh, input_exng, input_oldpeak, input_slp, input_caa, input_thall], 0)
    prediction = best_xgboost_model.predict(inputs)
    print("final pred", np.squeeze(prediction, -1))
    st.write(f"Your Heart Attack Chances are: {np.squeeze(prediction, -1):.2f}")

