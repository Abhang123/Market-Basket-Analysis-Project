# Importing required libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("\n")
# Displaying the dummy dataset
df = pd.read_csv("1000groceries.csv")
print(df)

print("\n")

# Data Preprocessing

# Converting the Date attribute into Universal Date format
df['Date'] = pd.to_datetime(df['Date'])
print(df)

print("\n")

# Heatmap for correlation
# corr = df.corr()
# sns.heatmap(df.corr(), annot = True)
# plt.show()

print("\n")

# Train test split
x = df['Member_number']
y = df['itemDescription']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,x_test = train_test_split(x,y,test_size = 0.70, random_state = 7)
print(X_train)
print("\n")

print(y_train)
print("\n")

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

figure = plt.figure()
Item_distr = df.groupby(by = 'itemDescription').size().reset_index(name = 'Frequency').sort_values(by = 'Frequency', ascending = False).head(10)
bars = Item_distr['itemDescription']
height = Item_distr['Frequency']
index = np.arange(len(bars))
plt.xlabel("Item names")
plt.ylabel("Frequency")
plt.bar(index, height, color = (0.1,0.3,0.5,0.7))
plt.xticks(index,bars)
plt.gcf().autofmt_xdate()
plt.plot(index, height)
plt.show(figure, width = 700)
print("\n")


























