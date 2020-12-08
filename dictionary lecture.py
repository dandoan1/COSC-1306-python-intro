# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:31:43 2020
dictionary lecture
cosc1306
@author: dan doan 1986920
"""
data = [1,2,3,4,5]

dictionary = {"Dan":12345,"Bob":12543,"Jane":195043,"Han Solo":1}

dictionary["Dan"]

words = {}
with open("words.txt") as file:#r(read) is default
    for temp in file.readlines():
        temp = temp.strip()
        if len(temp) not in words:
            words[len(temp)] = [temp]
        else:
            words[len(temp)].append(temp)
            
three_letter_words = words[3]
test = three_letter_words[0]
letter_count = {}
for letter in test:
    if letter not in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] +=1
print(letter_count)