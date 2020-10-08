# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:03:58 2020

@author: kevin
"""

uI = eval(input("please enter input:"))

for i in range(uI):
    print(" "*(uI-i), "x"(i*2+1))
for j in range(uI-2, -1, -1):
    print(" "*(uI-j), "x"(j*2+1))