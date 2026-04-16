import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

# Safety checks (VERY IMPORTANT)
if GEMINI_API_KEY is None:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

if GOOGLE_MAPS_API_KEY is None:
    raise ValueError("GOOGLE_MAPS_API_KEY not found in environment variables")