import pickle
import streamlit as st
import numpy as np

# Load the model
with open('performa_model.sav', 'rb') as model_file:
    performa_model = pickle.load(model_file)

# Title of the web app
st.title('Prediksi Performa Siswa')

# Input fields
Hours_Studied = st.text_input('Jam Belajar')
Sleep_Hours = st.text_input('Jam Tidur')
SampleQuestionPapersPracticed = st.text_input('Soal Latihan yang Dikerjakan')
Previous_Scores = st.text_input('Nilai Sebelumnya')
Extracurricular_Activities = st.selectbox('Ekstrakurikuler', ['Ya', 'Tidak'])

# Initialize prediction output
performa_prediksi = ''

# Convert inputs to appropriate data types and make prediction
if st.button('Prediksi Performa Siswa'):
    try:
        # Convert text inputs to numerical values
        Hours_Studied = int(Hours_Studied)
        Sleep_Hours = int(Sleep_Hours)
        SampleQuestionPapersPracticed = int(SampleQuestionPapersPracticed)
        Previous_Scores = int(Previous_Scores)
        
        # Encode Extracurricular_Activities to binary
        if Extracurricular_Activities == 'Ya':
            Extracurricular_Activities = 1
        else:
            Extracurricular_Activities = 0
        
        # Prepare data for prediction
        data = [
            Hours_Studied,
            Previous_Scores,
            Sleep_Hours,
            SampleQuestionPapersPracticed,
            Extracurricular_Activities
        ]
        
        # Convert list to NumPy array
        data = np.array(data).reshape(1, -1)
        
        # Predict
        performa_prediksi = performa_model.predict(data)
        st.success(f'Performa Siswa adalah {performa_prediksi[0]:.2f}')

    except ValueError as e:
        st.error(f"Error: {e}")
