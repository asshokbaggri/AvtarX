import firebase_admin
from firebase_admin import credentials, auth
from config.settings import settings

# Load Firebase service account key
if not firebase_admin._apps:
    cred = credentials.Certificate(settings.FIREBASE_CRED)
    firebase_admin.initialize_app(cred)

def get_auth():
    return auth
