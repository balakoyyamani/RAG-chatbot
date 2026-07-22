from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key=os.getenv("GOOGLE_API_KEY_RAG_BOT_01")
if not api_key:
    raise ValueError("Error: Api Key not loaded")

client=genai.Client(api_key=api_key)

chat_model="gemma-4-31b-it"
embedding_model="gemini-embedding-001"