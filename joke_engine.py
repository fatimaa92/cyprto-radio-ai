import openai
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

print("OpenAI Key:", os.getenv("OPENAI_API_KEY"))
print("ElevenLabs Key:", os.getenv("ELEVENLABS_API_KEY"))

async def generate_joke_audio():
    # Replace with live headline fetch later
    headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."

    # Use GPT to roast the headline
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a bitter ex-crypto investor turned sarcastic news anchor."},
            {"role": "user", "content": f"Roast this crypto headline: {headline}"}
        ]
    )
    roast = response.choices[0].message.content
    print("[JOKE]", roast)

    # Send to ElevenLabs TTS
    tts_response = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID",
        headers={
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        },
        json={"text": roast, "voice_settings": {"stability": 0.4, "similarity_boost": 0.6}},
    )

    # Save to file (OBS can read from this)
    with open("speech.mp3", "wb") as f:
        f.write(tts_response.content)
    print("[TTS] Saved to speech.mp3")
