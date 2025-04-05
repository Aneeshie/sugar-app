import streamlit as st

def show():
    st.header("🎮 Play a Small Game")
    st.write("Choose the food item that does **not** promote diabetes by clicking its card.")

    # Sample food items (replace with local paths or more URLs as needed)
    food_items = [
        {
            "name": "Apple",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/1200px-Red_Apple.jpg",
            "diabetes_friendly": True
        },
        {
            "name": "Candy Bar",
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Chocolate_candy_bar.jpg/1200px-Chocolate_candy_bar.jpg",
            "diabetes_friendly": False
        }
    ]

    # Display cards side-by-side
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

    # Skip option
    if st.button("Skip Game"):
        st.session_state.game_completed = True
        st.rerun()