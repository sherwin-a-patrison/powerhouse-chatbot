# train_chatbot.py

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# 1. Load dataset
df = pd.read_csv("intents.csv")

# 2. Features (utterance) and Labels (intent)
X = df["utterance"]
y = df["intent"]

# 3. Build pipeline (Vectorizer + Classifier)
model = Pipeline([
    ("tfidf", TfidfVectorizer()), 
    ("clf", MultinomialNB())
])

# 4. Train model
model.fit(X, y)

# 5. Save model
joblib.dump(model, "chatbot_model.pkl")

print("✅ Chatbot model trained and saved as chatbot_model.pkl")
