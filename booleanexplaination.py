# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
boolean explainations
cosc1306
@author: dan doan 1986920
"""

def _fizz_buzz(number):
    if number%3 == 0 and number%5 == 0:
        print("Fizz, Buzz")
    elif number%3 == 0:
        print("Fizz")
    elif number%5 == 0:
        print("Buzz")
    else:
        print(number)

def _is_cleap(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    else:
        return False
    


for i in range(1,16):
    _fizz_buzz(i)
    