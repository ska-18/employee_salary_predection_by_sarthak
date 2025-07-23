
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Load Model and Encoders ---
model = joblib.load('best_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# --- Page Configuration ---
st.set_page_config(page_title="Employee Salary Predictor", page_icon="💼", layout="centered")

# --- App Header with Image ---
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://cdn-icons-png.flaticon.com/512/3135/3135768.png" width="120" />
        <h1 style="color:#4CAF50;">Employee Salary Prediction App</h1>
        <p style="font-size:18px;">Predict whether an employee earns <b>>100K</b> or <b>≤100K</b> based on their profile</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Sidebar Input ---
st.sidebar.header("📝 Enter Employee Details")

age = st.sidebar.slider("🎂 Age", 18, 70, 30)
gender = st.sidebar.selectbox("⚧️ Gender", label_encoders['Gender'].classes_)
education = st.sidebar.selectbox("🎓 Education Level", label_encoders['Education Level'].classes_)
job_title = st.sidebar.selectbox("💼 Job Title", label_encoders['Job Title'].classes_)
experience = st.sidebar.slider("📈 Years of Experience", 0, 50, 5)

# --- Input Preview ---
with st.expander("🔍 View Entered Details"):
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Education Level:** {education}")
    st.write(f"**Job Title:** {job_title}")
    st.write(f"**Years of Experience:** {experience}")

# --- Encode Inputs ---
input_data = {
    'Age': age,
    'Gender': label_encoders['Gender'].transform([gender])[0],
    'Education Level': label_encoders['Education Level'].transform([education])[0],
    'Job Title': label_encoders['Job Title'].transform([job_title])[0],
    'Years of Experience': experience
}
input_df = pd.DataFrame([input_data])

# --- Predict Button ---
if st.button("🚀 Predict Salary Range"):
    prediction = model.predict(input_df)[0]
    salary_label = ">100K" if prediction == 1 else "≤100K"
    st.markdown(
        f"""
        <div style="padding: 20px; background-color: #e0f7fa; border-radius: 10px; text-align: center;">
            <h2>💰 Predicted Salary Range: <span style="color: #2E7D32;">{salary_label}</span></h2>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- Footer ---
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 14px; color: grey;">
        Built with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
