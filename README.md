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