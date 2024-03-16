# -*- coding: utf-8 -*-
# @Author: Your name
# @Date:   2024-03-16 13:18:22
# @Last Modified by:   Your name
# @Last Modified time: 2024-03-16 13:18:45


import pandas as pd


# Create the dataset
def create_dataset():
    data = {
        'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rainy', 'Rainy', 'Rainy', 'Overcast',
                    'Sunny', 'Sunny', 'Rainy', 'Sunny', 'Overcast', 'Overcast', 'Rainy'],
        'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild', 'Cool',
                 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
        'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High',
                     'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
        'Windy': [False, True, False, False, False, True, True, False, False, False,
                  True, True, False, True],
        'Play': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes',
                 'Yes', 'Yes', 'Yes', 'No']
    }
    # Create DataFrame
    df = pd.DataFrame(data)
    return df


def main():
    # Create the dataset
    dataset = create_dataset()
    # Save the dataset to a CSV file
    dataset.to_csv('weather_dataset.csv', index=False)
    print("Dataset created and saved successfully!")


if __name__ == "__main__":
    main()
