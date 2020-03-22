# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 5:20 2020

@author: KatherineYu
"""

# User Input

gender = input("Gender: ")

gender = gender.lower()

waist = float(input("Waist Measurements: "))

# Determine whether user is fat or not

if gender == "male" and waist >= 90:
    print('\n' "FAT.")
elif gender == "male" and waist < 90:
    print('\n' "NOT FAT.")
elif gender == "female" and waist >= 85:
    print('\n' "FAT.")
elif gender == "female" and waist < 85:
    print('\n' "NOT FAT.")
else:
    print('\n' "Input undefined. Please input 'female' or 'male'")
