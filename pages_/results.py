import streamlit as st
import pickle
import requests
import numpy as np
from PIL import Image
import io
import base64

# Load the XGBoost model with error handling
try:
    model = pickle.load(open("model/xgb_model.pkl", "rb"))
except FileNotFoundError:
    st.error("Model file 'model/xgb_model.pkl' not found. Please ensure it exists in the correct directory.")
    st.stop()

def show():
    data = st.session_state.get("form_data")
    goal = st.session_state.get("goal_data", [""])[0]  # Default to empty string if not set
    uploaded_file = st.session_state.get("image_data")

    # Check if required data is present
    if not goal:
        st.warning("It is recommended to fill the goal.")
    if not data:
        st.warning("Please fill the form first.")
        if st.button("Go to Form"):
            st.session_state.current_page = "📝 Form"
            st.rerun()
        st.stop()

    # Unpack the form data
    pregnancies, glucose, blood_pressure, insulin, bmi, diabetes_pedigree, age = data

    st.header("🔬 AI Model Results")

    # Show the data back to user
    st.write("### 🧾 Patient Input Data")
    st.write(f"**Pregnancies:** {pregnancies}")
    st.write(f"**Glucose:** {glucose}")
    st.write(f"**Blood Pressure:** {blood_pressure}")
    st.write(f"**Insulin Level:** {insulin}")
    st.write(f"**BMI:** {bmi}")
    st.write(f"**Diabetes Pedigree Function:** {diabetes_pedigree}")
    st.write(f"**Age:** {age}")
    st.write(f"**Goals:** {goal}")

    # Predict using model
    input_array = np.array([data])
    probability = model.predict_proba(input_array)[0][1] * 100
    probability = round(probability, 2)

    st.success(f"📈 **Predicted Risk of Diabetes: {probability}**")

    # Prepare prompt for Gemini text-based recommendation
    prompt = f"""
Patient Report:
- Pregnancies: {pregnancies}
- Glucose: {glucose}
- Blood Pressure: {blood_pressure}
- Insulin Level: {insulin}
- BMI: {bmi}
- Diabetes Pedigree: {diabetes_pedigree}
- Age: {age}
- Predicted Diabetes Risk: {probability}%
- Goals: {goal}

Based on this data and the goal provided, provide a detailed diet and lifestyle recommendation to help manage or prevent diabetes. Please highlight the goal in the response. The balanced diet should be in bullet points with each point containing the calories and other metrics. Also give a rough estimate of when the person can achieve their goal.
"""

    # Gemini API integration for text recommendation
    st.markdown("### 🧠 Recommendations")  # Fixed the typo here
    API_KEY = st.secrets.get("GEMINI_API_KEY", "AIzaSyDP6ycVUyatybGwjzm1k9F4P65XMc0NZpM")
    ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

    payload = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }

    with st.spinner("Fetching recommendation..."):
        response = requests.post(ENDPOINT, json=payload)
        if response.status_code == 200:
            reply = response.json()['candidates'][0]['content']['parts'][0]['text']
            st.session_state.gemini_result = reply
            st.write(reply)
        else:
            st.session_state.gemini_result = "❌ Gemini API failed to respond properly."
            st.error(f"Gemini API Error: {response.status_code}. Please check your API key or input format.")

    # Image analysis if an image was uploaded
    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        image_prompt = "Analyze the uploaded image and give insights based on diabetes, if these are helping or are worse. Else need not oppose them. If not provided, at least suggest if the food in the above image is healthy; if not, provide TASTY alternatives."

        def generate_response(image, prompt):
            image_data = Image.open(image)
            with io.BytesIO() as byte_io:
                image_data.save(byte_io, format='PNG')
                image_bytes = byte_io.getvalue()
                image_base64 = base64.b64encode(image_bytes).decode('utf-8')

            payload = {
                "contents": [{
                    "parts": [
                        {"text": prompt},
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
                return response.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                return f"API Error: {response.status_code}"

        with st.spinner("Analyzing image with Gemini..."):
            try:
                answer = generate_response(uploaded_file, image_prompt)
                st.success("🧠 Image Analysis Result:")
                st.write(answer)
            except Exception as e:
                st.error(f"❌ Error during image analysis: {e}")