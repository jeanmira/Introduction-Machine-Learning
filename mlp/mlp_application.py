# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-03-31 17:36:42
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-03-31 17:52:54


"""
The UCI Machine Learning Repository for the Wine dataset is available for download at the following link:
UCI Machine Learning Repository: https://archive.ics.uci.edu/dataset/109/wine
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv('dataset.csv')

# Splitting the data into independent and dependent variables
X = df.drop(columns=['Class'])
y = df['Class']

# Splitting the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.7, random_state=105)

# Scaling the data
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Building the model
model = MLPClassifier(hidden_layer_sizes=(
    X.shape[1], X.shape[1], X.shape[1]), max_iter=500, random_state=105)

# Training the model
model.fit(X_train_scaled, y_train)

# Obtaining the classification report of the model
y_pred = model.predict(X_test_scaled)
report = classification_report(y_test, y_pred)
print("Classification Report:")
print(report)

# Obtaining the weights
weights = model.coefs_
print("Model Weights:")
print(weights)
