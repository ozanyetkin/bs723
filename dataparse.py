import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("sample_data.xlsx")
# df = df.drop([4, 6])
# print(df)
count_a = df['firm'].value_counts()['A']
count_b = df['firm'].value_counts()['B']
count_c = df['firm'].value_counts()['C']

fig, ax = plt.subplots()
ax.pie([count_a, count_b, count_c], labels=['A', 'B', 'C'])

plt.show()

fig, ax = plt.subplots()

colors = df['firm'].replace(to_replace=['A', 'B', 'C'], value=['red', 'green', 'blue'])
sizes = df['bonus'].replace(to_replace=[0, 1], value=[50, 100])
ax.scatter(df['age'], df['salary'], c=colors, s=sizes)

plt.show()
