import csv
import os
import sys

# Paths
raw = "data/fake_source.csv"
out = "data/fake_news.csv"

# Sanity check
if not os.path.isfile(raw):
    print(f"❌ Raw file not found at {raw}")
    sys.exit(1)

# LIAR dataset columns (train.tsv has no header)
fieldnames = [
    "id",
    "label",
    "statement",
    "subject",
    "speaker",
    "speaker_job",
    "state",
    "party_affiliation",
    "barely_true_counts",
    "false_counts",
    "half_true_counts",
    "mostly_true_counts",
    "pants_on_fire_counts",
    "venue"
]

with open(raw, encoding="utf-8") as inf, \
     open(out, "w", newline="", encoding="utf-8") as outf:

    reader = csv.DictReader(inf, delimiter="\t", fieldnames=fieldnames)
    writer = csv.writer(outf)

    # Write header
    writer.writerow(["text", "source", "label"])

    count_in = 0
    count_out = 0

    for row in reader:
        count_in += 1
        # Extract the claim text
        txt = row["statement"]
        # Skip empty or placeholder header-like lines
        if not txt or txt.lower() == "statement":
            continue
        # Tag with a dataset source
        src = "liar-dataset"
        writer.writerow([txt.replace("\n", " "), src, "fake"])
        count_out += 1

    print(f"🔍 Read {count_in} raw rows")
    print(f"✅ Wrote {count_out} fake-news rows to {out}")

if count_out == 0:
    print("⚠️  No rows written—please check that your raw file matches the LIAR format.")
