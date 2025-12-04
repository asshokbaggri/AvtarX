# tone_detector.py

def detect_tone(text):
    text = text.lower()

    if any(x in text for x in ["sad", "upset", "tired", "down"]):
        return "sad"
    if any(x in text for x in ["angry", "mad", "frustrated"]):
        return "angry"
    if any(x in text for x in ["happy", "great", "awesome"]):
        return "happy"
    
    return "neutral"
