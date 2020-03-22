
"""
Created on Sat Feb 8 12:31 2020

@author: KatherineYu
"""
# define parameters for the circle
radius = float(input("Radius of the circle: "))
angle = float(input("Measure of an angle: "))
pi = 3.14

# finding surface area
print("Surface area: ")
area = radius * radius * pi * (angle / 360)
print(round(area, 3), end = '\n \n')

# finding circumference
print("Circumference: ")
circumference = radius * 2 * pi * (angle / 360)
print(round(circumference, 3), end = '\n')







