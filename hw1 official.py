# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
hw1
cosc1306
@author: dan doan 1986920
"""

def isMandelbrot(x, y):
    c = complex(x,y)
    z = 0
    for i in range(1000):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def picture(num_rows, num_columns):      
    for row in range(num_rows):
        for column in range (num_columns):
            # Convert row and column into x and y
            x = -2 + (2.5/(num_columns-1)) * column
            y = 1 - (2/(num_rows-1)) * row
            
            if isMandelbrot(x, y):
                print ("O", end="")
            else:
                print ("*", end="")
        print ()    
    
    

num_rows = int(input('Please enter the number of rows: '))
num_columns = int(input('Please enter the number of rows: '))

picture(num_rows, num_columns)
