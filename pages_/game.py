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
        # Original questions
        {
            "question": "Which food is better for blood sugar control?",
            "options": [
                {"name": "White Bread", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3%B6tchen.JPG/1200px-Korb_mit_Br%C3%B6tchen.JPG", "correct": False, "explanation": "Whole grains have more fiber which slows glucose absorption."},
                {"name": "Whole Grain Bread", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/Five-grain_bread.jpg/1200px-Five-grain_bread.jpg", "correct": True, "explanation": "The fiber in whole grains helps regulate blood sugar levels."}
            ]
        },
        {
            "question": "Which activity burns more calories?",
            "options": [
                {"name": "Walking", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg", "correct": False, "explanation": "Walking burns about 100-300 calories/hour depending on intensity."},
                {"name": "Swimming", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Swimming_in_the_sea_in_Kerala.jpg/1200px-Swimming_in_the_sea_in_Kerala.jpg", "correct": True, "explanation": "Swimming burns 400-700 calories/hour due to full-body engagement."}
            ]
        },
        {
            "question": "Which is better for heart health?",
            "options": [
                {"name": "Butter", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Emmentaler_und_Butter.JPG/1200px-Emmentaler_und_Butter.JPG", "correct": False, "explanation": "Butter contains saturated fats that can raise LDL cholesterol."},
                {"name": "Avocado", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Avocado_Hass_-_single_and_halved.jpg/1200px-Avocado_Hass_-_single_and_halved.jpg", "correct": True, "explanation": "Avocados contain heart-healthy monounsaturated fats."}
            ]
        },
        
        # 7 New questions added below
        {
            "question": "Which drink is better for hydration?",
            "options": [
                {"name": "Soda", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Cola-Cola_original_bottle.jpg/1200px-Cola-Cola_original_bottle.jpg", "correct": False, "explanation": "Soda's high sugar content can actually dehydrate you."},
                {"name": "Coconut Water", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Coconut_water_in_coconut.jpg/1200px-Coconut_water_in_coconut.jpg", "correct": True, "explanation": "Contains electrolytes that help with hydration."}
            ]
        },
        {
            "question": "Which snack is better for sustained energy?",
            "options": [
                {"name": "Candy Bar", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Chocolate_candy_bar.jpg/1200px-Chocolate_candy_bar.jpg", "correct": False, "explanation": "Causes blood sugar spikes followed by crashes."},
                {"name": "Almonds", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Almonds_-_single_-_2012-02-28.jpg/1200px-Almonds_-_single_-_2012-02-28.jpg", "correct": True, "explanation": "Provides protein and healthy fats for steady energy."}
            ]
        },
        {
            "question": "Which is better for gut health?",
            "options": [
                {"name": "White Rice", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7b/Steamed_rice.jpg/1200px-Steamed_rice.jpg", "correct": False, "explanation": "Lacks the fiber needed for good gut bacteria."},
                {"name": "Kimchi", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Kimchi.jpg/1200px-Kimchi.jpg", "correct": True, "explanation": "Fermented food rich in probiotics for gut health."}
            ]
        },
        {
            "question": "Which is better for bone strength?",
            "options": [
                {"name": "Ice Cream", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Strawberry_ice_cream_cone_%285076899310%29.jpg/1200px-Strawberry_ice_cream_cone_%285076899310%29.jpg", "correct": False, "explanation": "High in sugar but low in bone-building nutrients."},
                {"name": "Yogurt", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2c/Yogurt_%281%29.jpg/1200px-Yogurt_%28%29.jpg", "correct": True, "explanation": "Rich in calcium and vitamin D for bones."}
            ]
        },
        {
            "question": "Which is better for eye health?",
            "options": [
                {"name": "Potato Chips", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Potato-Chips.jpg/1200px-Potato-Chips.jpg", "correct": False, "explanation": "No significant eye health benefits."},
                {"name": "Carrots", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Carrots_of_many_colors.jpg/1200px-Carrots_of_many_colors.jpg", "correct": True, "explanation": "Rich in beta-carotene which converts to vitamin A."}
            ]
        },
        {
            "question": "Which is better for immune support?",
            "options": [
                {"name": "Energy Drink", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Red_Bull_Can.jpg/1200px-Red_Bull_Can.jpg", "correct": False, "explanation": "Contains stimulants but no immune-boosting nutrients."},
                {"name": "Oranges", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/Ambersweet_oranges.jpg/1200px-Ambersweet_oranges.jpg", "correct": True, "explanation": "High in vitamin C which supports immune function."}
            ]
        },
        {
            "question": "Which is better for post-workout recovery?",
            "options": [
                {"name": "Sports Drink", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Gatorade_bottles.jpg/1200px-Gatorade_bottles.jpg", "correct": False, "explanation": "Contains electrolytes but often too much sugar."},
                {"name": "Banana", "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Bananas_white_background_DS.jpg/1200px-Bananas_white_background_DS.jpg", "correct": True, "explanation": "Provides potassium and natural sugars for recovery."}
            ]
        }
    ]
    
    # Initialize game state
    if "current_level" not in st.session_state:
        st.session_state.current_level = 0
        st.session_state.score = 0
        st.session_state.game_feedback = ""
        st.session_state.show_explanation = False
        random.shuffle(levels)  # Shuffle questions for variety
        st.session_state.levels = levels
    
    # Display current question
    level = st.session_state.levels[st.session_state.current_level]
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
                    
                    st.session_state.show_explanation = True
                    st.session_state.explanation = option["explanation"]
                    
                    # Move to next level or end game
                    if st.session_state.current_level < len(st.session_state.levels) - 1:
                        st.session_state.current_level += 1
                    else:
                        st.session_state.game_completed = True
                        st.session_state.game_feedback += f" 🎉 Game complete! Your score: {st.session_state.score}/{len(st.session_state.levels)}"
                    st.rerun()
    
    # Display feedback and explanation
    if st.session_state.game_feedback:
        if "✅" in st.session_state.game_feedback:
            st.success(st.session_state.game_feedback)
        else:
            st.error(st.session_state.game_feedback)
        
        if st.session_state.show_explanation:
            with st.expander("💡 Learn why"):
                st.info(st.session_state.explanation)
    
    # Progress bar
    progress = (st.session_state.current_level + 1) / len(st.session_state.levels)
    st.progress(progress)
    st.caption(f"Question {st.session_state.current_level + 1} of {len(st.session_state.levels)}")
    
    # Skip option
    st.markdown("---")
    if st.button("Skip to Health Assessment", use_container_width=True):
        st.session_state.game_completed = True
        st.rerun()