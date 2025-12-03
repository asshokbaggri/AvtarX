from auth.firebase_init import get_auth
from firebase_admin import auth
import uuid
import time

def signup_user(data):
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return {"error": "Email & Password required"}

    try:
        user = get_auth().create_user(
            email=email,
            password=password
        )

        return {
            "status": "success",
            "message": "Signup successful",
            "uid": user.uid
        }

    except Exception as e:
        return {"error": str(e)}
