# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
assignment4
cosc1306
@author: dan doan 1986920
"""

import math
def formula(terms): #calculation function
    result = 0
    for denom in range(terms):
        result = result + (1/((2*denom+1)*(-1)**denom))
    return result*4


print("Estimating Pi!")

power_of_ten = (int(input("Please enter the number of terms in the powers of ten: ")))


print("="*40)

for terms in range (power_of_ten+1):
    print("10^"+ str(terms), "  ->", formula(10**terms) )
print("pi     -> " + str(math.pi) )
print("="*40)
print("Thank you! Good Bye")