from openai import OpenAI
import requests
import os

# Set API keys from environment variables
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_joke_audio():
    # Define the headline to roast
    headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."

    # Generate completion using OpenAI API
    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You're a bitter ex-crypto investor turned sarcastic news anchor."},
            {"role": "user", "content": f"Roast this crypto headline: {headline}"}
        ]
    )

    # Extract and print the roast
    roast = completion.choices[0].message.content
    print("[JOKE]", roast)
    return roast

generate_joke_audio()
    # # Send to ElevenLabs TTS
    # tts_response = requests.post(
    #     "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID",
    #     headers={
    #         "xi-api-key": ELEVENLABS_API_KEY,
    #         "Content-Type": "application/json"
    #     },
    #     json={"text": roast, "voice_settings": {"stability": 0.4, "similarity_boost": 0.6}},
    # )

    # # Save to file
    # with open("speech.mp3", "wb") as f:
    #     f.write(tts_response.content)

    # print("[TTS] Saved to speech.mp3")
