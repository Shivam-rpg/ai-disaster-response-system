# 🚨 AI Disaster Response System

An AI-powered disaster response system built during a **Google Developer Hackathon** to intelligently analyze emergency messages and assist in rapid decision-making.

---

## 🌍 Project Overview

During disasters, thousands of messages are generated requesting help. This system uses **AI + NLP** to:

* Classify disaster-related messages
* Identify multiple urgent needs (water, food, medical, shelter)
* Recommend appropriate actions
* Assign suitable volunteers
* Visualize insights via an interactive dashboard
----

## 🧠 Key Features

* 🤖 **AI-based Message Classification** using Gemini API
* 🔥 **Multi-Label Detection** (handles multiple needs in one message)
* 👥 **Volunteer Matching System**
* 📊 **Interactive Dashboard (Streamlit)**
* 📈 **Real-time Insights & Resource Demand Visualization**
* 📍 **Map-based Affected Area Display**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Pandas**
* **Google Gemini API**
* **NLP (Rule-based + AI hybrid approach)**

---

## 📂 Project Structure

```id="k9z3yb"
├── app.py
├── ai_model.py
├── data_processing.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── images/
│   └── dashboard.png
```

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash id="2r2q1u"
git clone https://github.com/your-username/ai-disaster-response-system.git
cd ai-disaster-response-system
```

---

### 2️⃣ Install dependencies

```bash id="tklh1v"
pip install -r requirements.txt
```

---

### 3️⃣ Set environment variables

Create a `.env` file in the root directory:

```id="8n9d8w"
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_MAPS_API_KEY=your_google_maps_api_key
```

---

### 4️⃣ Run the application

```bash id="c7fxut"
streamlit run app.py
```

---

## 🧪 Example

**Input Message:**

```id="a7hlxz"
We need water, food and medical help urgently
```

**Output:**

* Categories → `water`, `food`, `medical`
* Actions → Water supply, Food distribution, Medical assistance
* Volunteers → Assigned accordingly

---

## 📊 Insights Generated

* Resource demand distribution
* Most urgent needs
* Disaster report summaries

---

## 🎯 Impact

This system can help:

* Disaster management authorities
* NGOs and relief organizations
* Emergency response teams

to **prioritize and respond effectively** during crises.

---

## 🔐 Environment Variables

| Variable            | Description           |
| ------------------- | --------------------- |
| GEMINI_API_KEY      | Google Gemini API key |
| GOOGLE_MAPS_API_KEY | Google Maps API key   |

---

## 🌐 Deployment

The app can be deployed using:

* Streamlit Cloud
* Render
* Hugging Face Spaces

---

## 🚀 Future Improvements

* 📍 Automatic location extraction from messages
* 🚨 Priority & severity detection
* 🤖 Advanced ML/NLP models
* 🌐 Real-time data integration

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repository and submit pull requests.

---

## ⭐ Support

If you find this project useful, please give it a ⭐ on GitHub!

