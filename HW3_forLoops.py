# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 5:57 2020

@author: KatherineYu
"""

# User Input
biggest = int(input("Enter Ending number: "))
# Loops
total = 0
for i in range(1, biggest + 1, 1):
    total = total + i

# print sum of numbers
print(total)

box = 1
for i in range(1, biggest + 1, 1):
    box = box * i

# print product of numbers
print(box)
