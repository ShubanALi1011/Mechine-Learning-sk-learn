# predictor.py
import streamlit as st
import pickle
import numpy as np
import json

# Page setup
st.set_page_config(page_title="Student Score Predictor", layout="centered")
st.title("Student Final Score Predictor")


col1, col2 = st.columns(2)

with col1:
    hours = st.number_input(
        "Kitne ghante padhai?",
        min_value=0.0,
        max_value=24.0,
        value=5.0,
        step=0.5,
        help="Rozana ke padhai ke ghante"
    )
    
    attendance = st.number_input(
        "Attendance kitni %?",
        min_value=0.0,
        max_value=100.0,
        value=75.0,
        step=1.0,
        help="Classes mein kitna attend kiya"
    )

with col2:
    past_score = st.number_input(
        "Pehle ka score?",
        min_value=0.0,
        max_value=100.0,
        value=70.0,
        step=1.0,
        help="Pichla exam ka score"
    )
    
    sleep = st.number_input(
        "Kitni neend?",
        min_value=0.0,
        max_value=24.0,
        value=6.0,
        step=0.5,
        help="Rozana ke neend ke ghante"
    )

# Predict button
if st.button("Predict Score", type="primary", use_container_width=True):
    try:
        # Model load karo
        with open('student_model.pkl', 'rb') as f:
            model = pickle.load(f)
        
        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)
        
        # Input ko array mein convert karo
        input_data = np.array([[hours, attendance, past_score, sleep]])
        
        # Scale karo
        input_scaled = scaler.transform(input_data)
        
        # Predict karo
        prediction = model.predict(input_scaled)
        
        # Result show karo
        st.markdown("---")
        st.markdown(f"""
        <div style='text-align: center; padding: 20px; background-color: #f0f9ff; border-radius: 10px;'>
            <h2> Predicted Score</h2>
            <h1 style='color: #2563eb; font-size: 48px;'>{prediction[0]:.1f}/100</h1>
        </div>
        """, unsafe_allow_html=True)
        
        # Grade calculate karo
        score = prediction[0]
        if score >= 90:
            grade = "A+ 🎉"
            color = "green"
        elif score >= 80:
            grade = "A 👍"
            color = "lightgreen"
        elif score >= 70:
            grade = "B 🙂"
            color = "blue"
        elif score >= 60:
            grade = "C 🤔"
            color = "orange"
        else:
            grade = "F 😟"
            color = "red"
        
        st.markdown(f"**Grade:** <span style='color:{color}; font-weight:bold'>{grade}</span>", unsafe_allow_html=True)
        
        # Simple tips
        if score < 70:
            st.warning("💡 Tips: Zyada padhao, attendance badhao!")
        else:
            st.success("🎉 Bahut accha! Aise hi continue karo!")
            
    except Exception as e:
        st.error(f"Error: {e}")
        st.info("Pehle model save karo Jupyter notebook se!")