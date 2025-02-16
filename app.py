import streamlit as st 
import time
from datetime import datetime
import random

# Page configuration
st.set_page_config(page_title="Animated Chatbot", layout="wide")

# Custom CSS for animations and styling
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        animation: fadeIn 0.5s ease-in;
    }
    
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
    
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(20px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    .typing-indicator {
        padding: 1rem;
        background-color: #f5f5f5;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        animation: pulse 1s infinite;
    }
    
    @keyframes pulse {
        0% { opacity: 0.4; }
        50% { opacity: 0.7; }
        100% { opacity: 0.4; }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Title
st.title("✨ Animated Chatbot")

# Function to simulate bot thinking
def show_typing_animation():
    with st.empty():
        st.markdown('<div class="typing-indicator">Bot is typing...</div>', unsafe_allow_html=True)
        time.sleep(random.uniform(1, 2))

# Function to generate bot response
def get_bot_response(user_input):
    # Add your chatbot logic here
    responses = [
        "That's interesting! Tell me more about it.",
        "I understand what you're saying. Let me think about that.",
        "Thanks for sharing! Here's what I think...",
        "That's a great point! Have you considered...",
        "I see what you mean. From my perspective..."
    ]
    return random.choice(responses)

# Function to display message with animation
def display_message(message, is_user):
    message_type = "user-message" if is_user else "bot-message"
    timestamp = datetime.now().strftime("%H:%M")
    st.markdown(f"""
        <div class="chat-message {message_type}">
            <div style="font-size: 0.8rem; color: gray;">{timestamp}</div>
            {message}
        </div>
    """, unsafe_allow_html=True)

# Chat interface
user_input = st.text_input("Type your message:", key="user_input")

if user_input:
    # Add user message to chat
    st.session_state.messages.append(("user", user_input))
    
    # Show typing animation
    show_typing_animation()
    
    # Generate and add bot response
    bot_response = get_bot_response(user_input)
    st.session_state.messages.append(("bot", bot_response))
    
    # Clear input
    st.empty()

# Display chat history with animations
for author, message in st.session_state.messages:
    display_message(message, author == "user")

# Add some space at the bottom
st.markdown("<br>" * 3, unsafe_allow_html=True)

# Sidebar with information
with st.sidebar:
    st.title("💡 About")
    st.write("""
    This is an animated chatbot demo built with Streamlit.
    Features:
    - Message animations
    - Typing indicators
    - Timestamps
    - Responsive design
    """)
