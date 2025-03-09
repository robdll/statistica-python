import pandas as pd

from heroes.reader import heroes_list

# Extract years and names
years = [int(h[7]) if h[7] else None for h in heroes_list[1:]]
names = [h[0] for h in heroes_list[1:]]
first_appearance = pd.Series(years, index=names)

first_appearance = first_appearance[[1970 <= y <1975 for y in first_appearance]]

print(first_appearance.head(15))
print(first_appearance.value_counts().sort_index())



