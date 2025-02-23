import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Growth Mindset project", page_icon="🌟", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&display=swap');
        
        html, body, .stApp { 
            background-color: #1e1e2f !important; 
            color: white !important; 
            font-family: 'Montserrat', sans-serif !important; 
        }
        
        h1, h2, h3, h4, h5, h6, p, span, div, label { 
            color: white !important; 
        }

        .title { 
            font-size: 50px; 
            font-weight: bold; 
            text-align: center; 
            background: linear-gradient(90deg, #ff8c00, #ff3e6c);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 20px; 
            animation: fadeIn 1.5s ease-in-out; 
        }

        .stButton>button { 
            background: linear-gradient(90deg, #ff8c00, #ff3e6c);
            color: white; 
            font-size: 18px; 
            font-weight: bold; 
            border: none; 
            border-radius: 8px; 
            padding: 12px 25px; 
            cursor: pointer; 
            transition: all 0.3s ease; 
            margin-top: 10px; 
        }
        
        .stButton>button:hover { 
            transform: scale(1.1); 
            background: linear-gradient(90deg, #ff3e6c, #ff8c00);
        }
        
        @keyframes fadeIn { 
            from { opacity: 0; } 
            to { opacity: 1; } 
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>🌟 Elevate Your Mindset 💡</h1>", unsafe_allow_html=True)

# Daily Motivational Quotes
quotes = [
    "Dream big and dare to fail. — Norman Vaughan",
    "Do what you can, with what you have, where you are. — Theodore Roosevelt",
    "Act as if what you do makes a difference. It does. — William James",
    "Happiness is not something ready-made. It comes from your own actions. — Dalai Lama",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. — Winston Churchill"
]
st.markdown("<h2 class='subheader'>💡 Daily Inspiration</h2>", unsafe_allow_html=True)

# Add space before the "Inspire Me!" button
st.write("")  # Empty space to move the button down
if st.button("✨ Inspire Me!"):
    st.markdown(f"<div class='quote-box'>{random.choice(quotes)}</div>", unsafe_allow_html=True)

# Goal Setting Section
st.markdown("<h2 class='subheader'>🎯 Set & Achieve Goals</h2>", unsafe_allow_html=True)
goal = st.text_input("What is your goal for this week?")
if goal:
    st.success(f"🚀 Goal Set: **{goal}**. Stay committed and keep moving forward!")

# Productivity Challenges
challenges = [
    "Learn something new today and teach it to someone.",
    "Step out of your comfort zone and try something different!",
    "Spend 15 minutes reflecting on your achievements.",
    "List three things you're grateful for today.",
    "Declutter your workspace and organize your thoughts."
]
st.markdown("<h2 class='subheader'>🔥 Productivity Boost</h2>", unsafe_allow_html=True)

# Add space before the "Get Challenge!" button
st.write("")  # Empty space to move the button down
if st.button("💡 Get Challenge!"):
    st.info(f"💡 **Challenge:** {random.choice(challenges)}")

# Self Reflection Section
st.markdown("<h2 class='subheader'>💭 Reflect & Grow</h2>", unsafe_allow_html=True)
reflection = st.text_area("Write your thoughts:")
if reflection:
    st.success(f"💡 **Insightful Reflection:** {reflection}")

# Achievements Celebration
st.markdown("<h2 class='subheader'>🏆 Celebrate Success</h2>", unsafe_allow_html=True)
achievement = st.text_input("Share a recent win:")
if achievement:
    st.markdown(f"<div class='success-box'>🎉 You achieved: {achievement}</div>", unsafe_allow_html=True)

# Self-Growth Quiz
st.markdown("<h2 class='subheader'>📊 Growth Quiz</h2>", unsafe_allow_html=True)
quiz_question = "How often do you challenge yourself?"
quiz_answers = ["Rarely", "Sometimes", "Often", "Always"]
quiz_choice = st.radio(quiz_question, quiz_answers)
if st.button("Submit Answer"):
    feedback = {
        "Rarely": "Start taking small risks to grow!",
        "Sometimes": "Good effort! Keep stepping up.",
        "Often": "Great work! You're pushing yourself.",
        "Always": "Awesome! You truly have a growth mindset!"
    }
    st.success(feedback[quiz_choice])

# Success Wall
st.markdown("<h2 class='subheader'>🌟 Success Wall</h2>", unsafe_allow_html=True)
if "success_wall" not in st.session_state:
    st.session_state.success_wall = []
success_message = st.text_input("Post a success story:")
if st.button("Post to Wall"):
    if success_message:
        st.session_state.success_wall.append(success_message)
        st.success("🎉 Success story added!")

# Display Success Wall
if st.session_state.success_wall:
    for story in st.session_state.success_wall:
        st.markdown(f"<div class='success-box'>{story}</div>", unsafe_allow_html=True)

# Daily Reminders
st.markdown("<h2 class='subheader'>🔄 Stay Motivated</h2>", unsafe_allow_html=True)
reminders = [
    "Every small step counts. Keep moving forward. 🚀",
    "Your future self will thank you for today's effort! 🌟",
    "Success comes from consistency. Keep showing up! 💪",
    "Failure is just another step towards growth. Never give up! 🔥",
    "Great things take time. Stay patient and persistent! ⏳"
]
if st.button("🔔 Get Reminder!"):
    st.success(random.choice(reminders))

# Footer
st.markdown("""
<div class='footer'>
🚀 Believe in yourself—every challenge you overcome, every step you take, and every lesson you learn shapes your incredible journey! ❤️🌟<br>
<strong>Created by Mehak Rehman</strong>
</div>
""", unsafe_allow_html=True)