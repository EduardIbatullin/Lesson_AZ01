import pandas as pd


df = pd.read_csv("dz.csv")

print(df.head())
print()
print(df.info())
print()
print(df.describe())
print()

group = df.groupby('City')['Salary'].mean()
print('Средняя зарплата по городам:')
print(group)
