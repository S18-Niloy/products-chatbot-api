from fastapi import FastAPI
from dotenv import load_dotenv
import os
from app.api import routes_chatbot

# Load .env from the server root directory
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

api_key = os.getenv("GROQ_API_KEY")
if api_key:
    print("Loaded GROQ_API_KEY:", api_key[:10], "...")
else:
    print("GROQ_API_KEY not found. Check .env file location!")

app = FastAPI(title="Products Chatbot API")
app.include_router(routes_chatbot.router)

@app.get("/")
def root():
    return {"message": "Welcome to Products Chatbot API"}
