# -*- coding: utf-8 -*-
"""
Created on Sat May 23 8:54 2020

@author: KatherineYu
"""
import os

print(os.getcwd())

f = open('bmistorage.txt', 'r')

txt = f.readlines()

height = int(txt[0])/100
weight = int(txt[1])
bmi = weight/(height * height)

f.close()

print("BMI: ", round(bmi, 3))

