# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
hw0
cosc1306
@author: dan doan 1986920
"""
import math
GALLON_COVERAGE = 400 #square feet
#Dimension ipnut
x = int(input("Please enter the length (f): "))
y = int(input("Please enter the width (f): "))
z = int(input("Please enter the height (f): "))
long_side = x*z
short_side = y*z
top_side = x*y
total = long_side*2+short_side*2+x*y
gallons = total / GALLON_COVERAGE
num_of_bottles = math.ceil(gallons / 2)
print ()
print ("Known Infos: ")
print ("Area of the 2 long side walls:", long_side*2, "square feet")
print ("Area of the 2 short side walls:", short_side*2, "square feet")
print ("Area of the top side wall:", top_side, "square feet")
print ("Total area to cover: ", long_side*2 + short_side*2 + top_side, "square feet.")
print ("Total sqft area covered per gallon: ", GALLON_COVERAGE)
print ("Gallon(s) needed to cover:", gallons)
print ("Gallons per bottle: 2")
print ("Area of the floor:", top_side, "square feet.")
print ("Numbers of tiles needed per square feet: 9")
print ()
print ("Answers: ")
print ("You will need", num_of_bottles, "bottle(s) of paint.")
print ("Total numbers of tiles needed to cover the floor: ", top_side*9)