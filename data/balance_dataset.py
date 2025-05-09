import pandas as pd

# 1. Load the merged labeled file
df = pd.read_csv("data/labeled_news.csv")

# 2. Separate by class
real_df = df[df.label == "real"]
fake_df = df[df.label == "fake"]

# 3. Down-sample the fake class to the real count
n_real   = len(real_df)
fake_sub = fake_df.sample(n_real, random_state=42)

# 4. Combine and shuffle
balanced = pd.concat([real_df, fake_sub]).sample(frac=1, random_state=42)

# 5. Write out
balanced.to_csv("data/labeled_news_balanced.csv", index=False)
print(f"✅ Balanced dataset saved with {len(balanced)} samples (real={n_real}, fake={n_real})")
