# data/merge_labeled.py

import csv
import random

REAL_PATH = "data/real_news.csv"
FAKE_PATH = "data/fake_news.csv"
OUT_PATH  = "data/labeled_news.csv"

rows = []

# Read real-news (assumes a “label” column with value “real”)
with open(REAL_PATH, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append([r["text"], r["source"], r["label"]])

# Read fake-news (assumes “label” column with value “fake”)
with open(FAKE_PATH, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        rows.append([r["text"], r["source"], r["label"]])

# Shuffle to mix real & fake
random.shuffle(rows)

# Write out merged file
with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["text", "source", "label"])
    writer.writerows(rows)

print(f"✅ {OUT_PATH} generated with {len(rows)} samples")
