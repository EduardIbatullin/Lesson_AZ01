import pandas as pd


df = pd.read_csv("Top_100_Movies.csv")

print(df.head())
print()
print(df.info())
print()
print(df.describe())

