import pandas as pd
import matplotlib.pyplot as plt

heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

male_strength_freq = (pd.crosstab(index=heroes.loc[heroes['Gender']=='M',
                                                   'Strength'],
                                 columns='Rel. freq.',
                                 normalize=True)
                        .loc[:, 'Rel. freq.'])
male_strength_freq = male_strength_freq.reindex(heroes['Strength'].unique()).dropna().sort_index()                                       
female_strength_freq = (pd.crosstab(index=heroes.loc[heroes['Gender']=='F',
                                                     'Strength'],
                                   columns='Rel. freq.',
                                   normalize=True)
                          .loc[:, 'Rel. freq.'])
male_strength_freq = male_strength_freq.reindex(heroes['Strength'].unique()).dropna().sort_index()
male_strength_freq.plot(marker='o', color='blue', legend=False)
female_strength_freq.plot(marker='o', color='pink', legend=False)
# stacked bar chart
plt.show()

# overlapped bar chart
male_strength_freq.plot.bar(color='blue', alpha=.7)
female_strength_freq.plot.bar(color='pink', alpha=.7)
plt.show()

# Pie Chart
heroes_with_year = heroes[heroes['First appearance'] > 1900]
gender_freq = pd.crosstab(index=heroes_with_year['Gender'],
                          columns=['Abs. frequence'],
                          colnames=[''])
gender_freq.plot.pie(y='Abs. frequence', colors=['pink', 'blue'])
plt.show()
