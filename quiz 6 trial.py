# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
quiz6
cosc1306
@author: dan doan 1986920
"""
import math

#1
def total(number):
    result = 0
    for x in range(0,number+1):
        if x%3 == 0 or x%5 ==0 :
            pass
        else:
            result = result + x
    print (result)
    

total(1000000)   

#2         

def count(number):
    result = 0
    for x in range(0,number+1):
        result = result + (x*(x+1))/2
    print (result)
    
count(2020)

#3

def outside(number):
    radius = ((3*number)/(4*math.pi))**(1./3.)
    sidelength = radius * 2
    cubevolume = sidelength ** 3
    print (cubevolume - number)
outside(10)

#4

def isPrime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number%2 == 0:
        return False
    for x in range(3,int(math.sqrt(number))+1, 2):
        if number%x == 0:
            return False
    return True

def primesadd(number):
    total = 0
    for num in range(1, number):
        if isPrime(num):
            total += num
        else:
            pass
    print (total)
            
primesadd(2020)

#5

def numdivisor(number):
    total = 0
    for x in range(1, number):
        if number % x == 0:
            total += 1
        else:
            pass
    print (total)

numdivisor(123456)

#6

def primenum(number):
    if number == 1:
        return 2
    count = 1
    num = 1
    while number > count:
        num += 2
        if isPrime(num):
            count += 1
    return num
        
print(primenum(2020))        


#7

def sumdivisor(number):
    total = 0
    for x in range(1, number):
        if number % x == 0:
            total += x
    return total

def highest(number):
    highest = 0
    for x in range(1, number):
        if highest < sumdivisor(x):
            highest = sumdivisor(x)
            print (x, highest)

highest(2020)
            
            
            