# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 7:51 2020

@author: KatherineYu
"""

# for loops i and j

for i in range(1, 10, 1):
    # this part will run 9 times
    for j in range(1, 10, 1):
        print(j, "x", i, "=", (j * i), end='\t')
    # a new line will be added after every row of 9 equations
    print()