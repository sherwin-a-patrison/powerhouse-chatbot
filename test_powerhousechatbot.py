import joblib
import json
import random

# Load trained model
model = joblib.load("chatbot_model.pkl")

# Load responses.json
with open("responses.json", "r", encoding="utf-8") as f:
    responses = json.load(f)

while True:
    text = input("You: ")
    if text.lower() in ["exit", "quit", "bye"]:
        print("Bot: Bye! 👋")
        break

    # Predict intent
    pred_intent = model.predict([text])[0]

    # Find reply from responses.json
    if pred_intent in responses:
        reply = random.choice(responses[pred_intent])
        print(f"Bot: {reply}")
    else:
        print("Bot: Sorry, I didn't understand 🤔")
