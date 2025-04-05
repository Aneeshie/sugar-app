# app.py
import streamlit as st
from pages_ import form, results, game
import base64

# Set page config (should be first Streamlit command)
st.set_page_config(
    page_title="Health AI Companion",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles/styles.css")

# Background image with overlay
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .main::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(0, 0, 0, 0.7);
            z-index: -1;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local('assets/NEW_BACKGROUND.jpg')  # Add your background image

# Initialize session state
session_defaults = {
    "app_started": False,
    "game_completed": False,
    "current_page": "📝 Health Form",
    "navigate_to_results": False,
    "form_submitted": False,
    "show_game": False,
    "user_name": ""
}

for key, value in session_defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value

# Main app logic
if not st.session_state.app_started:
    st.markdown("""
    <div class='landing-container'>
        <h1 class='title'>Health AI Companion</h1>
        <p class='subtitle'>Your personalized health assessment and wellness guide</p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.container():
        col1, col2 = st.columns([1, 1])
        with col1:
            st.session_state.user_name = st.text_input("What should we call you?", placeholder="Enter your name")
        
        with st.container():
            st.write("")
            st.markdown("### Would you like to play a quick health awareness game?")
            
            game_col1, game_col2 = st.columns(2)
            with game_col1:
                if st.button("🎮 Yes, let's play!", key="yes_game", use_container_width=True):
                    st.session_state.show_game = True
                    st.session_state.app_started = True
                    st.rerun()
            with game_col2:
                if st.button("📝 No, go straight to assessment", key="no_game", use_container_width=True):
                    st.session_state.show_game = False
                    st.session_state.app_started = True
                    st.session_state.game_completed = True
                    st.rerun()

elif st.session_state.app_started and not st.session_state.game_completed and st.session_state.show_game:
    game.show()

else:
    if st.session_state.get("navigate_to_results"):
        st.session_state.current_page = "📊 Health Report"
        st.session_state.navigate_to_results = False

    # Sidebar navigation
    with st.sidebar:
        if st.session_state.user_name:
            st.markdown(f"<div class='sidebar-welcome'>👋 Hello, {st.session_state.user_name}!</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='sidebar-welcome'>👋 Welcome!</div>", unsafe_allow_html=True)
        
        st.markdown("### Navigation")
        if st.button("📝 Health Form", use_container_width=True):
            st.session_state.current_page = "📝 Health Form"
            st.rerun()
        if st.button("📊 Health Report", disabled=not st.session_state.form_submitted, use_container_width=True):
            st.session_state.current_page = "📊 Health Report"
            st.rerun()
        
        st.markdown("---")
        st.markdown("### Health Tips")
        st.info("💡 Regular exercise can reduce diabetes risk by up to 58%")
        st.info("🍎 Eating whole fruits is better than drinking fruit juices")
        st.info("💤 7-8 hours of sleep helps regulate blood sugar levels")

    # Page routing
    page = st.session_state.current_page
    if page == "📝 Health Form":
        form.show()
    elif page == "📊 Health Report":
        results.show()
