"""
Logistic Regression test on iris data.
"""
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
print("X shape / y shape: ", X.shape, y.shape)
print("X train / X test shape: ", X_train.shape, X_test.shape)
print("y train / y test shape: ", y_train.shape, y_test.shape)

model = LogisticRegression()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
print("Accuracy score: ", metrics.accuracy_score(y_test, y_predicted))
print("Cross-validation mean accuracy score: ",
      cross_val_score(model, X, y, cv=10, scoring='accuracy').mean())
