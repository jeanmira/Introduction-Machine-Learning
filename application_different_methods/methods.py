# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-04-18 18:58:50
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-04-23 19:46:06


from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings("ignore", category=Warning)

# Load Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

# Define number of nearest neighbors to test in KNN
k_values = [3, 6]

# Network configurations to test in MLP (two hidden layers)
mlp_configurations = [(1, 2), (20, 30), (300, 400), (15, 5)]

# Define kernels to test in SVM
svm_kernels = ['linear', 'rbf']

# Define number of folds for cross validation
n_folds = 10
kf = KFold(n_splits=n_folds)


# Function to calculate average accuracy using cross validation
def evaluate_model(model, X, y, kf):
    scores = cross_val_score(model, X, y, cv=kf)
    return scores.mean()


# Function to evaluate the model using the accuracy metric
def evaluate_model_accuracy(model, X, y, kf):
    accuracies = []
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        accuracies.append(accuracy)
    return sum(accuracies) / len(accuracies)


# KNN
print("KNN:")
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    accuracy_cv = evaluate_model(knn, X, y, kf)
    accuracy = evaluate_model_accuracy(knn, X, y, kf)
    print(
        f"KNN (k={k}): Average accuracy (CV) = {accuracy_cv:.2f}, Average accuracy = {accuracy:.2f}")

# MLP
print("\nMLP:")
for config in mlp_configurations:
    mlp = MLPClassifier(hidden_layer_sizes=config, max_iter=1000)
    accuracy_cv = evaluate_model(mlp, X, y, kf)
    accuracy = evaluate_model_accuracy(mlp, X, y, kf)
    print(
        f"MLP (config={config}): Average accuracy (CV) = {accuracy_cv:.2f}, Average accuracy = {accuracy:.2f}")

# SVM
print("\nSVM:")
for kernel in svm_kernels:
    svm = SVC(kernel=kernel)
    accuracy_cv = evaluate_model(svm, X, y, kf)
    accuracy = evaluate_model_accuracy(svm, X, y, kf)
    print(
        f"SVM (kernel={kernel}): Average accuracy (CV) = {accuracy_cv:.2f}, Average accuracy = {accuracy:.2f}")
