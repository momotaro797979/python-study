import pandas as pd

pokemon = {
    "名前": ["ピカチュウ", "リザードン", "ルカリオ"],
    "タイプ": ["でんき", "ほのお", "かくとう"],
    "レベル": [25, 36, 50]
}

df = pd.DataFrame(pokemon)

print(df["レベル"])