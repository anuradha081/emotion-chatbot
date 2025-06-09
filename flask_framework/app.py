from flask import Flask, render_template, request, jsonify
import json
import requests
import os


app = Flask(__name__)


file_id = "1nVMoBCl1IUgjMoYnbtBGzQwe0Pv6sJxd"      
url = f"https://drive.google.com/uc?id={file_id}"

resp = requests.get(url)
resp.raise_for_status()            # stop the app if the download fails
dialog_data= json.loads(resp.text)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "").strip().lower()
    response = dialog_data.get(user_message, "Sorry, I didn't understand that.")
    return jsonify({"response": response})
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
