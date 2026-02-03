from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
CHATBOT_NAME = os.getenv("CHATBOT_NAME", "Instructor for Agentic AI")
