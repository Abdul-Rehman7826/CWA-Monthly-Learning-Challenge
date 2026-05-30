import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

prompt = "Tell me a joke."
payload = {
    "contents": [{
        "parts": [{"text": prompt}]
    }]
}

response = requests.post(url, json=payload)
data = response.json()
print(data["candidates"][0]["content"]["parts"][0]["text"])