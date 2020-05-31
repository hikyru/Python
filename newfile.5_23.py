# -*- coding: utf-8 -*-
"""
Created on Sat May 7 8:207 2020

@author: KatherineYu
"""

import os

print(os.getcwd())

if os.path.exists('FileTest.txt'):
    print("exist")
"""
f = open('FileTest.txt', 'r')

txt = f.read()

# print(txt)

 while txt != '':
    print(txt)
    txt = f.readline() 



f.close()"""

f = open('FileTest.txt', 'a')

f.write("\nHello Good night")

strlist = ['A', 'B']

f.writelines(strlist)

f.close()

f = open('FileTest.txt', 'r')

txt = f.read()

while txt != '':
    print(txt)
    txt = f.readline()
