import os
import requests
import time

# Joke API URL
JOKE_API_URL = "https://crypto-radio-ai.onrender.com/generate-joke"

# ElevenLabs API setup
ELEVENLABS_API_KEY = ""
VOICE_ID = ""

def fetch_joke():
    """ Fetch the latest joke from the API """
    print("Fetching joke from API...")
    response = requests.get(JOKE_API_URL)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data.get("joke", "No joke found.")
        print(f"Joke Retrieved: {joke_text[:100]}...")  # Show preview
        return joke_text
    else:
        print(f"Error fetching joke: {response.status_code}")
        return None

def text_to_speech(joke_text):
    """ Convert joke to speech using ElevenLabs """
    if not joke_text:
        print("No joke available for conversion.")
        return None

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

    print(f"API Response Code: {response.status_code}")

    if response.status_code == 200:
        audio_file = "joke_audio.mp3"
        with open(audio_file, "wb") as f:
            f.write(response.content)

        if os.path.exists(audio_file):
            print(f"Audio file created successfully: {audio_file}")
            return audio_file
        else:
            print("Audio file was not created.")
            return None
    else:
        print(f"ElevenLabs TTS failed: {response.text}")
        return None

def main():
    """ Run the script every 90 seconds """
    while True:
        joke_text = fetch_joke()  # Get joke from API
        text_to_speech(joke_text)  # Convert to speech
        print("Waiting 90 seconds before fetching the next joke...")
        time.sleep(90)  # Wait for 90 seconds

if __name__ == "__main__":
    main()
