import streamlit as st
import random

# Custom CSS for background and UI elements with improved readability
st.markdown("""
    <style>
    body {
        background-image: url('https://images.unsplash.com/photo-1506748686214-e9df14d4d9d0');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #ffffff;
    }
    .stApp {
        background: rgba(0, 0, 0, 0.8); /* Increased opacity for better readability */
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.2), 0 6px 20px 0 rgba(255, 255, 255, 0.19);
    }
    .stButton>button {
        border-radius: 10px;
        background-color: #f72585;
        color: #ffffff;
        border: none;
        padding: 10px 20px;
        font-size: 1.2rem;
        cursor: pointer;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #7209b7;
    }
    .stTextInput>div>input {
        border-radius: 10px;
        padding: 10px;
        font-size: 1rem;
        border: 1px solid #ffffff;
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown h4, .stMarkdown h5, .stMarkdown h6, .stMarkdown p {
        color: #ffffff; /* Ensuring all text is white for better visibility */
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); /* Subtle shadow for text readability */
    }
    </style>
    """, unsafe_allow_html=True)

# Dynamic Quotes
good_quotes = [
    "You're on the right track! Keep it up! 🌟",
    "Today is your day, make it count! 🌞",
    "Positivity is your superpower! 💪",
]

bad_quotes = [
    "Tough times never last, but tough people do. 💪",
    "Every day may not be good, but there is something good in every day. 🌈",
    "Believe you can, and you're halfway there. 🌠"
]

# Jokes
jokes = [
    "Why don't scientists trust atoms? Because they make up everything! 🧪",
    "Why did the math book look sad? Because it had too many problems. 📘",
    "What do you call fake spaghetti? An impasta! 🍝",
    "Parallel lines have so much in common. It’s a shame they’ll never meet. 📏",
    "Why can't you trust an atom? Because they literally make up everything! 🧬",
    "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them. ➖",
    "Why was the equal sign so humble? Because it knew it wasn’t less than or greater than anyone else. 🤝",
    "Why did the physicist break up with the biologist? There was no chemistry. 🧑‍🔬",
    "How do you organize a space party? You planet. 🌌",
    "What do you get when you cross a snowman and a vampire? Frostbite. ☃️🧛",
    "I told my computer I needed a break, and now it won’t stop sending me Kit-Kats. 🍫",
    "Why don't programmers like nature? It has too many bugs. 🐛",
    "I would tell you a joke about an elevator, but it's an uplifting experience that might let you down. 🚪"
]

# Title of the app
st.title("How Are You?")

# Get user name
user_name = st.text_input("What's your name?")

if user_name:
    st.write(f"Hi {user_name}, let's see how you're feeling today!")

    # Buttons for user input
    good_button = st.button("I'm Good!")
    bad_button = st.button("Not So Good")

    # Function to show additional personalized uplifting content
    def show_additional_uplift(is_good, user_name):
        if is_good:
            st.write(f"{user_name}, you're doing an amazing job, and your positivity is contagious! 😊")
        else:
            st.write(f"{user_name}, remember that you bring so much light to the people around you, even on tough days. 🌟")
        st.write(f"{user_name}, take a moment to appreciate something small that made you smile today. 🌸")

    # Function to show motivational messages, jokes, and emojis
    def show_response(is_good):
        if is_good:
            message = random.choice(good_quotes)
        else:
            message = random.choice(bad_quotes)

        st.subheader(message)
        st.write("Here's a joke to brighten your day: 😄")
        st.write(random.choice(jokes))

        # Show additional personalized uplifting content
        show_additional_uplift(is_good, user_name)

    # Check which button was pressed
    if good_button:
        show_response(is_good=True)
    elif bad_button:
        show_response(is_good=False)



# Embed a YouTube video in the background (Rick Astley - Never Gonna Give You Up)
st.markdown(
    """
    <iframe width="0" height="0" src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1&loop=1&playlist=dQw4w9WgXcQ" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
