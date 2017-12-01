"""
Linear Regression test on startups data.
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm

df = pd.read_csv('./data/startups.csv')
X = df.iloc[:, :-1].values
y = df.iloc[:, 4].values

labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:, 1:]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
print("X shape / y shape: ", X.shape, y.shape)
print("X train / X test shape: ", X_train.shape, X_test.shape)
print("y train / y test shape: ", y_train.shape, y_test.shape)

model = LinearRegression()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
print("y predicted: ", y_predicted)

X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1)

model_OLS = sm.OLS(endog = y, exog = X[:, [0, 1, 2, 3, 4, 5]]).fit()
print("OLS [0, 1, 2, 3, 4, 5]\n", model_OLS.summary())

model_OLS = sm.OLS(endog = y, exog = X[:, [0, 1, 3, 4, 5]]).fit()
print("OLS [0, 1, 3, 4, 5]\n", model_OLS.summary())

model_OLS = sm.OLS(endog = y, exog = X[:, [0, 3, 4, 5]]).fit()
print("OLS [0, 3, 4, 5]\n", model_OLS.summary())

model_OLS = sm.OLS(endog = y, exog = X[:, [0, 3, 5]]).fit()
print("OLS [0, 3, 5]\n", model_OLS.summary())

model_OLS = sm.OLS(endog = y, exog = X[:, [0, 3]]).fit()
print("OLS [0, 3]\n", model_OLS.summary())