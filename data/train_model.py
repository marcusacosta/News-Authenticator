import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Paths
DATA_PATH    = "data/labeled_news_balanced.csv"
ARTIFACT_DIR = "app/artifacts"
MODEL_PATH   = os.path.join(ARTIFACT_DIR, "model.pkl")
VECT_PATH    = os.path.join(ARTIFACT_DIR, "vectorizer.pkl")

# 1. Load data
df = pd.read_csv(DATA_PATH)
texts   = df["text"].astype(str)
labels  = df["label"]

# 2. Split for quick eval
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.2, stratify=labels, random_state=42
)

# 3. Build pipeline
pipeline = make_pipeline(
    TfidfVectorizer(max_features=5000, ngram_range=(1,2)),
    LogisticRegression(solver="liblinear", class_weight="balanced")
)

# 4. Train
print("Training classifier…")
pipeline.fit(X_train, y_train)

# 5. Evaluate
print("Evaluating on hold-out set:")
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# 6. Save artifacts
os.makedirs(ARTIFACT_DIR, exist_ok=True)
# pipeline.named_steps['vectorizer'] if you need it separately:
joblib.dump(pipeline.named_steps['tfidfvectorizer'], VECT_PATH)
joblib.dump(pipeline.named_steps['logisticregression'], MODEL_PATH)
print(f"✅ Saved vectorizer to {VECT_PATH}")
print(f"✅ Saved model to      {MODEL_PATH}")
