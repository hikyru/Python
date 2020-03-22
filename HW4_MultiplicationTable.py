# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 7:24 2020

@author: KatherineYu
"""
# i loop in j
for i in range(1, 10, 1):
    # for every i, j runs i times
    for j in range(1, i+1, 1):
        print(j, "x", i, "=", (j*i), end='\t')
    # for every i, a new line will be added
    print()


