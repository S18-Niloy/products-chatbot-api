import httpx, os
from dotenv import load_dotenv

load_dotenv()

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"

    def chat(self, messages):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        payload = {
            "model": "llama-3.1-8b-instant",
            "messages": messages,
        }
        resp = httpx.post(self.base_url, headers=headers, json=payload)

        # 👇 Add this block for debugging
        print("Groq API status:", resp.status_code)
        print("Groq API response:", resp.text)

        data = resp.json()
        if "choices" not in data:
            return f"Groq API error: {data.get('error', resp.text)}"

        return data["choices"][0]["message"]["content"]
