# emotion-chatbot
This Chatbot give reply on the basis of your emotion connected in your question.

# Real-Time Emotion Support Chatbot

A simple rule-based chatbot using Flask + Streamlit.

## 💻 Features
- Rule-based dialog engine (JSON)
- Real-time chat with Streamlit UI
- Emotion-based support

## 📦 Installation
```bash
git clone <repo-url>
cd emotion_chatbot
pip install -r requirements.txt
```

## 🚀 Running the App
Start the backend server:
```bash
cd backend
python app.py
```

Start the frontend:
```bash
cd ../frontend
streamlit run streamlit_app.py
```

## 🧠 Customize
Modify `dialog.json` to add your own custom dialog flows.