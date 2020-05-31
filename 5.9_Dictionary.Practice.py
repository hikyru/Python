# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4/25 8:46 2020

@author: KatherineYu
"""

def printletters(letters):
    for key, value in letters.items():
        print(key, value, end='; ')

import operator

letters = {}
appear = input("Enter letters: ")
print(appear)
for i in appear:
    print(i)
    if i not in letters:
        letters[i] = 1
    else:
        letters[i] += 1
printletters(letters)

print(sorted(letters.items(), key=lambda d: d[1]))
# printletters(letters)