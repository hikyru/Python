# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 1:25 2020

@author: KatherineYu
"""

# define variables

gender = input("Gender: ")

gender = gender.lower()

waist = float(input("Waist Measurements: "))

# Determine whether user is fat or not
if gender == "male":
    if waist >= 90:
        print('\n' "FAT.")
    else:
        print('\n' "NOT FAT.")
elif gender == "female":
    if waist >= 85:
        print('\n' "FAT.")
    else:
        print('\n' "NOT FAT.")
else:
    print('\n' "Input undefined. Please input 'female' or 'male'")