# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:59:36 2020
assignment11
cosc1306
@author: dan doan 1986920
"""
import math
total = {}
def is_right_triangle(a,b,c):
    return a**2+b**2==c**2
for a in range(1,1000):
    for b in range(a+1,1010):
        c = int(math.sqrt(a**2+b**2))
        if is_right_triangle(a, b, c):
            #print((a,b,c), a+b+c)
            perimeter = a+b+c
            triangle = (a,b,c)
            if perimeter < 2020:
                if perimeter not in total:
                    total[perimeter] = [triangle]
                else:
                    total[perimeter].append(triangle)
longest = 0
biggest = 0
for x in total:
    if len(total[x]) > longest:
        #print (x, len(total[x]))
        biggest = x
        longest = len(total[x])
print ("The perimeter of {} gives a maximum number of {} triangles.".format(biggest, longest))
print ("The triangles are: ")

for x in (total[biggest]):
    print (x)

