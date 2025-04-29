from openai import OpenAI
import requests
import os

# Set API keys from environment variables
# ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
# openai.api_key = os.getenv("OPENAI_API_KEY")
# Initialize OpenAI client
client = OpenAI(api_key="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")# Debugging
# print("OpenAI API Key:", os.getenv("OPENAI_API_KEY"))  # Check if API key is loaded
# print("OpenAI Version:", openai.__version__)  # Check installed OpenAI version

def generate_joke_audio():
    # Define the headline to roast
    headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."

    # GPT joke generation using new SDK syntax
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a bitter ex-crypto investor turned sarcastic news anchor."},
            {"role": "user", "content": f"Roast this crypto headline: {headline}"}
        ]
    )
    roast = response.choices[0].message.content
    print("[JOKE]", roast)

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
