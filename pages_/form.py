# form.py
import streamlit as st
from datetime import date

def show():
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1>📝 Comprehensive Health Assessment</h1>
        <p class='subtitle'>Please fill in your details for a personalized health report</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.form("health_form"):
        # Personal Information
        st.markdown("### Personal Information")
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("Full Name", placeholder="John Doe")
            gender = st.selectbox("Gender", ["Male", "Female", "Other", "Prefer not to say"])
        with col2:
            birth_date = st.date_input("Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())
            phone = st.text_input("Phone Number", placeholder="+1 234 567 8900")
        
        # Health Metrics
        st.markdown("### Health Metrics")
        col1, col2 = st.columns(2)
        with col1:
            height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)
            weight = st.number_input("Weight (kg)", min_value=30, max_value=300, value=70)
            blood_pressure = st.selectbox("Blood Pressure Category", 
                                        ["Normal (<120/80)", "Elevated (120-129/<80)", 
                                         "Hypertension Stage 1 (130-139/80-89)", 
                                         "Hypertension Stage 2 (≥140/90)"])
        with col2:
            pregnancies = 0
            if gender == "Female":
                pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)
            glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, value=90, help="Normal range: 70-100 mg/dL (fasting)")
            bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=24.0, disabled=True)
        
        # Lifestyle Factors
        st.markdown("### Lifestyle Factors")
        col1, col2 = st.columns(2)
        with col1:
            exercise = st.selectbox("Exercise Frequency", 
                                   ["None", "1-2 times/week", "3-4 times/week", "5+ times/week"])
            sleep = st.number_input("Average Sleep Hours/Night", min_value=0, max_value=24, value=7)
        with col2:
            smoking = st.selectbox("Smoking Status", 
                                 ["Never", "Former smoker", "Occasional smoker", "Regular smoker"])
            alcohol = st.selectbox("Alcohol Consumption", 
                                 ["None", "Occasional", "Moderate", "Heavy"])
        
        # Family History
        st.markdown("### Family History")
        family_diabetes = st.checkbox("Diabetes in immediate family")
        family_heart = st.checkbox("Heart disease in immediate family")
        family_hypertension = st.checkbox("Hypertension in immediate family")
        
        # Goals and Preferences
        st.markdown("### Health Goals")
        primary_goal = st.selectbox("Primary Health Goal", 
                                   ["Weight loss", "Muscle gain", "Diabetes prevention", 
                                    "Heart health", "General wellness"])
        additional_goals = st.text_area("Specific Goals/Preferences", 
                                      placeholder="Describe your specific health goals, dietary preferences, or any other relevant information")
        
        # Image upload
        st.markdown("### Food Diary (Optional)")
        uploaded_file = st.file_uploader("Upload images of your typical meals", 
                                       type=["jpg", "jpeg", "png"], 
                                       accept_multiple_files=True)
        
        if uploaded_file:
            st.image(uploaded_file, caption="Uploaded Meal Photos", width=150)
        
        # Submit button
        st.markdown("---")
        submitted = st.form_submit_button("Generate Health Report", type="primary")
        
        if submitted:
            # Calculate BMI
            height_m = height / 100
            calculated_bmi = round(weight / (height_m ** 2), 1)
            
            # Prepare form data
            form_data = {
                "personal": {
                    "name": full_name,
                    "gender": gender,
                    "birth_date": str(birth_date),
                    "phone": phone
                },
                "metrics": {
                    "height": height,
                    "weight": weight,
                    "bmi": calculated_bmi,
                    "blood_pressure": blood_pressure,
                    "pregnancies": pregnancies,
                    "glucose": glucose
                },
                "lifestyle": {
                    "exercise": exercise,
                    "sleep": sleep,
                    "smoking": smoking,
                    "alcohol": alcohol
                },
                "family_history": {
                    "diabetes": family_diabetes,
                    "heart_disease": family_heart,
                    "hypertension": family_hypertension
                },
                "goals": {
                    "primary_goal": primary_goal,
                    "additional_goals": additional_goals
                }
            }
            
            # Validate inputs
            if not full_name:
                st.error("Please enter your name")
                return
            if glucose < 20 or glucose > 500:
                st.error("Please enter a valid glucose level (20-500 mg/dL)")
                return
            
            # Store in session state
            st.session_state.form_data = form_data
            st.session_state.image_data = uploaded_file
            st.session_state.navigate_to_results = True
            st.session_state.form_submitted = True
            st.success("Data submitted successfully! Generating your personalized health report...")
            st.rerun()