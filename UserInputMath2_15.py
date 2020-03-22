# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 6:30 2020

@author: KatherineYu
"""
# User Inputs
while True:
    a = int(input("Enter 1st Value: "))
    if a <= 0:
        continue  # re-run program until user inputs a positive number
    else:
        break

while True:
    b = int(input("Enter 2nd Value: "))
    if b <= 0:
        continue
    else:
        break

while True:    # start here on 2/29

    choice = int(input("Choose 1: Addition 2: Subtraction 3: Multiplication 4: Division -1: End Program "))

    # Calculation
    if choice == 1:
        print(a + b)  # addition
    elif choice == 2:
        print(a - b)  # subtraction
    elif choice == 3:
        print(a * b)  # multiplication
    elif choice == 4:
        print(a / b)  # division
    elif choice == -1:
        break   # end the loop
    else:
        print("ERROR.")