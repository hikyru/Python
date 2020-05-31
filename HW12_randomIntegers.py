# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:45 2020

@author: KatherineYu
"""
import random

x = []

while len(x) != 100:
    x.append(random.randint(0, 100))

total = 0

for i in x:
    total += int(x[i-1])
    i += 1

file = open("rand.txt", "w")

for i in x:
    file.write(str(x))

file.write("\nSum = ")
file.write(str(total))

