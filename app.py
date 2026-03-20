import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🎓 Student Exam Score Predictor")

# Inputs
hours = st.number_input("Hours Studied", 0, 24, 0)
attendance = st.number_input("Attendance (%)", 0, 100, 0)
sleep = st.number_input("Sleep Hours", 0.0, 12.0, 0.0)
previous = st.number_input("Previous Score", 0, 100, 0)
tutoring = st.number_input("Tutoring Sessions", 0, 10, 0)
physical = st.number_input("Physical Activity", 0, 20, 0)

# Dropdowns
access = st.selectbox("Access to Resources", ["Low","Medium","High"])
teacher = st.selectbox("Teacher Quality", ["Low","Medium","High"])
school = st.selectbox("School Type", ["Public","Private"])
extra = st.selectbox("Extracurricular Activities", ["No","Yes"])
internet = st.selectbox("Internet Access", ["No","Yes"])
family = st.selectbox("Family Income", ["Low","Medium","High"])
distance = st.selectbox("Distance from Home", ["Near","Moderate","Far"])
gender = st.selectbox("Gender", ["Male","Female"])

# Predict
if st.button("Predict Score"):

    # Encoding
    map_LMH = {"Low":0,"Medium":1,"High":2}
    map_yesno = {"No":0,"Yes":1}
    map_school = {"Public":0,"Private":1}
    map_distance = {"Near":0,"Moderate":1,"Far":2}
    map_gender = {"Male":1,"Female":0}

    sample = pd.DataFrame([[ 
        hours, attendance, map_LMH[access], sleep,
        previous, tutoring, map_LMH[teacher],
        map_school[school], physical, map_yesno[extra],
        map_yesno[internet], map_LMH[family],
        map_distance[distance], map_gender[gender]
    ]], columns=[
        "Hours_Studied","Attendance","Access_to_Resources","Sleep_Hours",
        "Previous_Scores","Tutoring_Sessions","Teacher_Quality",
        "School_Type","Physical_Activity","Extracurricular_Activities",
        "Internet_Access","Family_Income","Distance_from_Home","Gender"
    ])

    prediction = model.predict(sample)

    st.success(f"🎯 Predicted Score: {prediction[0]:.2f}")
