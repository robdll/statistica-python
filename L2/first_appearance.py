import pandas as pd

from heroes.reader import heroes_list

# Extract years and names
years = [int(h[7]) if h[7] else None for h in heroes_list[1:]]
names = [h[0] for h in heroes_list[1:]]

# Create a Pandas Series
first_appearance = pd.Series(years, index=names)

# access series by prop, loc, iloc
print(first_appearance['Ant-Man'])
print(first_appearance.loc['Ant-Man'])
print(first_appearance.iloc[-3])
