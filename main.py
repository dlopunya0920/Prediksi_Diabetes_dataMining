import pickle
import streamlit as st

#membaca model 

diabates_model = pickle.load(open("diabetes_model.sav", "rb"))

#Judul web
st.title("Aplikasi Prediksi Diabetes")

#Membagi Kolom

col1, col2=st.columns(2)

with col1 :
    Pregnancies = st.text_input ("Input nilai Pregnancies")
    Glucose = st.text_input ("Input nilai Glucose")
    BloodPressure = st.text_input ("Input nilai BloodPressure")
    SkinThickness = st.text_input ("Input nilai SkinThickness")
with col2 :
    Insulin = st.text_input ("Input nilai Insulin")
    BMI = st.text_input ("Input nilai BMI")
    DiabetesPedigreeFunction = st.text_input ("Input nilai DiabetesPedigreeFunction")
    Age = st.text_input ("Input nilai Age")


# code untuk diprediksi

hasildb_diagnosis =""

#membuat button prediksi

if st.button("Test Prediksi Diabetes"):
    hasildb_prediction = diabates_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])


    if(hasildb_prediction[0]==1):
        hasildb_diagnosis = "Pasien Terkena Diabetes"
    
    else :
        hasildb_diagnosis ="Pasien Tidak Terkena Diabetes"
    st.success(hasildb_diagnosis)
        