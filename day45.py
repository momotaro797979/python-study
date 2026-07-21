import pandas as pd

df = pd.read_csv("sample.csv")
print("=== dropna ===")
print(df.dropna())

print("=== fillna ===")
print(df.fillna(0))