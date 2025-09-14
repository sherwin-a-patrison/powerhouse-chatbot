# Cypher Chatbot 🤖

A simple AI chatbot built with **Flask**, **scikit-learn**, and a custom intent model.  
It runs on [Render](https://render.com) and serves a responsive web UI.

---

## 🚀 Demo

👉 [cypher chatbot](https://cypher-chatbot.onrender.com)

Type a message and get an instant reply.

---

## 📁 Project Structure

E:\CHATBOT
│

├── app.py # Flask backend

├── chatbot_model.pkl # Trained model

├── responses.json # Bot responses

├── intents.csv # Training data 

├── requirements.txt # Python dependencies

├── Procfile # Start command for Render

├── static/

│ └── index.html # Frontend (chat UI)

└── train_chatbot.py #  script to train model

yaml
Copy code

---

## 🧑‍💻 Local Development

1. **Clone the repo**

```bash
git clone https://github.com/HarishKanna333/cypher-chatbot.git
cd cypher-chatbot
Create virtual environment & install deps

bash
Copy code
python -m venv venv
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
Run locally

bash
Copy code
python app.py
Open http://127.0.0.1:5000 in browser.

🌐 Deployment
Hosted on Render.

Push code to GitHub → Render auto builds and deploys.

🛠️ Technologies Used
Flask

Flask-CORS

scikit-learn

joblib

HTML / CSS / JavaScript (frontend)

✨ Features
Particle background with light/dark theme

Intent classification using ML

Responsive design (mobile-friendly)

REST API endpoint: /chat

📄 License
MIT License © 2025 Harish Kanna

yaml
Copy code

---

### How to add

1. Create a new file `E:\CHATBOT\README.md`.
2. Paste the above content.
3. Save.
4. Push to GitHub:

```powershell
cd /d E:\CHATBOT
git add README.md
git commit -m "add README"
git push
