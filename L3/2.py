import pandas as pd

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

sorted = heroes.sort_values(by='Weight', ascending=False)[:5]

# Print weight sorted
print(sorted['Weight'])