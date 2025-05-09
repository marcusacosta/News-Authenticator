# News Outlet Authenticator (Flask)

A Flask-based service to classify news text as 'real' or 'fake' using a simple ML model.

## Project Structure

```
news-authenticator-flask/
├── app/
│   ├── __init__.py      # App factory
│   ├── routes.py        # Authentication endpoints
│   ├── model.py         # Model loading & inference stub
│   └── utils.py         # Payload validation
├── data/
│   └── README.md        # Instructions for dataset placement
├── tests/
│   └── test_api.py      # API integration tests
├── run.py               # App entrypoint
├── requirements.txt     # Python dependencies
└── README.md            # Project overview and setup
```

## Local Setup

```bash
git clone <repo-url>
cd news-authenticator-flask
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running the Service

```bash
python3 run.py
```

Endpoints:
- **GET /health**: health check
- **POST /authenticate**: `{ "source": "...", "text": "..." }`

## Testing

```bash
pytest
```
