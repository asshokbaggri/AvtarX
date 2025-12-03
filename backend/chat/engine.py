from .tone_detector import detect_tone
from .personality_adapter import adapt_personality
from .llm_client import generate_ai_response

async def process_message(user_id, text):
    # Step 1 — Tone detection
    tone = detect_tone(text)

    # Step 2 — Adapt message (user behavior)
    adapted_prompt = adapt_personality(text, tone)

    # Step 3 — LLM final output
    reply = generate_ai_response(adapted_prompt)

    return {
        "status": "success",
        "reply": reply,
        "tone_detected": tone
    }
