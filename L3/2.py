import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

sorted = heroes.sort_values(by='Weight', ascending=False)[:5]

# Print weight sorted
print(sorted['Weight'])