import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/placement_model.pkl")

st.title("🎓 Student Placement Predictor")

st.write("Enter student details below:")

# Inputs
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=8.0)

internships = st.number_input("Internships", min_value=0, value=1)

projects = st.number_input("Projects", min_value=0, value=2)

workshops = st.number_input(
    "Workshops/Certifications",
    min_value=0,
    value=1
)

aptitude = st.number_input(
    "Aptitude Test Score",
    min_value=0,
    max_value=100,
    value=75
)

softskills = st.number_input(
    "Soft Skills Rating",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

extra = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

training = st.selectbox(
    "Placement Training",
    ["No", "Yes"]
)

ssc = st.number_input(
    "SSC Marks",
    min_value=0,
    max_value=100,
    value=80
)

hsc = st.number_input(
    "HSC Marks",
    min_value=0,
    max_value=100,
    value=80
)

# Convert Yes/No
extra = 1 if extra == "Yes" else 0
training = 1 if training == "Yes" else 0

# Prediction button
if st.button("Predict Placement"):

    input_data = pd.DataFrame({
        "CGPA": [cgpa],
        "Internships": [internships],
        "Projects": [projects],
        "Workshops/Certifications": [workshops],
        "AptitudeTestScore": [aptitude],
        "SoftSkillsRating": [softskills],
        "ExtracurricularActivities": [extra],
        "PlacementTraining": [training],
        "SSC_Marks": [ssc],
        "HSC_Marks": [hsc]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Student is likely to be Placed")
    else:
        st.error("❌ Student is likely to be Not Placed")