# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
assignment 1
@author: dan d 1986920
"""
import math
radius = (float(input("enter your radius value in the tenth of decimal here: ")))
area = math.pi*radius**2
area_hexagon = (3*math.sqrt(3))/2*radius**2
print ()
print ("=" *40)
print ("circle area  = ", area)
print ("hexagon area = ", area_hexagon)
print ("shaded area  = ", area - area_hexagon)
print ("=" *40) 
#The magic number is 1.839871