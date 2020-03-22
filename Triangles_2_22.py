# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 7:12 2020

@author: KatherineYu
"""

# Input Side Lengths

a = int(input("Input 1st Side length: "))
b = int(input("Input 2nd Side length: "))
c = int(input("Input 3rd Side length: "))

# Is it true that the sum of any two sides is greater than the third side?

if a + b > c and a + c > b and b + c > a:
    print("This is a triangle.")
else:
    print("This is not a triangle.")
