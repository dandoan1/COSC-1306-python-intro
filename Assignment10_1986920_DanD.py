# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:31:43 2020
assignment10
cosc1306
@author: dan doan 1986920
"""


num2letter = {"0":["O"], "1":["I", "L"], "2":["A", "B", "C"], 
              "3":["D", "E", "F"], "4":["G", "H", "I"], "5":["J", "K", "L"],
              "6":["M", "N", "O"], "7":["P", "Q", "R", "S"], 
              "8":["T", "U", "V"], "9":["W", "X", "Y", "Z"], }

def helper(start, end):
    result = []
    for first in start:
        for last in end:
            result.append(first + last)
    return result
def translate(numbers, words):
    result = [""]
    for x in range(len(numbers)):
        result = helper(result, num2letter[numbers[x]])
    actualresult = []
    for possible in result:
        if possible in words:
            actualresult.append(possible)
    return actualresult #return list of words

three_letter_words = []
four_letter_words = []
with open("words.txt") as file1:
    for word in file1.readlines():
        word = word.strip()
        if len(word) == 3:
            three_letter_words.append(word)
        if len(word) == 4:
            four_letter_words.append(word)




while True:
    number = input("Please enter a phone number (xxx-xxxx): ")
    first = (translate(number[:3], three_letter_words))
    second = (translate(number[-4:], four_letter_words))  
    for word in (helper(first, second)):
        print (word[:3] + "-" + word[-4:])
    yesno = input("Try another (Y/N)? ")
    if yesno.upper() == "N":
        break 
print("Good Bye!")