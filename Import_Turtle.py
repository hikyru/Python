# -*- coding: utf-8 -*-
"""
Created on Sat Mar 3/14 7:58 2020

@author: KatherineYu
"""
# call out the module turtle
import turtle

canvas = turtle.Screen()
canvas.title('Whiteboard')
canvas.bgcolor('#ffeea8')

pen = turtle.Turtle()
for i in range(1, 5, 1):
    pen.forward(100)
    pen.left(90)

draw = turtle.Turtle()
for i in range(1, 4, 1):
    draw.color('cyan')
    draw.shape('turtle')
    draw.right(240)
    draw.backward(100)
draw.hideturtle()

spot = turtle.Turtle()
spot.dot(50, 'red')

turtle.done()

