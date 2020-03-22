# -*- coding: utf-8 -*-
"""
Created on Sat Feb 8 7:57 2020

@author: KatherineYu
"""

NumberGrade = float(input("Enter Grade: "))

if NumberGrade >= 90:
    print("A")
elif NumberGrade >= 80:
    print("B")
elif NumberGrade >= 70:
    print("C")
elif NumberGrade >= 60:
    print("D")
else:
    print("F")