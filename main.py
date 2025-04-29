from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
from joke_engine import generate_joke_audio

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "DELI is roasting."}

@app.on_event("startup")
async def run_background_task():
    async def loop():
        while True:
            await generate_joke_audio()
            await asyncio.sleep(90)
    asyncio.create_task(loop())
