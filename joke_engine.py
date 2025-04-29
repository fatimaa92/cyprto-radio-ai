import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def roast_headline(headline: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a sarcastic, salty crypto news anchor who roasts headlines."},
            {"role": "user", "content": f"Roast this headline in a funny tone: {headline}"}
        ]
    )
    return response["choices"][0]["message"]["content"]
