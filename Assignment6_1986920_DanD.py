# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
assignment6
cosc1306
@author: dan doan 1986920
"""

#i know it does not look clean but everything works like its suppsoed to be
#i also know that you can probably reduce the amount of lines by a lot but
#i am too lazy to do it

#function to draw the shapes

def square(request):
    for x in range(request):
        print ("X"*request)

def rectangle(width, length):
    for x in range(width):
        print ("X"*length)
    
def left_triangle(request):
    for x in range(1,request+1):
        print ("^"*x)

def right_triangle(request):
    for x in range(1, request+1):
        print (" "* (request - x) + "^"*x)

def diamond(request):
    y = 1
    for x in range(1,request+1):
        if x == 1:
            print (" "*(request-1) + "#"*x)
        elif x%2 == 1:
            print (" "*(request-(y+1)) + "#"*x)
            y = y+1
        else:
            pass
    for x in range(1,request):
        if x%2 == 1:
            print (" "*y + "#"*(request-x-1))
            y = y+1
        else:
            pass
    
def choices():
    print (("""Please select from the following shapes:
    1– Square
    2– Rectangle
    3– Right Triangle (left)
    4– Right Triangle (right)
    5– Diamond
    0- Exit"""))

        
#input for the function to start
request = int(input((("""Please select from the following shapes:
    1– Square
    2– Rectangle
    3– Right Triangle (left)
    4– Right Triangle (right)
    5– Diamond
    0- Exit 
    Please enter your selection: """))))
        
    
    
while True: #infin loops until user exit
    if request == 1:
        size = int(input("Please enter the size of the square: "))
        while size <= 0: #instead of function to check i manually check it for each one of them
            print ("Please enter a positive interger.")
            size = int(input("Please enter the size of the square: "))
        square(size)
    if request == 2:
        width = int(input("Please enter the width of the rectangle: "))
        length = int(input("Please enter the length of the rectangle: "))
        while width <= 0 or length <= 0:
            print ("Please input a positive interger for each value.")
            width = int(input("Please enter the width of the rectangle: "))
            length = int(input("Please enter the length of the rectangle: "))
        rectangle(width, length)
    if request == 3:
        size = int(input("Please enter the size of the triangle: "))
        while size <= 0:
            print ("Please enter a positive interger.")
            size = int(input("Please enter the size of the triangle: "))
        left_triangle(size)
    if request == 4:
        size = int(input("Please enter the size of the triangle: "))
        while size <= 0:
            print ("Please enter a positive interger.")
            size = int(input("Please enter the size of the triangle: "))
        right_triangle(size)
    if request == 5:
        size = int(input("Please enter the size of the diamond: "))
        while size <= 0 or size%2 == 0:
            print ("Please enter a positive odd interger.")
            size = int(input("Please enter the size of the diamond: "))       
        diamond(size)
    if request == 0:
        break
    if request < 0 or request > 5:
        print ("Please enter a positive value that is 5 or less.")
    else:
        pass
    choices()
    request = int(input("Please enter your selection: "))


#exit message when loops end
print ("Good Bye!")
