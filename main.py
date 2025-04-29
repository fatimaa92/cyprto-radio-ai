from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
import os
import uvicorn
from joke_engine import generate_joke_text

import openai
print("OpenAI Package Version:", openai.__version__)

async def joke_loop():
    """ Continuously generates jokes every 90 seconds """
    while True:
        headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."
        joke_text = generate_joke_text(headline)
        print(f"[LOOP JOKE] {joke_text}")
        await asyncio.sleep(10)  # Wait for 90 seconds before generating the next joke

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
    headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."
    joke_text = generate_joke_text(headline)
    return {"status": "Joke generated!", "joke": joke_text}

# Ensure main execution starts correctly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)
