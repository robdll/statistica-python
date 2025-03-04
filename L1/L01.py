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
    years = [int(h[7]) if h[7] else None for h in heroes[1:]]
    names = [h[0] for h in heroes[1:]]
    first_appearance = pd.Series(years, index = names)

    #print(first_appearance)

    count_by_year_of_appearance = first_appearance.value_counts()
    #print(count_by_year_of_appearance)
    
    # get index of element in count_by_year_of_appearance with key = 1960
    
    # count_by_year_of_appearance.index.get_loc(1960)
    # count heroes appeared after 1960
    totalAfter1960 = count_by_year_of_appearance[count_by_year_of_appearance.index >= 1960].sum() 
    totalAfter1940 = count_by_year_of_appearance[count_by_year_of_appearance.index >= 1940].sum()
    totalBefore1966 = count_by_year_of_appearance[count_by_year_of_appearance.index <= 1965].sum()
    totalBefore1970 = count_by_year_of_appearance[count_by_year_of_appearance.index < 1970].sum()
    print(totalAfter1960)
    print(totalAfter1940 + totalBefore1966)
    print(totalBefore1970)
    #count_by_year_of_appearance.plot.bar()
    #plt.show()