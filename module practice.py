# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
module examples
cosc1306
@author: dan doan 1986920
"""

import time
import random

number = random.randint(5,15)

print ("Get ready to count down", number, "seconds")
for seconds in range(3, 0, -1):
    print(seconds)
    time.sleep(1)
print ("Go!")
start = time.time()

input ("Press enter")
end = time.time()
elapse = end - start
print (end - start)
print ("You were", abs(elapse - number),"seconds away" )