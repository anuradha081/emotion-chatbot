import streamlit as st
import requests

st.set_page_config(page_title="Emotion Support Bot")
st.title("🧠 Emotional Support Chatbot")
st.markdown("""Ask me anything. I'm here to help! 💬""")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    # Show user message
    st.session_state.messages.append(("user", user_input))

    # Send to backend
    try:
        response = requests.post("http://localhost:8501", json={"message": user_input})
        reply = response.json()["response"]
    except:
        reply = "Backend not reachable. Please start Flask backend."

    st.session_state.messages.append(("bot", reply))

# Display chat
for role, message in st.session_state.messages:
    if role == "user":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
