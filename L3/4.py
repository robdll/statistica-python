import pandas as pd

# Dati quantitativi e qualitativi
# Una delle principali distinzioni che si possono fare sui dati osservabili riguarda il modo in cui questi sono misurati
# - si parla di dati _quantitativi_ se l'esito della misurazione è una quantità numerica;
# - si parla invece di dati _qualitativi_ (o categorici, o nominali) quando la misurazione è fatta scegliendo un'etichetta a partire da un insieme disponibili.


# Read the CSV file
heroes = pd.read_csv('heroes.csv', index_col=0, delimiter=';')

print(heroes['Publisher'].value_counts())
