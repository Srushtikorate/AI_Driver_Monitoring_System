import streamlit as st

st.set_page_config(
    page_title="AI Driver Monitoring System",
    layout="wide"
)

st.title("AI Driver Monitoring System")

st.markdown("---")

# Metrics Section
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Dataset Records", "600")

with col2:
    st.metric("Features Used", "4")

with col3:
    st.metric("Classes", "3")

with col4:
    st.metric("Model", "Random Forest")

st.markdown("---")

# Project Overview
st.header("Project Overview")

st.write("""
The AI Driver Monitoring System is designed to monitor a driver's condition
in real time using Computer Vision and Machine Learning techniques.

The system continuously analyzes facial landmarks obtained from a webcam
to identify driver fatigue and distraction.
""")

st.markdown("---")

# System Modules
st.header("System Modules")

col1, col2 = st.columns(2)

with col1:
    st.success("Face Mesh Detection")
    st.success("Blink Detection")
    st.success("Drowsiness Detection")

with col2:
    st.success("Head Pose Detection")
    st.success("Random Forest Classification")
    st.success("Real-Time Monitoring")

st.markdown("---")

# Machine Learning Details
st.header("Machine Learning Details")

st.info("""
Algorithm Used:
Random Forest Classifier

Input Features:
• Eye Opening

• Blink Count

• Eye Closed Duration

• Head Direction

Output Classes:
• Alert

• Drowsy

• Distracted
""")

st.markdown("---")

# Technologies Used
st.header("Technologies Used")

st.write("""
• Python

• OpenCV

• CVZone

• MediaPipe Face Mesh

• Pandas

• Scikit-Learn

• Streamlit
""")

st.markdown("---")

# Project Workflow
st.header("System Workflow")

st.write("""
Webcam Input

↓
    
Face Mesh Detection

↓

Feature Extraction

(Eye Opening, Blink Count, Closed Time, Head Direction)

↓

Random Forest Model

↓

Driver Classification

(Alert / Drowsy / Distracted)
""")

st.markdown("---")

# Project Status
st.header("Project Status")

st.success("Computer Vision Module Completed")
st.success("Machine Learning Model Trained")
st.success("Real-Time Prediction Integrated")
st.success("Driver Monitoring System Successfully Implemented")

st.markdown("---")

# Outcome
st.header("Project Outcome")

st.write("""
The developed system successfully detects driver drowsiness and distraction
using facial landmark analysis and machine learning. The solution can assist
in improving road safety by providing early warnings when unsafe driving
behavior is detected.
""")