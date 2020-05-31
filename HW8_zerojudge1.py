# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4/25 5:33 2020

@author: KatherineYu
"""

'''
M, D = map(int, input().split());
S = ((M * 2 + D) % 3)
if S == 0:
    print(1)
elif S == 1:
    print(2)
elif S == 2:
    print(2)

'''

'''
while True:
        try:
            n = [(int(input())), (int(input()))]
            print(n[-1] + n[-2])

        except:
            break
'''

'''
while True:
    try:
        n = int(input())
        if (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0):
            print("閏年")
        else:
            print("平年")
    except:
         break
'''

n = int(input())
for i in range(0, n, 1):
    a, b, c, d = map(int, input().split())
    if d - c == c - b:
        print(a, b, c, d, d + (d - c))
    elif d // c == c // b:
        print(a, b, c, d, d * (d // c))
