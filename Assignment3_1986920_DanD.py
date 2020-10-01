# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
assignment3 trial
cosc1306
@author: dan doan 1986920
"""

import math
number = abs(float(input("Please enter a number for square root calculation: ")))

guess = 2

print ("Step = value")
print ("="*40)
for count in range(6): 
    for trials in range(2**count):
        temp = (number / guess) #temp has value 5
        guess = (guess + temp) / 2
    print (2**count, "  =", guess)
print ("sqrt = ", math.sqrt(number))
print ("="*40)
print ("Thank you, Good Bye!")