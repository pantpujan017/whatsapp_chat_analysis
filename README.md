# 📊 WhatsApp Chat Analyzer

A powerful Streamlit-based web app to analyze WhatsApp group or personal chats with insightful visualizations.

🚀 **[Click here to try the app!](https://whatsappchatanalysis-d2fffjhxkrjudskyyqfh7x.streamlit.app/)**
---

## 🎯 Features

- 📅 Monthly & Daily activity timeline
- 👥 Most active users and message counts
- 💬 Word frequency & common keywords
- 🤩 Emoji usage analysis
- 📎 Media and link sharing stats
- 🔥 Weekly activity heatmap
- 🎨 Clean, interactive dashboard built with Streamlit

---

## 📂 How to Use

1. Export your WhatsApp chat from the app (in `.txt` format).
2. Open the [deployed web app](https://whatsappchatanalysis-d2fffjhxkrjudskyyqfh7x.streamlit.app/).
3. Upload the exported file.
4. Choose a user (or "Overall") to view analytics.

✔️ No need to install anything locally!

---

## 🧠 Tech Stack

- Python 🐍
- Streamlit 🎈
- Pandas & Regex 📊
- Matplotlib 📈
- Emoji 😊

---

---

## 🛠️ Developer Setup (Optional)

If you'd like to run it locally:

```bash
git clone https://github.com/pantpujan017/whatsapp-chat-analyzer.git
cd whatsapp-chat-analyzer

# Create virtual environment (optional)
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
