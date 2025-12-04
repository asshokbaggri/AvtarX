# personality_adapter.py

def apply_personality(user_text, base="neutral"):
    if base == "neutral":
        return user_text
    
    if base == "friendly":
        return f"Talk in a friendly warm tone.\nUser: {user_text}"

    if base == "funny":
        return f"Talk in a humorous tone.\nUser: {user_text}"

    return user_text
