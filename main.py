from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
import os
import uvicorn
from joke_engine import generate_joke_text, get_latest_crypto_headline, text_to_speech
from fastapi.responses import FileResponse
from crypto_ticker import get_crypto_prices

import openai

app = FastAPI()

# Serve static files (for JavaScript & frontend assets)
app.mount("/static", StaticFiles(directory="static"), name="static")

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
        await asyncio.sleep(90)  # Change from 30 to 90 seconds

async def ticker_loop():
    """ Continuously fetch crypto prices every 30 seconds """
    while True:
        prices = get_crypto_prices()
        print("Latest Prices:", prices)
        await asyncio.sleep(60)

@app.on_event("startup")
async def startup_event():
    """ Start background loops when the app starts """
    asyncio.create_task(joke_loop())
    asyncio.create_task(ticker_loop())

@app.get("/")
def read_root():
    return {"message": "DELI is roasting."}

@app.get("/generate-joke")
async def trigger_joke():
    headline = get_latest_crypto_headline()
    joke_text = generate_joke_text(headline)

    return {
        "status": "Joke generated",
        "joke": joke_text
    }

# @app.get("/latest-audio")
# async def serve_audio():
#     """ Serve the latest generated joke audio file """
#     audio_path = "joke_audio.mp3"
#     if os.path.exists(audio_path):
#         return FileResponse(audio_path, media_type="audio/mpeg")
#     return {"error": "Audio file not found"}

@app.get("/crypto-prices")
async def fetch_crypto_prices():
    """ API endpoint to manually fetch crypto prices """
    return get_crypto_prices()

# Ensure main execution starts correctly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)
