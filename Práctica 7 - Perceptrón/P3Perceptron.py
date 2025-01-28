import numpy as np
from sklearn.linear_model import Perceptron
#from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# Datos de entrada
X = np.array([
    [0, 0, 1],
    [0, 0, 0],
    [1, 1, 1],
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 0],
    [1, 0, 1],
    [1, 0, 0]
])

y = np.array([1, 0, 1, 0, 0, 1, 0, 1])

# Probar primero con un Perceptrón
print("Intentando con Perceptrón simple...")
perceptron = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
perceptron.fit(X, y)
y_pred_perceptron = perceptron.predict(X)
acc_perceptron = accuracy_score(y, y_pred_perceptron)
print(f"Accuracy del Perceptrón: {acc_perceptron:.4f}")