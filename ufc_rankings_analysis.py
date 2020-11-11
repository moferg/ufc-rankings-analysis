# Marshall Ferguson - 11/2020

# OUTLINE
# Create a DB from CSV file
# Use CSV file for data viz
# Use DB for data analysis
# Have options for user to choose between graphs or text
# Potential options: duration in rankings (longest/shortest), info of a fighter given fighter's name,
                   # info for a weight class, info for P4P, duration as champ (longest/shortest),
                   # fighters who were champs multiple times, fighters who were champs in multiple weight classes

# Imports

import csv
import numpy as np

# Variables created before opening CSV file

date =[]
weight_class = []
fighter_name = []
rank = []

with open('rankings_history.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            line_count += 1
        else:
            date.append(row[0])
            weight_class.append(row[1])
            fighter_name.append(row[2])
            rank.append(row[3])
            line_count +=1

with open('rankings_history.csv') as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    for dicts in csv_dict_reader:
        if dicts.get('rank') == '0':
            print(f'{dicts.get("fighter")} was the {dicts.get("weightclass")} champ on {dicts.get("date")}')

print(f'Successfully processed {line_count} lines.')