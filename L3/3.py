import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

sorted_heroes = heroes.sort_values(by='Weight', ascending=False)[:5]

# Create a boolean mask for Weight > 700
filtered_mask = sorted_heroes['Weight'] > 700

# Apply the mask to get the filtered DataFrame
filtered_heroes = sorted_heroes[filtered_mask]

# Print the filtered heroes
print(filtered_heroes.head(1))