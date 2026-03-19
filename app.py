import streamlit as st
import pandas as pd
import pickle

# Page config
st.set_page_config(page_title="Student Score Predictor", page_icon="🎓", layout="wide")

# Dark UI styling
st.markdown("""
<style>
body {
    background-color:  #1F2937;
    color: black;
}
.stButton>button {
    background-color: #00ADB5;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Title
st.title("🎓 Student Exam Score Predictor")
st.markdown("### Enter details to predict exam score")

st.markdown("---")

# ---- 2 COLUMN LAYOUT ----
col1, col2 = st.columns(2)

# ---- COLUMN 1: BASIC INPUTS ----
with col1:
    st.subheader("🧍 Student Basic Details")

    hours = st.number_input("Hours Studied", min_value=0, max_value=24, value=None, placeholder="e.g. 5")
    attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=None, placeholder="e.g. 80")
    sleep = st.number_input("Sleep Hours", min_value=0.0, max_value=12.0, value=None, placeholder="e.g. 6-8")
    previous = st.number_input("Previous Score", min_value=0, max_value=100, value=None, placeholder="e.g. 70")
    tutoring = st.number_input("Tutoring Sessions", min_value=0, max_value=10, value=None, placeholder="e.g. 2")
    physical = st.number_input("Physical Activity", min_value=0, max_value=20, value=None, placeholder="e.g. 3")
    gender = st.selectbox("Gender", ["Select","Male","Female"])
    distance = st.selectbox("Distance from Home", ["Select","Near","Moderate","Far"])

# ---- COLUMN 2: ACADEMIC + SOCIAL ----
with col2:
    st.subheader("📊 Academic & Social Factors")

    parental = st.selectbox("Parental Involvement", ["Select","Low","Medium","High"])
    resources = st.selectbox("Access to Resources", ["Select","Low","Medium","High"])
    extra = st.selectbox("Extracurricular Activities", ["Select","No","Yes"])
    motivation = st.selectbox("Motivation Level", ["Select","Low","Medium","High"])
    internet = st.selectbox("Internet Access", ["Select","No","Yes"])
    family = st.selectbox("Family Income", ["Select","Low","Medium","High"])
    teacher = st.selectbox("Teacher Quality", ["Select","Low","Medium","High"])
    school = st.selectbox("School Type", ["Select","Public","Private"])
    peer = st.selectbox("Peer Influence", ["Select","Negative","Neutral","Positive"])
    learning = st.selectbox("Learning Disabilities", ["Select","No","Yes"])
    parent_edu = st.selectbox("Parental Education Level", ["Select","High School","College","Postgraduate"])

# ---- VALIDATION ----
if st.button("🚀 Predict Score"):

    if None in [hours, attendance, sleep, previous] or "Select" in [
        gender, distance, parental, resources, extra, motivation,
        internet, family, teacher, school, peer, learning, parent_edu
    ]:
        st.error("⚠️ Please fill all fields correctly")
    else:

        # Mapping
        map_LMH = {"Low":0,"Medium":1,"High":2}
        map_yesno = {"No":0,"Yes":1}
        map_peer = {"Negative":0,"Neutral":1,"Positive":2}
        map_school = {"Public":0,"Private":1}
        map_distance = {"Near":0,"Moderate":1,"Far":2}
        map_parentedu = {"High School":0,"College":1,"Postgraduate":2}
        map_gender = {"Male":1,"Female":0}

        # Convert
        sample = pd.DataFrame([[ 
            hours,
            attendance,
            map_LMH[parental],
            map_LMH[resources],
            map_yesno[extra],
            sleep,
            previous,
            map_LMH[motivation],
            map_yesno[internet],
            tutoring,
            map_LMH[family],
            map_LMH[teacher],
            map_school[school],
            map_peer[peer],
            physical,
            map_yesno[learning],
            map_parentedu[parent_edu],
            map_distance[distance],
            map_gender[gender]
        ]], columns=[
            "Hours_Studied","Attendance","Parental_Involvement","Access_to_Resources",
            "Extracurricular_Activities","Sleep_Hours","Previous_Scores",
            "Motivation_Level","Internet_Access","Tutoring_Sessions",
            "Family_Income","Teacher_Quality","School_Type","Peer_Influence",
            "Physical_Activity","Learning_Disabilities",
            "Parental_Education_Level","Distance_from_Home","Gender"
        ])

        prediction = model.predict(sample)[0]

        st.markdown(f"""
        <div style="
            background-color:#1F2937;
            padding:25px;
            border-radius:15px;
            text-align:center;
            box-shadow: 0px 0px 20px rgba(0,255,255,0.2);
        ">
            <h2 style="color:#00ADB5;">🎯 Predicted Exam Score</h2>
            <h1 style="color:white;">{prediction:.2f}</h1>
        </div>
        """, unsafe_allow_html=True)