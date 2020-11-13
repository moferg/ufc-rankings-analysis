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
from consolemenu import ConsoleMenu, SelectionMenu

# Variables

filepath = 'rankings_history.csv'
selection_menu_options = ["See a fighter's rank throughout time",
                          "See the ranked fighters in a weight class", 
                          "See the champs of each weight class"]
title = "Welcome to the UFC Rankings Analyzer and Visualizer!"
subtitle = "Please choose from one of the following selections:"

# Functions

def unique_values(list1):
    '''Takes a list as input and outputs a list with all duplicates removed'''
    x = np.array(list1)
    return list(np.unique(x))

df = pd.read_csv(filepath)
# print(df)

# df_sort_by_name = df.sort_values(by='fighter')
# print(df_sort_by_name)

# df_anderson_silva = df['fighter'] == 'Anderson Silva'
# print(df[df_anderson_silva].sort_values(by=['weightclass', 'date']))

# name_input = input("Please enter a fighter's name to see their rankings on different dates:     ")
# df_name_input = df['fighter'] == name_input
# print(df[df_name_input])

# menu = ConsoleMenu("Welcome to the UFC Rankings Analyzer and Visualizer!", "Please choose from one of the following selections:")
selection = SelectionMenu.get_selection(selection_menu_options, title, subtitle)
selection += 1
if selection == 1:
    name_input = input("Please enter a fighter's name to see their rankings on different dates:     ")
elif selection == 2:
    weightclass_input = input("Please enter the weightclass for which you would like to see the rankings:   ")
elif selection == 3:
    print("Here are the champs of each weight class:")
# menu.show()
# menu.join()