import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    ENV = os.getenv("ENV", "dev")

    # Firebase
    FIREBASE_CRED = os.getenv("FIREBASE_CREDENTIALS")
    FIREBASE_PROJECT = os.getenv("FIRESTORE_PROJECT")

    # Cloudflare R2
    R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
    R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
    R2_BUCKET = os.getenv("R2_BUCKET")
    R2_ENDPOINT = os.getenv("R2_ENDPOINT")

    # LLM / AI Keys
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
