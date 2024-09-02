import streamlit as st
import random

# Set the page configuration
st.set_page_config(
    page_title="Interactive Greeting",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# CSS styling for the app with fancy effects
st.markdown(
    """
    <style>
    .stApp {
        background-color: #2ecc71;
        color: white;
        font-family: 'Arial', sans-serif;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        flex-direction: column;
        text-align: center;
    }

    .title {
        font-size: 3rem;
        margin-bottom: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    .input-box {
        margin-bottom: 20px;
        width: 60%;
        font-size: 1.5rem;
        padding: 10px;
        border-radius: 10px;
        border: none;
        outline: none;
    }

    .input-box::placeholder {
        color: #95a5a6;
    }

    .response {
        font-size: 2.5rem;
        margin-top: 20px;
        animation: blink 1.5s infinite alternate;
        font-weight: bold;
    }

    .quote {
        margin-top: 20px;
        font-size: 1.8rem;
        font-style: italic;
        color: #f5f5f5;
    }

    img.motivational-image {
        margin-top: 30px;
        width: 80%;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }

    @keyframes blink {
        from { opacity: 1; }
        to { opacity: 0; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the greeting message
st.markdown('<div class="title">Hello, how are you?</div>', unsafe_allow_html=True)

# User input box
user_input = st.text_input("", placeholder="Type your response here...", key="input", label_visibility="collapsed")

if user_input:
    st.markdown(f'<div class="response">{user_input.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="response">HAVE A NICE DAY AHEAD!</div>', unsafe_allow_html=True)
    
    # List of inspirational quotes
    inspirational_quotes = [
        "Give yourself a pat on the back, you're doing great!",
        "Remember to take a moment to celebrate your small wins.",
        "You’ve come so far. Take a moment to appreciate yourself.",
        "Believe in yourself—you are more capable than you think.",
        "Every step forward, no matter how small, is a step closer to your goal."
    ]
    
    # Randomly select a quote
    selected_quote = random.choice(inspirational_quotes)
    
    # Display the quote
    st.markdown(f'<div class="quote">"{selected_quote}"</div>', unsafe_allow_html=True)
    
    # Specific motivational image URLs
    motivational_images = [
        "https://plus.unsplash.com/premium_photo-1671599016130-7882dbff302f?q=80&w=1887&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "https://images.unsplash.com/photo-1496449903678-68ddcb189a24?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    ]

    # Select a random image from the list
    selected_image = random.choice(motivational_images)

    # Display the motivational image with styling
    st.markdown(f'<img src="{selected_image}" class="motivational-image" alt="Motivational Image">', unsafe_allow_html=True)

# Embed a YouTube video in the background (Rick Astley - Never Gonna Give You Up)
st.markdown(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&loop=1&playlist=dQw4w9WgXcQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
