import pandas as pd

df = pd.read_csv("/Users/macbook/Sergey/zhunt/z-score-filtered.csv").iloc[:15000]

df.to_csv("/Users/macbook/Sergey/zhunt/z-score-head.csv")