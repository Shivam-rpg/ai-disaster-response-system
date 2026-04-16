# utils.py

import pandas as pd

# ----------------------------------
# ACTION RECOMMENDATION
# ----------------------------------

def recommend_action(category):

    actions = {
        "water": "Send clean drinking water tankers",
        "food": "Deploy emergency food supply",
        "medical": "Send medical team and medicines",
        "shelter": "Provide tents and temporary housing",
        "none": "No emergency resource needed"
    }

    # ✅ Handle list (multi-category)
    if isinstance(category, list):
        return [actions.get(cat, "No emergency resource needed") for cat in category]

    # ✅ Handle single category
    return actions.get(category, "No emergency resource needed")


# ----------------------------------
# VOLUNTEER DATA
# ----------------------------------

volunteers = pd.DataFrame({
    "name": ["Rahul", "Aisha", "John", "Meera"],
    "skill": ["medical", "food", "water", "shelter"],
    "location": ["Delhi", "Mumbai", "Delhi", "Bangalore"]
})


# ----------------------------------
# VOLUNTEER MATCHING
# ----------------------------------

def match_volunteer(category):

    # ✅ Handle list (multi-category)
    if isinstance(category, list):
        assigned = []

        for cat in category:
            match = volunteers[volunteers["skill"] == cat]

            if len(match) > 0:
                assigned.append(match.iloc[0]["name"])
            else:
                assigned.append("No volunteer available")

        return assigned

    # ✅ Handle single category
    match = volunteers[volunteers["skill"] == category]

    if len(match) > 0:
        return match.iloc[0]["name"]

    return "No volunteer available"