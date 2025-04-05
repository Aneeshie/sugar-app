import streamlit as st

def show():
    st.header("📝 Health Assessment Form")

    # Form fields
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=120, step=1)
    pregnancies = 0
    if gender == "Female":
        pregnancies = st.number_input("Number of Pregnancies", min_value=0, max_value=20, step=1)

    glucose = st.number_input("Glucose Level (mg/dL)", min_value=0, value=70)
    blood_pressure = st.selectbox("Blood Pressure", [70, 80, 90, 100, 110, 120, 130])
    insulin = st.selectbox("Insulin Level", [15, 30, 45, 60, 75, 90, 105])
    bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=24.0)
    dp_function = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.2)
    goals = st.text_input("Goals", placeholder="Lose weight, gain muscle, etc.")

    # Image uploader
    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image Preview", use_container_width=True)

    st.write("---")
    submitted = st.button("Start Analysis")

    if submitted:
        # Input validation
        if glucose < 20:
            st.error("Glucose level seems too low. Please enter a realistic value (e.g., 20-200 mg/dL).")
            return
        if bmi < 10:
            st.error("BMI seems too low. Please enter a realistic value (e.g., 10-50).")
            return

        # Store the form data in the session state
        form_data = [
            pregnancies,
            glucose,
            blood_pressure,
            insulin,
            bmi,
            dp_function,
            age,
        ]

        goal_data = [
            goals
        ]

        

        
        st.session_state.form_data = form_data
        st.session_state.goal_data = goal_data
        st.session_state.image_data = uploaded_file
        st.session_state.navigate_to_results = True  # Set flag for results page navigation
        st.session_state.form_submitted = True
        st.success("Data submitted successfully! Navigating to results...")
        st.rerun()  # Re-render the page