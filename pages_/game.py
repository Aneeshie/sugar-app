# game.py
import streamlit as st
import random

def show():
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1>🎮 Health Knowledge Challenge</h1>
        <p class='subtitle'>Test your health awareness by selecting the healthier option</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Game levels with increasing difficulty
    levels = [
        {
            "question": "Which food is better for blood sugar control?",
            "options": [
                {"name": "White Bread", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3%B6tchen.JPG/1200px-Korb_mit_Br%C3%B6tchen.JPG", "correct": False},
                {"name": "Whole Grain Bread", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Five-grain_bread.jpg/1200px-Five-grain_bread.jpg", "correct": True}
            ]
        },
        {
            "question": "Which activity burns more calories?",
            "options": [
                {"name": "Walking", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg", "correct": False},
                {"name": "Swimming", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Swimming_in_the_sea_in_Kerala.jpg/1200px-Swimming_in_the_sea_in_Kerala.jpg", "correct": True}
            ]
        },
        {
            "question": "Which is better for heart health?",
            "options": [
                {"name": "Butter", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Emmentaler_und_Butter.JPG/1200px-Emmentaler_und_Butter.JPG", "correct": False},
                {"name": "Avocado", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Avocado_Hass_-_single_and_halved.jpg/1200px-Avocado_Hass_-_single_and_halved.jpg", "correct": True}
            ]
        }
    ]
    
    # Initialize game state
    if "current_level" not in st.session_state:
        st.session_state.current_level = 0
        st.session_state.score = 0
        st.session_state.game_feedback = ""
    
    # Display current question
    level = levels[st.session_state.current_level]
    st.markdown(f"<h3 style='text-align: center; margin-bottom: 30px;'>{level['question']}</h3>", unsafe_allow_html=True)
    
    # Display options
    cols = st.columns(2)
    for i, option in enumerate(level["options"]):
        with cols[i]:
            with st.container():
                st.markdown(f"""
                <div class='card' style='text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
                    <img src='{option["image"]}' style='width: 100%; border-radius: 10px; height: 200px; object-fit: cover;'>
                    <h4>{option["name"]}</h4>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Select {option['name']}", key=f"option_{i}", use_container_width=True):
                    if option["correct"]:
                        st.session_state.score += 1
                        st.session_state.game_feedback = f"✅ Correct! {option['name']} is the healthier choice."
                    else:
                        st.session_state.game_feedback = f"❌ Not quite. {option['name']} is less healthy for this category."
                    
                    # Move to next level or end game
                    if st.session_state.current_level < len(levels) - 1:
                        st.session_state.current_level += 1
                    else:
                        st.session_state.game_completed = True
                        st.session_state.game_feedback += f" 🎉 Game complete! Your score: {st.session_state.score}/{len(levels)}"
                    st.rerun()
    
    # Display feedback
    if st.session_state.game_feedback:
        if "✅" in st.session_state.game_feedback:
            st.success(st.session_state.game_feedback)
        else:
            st.error(st.session_state.game_feedback)
    
    # Skip option
    st.markdown("---")
    if st.button("Skip to Health Assessment", use_container_width=True):
        st.session_state.game_completed = True
        st.rerun()