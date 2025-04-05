import streamlit as st
import pickle
import requests
import numpy as np
from PIL import Image
import io
import base64
from datetime import datetime

# Blood pressure mapping to numerical values
BP_MAPPING = {
    "Normal (<120/80)": (110, 70),  # Using midpoint values
    "Elevated (120-129/<80)": (125, 70),
    "Hypertension Stage 1 (130-139/80-89)": (135, 85),
    "Hypertension Stage 2 (≥140/90)": (145, 95)
}

def get_bp_values(bp_category):
    """Convert blood pressure category to systolic/diastolic values"""
    return BP_MAPPING.get(bp_category, (120, 80))  # Default if not found

# Load the XGBoost model with error handling
try:
    model = pickle.load(open("model/xgb_model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file 'model/xgb_model.pkl' not found. Please ensure it exists in the correct directory.")
    st.stop()

def show():
    # Get all session data
    form_data = st.session_state.get("form_data")
    uploaded_files = st.session_state.get("image_data", [])
    
    # Check if required data is present
    if not form_data:
        st.warning("Please complete the health form first.")
        if st.button("Go to Health Form"):
            st.session_state.current_page = "📝 Health Form"
            st.rerun()
        st.stop()

    try:
        # Calculate age from birth date
        birth_date = datetime.strptime(form_data["personal"]["birth_date"], "%Y-%m-%d")
        age = datetime.now().year - birth_date.year
        
        # Get blood pressure values
        systolic, diastolic = get_bp_values(form_data["metrics"]["blood_pressure"])
        
        # Prepare model input (must match exactly what your model expects)
        model_input = [
            form_data["metrics"]["pregnancies"],  # Pregnancies
            form_data["metrics"]["glucose"],      # Glucose
            systolic,                            # Blood Pressure (systolic)
            75,                                  # Insulin (default value)
            form_data["metrics"]["bmi"],         # BMI
            0.5,                                 # Diabetes Pedigree (default)
            age                                  # Age
        ]
        
        # If you have actual insulin and diabetes pedigree values in your form:
        # model_input[3] = form_data["metrics"].get("insulin", 75)
        # model_input[5] = form_data["metrics"].get("diabetes_pedigree", 0.5)

    except Exception as e:
        st.error(f"Error processing health data: {str(e)}")
        st.stop()

    # --- Model Prediction Section ---
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1>🔬 Your Health Analysis Report</h1>
        <p class='subtitle'>Powered by AI and medical research</p>
    </div>
    """, unsafe_allow_html=True)

    with st.expander("📊 Core Health Metrics", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Glucose Level", f"{model_input[1]} mg/dL", 
                     help="Normal range: 70-100 mg/dL (fasting)")
            st.metric("Blood Pressure", form_data["metrics"]["blood_pressure"])
            st.metric("BMI", f"{model_input[4]:.1f}", 
                     help="Normal range: 18.5-24.9")
        with col2:
            st.metric("Age", model_input[6])
            if form_data["personal"]["gender"] == "Female":
                st.metric("Pregnancies", model_input[0])
            st.metric("Insulin Level", f"{model_input[3]} μU/mL")

    # Predict diabetes probability
    input_array = np.array([model_input])
    probability = model.predict_proba(input_array)[0][1] * 100
    probability = round(probability, 2)

    # Display risk with color coding
    risk_color = "#ff4d4f" if probability > 50 else "#ffc107" if probability > 30 else "#00ff9c"
    st.markdown(f"""
    <div style='text-align: center; margin: 30px 0; padding: 20px; border-radius: 10px; background: rgba(30, 30, 30, 0.7);'>
        <h3>Diabetes Risk Assessment</h3>
        <h1 style='color: {risk_color}; font-size: 3em;'>{probability}%</h1>
        <p>Probability of developing diabetes</p>
    </div>
    """, unsafe_allow_html=True)

    # --- Gemini API Integration ---
    st.markdown("## 🧠 Personalized Recommendations")
    
    # Prepare comprehensive prompt
    prompt = f"""
**Comprehensive Health Analysis Request**

Patient Profile:
- Name: {form_data["personal"]["name"]}
- Gender: {form_data["personal"]["gender"]}
- Age: {model_input[6]}
- BMI: {model_input[4]:.1f}

Health Metrics:
- Glucose: {model_input[1]} mg/dL
- Blood Pressure: {form_data["metrics"]["blood_pressure"]}
- Insulin: {model_input[3]} μU/mL
- Pregnancies: {model_input[0]} (if applicable)
- Diabetes Pedigree: {model_input[5]:.2f}

Lifestyle Factors:
- Exercise: {form_data["lifestyle"]["exercise"]}
- Sleep: {form_data["lifestyle"]["sleep"]} hours/night
- Smoking: {form_data["lifestyle"]["smoking"]}
- Alcohol: {form_data["lifestyle"]["alcohol"]}

Family History:
- Diabetes: {"Yes" if form_data["family_history"]["diabetes"] else "No"}
- Heart Disease: {"Yes" if form_data["family_history"]["heart_disease"] else "No"}
- Hypertension: {"Yes" if form_data["family_history"]["hypertension"] else "No"}

Health Goals:
- Primary: {form_data["goals"]["primary_goal"]}
- Additional: {form_data["goals"]["additional_goals"]}

Diabetes Risk: {probability}%

**Please provide:**
1. Detailed lifestyle recommendations specific to the user's profile
2. Dietary plan with calorie counts and nutritional info
3. Exercise suggestions based on current activity level
4. Timeline estimates for achieving their goals
5. Specific warnings based on risk factors
6. Encouragement for positive aspects of their profile

Format the response with clear sections and bullet points. Be empathetic and professional.
"""

    # Call Gemini API
    API_KEY = st.secrets.get("GEMINI_API_KEY", "AIzaSyDP6ycVUyatybGwjzm1k9F4P65XMc0NZpM")
    ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    with st.spinner("Generating your personalized health plan..."):
        try:
            response = requests.post(ENDPOINT, json=payload)
            if response.status_code == 200:
                reply = response.json()['candidates'][0]['content']['parts'][0]['text']
                st.session_state.gemini_result = reply
                st.markdown(reply)
            else:
                st.error(f"Gemini API Error: {response.status_code}")
                st.session_state.gemini_result = None
        except Exception as e:
            st.error(f"Failed to connect to Gemini API: {str(e)}")

    # --- Image Analysis Section ---
    if uploaded_files:
        st.markdown("## 🍽️ Meal Analysis")
        for img in uploaded_files:
            with st.expander(f"Analysis for {img.name}", expanded=False):
                st.image(img, use_column_width=True)
                
                image_prompt = f"""
Analyze this meal image for someone with:
- Diabetes risk: {probability}%
- Goals: {form_data["goals"]["primary_goal"]}
- Current diet: {form_data["lifestyle"]["exercise"]} exercise level

Provide:
1. Healthiness score (1-10)
2. Nutritional breakdown
3. Suggested improvements
4. Healthier alternatives that are still tasty
5. How this meal affects their specific goals
"""
                with st.spinner("Analyzing meal..."):
                    try:
                        image_data = Image.open(img)
                        with io.BytesIO() as byte_io:
                            image_data.save(byte_io, format='PNG')
                            image_bytes = byte_io.getvalue()
                            image_base64 = base64.b64encode(image_bytes).decode('utf-8')

                        payload = {
                            "contents": [{
                                "parts": [
                                    {"text": image_prompt},
                                    {
                                        "inline_data": {
                                            "mime_type": "image/png",
                                            "data": image_base64
                                        }
                                    }
                                ]
                            }]
                        }
                        
                        response = requests.post(ENDPOINT, json=payload)
                        if response.status_code == 200:
                            analysis = response.json()['candidates'][0]['content']['parts'][0]['text']
                            st.markdown(analysis)
                        else:
                            st.error(f"Image analysis failed (Status: {response.status_code})")
                    except Exception as e:
                        st.error(f"Error analyzing image: {str(e)}")

    # Download report button
    st.download_button(
        label="📄 Download Full Report",
        data=f"Health Report\n\n{st.session_state.get('gemini_result', 'No recommendations generated')}",
        file_name=f"{form_data['personal']['name']}_Health_Report.txt",
        mime="text/plain"
    )