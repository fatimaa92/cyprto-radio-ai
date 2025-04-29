import os
from openai import OpenAI
import requests


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ElevenLabs API setup
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = "GcPTBXiuIz3xYDstbCNX"

### Fetch the Latest Crypto Headline
def get_latest_crypto_headline():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        trending_coins = data["coins"]
        
        if trending_coins:
            latest_headline = f"{trending_coins[0]['item']['name']} is trending with {trending_coins[0]['item']['symbol']}!"
            return latest_headline
        else:
            return "No trending crypto found."

    else:
        return f"Error fetching data: {response.status_code}"

def generate_joke_text(headline):
    prompt = f"You're a sarcastic crypto radio host. Given the headline: {headline}, roast it with a funny, dramatic monologue like someone who lost everything in a yield farm. Add dry humor and irony."
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )
    joke_text = response.choices[0].message.content
    print(f"[JOKE] {joke_text}")
    return joke_text

def text_to_speech(joke_text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": joke_text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.3,
            "similarity_boost": 0.8
        }
    }
    response = requests.post(url, headers=headers, json=payload)

    # if response.status_code != 200:
    #     raise Exception(f"ElevenLabs TTS failed: {response.text}")
    
    # Save to file (optional)
    with open("joke_audio.mp3", "wb") as f:
        f.write(response.content)

    return "joke_audio.mp3"

# def generate_joke_audio(headline):
#     joke_text = generate_joke_text(headline)
#     audio_file = text_to_speech(joke_text)
#     return audio_file  # You can stream or serve this file as needed
