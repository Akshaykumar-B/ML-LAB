import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("sales_data.csv")

print(data.head())
print(data.describe())
print(data.dtypes)

plt.scatter(data["Advertising"], data["Sales"])
plt.xlabel("Advertising")
plt.ylabel("Sales")
plt.show()

print(data.isnull().sum())

for col in data.columns:
    data[col].fillna(data[col].mode()[0], inplace=True)

X = data[["Advertising"]]
y = data["Sales"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)
