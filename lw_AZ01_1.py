
import pandas as pd


# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
#
# print(series)

# data = {
#     'Name': ['Alice', 'Bob', 'Roman', 'Anna'],
#     'Age': [23, 45, 17, 24],
#     'City': ['New York', 'LA', 'Chicago', 'Moscow']
# }
#
# df = pd.DataFrame(data)
#
# print(df)

df = pd.read_csv('World-happiness-report-2024.csv')
print(df[df['Healthy life expectancy'] > 0.7])

