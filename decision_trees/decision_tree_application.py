# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-03-16 13:55:23
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-03-16 14:05:37


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# Function to load dataset or generate a sample dataset
def load_or_generate_dataset():
    # Check if the dataset file exists, if not, generate a sample dataset
    try:
        # Load dataset if it exists
        dataset = pd.read_csv('dataset.csv')
    except FileNotFoundError:
        # Generate a sample dataset
        dataset = generate_sample_dataset()
        # Save generated dataset to file
        dataset.to_csv('dataset.csv', index=False)
    return dataset


# Function to generate a sample dataset
def generate_sample_dataset():
    # Create sample dataset
    data = {'Age': [25, 35, 45, 20, 30, 40, 55, 33, 42, 60],
            'Income': [50000, 60000, 75000, 32000, 43000, 62000, 100000, 72000, 80000, 95000],
            'Loan_Default': ['No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'Yes']}
    return pd.DataFrame(data)


# Main function to build and evaluate Decision Tree model
def main():
    # Load or generate dataset
    dataset = load_or_generate_dataset()

    # Check the distribution of classes
    print("Loan_Default")
    print(dataset['Loan_Default'].value_counts())

    # Split dataset into features (X) and target variable (y)
    X = dataset.drop('Loan_Default', axis=1)
    y = dataset['Loan_Default']

    # Split dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Initialize Decision Tree classifier
    clf = DecisionTreeClassifier()

    # Train Decision Tree classifier
    clf.fit(X_train, y_train)

    # Predict on the testing set
    y_pred = clf.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy:.2f}')


# Execute main function
if __name__ == "__main__":
    main()
