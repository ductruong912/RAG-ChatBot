from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(message: str) -> str:
    response = client.chat.completions.create(
        model = os.getenv("model"),
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": message}            
            ],
            temperature=0.2
    )
    return response.choices[0].message.content
