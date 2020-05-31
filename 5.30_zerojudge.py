# -*- coding: utf-8 -*-
"""
Created on Sat May 5/30 7:47 2020

@author: KatherineYu
"""
"""
# a009 解碼器
x = input()
for i in x:
    print(chr(ord(i) - 7), end = '')

# d498 我不說髒話
n = int(input())
for i in range (0, n, 1):
    print("I don't say swear words!")

# c185 Hey Jude
print("Hey " + input())

# c418 Bert的三角形
n = int(input())
for i in range(1, n + 1, 1):
     print("*" * i)
"""
# a053 Sagit's 計分程式

while True:
    try:
        n = int(input())
        if n >= 0 and n <= 10:
            print(n * 6)
        elif n >= 11 and n <= 20:
            print(((n - 10) * 2) + 60)
        elif n >= 21 and n <=40:
            print((n - 20) + 80)
        elif n >= 40:
            print('100')
    except:
        break




