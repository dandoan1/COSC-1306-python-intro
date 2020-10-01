# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
assignment2
cosc1306
@author: dan doan 1986920
"""
SCREEN_SIZE = 500
#user input here
squares = int(input("Please enter the number of square per line: "))

import turtle
scn = turtle.Screen()
scn.setup(1000, 1000)
scn.bgcolor("white")
dan = turtle.Turtle()
dan.color("black")
dan.speed(0)
#move up to corner
dan.penup()
dan.backward(SCREEN_SIZE//2)
dan.left(90)
dan.forward(SCREEN_SIZE//2)
dan.right(90)
dan.pendown()
for e in range(4): #border
    dan.pensize(3)
    dan.forward(SCREEN_SIZE)
    dan.right(90)
dan.pensize(1)

for grid in range(squares): #grid
    for line in range(squares): #one line
        for i in range(2): #single square
            dan.pendown()
            dan.forward(SCREEN_SIZE//squares/4)
            dan.backward(SCREEN_SIZE//squares/2)
            dan.forward(SCREEN_SIZE//squares/4)
            dan.left(90)
            dan.dot(10, "blue")
            dan.penup()
        dan.right(180)
        dan.forward(SCREEN_SIZE//squares)
    dan.backward(SCREEN_SIZE)
    dan.right(90)
    dan.forward(SCREEN_SIZE//squares)
    dan.left(90)
scn.exitonclick()
