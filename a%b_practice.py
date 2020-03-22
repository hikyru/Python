# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 6:37 2020

@author: KatherineYu
"""

# Input a value
x = int(input("Enter a value: "))

# is the number a common factor of 3 and 5?
if x % 15 == 0:
    print("HI")
elif x % 3 == 0:
    print("Goodnight")
elif x % 5 == 0:
    print("happy")
else:
    print("NO")
