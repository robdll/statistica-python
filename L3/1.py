import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

# Print the Genders
print(heroes['Gender'])

# print the Strength of Superman
print(heroes.at['Superman', 'Strength'])