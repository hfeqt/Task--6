import os
import requests
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

# Get AI response from Groq
def get_groq_response(user_input):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": "You are a clueless, overly sweet, and emotionally sensitive chatbot. You try really hard to help people, but often get confused. You constantly compliment users and apologize even when you haven’t done anything wrong. You use lots of emojis and get excited about silly things."},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

# Get GIF from GIPHY
def get_gif_url(query):
    api_key = os.getenv("GIPHY_API_KEY")
    url = f"https://api.giphy.com/v1/gifs/search?api_key={api_key}&q={query}&limit=1"
    response = requests.get(url)
    data = response.json()
    if data['data']:
        return data['data'][0]['images']['original']['url']
    else:
        return None
