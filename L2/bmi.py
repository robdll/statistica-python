import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# Open and read the file
with open('heroes.csv', 'r') as heroes_file:
    heroes_reader = csv.reader(heroes_file, delimiter=';', quotechar='"')
    
    # Convert reader to a list (excluding the header)
    heroes = list(heroes_reader)
    
    # Create Series first appearance
    weight = [float(h[5]) if h[5].strip() else None for h in heroes[1:]]
    height = [float(h[4]) if h[4].strip() else None for h in heroes[1:]]

    weight = pd.Series(weight)
    height = pd.Series(height)

    bmi = weight / height.apply(lambda h: (h/100)**2)

    print(bmi)