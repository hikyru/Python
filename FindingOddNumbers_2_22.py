# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 7:28 2020

@author: KatherineYu
"""

# Input a Number

x = int(input("Enter a Number: "))

# Find all odd numbers in the number

print("Finding all odd numbers in", x, "!")

# m is a variable used for counting the number of digits printed
m = 0

for i in range(1, x + 1, 1):
    # if there are remainers after i is divided by 2, that means i is an odd number
    # because even numbers are perfectly divisible
    if i % 2 == 1:
        print(i, end='\t')
        # for every time an odd number is printed, m a number is stored into m
        m += 1
    if m % 10 == 0:
        # if m is perfectly divisible by 10, that means there are at least ten odd numbers in x
        # a new line will be added
        print()    # will only run every every time there are ten more digits added to m
