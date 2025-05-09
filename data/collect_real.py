import os, csv, requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWSAPI_KEY")
if not API_KEY:
    raise RuntimeError("Set NEWSAPI_KEY in .env")

SOURCES = ["bbc-news","the-new-york-times","associated-press"]
URL     = "https://newsapi.org/v2/top-headlines"
PARAMS  = {"apiKey": API_KEY, "pageSize": 100, "language": "en"}

with open("data/real_news.csv", "w", newline="", encoding="utf-8") as fp:
    writer = csv.writer(fp)
    writer.writerow(["text","source","label"])
    for src in SOURCES:
        PARAMS["sources"] = src
        r = requests.get(URL, params=PARAMS).json().get("articles", [])
        for art in r:
            txt = art.get("content") or art.get("description") or art.get("title")
            if txt:
                writer.writerow([txt.replace("\n"," "), src, "real"])
print("✅ real_news.csv generated")
