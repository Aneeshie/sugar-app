import streamlit as st
from pages_ import form, results

if "app_started" not in st.session_state:
    st.session_state.app_started = False
if "game_completed" not in st.session_state:
    st.session_state.game_completed = False
if "current_page" not in st.session_state:
    st.session_state.current_page = "📝 Form"
if "navigate_to_results" not in st.session_state:
    st.session_state.navigate_to_results = False
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False

if not st.session_state.app_started:
    st.header("🎉 Welcome to the Health Assessment App!")
    st.write("Would you like to play a small game before starting?")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes"):
            st.session_state.show_game = True
            st.session_state.app_started = True
            st.rerun()
    with col2:
        if st.button("No"):
            st.session_state.show_game = False
            st.session_state.app_started = True
            st.session_state.game_completed = True
            st.rerun()

elif st.session_state.app_started and not st.session_state.game_completed and st.session_state.get("show_game"):
    st.header("🎮 Play a Small Game")
    st.write("Choose the food item that does **not** promote diabetes by clicking its card.")

    food_items = [
        {"name": "Apple", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/1200px-Red_Apple.jpg", "diabetes_friendly": True},
        {"name": "Candy Bar", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Chocolate_candy_bar.jpg/1200px-Chocolate_candy_bar.jpg", "diabetes_friendly": False}
    ]

    col1, col2 = st.columns(2)
    with col1:
        st.image(food_items[0]["image"], caption=food_items[0]["name"], use_column_width=True)
        if st.button("Choose " + food_items[0]["name"], key="food1"):
            st.session_state.game_choice = food_items[0]["name"]
            st.session_state.game_correct = food_items[0]["diabetes_friendly"]
            if food_items[0]["diabetes_friendly"]:
                st.success(f"Correct! {food_items[0]['name']} is a better choice for managing diabetes.")
            else:
                st.error(f"Oops! {food_items[0]['name']} is less diabetes-friendly.")
            st.session_state.game_completed = True
            st.rerun()

    with col2:
        st.image(food_items[1]["image"], caption=food_items[1]["name"], use_column_width=True)
        if st.button("Choose " + food_items[1]["name"], key="food2"):
            st.session_state.game_choice = food_items[1]["name"]
            st.session_state.game_correct = food_items[1]["diabetes_friendly"]
            if food_items[1]["diabetes_friendly"]:
                st.success(f"Correct! {food_items[1]['name']} is a better choice for managing diabetes.")
            else:
                st.error(f"Oops! {food_items[1]['name']} is less diabetes-friendly.")
            st.session_state.game_completed = True
            st.rerun()

    if st.button("Skip Game"):
        st.session_state.game_completed = True
        st.rerun()

else:
    if st.session_state.get("navigate_to_results"):
        st.session_state.current_page = "📊 Results"
        st.session_state.navigate_to_results = False

    st.sidebar.markdown("<div class='sidebar-welcome'>👋 Welcome</div>", unsafe_allow_html=True)
    st.sidebar.markdown("### Go to")
    if st.sidebar.button("📝 Form"):
        st.session_state.current_page = "📝 Form"
        st.rerun()
    if st.sidebar.button("📊 Results", disabled=not st.session_state.form_submitted):
        st.session_state.current_page = "📊 Results"
        st.rerun()

    page = st.session_state.current_page
    if page == "📝 Form":
        form.show()
    elif page == "📊 Results":
        results.show()