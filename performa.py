import pickle
import streamlit as st
import numpy as np

with open('performa_model.sav', 'rb') as model_file:
    performa_model = pickle.load(model_file)

st.title('Prediksi Performa Siswa')

Hours_Studied = st.text_input('Jam Belajar')
Sleep_Hours = st.text_input('Jam Tidur')
SampleQuestionPapersPracticed = st.text_input('Jumlah soal contoh yang telah dikerjakan')
Previous_Scores = st.text_input('Nilai Sebelumnya')
Extracurricular_Activities = st.selectbox('Ekstrakurikuler', ['Ya', 'Tidak'])

performa_prediksi = ''

if st.button('Prediksi Performa Siswa'):
    try:
        Hours_Studied = int(Hours_Studied)
        Sleep_Hours = int(Sleep_Hours)
        SampleQuestionPapersPracticed = int(SampleQuestionPapersPracticed)
        Previous_Scores = int(Previous_Scores)
    
        if Extracurricular_Activities == 'Ya':
            Extracurricular_Activities = 1
        else:
            Extracurricular_Activities = 0
        
        data = [
            Hours_Studied,
            Previous_Scores,
            Sleep_Hours,
            SampleQuestionPapersPracticed,
            Extracurricular_Activities
        ]
        
        data = np.array(data).reshape(1, -1)

        performa_prediksi = performa_model.predict(data)
        st.success(f'Performa Siswa adalah {performa_prediksi[0]:.2f}')

    except ValueError as e:
        st.error(f"Error: {e}")
