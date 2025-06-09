from flask import Flask, request, jsonify
import json
import requests                    
from fuzzywuzzy import process

app = Flask(__name__)

# ── Load dialog from Google Drive ────────────────────────────────────────
file_id = "1-IBhusUoWsD96rcp96cW126GNw27CayN"      
url = f"https://drive.google.com/uc?id={file_id}"

resp = requests.get(url)
resp.raise_for_status()            # stop the app if the download fails
dialog = json.loads(resp.text)
# ─────────────────────────────────────────────────────────────────────────

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    best_match, score = process.extractOne(user_input, dialog.keys())
    if score >= 60:
        response = dialog[best_match]
    else:
        response = ("I'm here for you, even if I don’t fully understand. "
                    "Can you tell me more?")

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)