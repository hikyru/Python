# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 5:28 2020

@author: KatherineYu
"""

import math as m

# Input Circle Dimensions

r = float(input("Enter Radius: "))

# Calculate

area = r * r * m.pi

circumference = 2 * r * m.pi

# Print Result

print("\n Area: ", area)
print("\n Circumference: ", circumference)
