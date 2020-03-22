# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 5:07 2020

@author: KatherineYu
"""
# User Input
day = int(input("Pick A Number (1, 2, 3, 4, 5, 6, or 7): "))

# Identifying Day of the Week

if day == 6 or day == 7:
    print("Weekend")
elif day >= 1 and day <= 5:
    print("Weekday")
else:
    print("Error.")
