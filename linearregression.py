import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel("sample_data.xlsx")
df = df.drop([4, 6])
# print(df)

x = np.array(df['age']).reshape(-1, 1)
y = np.array(df['salary'])

fig, ax = plt.subplots()

colors = df['firm'].replace(to_replace=['A', 'B', 'C'], value=['red', 'green', 'blue'])
sizes = df['bonus'].replace(to_replace=[0, 1], value=[50, 100])
ax.scatter(x, y, c=colors, s=sizes)

reg = LinearRegression().fit(x, y)
print(reg.predict(np.array([[60]])))

plt.plot(x, reg.coef_ * x + reg.intercept_)

plt.show()
