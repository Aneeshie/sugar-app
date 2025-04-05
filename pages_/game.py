import streamlit as st
import random

def show():
    st.markdown("""
    <div style='text-align: center; margin-bottom: 30px;'>
        <h1>🎮 Health Knowledge Challenge</h1>
        <p class='subtitle'>Test your health awareness by selecting the healthier option</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Game questions with detailed explanations
    questions = [
    {
        "question": "Which food is better for blood sugar control?",
        "options": [
            {
                "name": "White Bread", 
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Korb_mit_Br%C3%B6tchen.JPG/1200px-Korb_mit_Br%C3%B6tchen.JPG", 
                "correct": False, 
                "explanation": "White bread is made from refined flour which is quickly digested, causing rapid spikes in blood sugar. The lack of fiber means your body absorbs the carbohydrates too quickly."
            },
            {
                "name": "Whole Grain Bread", 
                "image": "/home/zerome/coding/sugar-app/assets/wholewheat.png", 
                "correct": True, 
                "explanation": "Whole grain bread contains all parts of the grain, including fiber which slows digestion. This results in a more gradual release of glucose into your bloodstream."
            }
        ]
    },
    {
        "question": "Which activity burns more calories?",
        "options": [
            {
                "name": "Walking", 
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6d/Good_Food_Display_-_NCI_Visuals_Online.jpg/1200px-Good_Food_Display_-_NCI_Visuals_Online.jpg", 
                "correct": False, 
                "explanation": "While walking is excellent for general health, it's a low-intensity activity. A 30-minute walk typically burns 100-200 calories depending on your pace."
            },
            {
                "name": "Swimming", 
                "image": "/home/zerome/coding/sugar-app/assets/swimming.png", 
                "correct": True, 
                "explanation": "Swimming engages nearly all muscle groups simultaneously while providing resistance from the water. This full-body workout can burn 400-700 calories per hour."
            }
        ]
    },
    {
        "question": "Which type of fat is considered healthier?",
        "options": [
            {
                "name": "Saturated Fat", 
                "image": "/home/zerome/coding/sugar-app/assets/butter.png", 
                "correct": False, 
                "explanation": "Saturated fats, found in foods like butter and fatty cuts of meat, can increase your cholesterol levels, leading to higher risks of heart disease."
            },
            {
                "name": "Unsaturated Fat", 
                "image": "/home/zerome/coding/sugar-app/assets/avacados.png", 
                "correct": True, 
                "explanation": "Unsaturated fats, found in foods like olive oil, nuts, and avocados, can help lower cholesterol levels and reduce heart disease risk."
            }
        ]
    },
    {
        "question": "Which beverage is better for hydration?",
        "options": [
            {
                "name": "Coffee", 
                "image": "/home/zerome/coding/sugar-app/assets/coffee.png", 
                "correct": False, 
                "explanation": "Coffee, due to its caffeine content, can have a mild diuretic effect, leading to increased urination and possible dehydration."
            },
            {
                "name": "Water", 
                "image": "/home/zerome/coding/sugar-app/assets/water.png", 
                "correct": True, 
                "explanation": "Water is the most effective drink for hydration as it helps maintain bodily functions and replenishes fluids lost through sweat and urination."
            }
        ]
    }
    
]


    # Initialize game state
    if 'game_state' not in st.session_state:
        st.session_state.game_state = {
            'current_question': 0,
            'score': 0,
            'questions': random.sample(questions, len(questions)),  # Shuffle questions
            'feedback': None,
            'show_explanation': False
        }

    # Get current question
    game_state = st.session_state.game_state
    current_q = game_state['questions'][game_state['current_question']]
    
    # Display question
    st.markdown(f"<h3 style='text-align: center;'>{current_q['question']}</h3>", unsafe_allow_html=True)
    
    # Display options
    cols = st.columns(2)
    for i, option in enumerate(current_q['options']):
        with cols[i]:
            st.image(option['image'], caption=option['name'], use_container_width=True)
            if st.button(f"Select {option['name']}", key=f"option_{i}"):
                if option['correct']:
                    game_state['score'] += 1
                    game_state['feedback'] = f"✅ Correct! {option['name']} is the healthier choice."
                else:
                    game_state['feedback'] = f"❌ Not quite. {option['name']} is less healthy for this category."
                
                game_state['show_explanation'] = True
                game_state['explanation'] = option['explanation']
                
                # Move to next question or end game
                if game_state['current_question'] < len(game_state['questions']) - 1:
                    game_state['current_question'] += 1
                else:
                    game_state['game_completed'] = True
                    game_state['feedback'] += f" 🎉 Game complete! Your score: {game_state['score']}/{len(game_state['questions'])}"
                
                st.rerun()

    # Display feedback
    if game_state['feedback']:
        if "✅" in game_state['feedback']:
            st.success(game_state['feedback'])
        else:
            st.error(game_state['feedback'])
        
        if game_state['show_explanation']:
            with st.expander("💡 Learn why"):
                st.info(game_state['explanation'])

    # Progress
    st.progress((game_state['current_question'] + 1) / len(game_state['questions']))
    st.caption(f"Question {game_state['current_question'] + 1} of {len(game_state['questions'])}")

    # Skip button
    if st.button("Skip to Assessment"):
        st.session_state.game_completed = True
        st.rerun()