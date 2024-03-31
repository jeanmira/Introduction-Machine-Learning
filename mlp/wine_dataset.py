# -*- coding: utf-8 -*-
# @Author: Jean Mira
# @Date:   2024-03-31 17:25:56
# @Last Modified by:   Jean Mira
# @Last Modified time: 2024-03-31 17:29:28

import pandas as pd

data = {
    'Class': [1, 1, 1, 1, 1],
    'Alcohol': [14.23, 13.20, 13.16, 14.37, 13.24],
    'Malic acid': [1.71, 1.78, 2.36, 1.95, 2.59],
    'Ash': [2.43, 2.14, 2.67, 2.50, 2.87],
    'Alcalinity of ash': [15.6, 11.2, 18.6, 16.8, 21.0],
    'Magnesium': [127, 100, 101, 113, 118],
    'Total phenols': [2.80, 2.65, 2.80, 3.85, 2.80],
    'Flavanoids': [3.06, 2.76, 3.24, 3.49, 2.69],
    'Nonflavanoid phenols': [0.28, 0.26, 0.30, 0.24, 0.39],
    'Proanthocyanins': [2.29, 1.28, 2.81, 2.18, 1.82],
    'Color intensity': [5.64, 4.38, 5.68, 7.80, 4.32],
    'Hue': [1.04, 1.05, 1.03, 0.86, 1.04],
    'OD280/OD315 of diluted wines': [3.92, 3.40, 3.17, 3.45, 2.93],
    'Proline': [1065, 1050, 1185, 1480, 735]
}

df = pd.DataFrame(data)

df.to_csv('dataset.csv', index=False)

print("Dataset gerado e salvo como 'dataset.csv'")
