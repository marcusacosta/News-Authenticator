# app/routes.py

from flask import Blueprint, request, jsonify, current_app
from .utils import validate_payload
from .model import predict
import time

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/health', methods=['GET'])
def health():
    """Health‐check endpoint."""
    return 'Flask API working!'

@auth_bp.route('/authenticate', methods=['POST'])
def authenticate():
    """
    POST /authenticate
    Request JSON:
      {
        "source": "<news source identifier>",
        "text": "<article or claim text>"
      }
    Response JSON:
      {
        "source": "<same as input>",
        "raw_prediction": "...",
        "raw_confidence": 0.0–1.0,
        "source_score":  ...,
        "final_prediction": "...",
        "final_confidence": 0.0–1.0
      }
    """
    data = request.get_json()
    try:
        validate_payload(data)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

    source = data['source']
    text   = data['text']

    # Measure inference time
    start = time.perf_counter()
    results = predict(text, source)
    elapsed = time.perf_counter() - start

    # Log timing and cache info
    try:
        ci = predict.cache_info()
        cache_info = f"hits={ci.hits}, misses={ci.misses}, maxsize={ci.maxsize}, currsize={ci.currsize}"
    except AttributeError:
        cache_info = "n/a"

    current_app.logger.info(
        "Authenticate: %.2f ms | cache: %s",
        elapsed * 1000,
        cache_info
    )

    return jsonify({
        'source':           source,
        'raw_prediction':   results['raw_prediction'],
        'raw_confidence':   results['raw_confidence'],
        'source_score':     results['source_score'],
        'final_prediction': results['final_prediction'],
        'final_confidence': results['final_confidence']
    })
