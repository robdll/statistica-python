import pandas as pd

from heroes.reader import heroes_list

# Extract years and names
years = [int(h[7]) if h[7] else None for h in heroes_list[1:]]
names = [h[0] for h in heroes_list[1:]]

# Create Series first appearance
weight = [float(h[5]) if h[5].strip() else None for h in heroes_list[1:]]
height = [float(h[4]) if h[4].strip() else None for h in heroes_list[1:]]

weight = pd.Series(weight)
height = pd.Series(height)

bmi = weight / height.apply(lambda h: (h/100)**2)

print(bmi)