# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 16:10:38 2020
assignment7
cosc1306
@author: dan doan 1986920
"""

def is_vowel(letter):
    return letter.upper() in "AEIOU"
def contains_vowel(word):
    for letter in word:
        if is_vowel(letter):
            return True
    return False    
    
def where_vowel(word):
    count = 0
    for x in word:
        if x.upper() not in "AEIOU":
            count +=1
        else:
            return count
def translate(word):
    if is_vowel(word[0]): #rule 1
        return word + "way"
    if contains_vowel(word): #rule 3
        if word[0].isupper(): #rule 4
            index = where_vowel(word)
            rule4 = word[index:] + word[:index] + "ay"
            return rule4[0].upper() + rule4[1:].lower()
        index = where_vowel(word) #rule 3
        return word[index:] + word[:index] + "ay"
    else: #rule 2
        return word + "way"
    return "temp"


print("This program will translate a word from English to Pig Latin.")
message = "{0} becomes {1}."

while True:
    word = input("Please enter a word in English: ")
    pig_latin = translate(word)
    print (message.format(word, pig_latin))
    option = input("Would you like another word? (Y/N) ")
    if option.upper() == "N":
        break
    
print ("Ankthay ouyay!")
