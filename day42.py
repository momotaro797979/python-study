import pandas as pd

df = pd.read_csv("sample.csv")

print(df.groupby("タイプ")["レベル"].mean())