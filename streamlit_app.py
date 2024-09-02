import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Interactive Greeting",
    page_icon="👋",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Use more advanced CSS for a modern look
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
        font-size: 2rem;
        margin-top: 20px;
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the greeting message with animation
st.markdown('<div class="title">Hello, how are you?</div>', unsafe_allow_html=True)

# Add a text input box with custom styles
user_input = st.text_input("", placeholder="Type your response here...", key="input", label_visibility="collapsed")

# If the user inputs something, display it in capital letters with a reply
if user_input:
    st.markdown(f'<div class="response">{user_input.upper()}</div>', unsafe_allow_html=True)
    st.markdown('<div class="response">HAVE A NICE DAY AHEAD!</div>', unsafe_allow_html=True)

# Embed a YouTube video in the background (Rick Astley - Never Gonna Give You Up)
st.markdown(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&loop=1&playlist=dQw4w9WgXcQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
