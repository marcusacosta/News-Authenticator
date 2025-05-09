import pandas as pd
df = pd.read_csv("data/labeled_news_balanced.csv")
print(df['label'].value_counts())