import streamlit as st
from pages_ import form, results  # Import from the pages_ directory

# Initialize session state if not set
if "current_page" not in st.session_state:
    st.session_state.current_page = "📝 Form"

if "navigate_to_results" not in st.session_state:
    st.session_state.navigate_to_results = False

if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False


# Redirect based on navigation flags
if st.session_state.get("navigate_to_results"):
    st.session_state.current_page = "📊 Results"
    st.session_state.navigate_to_results = False

# Sidebar Navigation
st.sidebar.markdown("<div class='sidebar-welcome'>👋 Welcome</div>", unsafe_allow_html=True)
st.sidebar.markdown("### Go to")
if st.sidebar.button("📝 Form"):
    st.session_state.current_page = "📝 Form"
    st.rerun()
if st.sidebar.button("📊 Results", disabled=not st.session_state.form_submitted):
    st.session_state.current_page = "📊 Results"
    st.rerun()

# Render the selected page
page = st.session_state.current_page
if page == "📝 Form":
    form.show()
elif page == "📊 Results":
   results.show()
