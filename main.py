from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
import os
import uvicorn
from joke_engine import generate_joke_text  # Updated import

import openai
print("OpenAI Package Version:", openai.__version__)

# Define FastAPI instance
app = FastAPI()

# Mount static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "DELI is roasting."}

@app.get("/generate-joke")
async def trigger_joke():
    headline = "Solana surges 20% after meme coin called 'Bonk Bonk' goes viral."  # Example headline
    joke_text = generate_joke_text(headline)  # Generate joke text
    return {"status": "Joke generated!", "joke": joke_text}

# Ensure main execution starts correctly
if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)
