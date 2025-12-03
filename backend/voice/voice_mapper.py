def map_voice(avatar_type: str):
    """
    Avatar type → voice preset mapping
    Later we will add more emotional voices.
    """

    mapping = {
        "male_model": "male_voice_1",
        "female_model": "female_voice_1",
        "anime": "anime_voice",
        "corporate": "corporate_voice",
        "energetic": "energetic_voice",
        "neutral": "neutral_voice"
    }

    return mapping.get(avatar_type, "neutral_voice")
