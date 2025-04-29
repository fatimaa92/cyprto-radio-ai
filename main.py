from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import asyncio
from joke_engine import generate_joke_audio
from contextlib import asynccontextmanager
import os
import uvicorn

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Default to 8000 if PORT isn't set
    uvicorn.run(app, host="0.0.0.0", port=port)

@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(loop())
    yield
    task.cancel()  # Clean up when shutting down

async def loop():
    while True:
        await generate_joke_audio()
        await asyncio.sleep(90)

app = FastAPI(lifespan=lifespan)  # Combine everything into one FastAPI instance
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def read_root():
    return {"message": "DELI is roasting."}
