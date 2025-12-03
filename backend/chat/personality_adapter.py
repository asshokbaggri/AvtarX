def adapt_personality(user_text: str, tone: str):
    if tone == "emotional":
        prefix = "Respond in a soft, caring, supportive way: "
    elif tone == "friendly":
        prefix = "Respond like a cool, friendly buddy: "
    elif tone == "urgent":
        prefix = "Respond quickly & directly: "
    else:
        prefix = "Respond normally: "

    return prefix + user_text
