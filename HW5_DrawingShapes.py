# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 5:39 2020

@author: KatherineYu
"""
# call out the module turtle
import turtle

# Define variables
sides = int(input("Enter # of sides(1-12): "))

if 1 <= sides <= 12:
    canvas = turtle.Screen()
    canvas.title('drawing shapes')
    canvas.bgcolor('white')
    pencil = turtle.Turtle()

    for i in range(1, sides + 1, 1):
        pencil.color('black')
        pencil.left(360 / sides)
        pencil.forward(100)
    pencil.hideturtle()
    turtle.done()

else:
    print("Error, try again")
