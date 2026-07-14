import pandas as pd

df = pd.read_csv("sample.csv")
pokemon = pd.DataFrame({
    "タイプ": ["でんき", "ほのお", "かくとう"],
    "地方": ["カントー", "カントー", "シンオウ"]
})

print(df.merge(pokemon, on="タイプ"))