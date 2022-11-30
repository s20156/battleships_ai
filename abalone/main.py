import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# DATA IN STRING VERSION
data = np.genfromtxt("abalone.data", delimiter=",", dtype="str")

x_init = data[:,:8]
y_init = data[:,8]

d = pd.get_dummies(y_init)
y = d.values.argmax(1)

x1_init = x_init[:,0]
x1 = pd.get_dummies(x1_init).values

x2_8 = x_init[:,1:8]
x = np.append(x1, x2_8, axis=1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.5)

poly_svc = SVC(kernel="poly").fit(x_train, y_train)
linear_svc = SVC(kernel="linear").fit(x_train, y_train)
svc = SVC(kernel="rbf").fit(x_train, y_train)

y_true, y_pred = y_test, svc.predict(x_test)
poly_y_true, poly_y_pred = y_test, poly_svc.predict(x_test)
lin_y_true, lin_y_pred = y_test, linear_svc.predict(x_test)

print("RBF kernel: ", accuracy_score(y_true, y_pred))
print("Polygon kernel: ", accuracy_score(poly_y_true, poly_y_pred))
print("Linear kernel: ", accuracy_score(lin_y_true, lin_y_pred))