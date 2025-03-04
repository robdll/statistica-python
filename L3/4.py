import pandas as pd
import numpy as np

# Dati quantitativi e qualitativi
# Una delle principali distinzioni che si possono fare sui dati osservabili riguarda il modo in cui questi sono misurati
# - si parla di dati _quantitativi_ se l'esito della misurazione è una quantità numerica;
# - si parla invece di dati _qualitativi_ (o categorici, o nominali) quando la misurazione è fatta scegliendo un'etichetta a partire da un insieme disponibili.

# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')
# print(heroes['Publisher'].value_counts())

heroes_with_year = heroes[heroes['First appearance'] > 1900]

publisher_freq = pd.crosstab(
  index=heroes_with_year['Publisher'],
  columns=['Abs. freqence'],
  colnames=['']
)
# print(publisher_freq)

publisher_abs_freq = pd.crosstab(
  index=heroes_with_year['Publisher'],
  columns=['Rel. frequence'],
  colnames=['']
)

publisher_rel_freq = publisher_abs_freq / publisher_abs_freq.sum()
# print(publisher_rel_freq)

publisher_rel_freq = publisher_rel_freq.apply(
  lambda p: np.round(100 *p, 2)
).astype(str) + '%'

print(publisher_rel_freq)