from flask import Flask, request, jsonify
import json
from fuzzywuzzy import process

app = Flask(__name__)

# Load dialog
with open("dialog.json", "r") as f:
    dialog = json.load(f)

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    # Fuzzy match user input to dialog keys
    best_match, score = process.extractOne(user_input, dialog.keys())
    if score >= 60:
        response = dialog[best_match]
    else:
        response = "I'm here for you, even if I don’t fully understand. Can you tell me more?"

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
