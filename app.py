import streamlit as st
from chatbot import get_groq_response, get_gif_url

st.set_page_config(page_title="Clueless Compliment Bot 🤖💖")
st.title("Clueless Compliment Bot 🤖💖")

user_input = st.text_input("Say something:")

if user_input:
    response = get_groq_response(user_input)
    st.markdown(f"**Bot:** {response}")

    gif_url = get_gif_url(user_input)
    if gif_url:
        st.image(gif_url, caption="Here's a GIF for you 💫")
