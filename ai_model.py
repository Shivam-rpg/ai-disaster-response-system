from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

def analyze_message(message):

    message_lower = message.lower()
    categories = []

    # ----------------------------------
    # 🔥 MULTI-LABEL RULE-BASED DETECTION
    # ----------------------------------

    # WATER
    if any(word in message_lower for word in [
        "water", "thirst", "drinkable", "clean water"
    ]):
        categories.append("water")

    # FOOD
    if any(word in message_lower for word in [
        "food", "hungry", "starving"
    ]):
        categories.append("food")

    # MEDICAL
    if any(word in message_lower for word in [
        "injured", "wounded", "doctor", "dead",
        "disease", "outbreak", "medical", "hospital",
        "immunization", "vaccine", "health", "supplies",
        "medicine", "medicines",

        # 🔥 important real-world terms
        "pregnant", "pregnancy", "baby", "childbirth",
        "delivery", "mother", "maternal"
    ]):
        categories.append("medical")

    # SHELTER
    if any(word in message_lower for word in [
        "shelter", "homeless", "tents", "shacks",
        "destroyed", "village", "house collapsed"
    ]):
        categories.append("shelter")

    # ----------------------------------
    # 🤖 GEMINI (ONLY IF NOTHING FOUND)
    # ----------------------------------

    if not categories:
        prompt = f"""
        You are an emergency disaster classifier.

        Identify ALL applicable categories from:
        medical, food, water, shelter

        IMPORTANT:
        - Return comma-separated values
        - No explanation
        - Example: food,water

        Message: {message}

        Answer:
        """

        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=prompt
            )

            result = response.text.strip().lower()

            valid_labels = ["medical", "food", "water", "shelter"]

            for label in valid_labels:
                if label in result:
                    categories.append(label)

        except Exception as e:
            print("Gemini Error:", e)

    # ----------------------------------
    # 🛑 FINAL SAFETY
    # ----------------------------------

    if not categories:
        return ["none"]

    return list(set(categories))