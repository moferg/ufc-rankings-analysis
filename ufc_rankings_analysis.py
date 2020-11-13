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
import pandas as pd

# Variables

filepath = 'rankings_history.csv'

# Functions

def unique_values(list1):
    '''Takes a list as input and outputs a list with all duplicates removed'''
    x = np.array(list1)
    return list(np.unique(x))

df = pd.read_csv(filepath)
print(df)
