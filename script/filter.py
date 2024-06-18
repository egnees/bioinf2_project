import pandas as pd

df = pd.read_csv("/Users/macbook/Sergey/zhunt/sequence.fna.Z-SCORE", sep="\s+", skiprows=1,
                 names=['start', 'end', 'c1', 'c2', 'c3', 'score', 'sequence', 'conformation'])

df = df.loc[df[df.columns[5]] > 400]

print(f'len of z-score after filter (threshold=400) is {len(df)}')

df = df.sort_values(by=df.columns[5], ascending=False)

df.to_csv("/Users/macbook/Sergey/zhunt/z-score-filtered.csv")
