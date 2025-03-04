import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

colors = ['blue', 'red', 'green', 'purple', 'orange']

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')
# print(heroes['Publisher'].value_counts())

heroes_with_year = heroes[heroes['First appearance'] > 1900]

gender_freq = pd.crosstab(index=heroes_with_year['Gender'],
                          columns=['Abs. frequence'],
                          colnames=[''])

gender_freq = gender_freq.loc[['M', 'F']]

print(gender_freq)

heroes_with_year['Publisher'].value_counts().plot.bar(color=colors)
heroes_with_year['Publisher'].value_counts().plot.bar(color=colors, legend=False)

plt.show()
