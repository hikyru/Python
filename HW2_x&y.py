# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 1:39 2020

@author: KatherineYu
"""

# define x & y

x = int(input("Enter X Value (Whole Number): "))

y = int(input("Enter Y Value (Whole Number): "))

# Compare X and Y

if x > y:
    print('\n', x, " is greater")
elif y > x:
    print('\n', y, " is greater")
else:
    print('\n', x, "=", y)
