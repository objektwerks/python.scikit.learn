"""
Linear Regression test on roles.salaries data.
"""
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values

model = LinearRegression()
model.fit(X, y)

features = PolynomialFeatures(degree = 4)
X_poly = features.fit_transform(X)
features.fit(X_poly, y)

ploy_model = LinearRegression()
ploy_model.fit(X_poly, y)

# Linear Regression plot.
plt.scatter(X, y, color = 'red')
plt.plot(X, model.predict(X), color = 'blue')
plt.title('Linear Regression')
plt.xlabel('Role-Level')
plt.ylabel('Salary')
plt.show()

# Linear Polynomial Regression plot.
plt.scatter(X, y, color = 'red')
plt.plot(X, ploy_model.predict(features.fit_transform(X)), color = 'blue')
plt.title('Linear Polynomial Regression')
plt.xlabel('Role-Level')
plt.ylabel('Salary')
plt.show()

# Linear Polynomial Regression smooth plot.
X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, ploy_model.predict(features.fit_transform(X_grid)), color = 'blue')
plt.title('Smooth Linear Polynomial Regression')
plt.xlabel('Role-Level')
plt.ylabel('Salary')
plt.show()

# Linear Regression
model.predict(6.5)

# Linear Polynomial Regression
ploy_model.predict(features.fit_transform(6.5))