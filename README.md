📰 News Authenticator Flask App
A Flask-powered web application leveraging Machine Learning to authenticate news articles or statements as Real or Fake. The app uses logistic regression combined with TF-IDF vectorization and incorporates source-based reputation heuristics to adjust predictions. A simple, user-friendly frontend allows quick authentication directly from the browser.

🌟 Features
ML-powered prediction: Authenticates news using logistic regression & TF-IDF.

Source Reputation Heuristics: Boosts or penalizes predictions based on trusted or questionable news outlets.

Caching & Performance Logging: LRU caching optimizes repeated requests; inference times are logged for performance insights.

RESTful API: JSON-based interface easy for integration.

Responsive Frontend: Simple, intuitive HTML/CSS frontend for manual checks.

🔧 Tech Stack
Backend
Python

Flask (REST API)

Scikit-learn (ML Model)

Joblib (Model Persistence)

Gunicorn (WSGI Server)

Frontend
HTML/CSS

JavaScript (Fetch API)

Additional Tools
pytest (Testing)

functools (Caching)

🗃 Project Structure
bash
Copy
Edit
news-authenticator-flask/
├── app/
│   ├── __init__.py
│   ├── routes.py         # Flask routes
│   ├── model.py          # ML model logic
│   ├── utils.py          # Source heuristics and validation
│   └── artifacts/        # ML artifacts (model, vectorizer)
│
├── data/                 # Dataset & preparation scripts
│   ├── labeled_news.csv
│   ├── train_model.py
│   ├── merge_labeled.py
│   └── balance_dataset.py
│
├── public/               # Frontend files
│   ├── index.html
│   └── style.css
│
├── tests/                # pytest API tests
│   └── test_api.py
│
├── requirements.txt
├── run.py                # Flask app entry point
└── README.md             # This document
🚀 Quick Start (Local Development)
1. Clone the Repo
bash
Copy
Edit
git clone https://github.com/<your-username>/news-authenticator-flask.git
cd news-authenticator-flask
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Launch the Flask API & Frontend
bash
Copy
Edit
python3 run.py
Frontend: http://127.0.0.1:5000/

API Health Check: http://127.0.0.1:5000/health

🖥 Using the Web Interface
Open http://127.0.0.1:5000/ in your browser. Enter the news source (e.g., bbc-news) and the text you want to authenticate. Click Authenticate and receive