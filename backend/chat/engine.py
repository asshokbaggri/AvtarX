# engine.py

from .llm_client import chat_completion
from .personality_adapter import apply_personality
from .tone_detector import detect_tone

async def process_chat(message, history):
    # Detect user mood
    tone = detect_tone(message)

    # Apply optional personality
    final_text = apply_personality(message, base="neutral")

    # Build messages list for GPT-5.1
    messages = []

    # Convert history to OpenAI format
    for h in history:
        messages.append({"role": "user", "content": h["user"]})
        messages.append({"role": "assistant", "content": h["bot"]})

    # Add new user message
    messages.append({"role": "user", "content": final_text})

    # Call GPT-5.1
    bot_reply = await chat_completion(messages)

    return {
        "reply": bot_reply,
        "tone": tone
    }
