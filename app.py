import streamlit as st
import pandas as pd
import joblib
import os
from io import BytesIO

st.set_page_config(page_title="Heart Disease Prediction", layout="wide", initial_sidebar_state="expanded")

# ====================== BACKGROUND GIF ======================
st.markdown("""
<style>
    .main-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        background-image: url('https://i.makeagif.com/media/1-17-2024/dw-jXM.gif');
        background-size: cover;
        background-position: center;
        opacity: 100%;
        pointer-events: none;
    }

    .stApp {
        background: rgba(10, 10, 10, 0.85); /* Dark overlay for better readability */
    }
</style>
""", unsafe_allow_html=True)

# Apply Background
st.markdown('<div class="main-background"></div>', unsafe_allow_html=True)

# ====================== MAIN APP ======================
st.title("❤️ Heart Disease Prediction App")

# Load model
if os.path.exists('heart_disease_model.pkl') and os.path.exists('scaler.pkl'):
    model = joblib.load('heart_disease_model.pkl')
    scaler = joblib.load('scaler.pkl')
    st.success("✅ Model loaded successfully!")
else:
    st.error("Model files not found!")
    st.stop()

option = st.radio("Choose Prediction Mode", ["Single Patient", "Bulk Prediction"])

if option == "Single Patient":
    st.sidebar.header("Patient Information")
    
    def fill_demo_data(risk_type):
        if risk_type == "High Risk":
            st.session_state.update({
                'age': 65, 'sex': 1, 'cp': 3, 'trestbps': 160, 'chol': 280,
                'fbs': 1, 'restecg': 2, 'thalach': 115, 'exang': 1,
                'oldpeak': 2.5, 'slope': 1, 'ca': 2, 'thal': 3
            })
        elif risk_type == "Low Risk":
            st.session_state.update({
                'age': 45, 'sex': 0, 'cp': 0, 'trestbps': 115, 'chol': 180,
                'fbs': 0, 'restecg': 0, 'thalach': 170, 'exang': 0,
                'oldpeak': 0.0, 'slope': 2, 'ca': 0, 'thal': 2
            })

    st.sidebar.write("**Autofill Demo Data:**")
    col1, col2 = st.sidebar.columns(2)
    with col1:
        st.button("🔴 High Risk", on_click=fill_demo_data, args=("High Risk",))
    with col2:
        st.button("🟢 Low Risk", on_click=fill_demo_data, args=("Low Risk",))

    if 'age' not in st.session_state:
        fill_demo_data("Low Risk")

    age = st.sidebar.slider("Age", 20, 80, key='age')
    sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male", key='sex')
    cp = st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3], key='cp')
    trestbps = st.sidebar.slider("Resting BP", 90, 200, key='trestbps')
    chol = st.sidebar.slider("Cholesterol", 100, 600, key='chol')
    fbs = st.sidebar.selectbox("Fasting Blood Sugar >120", [0, 1], key='fbs')
    restecg = st.sidebar.selectbox("Resting ECG", [0, 1, 2], key='restecg')
    thalach = st.sidebar.slider("Max Heart Rate", 60, 220, key='thalach')
    exang = st.sidebar.selectbox("Exercise Induced Angina", [0, 1], key='exang')
    oldpeak = st.sidebar.slider("Oldpeak", 0.0, 6.0, step=0.1, key='oldpeak')
    slope = st.sidebar.selectbox("Slope", [0, 1, 2], key='slope')
    ca = st.sidebar.slider("Major Vessels (ca)", 0, 4, key='ca')
    thal = st.sidebar.selectbox("Thalassemia", [1, 2, 3], key='thal')

    if st.button("Predict Single Patient"):
        input_data = pd.DataFrame([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]],
                                  columns=['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'])
        input_scaled = scaler.transform(input_data)
        pred = model.predict(input_scaled)[0]
        prob = model.predict_proba(input_scaled)[0][1]
        
        if pred == 1:
            st.error(f"⚠️ High Risk of Heart Disease ({prob:.1%})")
        else:
            st.success(f"✅ Low Risk of Heart Disease ({prob:.1%})")

else:  # Bulk Prediction
    st.header("Bulk Prediction - Upload File")
    st.write("Supported: CSV, Excel (.xlsx, .xls)")
    
    uploaded_file = st.file_uploader("Choose file", type=["csv", "xlsx", "xls"])
    
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.csv'):
                df_input = pd.read_csv(uploaded_file)
            else:
                df_input = pd.read_excel(uploaded_file)
            
            st.success(f"✅ File loaded: {uploaded_file.name}")
            st.write("Preview:", df_input.head())

            if st.button("Predict on Uploaded Data"):
                required_cols = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal']
                
                if all(col in df_input.columns for col in required_cols):
                    X_input = df_input[required_cols]
                    X_scaled = scaler.transform(X_input)
                    predictions = model.predict(X_scaled)
                    probabilities = model.predict_proba(X_scaled)[:, 1]
                    
                    df_input['Prediction'] = predictions
                    df_input['Risk_Probability'] = probabilities.round(4)
                    df_input['Risk'] = df_input['Prediction'].map({0: 'Low Risk', 1: 'High Risk'})
                    
                    st.success("🎉 Predictions Completed!")
                    st.dataframe(df_input)

                    # Download Options
                    st.subheader("📥 Download Results")
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        csv = df_input.to_csv(index=False)
                        st.download_button("Download as CSV", csv, "predictions.csv", "text/csv")
                    
                    with col2:
                        excel_buffer = BytesIO()
                        df_input.to_excel(excel_buffer, index=False)
                        st.download_button("Download as Excel", excel_buffer.getvalue(), "predictions.xlsx", 
                                         "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                    
                    with col3:
                        st.download_button("Download as HTML (Print as PDF)", 
                                         df_input.to_html(index=False), "predictions.html", "text/html")
                else:
                    st.error("Missing required columns!")
                    
        except Exception as e:
            st.error(f"Error: {str(e)}")