import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

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

y_true = np.array([1, 0, 1, 0, 0, 1, 0, 1])

w1, w2, w3 = -0.15, 0.5, -0.3
weights = np.array([w1, w2, w3])

theta = 0.3

z = np.dot(X, weights) 
probabilities = sigmoid(z)

print("Valores de salida (probabilidades):")
for i, prob in enumerate(probabilities, 1):
    print(f"Instancia {i}: {prob:.4f}")

y_pred = (probabilities >= theta).astype(int)

print("\nPredicciones binarias:")
print(y_pred)

conf_matrix = confusion_matrix(y_true, y_pred)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print("\nMétricas de desempeño:")
print(f"Exactitud (Accuracy): {accuracy:.4f}")
print(f"Precisión: {precision:.4f}")
print(f"Sensibilidad (Recall): {recall:.4f}")
print(f"F1-Score: {f1:.4f}")

print("\nMatriz de confusión detallada:")
print("          Predicho")
print("Real      1    0")
print(f"  1       {conf_matrix[1,1]}    {conf_matrix[1,0]}")
print(f"  0       {conf_matrix[0,1]}    {conf_matrix[0,0]}")