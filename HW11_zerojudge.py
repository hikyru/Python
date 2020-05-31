# -*- coding: utf-8 -*-
"""
Created on Sat May 5:34 2020

@author: KatherineYu
"""

"""
nlist = []
while True:
    try:
        n = int(input())
        while n != 0:
            nlist.append(int(n % 2))
            n = n//2
            print(n.reversed())
        print(nlist, sep='')

    except:
         break """
"""while True:
    try:
        x = bin(int(input()))[2:]
        print(x)
    except:
        break"""

"""
import math
while True:
    try:
        x = input()
        print(eval(input().replace("/", "//")))
    except:
        break

"""
"""
# a022: 迴文
import math
while True:
    try:
        n = list(input())
        if n.reverse() == n:
            print("yes")
        else:
            print("no")
    except:
        break
"""
"""
while True:
    try:
        n = map(int,input())
        
    except:
        break
"""
n = int(input())
for i in range(n):
    x = input()
    y = 1
    for i in x:
        y = y * int(i)
    print(y)
