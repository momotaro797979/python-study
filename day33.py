import pandas as pd

pokemon = {
    "名前": ["ピカチュウ", "リザードン", "ルカリオ"],
    "タイプ": ["でんき", "ほのお", "かくとう"]
}

df = pd.DataFrame(pokemon)

print(df)