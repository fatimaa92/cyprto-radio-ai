import os
import requests
from openai import OpenAI

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
            print(f"Latest Headline: {latest_headline}")  # Debugging
            return latest_headline
        else:
            print("No trending crypto found.")  # Debugging
            return "No trending crypto found."

    else:
        print(f"Error fetching data: {response.status_code}")  # Debugging
        return f"Error fetching data: {response.status_code}"

### Generate Joke Using the Latest Headline
def generate_joke_text(headline):

    prompt = f"You're a sarcastic crypto radio host. Given the headline: {headline}, roast it with a funny, dramatic monologue like someone who lost everything in a yield farm. Add dry humor and irony."
    
    print("Sending request to OpenAI API for joke generation...")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    joke_text = response.choices[0].message.content
    print(f"Joke Generated: {joke_text}")  # Debugging
    return joke_text

### Convert Joke to Speech Using ElevenLabs
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

    print("Invoking ElevenLabs Text-to-Speech API...")
    response = requests.post(url, headers=headers, json=payload)

    # Debugging Statements
    print(f"API Response Code: {response.status_code}")
    print(f"Response Content: {response.text}")

    if response.status_code == 200:
        audio_file = "joke_audio.mp3"
        with open(audio_file, "wb") as f:
            f.write(response.content)

        # Check if the file was successfully created
        if os.path.exists(audio_file):
            print(f"Audio file created: {audio_file}")
            return audio_file
        else:
            print("Audio file was not created.")
            return None
    else:
        print("ElevenLabs TTS failed.")
        return None

# def generate_joke_audio(headline):
#     joke_text = generate_joke_text(headline)
#     audio_file = text_to_speech(joke_text)
#     return audio_file  # You can stream or serve this file as needed
