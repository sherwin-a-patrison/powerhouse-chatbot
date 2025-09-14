
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import json
import random
from datetime import datetime
import os

app = Flask(__name__, static_folder="static")  # static folder for index.html
CORS(app)

# Load model & responses
model = joblib.load("chatbot_model.pkl")
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

# Serve frontend (index.html)
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Chat route
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = data["message"]
    intent = model.predict([user_message])[0]

    if intent in responses:
        bot_reply = random.choice(responses[intent])

        # 🔹 Dynamic replacements
        if "[time]" in bot_reply:
            current_time = datetime.now().strftime("%I:%M %p")
            bot_reply = bot_reply.replace("[time]", current_time)

        if "[date]" in bot_reply:
            current_date = datetime.now().strftime("%d-%m-%Y")
            bot_reply = bot_reply.replace("[date]", current_date)

    else:
        bot_reply = "Sorry, I didn't understand 🤔"

    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
