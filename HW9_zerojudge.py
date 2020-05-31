# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 8:17 2020

@author: KatherineYu
"""

#平面圓形切割

""" while True:
    try:
        n = int(input())
        print(n*n-n+2)

    except:
         break 

#最大公因數(GCD)

import math
while True:

    try:
        n, m = map(int,input().split())
        print(math.gcd(n, m))
    except:
         break

#空間切割

while True:
    try:
        n = int(input())
        print(int(1+(n) * (n ** 2 +5)/6 ))
    except:
        break

"""
#數字翻轉
while True:
    try:
        n = list(input())
        n.reverse()
        n = "".join(n)
        print(int(n))
    except:
        break

# Print it all
"""while True:
    try:
        n = int(input())
        if n == 0:
            print()
            break
        elif n < 1000:
            for i in range(1, n, 1):
                if i % 7 != 0:
                    print(i, end= ' ')
            print()
    except:
        break

while True:
    try:
        n = input()
        for i in range(int(n)):
            if i == 0 or i % 7 == 0:
                continue
            else:
                print(i, end=" ")
        print()
    except:
        break"""