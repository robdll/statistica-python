import pandas as pd

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

# Print the Genders
print(heroes['Gender'])

# print the Strength of Superman
print(heroes.at['Superman', 'Strength'])