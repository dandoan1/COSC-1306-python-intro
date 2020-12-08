# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:10:38 2020

@author: kevin
"""

size = 3

def draw(num):
    for x in range (num):
        for x in range(num):
            print ("+--", end="")
        print ("+")
        for x in range(num):
            print("|  ", end="")
        print ("|")
    for x in range(num):
        print ("+--", end="")
    print ("+")
    
draw(size)

def createGarden(size):
    for i in range(size):
        print("+--" * size + "+")
        print("|  " * size + "|")

    print("+--" * size + "+")
    
createGarden(size)