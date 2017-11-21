"""
Decision Tree Classifier test on iris data.
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics

X, y = load_iris(return_X_y=True)
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=3)
print(X_train.shape)
print(X_test.shape)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_predicted = model.predict(X_test)

print(metrics.accuracy_score(y_test, y_predicted))
