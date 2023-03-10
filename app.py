import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

st.title('Medical Diagnostic Web App')
st.subheader('Is the patient Diabetic?')

model = open('rf.pickle', 'rb')
clf = pickle.load(model)
model.close()

prg = st.number_input('Pregnancies', 0, 17, 0)
glu = st.slider('Glucose', 40, 200, 40)
bp = st.slider('BloodPressure', 20, 140, 20)
skt = st.slider('SkinThickness', 7.0, 99.0, 7.0 )
ins = st.slider('Insulin', 14, 850, 14)
bmi = st.slider('BMI', 18, 67, 18)
dpf = st.slider('DiabetesPedigreeFunction', 0.07, 2.50, 0.07)
age = st.number_input('Age', 20, 85, 20)

data = {'Pregnancies' : prg,
        'Glucose' : glu,
        'BloodPressure' : bp,
        'SkinThickness' : skt,
        'Insulin' : ins,
        'BMI' : bmi,
        'DiabetesPedigreeFunction' : dpf,
        'Age' : age}
input_data = pd.DataFrame([data])

preds = clf.predict(input_data)[0]

if st.button('Predict'):
    if preds == 1:
        st.error('Diabetic')
    if preds == 0:
        st.success('Non-Diabetic')
