import csv
import pandas as pd

with open('./heroes.csv', 'r') as heroes_file:
  heroes_reader = csv.reader(heroes_file, delimiter=';', quotechar='"')
  heroes_list = list(heroes_reader)[1:]

heroes_df = pd.read_csv('./heroes.csv', delimiter=';')
