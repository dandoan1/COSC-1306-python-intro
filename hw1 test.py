# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
hw1 test
cosc1306
@author: dan doan 1986920
"""
width = int(input("Enter width size square: "))
#height = int(input("Enter height size square: "))

for y in range (width):
    if y%2 == 0:
        for x in range (width):
            if x%2 == 0:
                print ("X", end="")
            else:
                print ("O", end="")
        print ()
    else:
        for x in range (width):
            if x%2 == 0:
                print ("O", end="")
            else:
                print ("X", end="")
        print ()

print ()
print ("Done!")