"""
Support Vector Machine test on iris data.
"""
from sklearn import metrics
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
print("X shape / y shape: ", X.shape, y.shape)
print("X train / X test shape: ", X_train.shape, X_test.shape)
print("y train / y test shape: ", y_train.shape, y_test.shape)

model = SVC()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)
print("Accuracy score: ", metrics.accuracy_score(y_test, y_predicted))
