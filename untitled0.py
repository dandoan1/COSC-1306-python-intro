# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
review
cosc1306
@author: dan doan 1986920
"""

def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for x in range(3, number, 2):
        if number % x == 0:
            return False
    return True
print(isPrime(7)) #true
print(isPrime(9)) #false
print(isPrime(25)) #false
print(isPrime(17)) #true
print(isPrime(47)) #true
print(isPrime(77)) #false

total = 0 # use this variable to hold the total of Prime numbers


lower = 1
higher = 10
total = 0
for x in range(lower, higher+1):
    if isPrime(x):
        total += x
    



print("The total of the Prime Numbers is", total)