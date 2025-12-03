import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME: str = "AvtarX"
    ENV: str = os.getenv("ENV", "dev")

    FIREBASE_CREDENTIALS = os.getenv("FIREBASE_CREDENTIALS")
    FIRESTORE_PROJECT = os.getenv("FIRESTORE_PROJECT")

    CLOUDFLARE_R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY")
    CLOUDFLARE_R2_SECRET_KEY = os.getenv("R2_SECRET_KEY")
    CLOUDFLARE_R2_BUCKET = os.getenv("R2_BUCKET")
    CLOUDFLARE_R2_ENDPOINT = os.getenv("R2_ENDPOINT")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

settings = Settings()
