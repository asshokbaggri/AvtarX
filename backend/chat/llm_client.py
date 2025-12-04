from openai import OpenAI
import os

def chat_completion(messages):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-5.1",
        messages=messages,
        max_tokens=800,
        temperature=0.7
    )
    return response.choices[0].message["content"]
