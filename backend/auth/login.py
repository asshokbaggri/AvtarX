from firebase_admin import auth
from auth.firebase_init import get_auth

def login_user(data):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email & Password required"}

    # Firebase does NOT support password login on backend
    # So user will login through Flutter & send ID token here

    return {"message": "Use /verify to validate ID token"}
