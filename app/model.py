# app/model.py

import os
import joblib
from functools import lru_cache

_art_path  = os.path.join(os.path.dirname(__file__), "artifacts")
MODEL_PATH = os.path.join(_art_path, "model.pkl")
VECT_PATH  = os.path.join(_art_path, "vectorizer.pkl")

_model      = None
_vectorizer = None

def load_model():
    global _model, _vectorizer
    _vectorizer = joblib.load(VECT_PATH)
    _model      = joblib.load(MODEL_PATH)
    print(f"Loaded model & vectorizer from {VECT_PATH} & {MODEL_PATH}")

def predict(text: str, source: str = None):
    """
    Runs inference on a single text.
    Returns a dict with raw & source-adjusted scores.
    """
    X = _vectorizer.transform([text])
    proba = _model.predict_proba(X)[0]
    idx_real = list(_model.classes_).index("real")
    raw_conf = float(proba[idx_real])
    raw_pred = "real" if raw_conf >= 0.5 else "fake"

    # Source reputation
    from .utils import get_source_score
    src_score   = get_source_score(source)
    final_conf  = min(raw_conf * src_score, 1.0)
    final_pred  = "real" if final_conf >= 0.5 else "fake"

    return {
        "raw_prediction":   raw_pred,
        "raw_confidence":   raw_conf,
        "source_score":     src_score,
        "final_prediction": final_pred,
        "final_confidence": final_conf
    }

# --- Add caching so identical (text, source) pairs hit the cache ---
# wrap the original predict in an lru_cache
predict = lru_cache(maxsize=128)(predict)
