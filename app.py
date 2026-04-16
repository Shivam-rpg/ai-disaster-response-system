# app.py

import streamlit as st
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables FIRST
load_dotenv()

from data_processing import load_and_clean_data
from ai_model import analyze_message
from utils import recommend_action, match_volunteer
from config import GOOGLE_MAPS_API_KEY

# ----------------------------------
# PAGE CONFIG (Important for UI)
# ----------------------------------

st.set_page_config(
    page_title="AI Disaster Response System",
    page_icon="🚨",
    layout="wide"
)

# ----------------------------------
# TITLE
# ----------------------------------

st.title("🚨 AI Disaster Response System (Google Hackathon Ready)")

# ----------------------------------
# CHECK API KEYS
# ----------------------------------

if not os.getenv("GEMINI_API_KEY"):
    st.warning("⚠️ GEMINI API key not found. AI features may not work.")

if not GOOGLE_MAPS_API_KEY:
    st.warning("⚠️ Google Maps API key not found. Map features limited.")

# ----------------------------------
# USER INPUT
# ----------------------------------

st.subheader("🧪 Test Your Own Message")

user_input = st.text_input("Enter a disaster message")

if user_input:
    with st.spinner("Analyzing message..."):
        try:
            category = analyze_message(user_input)
            action = recommend_action(category)
            volunteer = match_volunteer(category)

            st.success(f"Category: {category}")
            st.write("Recommended Action:", action)
            st.write("Assigned Volunteer:", volunteer)

        except Exception as e:
            st.error(f"Error analyzing message: {e}")

# ----------------------------------
# LOAD DATA (SAFE)
# ----------------------------------

@st.cache_data
def load_data():
    return load_and_clean_data()

try:
    df = load_data()
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# ----------------------------------
# SAMPLE DATA (SAFE)
# ----------------------------------

sample_size = min(5, len(df))  # avoid crash if small dataset
df_sample = df.sample(sample_size).copy()

# ----------------------------------
# AI CLASSIFICATION
# ----------------------------------

st.subheader("🤖 AI Classification in Progress")

df_sample["ai_category"] = ""

for i in range(len(df_sample)):
    try:
        df_sample.loc[df_sample.index[i], "ai_category"] = analyze_message(
            str(df_sample.iloc[i]["message"])
        )
    except Exception:
        df_sample.loc[df_sample.index[i], "ai_category"] = "unknown"

# ----------------------------------
# ACTIONS + VOLUNTEERS
# ----------------------------------

df_sample["recommended_action"] = df_sample["ai_category"].apply(recommend_action)
df_sample["assigned_volunteer"] = df_sample["ai_category"].apply(
    lambda cats: [match_volunteer(cat) for cat in cats] if isinstance(cats, list) else match_volunteer(cats)
)

# ----------------------------------
# DISPLAY DATA
# ----------------------------------

st.subheader("📊 Disaster Reports")
st.dataframe(df_sample, use_container_width=True)

# ----------------------------------
# INSIGHTS
# ----------------------------------

st.subheader("📈 Resource Demand")

need_counts = df_sample["ai_category"].value_counts()

st.bar_chart(need_counts)

# ----------------------------------
# MAP (INDIA LOCATIONS)
# ----------------------------------

st.subheader("📍 Affected Areas (India)")

map_data = pd.DataFrame({
    "lat": [28.61, 19.07, 12.97, 28.57, 28.45, 18.52, 17.38, 13.08, 22.57, 26.85],
    "lon": [77.20, 72.87, 77.59, 77.32, 77.03, 73.85, 78.48, 80.27, 88.36, 80.95],
})

st.map(map_data)

# ----------------------------------
# SUMMARY
# ----------------------------------

st.subheader("📌 Summary")

st.write("Total Messages:", len(df_sample))

if not need_counts.empty:
    st.write("Most Urgent Need:", need_counts.idxmax())
else:
    st.write("Most Urgent Need: N/A")

st.write("Volunteers Available:", 4)

