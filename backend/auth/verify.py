from firebase_admin import auth
from auth.firebase_init import get_auth

def verify_token(data):
    token = data.get("id_token")

    if not token:
        return {"error": "ID token required"}

    try:
        decoded = get_auth().verify_id_token(token)
        return {
            "status": "verified",
            "uid": decoded["uid"],
            "email": decoded.get("email")
        }
    except Exception as e:
        return {"error": str(e)}
