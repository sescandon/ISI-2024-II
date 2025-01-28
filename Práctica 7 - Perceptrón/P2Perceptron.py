import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

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


initial_weights = np.array([-0.15, 0.5, -0.3])
initial_bias = -0.3

perceptron = Perceptron(
    tol=None,
    random_state=42,
    max_iter=1000,
    fit_intercept=True,
    eta0=0.001
)


perceptron.coef_ = initial_weights.reshape(1, -1)
perceptron.intercept_ = np.array([initial_bias])

perceptron.fit(X, y)

y_pred = perceptron.predict(X)
decision_scores = perceptron.decision_function(X)

print("Resultados por instancia:")
for i, (score, pred, true) in enumerate(zip(decision_scores, y_pred, y), 1):
    print(f"Instancia {i}: Score = {score:.4f}, Predicción = {pred}, Valor real = {true}")

print("\nPesos finales del perceptrón:")
for i, coef in enumerate(perceptron.coef_[0], 1):
    print(f"w{i}: {coef:.4f}")
print(f"bias: {perceptron.intercept_[0]:.4f}")

conf_matrix = confusion_matrix(y, y_pred)
accuracy = accuracy_score(y, y_pred)
precision = precision_score(y, y_pred)
recall = recall_score(y, y_pred)
f1 = f1_score(y, y_pred)

print("\nMatriz de confusión:")
print(conf_matrix)

print("\nMétricas de desempeño:")
print(f"Exactitud (Accuracy): {accuracy:.4f}")
print(f"Precisión: {precision:.4f}")
print(f"Sensibilidad (Recall): {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

# Mostrar matriz de confusión en formato más legible
print("\nMatriz de confusión detallada:")
print("          Predicho")
print("Real      1    0")
print(f"  1       {conf_matrix[1,1]}    {conf_matrix[1,0]}")
print(f"  0       {conf_matrix[0,1]}    {conf_matrix[0,0]}")

# Número de iteraciones hasta la convergencia
print(f"\nNúmero de iteraciones hasta la convergencia: {perceptron.n_iter_}")