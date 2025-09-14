# PowerHouse Chatbot 🤖

A smart AI chatbot built with **Flask**, **scikit-learn**, and a custom **intent model**.  
It runs on **Render** and provides a responsive web UI for interactive chat.

---

## 🚀 Live Demo
click here : https://powerhouse-chatbot.onrender.com/  

Type a message and get an instant AI-powered reply.

---

## 📁 Project Structure

E:\powerhouse-chatbot
│

├── app.py # Flask backend

├── chatbot_model.pkl # Trained ML model

├── responses.json # Bot responses

├── intents.csv # Training data

├── intents.txt # Optional intent info

├── requirements.txt # Python dependencies

├── Procfile # Start command for Render

├── static/

│ └── index.html # Frontend chat UI

├── train_powerhousechatbot.py # Script to train model

└── test_powerhousechatbot.py # Optional testing script



---

## 🧑‍💻 Local Development

### 1. Clone the repo
```bash
git clone https://github.com/sherwin-a-patrison/powerhouse-chatbot.git
cd powerhouse-chatbot
2. Create virtual environment & install dependencies
bash
Copy code
python -m venv venv
.\venv\Scripts\activate   # Windows
pip install -r requirements.txt
3. Run locally
bash
Copy code
python app.py
Open http://127.0.0.1:5000 in your browser.

🌐 Deployment
Hosted on Render.

Steps:

Push code to GitHub.

Connect repo to Render.

Render auto builds and deploys the chatbot.

🛠️ Technologies Used
Python

Flask & Flask-CORS

scikit-learn

joblib

HTML / CSS / JavaScript (frontend)

✨ Features
Particle background with light/dark theme

Intent classification using machine learning

Responsive design (mobile-friendly)

REST API endpoint: /chat

📄 License
MIT License © 2025 sherwin-a-patrison

✅ How to Add This README
Create E:\powerhouse-chatbot\README.md

Paste the above content and save

Push to GitHub:

powershell
Copy code
cd /d E:\powerhouse-chatbot
git add README.md
git commit -m "Add README"
git push
