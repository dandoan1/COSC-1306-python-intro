# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:59:36 2020
assignment11
cosc1306
@author: dan doan 1986920
"""
import math
def is_right_triangle(a,b,c):
    return a**2+b**2==c**2
for a in range(1,50):
    for b in range(a+1,50):
        c = int(math.sqrt(a**2+b**2))
        if is_right_triangle(a, b, c):
            print((a,b,c), a+b+c)