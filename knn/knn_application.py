# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-03-16 13:25:39
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-03-16 13:50:50


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('weather_dataset.csv')

# Encode categorical variables
le = LabelEncoder()
data['Outlook'] = le.fit_transform(data['Outlook'])
data['Temp'] = le.fit_transform(data['Temp'])
data['Humidity'] = le.fit_transform(data['Humidity'])
data['Windy'] = le.fit_transform(data['Windy'])
data['Play'] = le.fit_transform(data['Play'])

# Split data into features and target variable
X = data.drop('Play', axis=1)
y = data['Play']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Initialize kNN classifier
knn = KNeighborsClassifier(n_neighbors=2)

# Train the classifier
knn.fit(X_train, y_train)

# Make predictions on the test set
y_pred = knn.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
