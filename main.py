from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
import os
import uvicorn
from joke_engine import generate_joke_text, get_latest_crypto_headline, text_to_speech
from fastapi.responses import FileResponse

import openai
print("OpenAI Package Version:", openai.__version__)

async def joke_loop():
    """ Continuously generates jokes every 90 seconds """
    while True:
        headline = get_latest_crypto_headline()
        joke_text = generate_joke_text(headline)

        # Convert joke into audio
        audio_file = text_to_speech(joke_text)

        if audio_file:
            print(f"Loop audio file generated: {audio_file}")
        else:
            print("Audio generation failed.")

        print(f"Loop joke: {joke_text}")
        await asyncio.sleep(30)

# Define FastAPI instance
app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """ Start the background loop when the app starts """
    asyncio.create_task(joke_loop())

@app.get("/")
def read_root():
    return {"message": "DELI is roasting."}

@app.get("/generate-joke")
async def trigger_joke():
    headline = get_latest_crypto_headline()
    joke_text = generate_joke_text(headline)

    # Invoke TTS to generate the audio file
    audio_file = text_to_speech(joke_text)

    if audio_file and os.path.exists(audio_file):
        return {
            "status": "Joke generated",
            "joke": joke_text,
            "audio_file": audio_file
        }
    
    return {
        "status": "Joke generated",
        "joke": joke_text,
        "error": "Audio file could not be created"
    }

@app.get("/latest-audio")
async def serve_audio():
    """ Serve the latest generated joke audio file """
    audio_path = "joke_audio.mp3"
    if os.path.exists(audio_path):
        return FileResponse(audio_path, media_type="audio/mpeg")
    return {"error": "Audio file not found"}

# Ensure main execution starts correctly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)
