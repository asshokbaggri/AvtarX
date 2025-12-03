def detect_tone(text: str):
    text = text.lower()

    if any(x in text for x in ["sad", "tired", "upset", "help"]):
        return "emotional"

    if any(x in text for x in ["hey", "bro", "bhai", "yo"]):
        return "friendly"

    if any(x in text for x in ["urgent", "now", "fast", "quick"]):
        return "urgent"

    return "neutral"
