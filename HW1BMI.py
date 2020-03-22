# -*- coding: utf-8 -*-
"""
Created on Sat Feb 8 12:00 2020

@author: KatherineYu
"""
# User Input
name = input("Name: ")
height = float(input("Height: "))
weight = float(input("Weight: "))

print(name)
print(height)
print(weight)

# BMI = kg/m2 * kg is a person's weight in kilograms and m2 is their height in metres squared *

m = (height / 100) * (height / 100)

bmi = weight/m

print("BMI=", bmi)

# Identifying BMI

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 28:
    print("Overweight")
elif bmi >=28 and bmi <32:
    print("Obese")
else:
    print("Intense Obesity")
