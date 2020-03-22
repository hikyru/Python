# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 7:28 2020

@author: KatherineYu
"""

import random as rm

# Computer picks a number

computer = rm.randint(1, 10)

while True:
    user = int(input("Enter a whole number: "))

# Compare values

    if user == computer:
        print("\n True")
        break
    elif user > computer:
        print("Your guess is a bit too large")
    elif user < computer:
        print("Your guess is a bit too small")

