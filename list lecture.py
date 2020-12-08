# -*- coding: utf-8 -*-
"""
Created on Oct 27 16:10:38 2020
list lecture
cosc1306
@author: dan doan 1986920
"""

x = []
for num in range(10):
    if num % 2 == 0:
        x.append(num)
print(x)

x = [num+0.5 for num in range(10) if num%2==0]

print (x)

for i in x:
    print(i)
    
word = "tree"
for index,letter in enumerate(word): #enumerate give the index of the given number
    if letter.upper() in "AEIOU":
        print (index, letter)
        break
    
def GCD(a, b):
    while b>0:
        a, b = b, a%b
        print (a, b)
    return a
print(GCD(18,45))
word = "I see car eaten"
		
print(word[2:-1:2])
def stringy(string1,string2):

    s = ""

    for c in string1:

        if c in string2:

            if c not in s:

                s += c

    return s

p = 'hello world'

q = 'houston'

print(stringy(p,q))

text = "Tacocat"

print(text[::-1])