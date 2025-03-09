import pandas as pd

from heroes.reader import heroes_list

# Extract years and names
years = [int(h[7]) if h[7] else None for h in heroes_list[1:]]
names = [h[0] for h in heroes_list[1:]]

# Create a Pandas Series
first_appearance = pd.Series(years, index=names)

count_by_year_of_appearance = first_appearance.value_counts()
print(count_by_year_of_appearance)

# get index of element in count_by_year_of_appearance with key = 1960

# count_by_year_of_appearance.index.get_loc(1960)
# count heroes appeared after 1960
# totalAfter1960 = count_by_year_of_appearance[count_by_year_of_appearance.index >= 1960].sum() 
# totalAfter1940 = count_by_year_of_appearance[count_by_year_of_appearance.index >= 1940].sum()
# totalBefore1966 = count_by_year_of_appearance[count_by_year_of_appearance.index <= 1965].sum()
# totalBefore1970 = count_by_year_of_appearance[count_by_year_of_appearance.index < 1970].sum()
# print(totalAfter1960)
# print(totalAfter1940 + totalBefore1966)
# print(totalBefore1970)
#count_by_year_of_appearance.plot.bar()
#plt.show()