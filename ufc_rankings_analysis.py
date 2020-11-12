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

# Functions

def unique_values(list1):
    '''Takes a list as input and outputs a list with all duplicates removed'''
    x = np.array(list1)
    return list(np.unique(x))

# Variables created before opening CSV file

dates =[]
weight_class = []
names = []
rank = []
filepath = 'rankings_history.csv'

with open(filepath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
            line_count += 1
        else:
            dates.append(row[0])
            weight_class.append(row[1])
            names.append(row[2])
            rank.append(row[3])
            line_count +=1

with open(filepath) as csv_file:
    csv_dict_reader = csv.DictReader(csv_file)
    for dicts in csv_dict_reader:
        if dicts.get('rank') == '0':
            # print(f'{dicts.get("fighter")} was the {dicts.get("weightclass")} champ on {dicts.get("date")}')
            pass

print(f'Successfully processed {line_count} lines.')

# Remove duplicates from names list
unique_names = unique_values(names)
print(f'The value of the unique_names variable is : {unique_names}')
print(f'The length of the unique_names variable is : {len(unique_names)}')

weeks_ranked = [names.count(name) for name in unique_names]
print(f'The value of the weeks_ranked variable is : {weeks_ranked}')
print(f'The length of the weeks_ranked variable is : {len(weeks_ranked)}')

for a, b in zip(unique_names, weeks_ranked):
    print(f'Fighter {a} spent {b} weeks in the rankings')