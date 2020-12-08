# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 15:49:33 2020
hw3
cosc1306
@author: dan doan 1986920
"""

def get_signature(word):
    result = list(word)
    result.sort()
    return tuple(result)
words = []
with open("words.txt") as file:
    for line in file.readlines():
        words.append(line.strip())
holder = {}
for word in words:
    length=len(word)
    if length not in holder:
        holder[length] = []
    holder[length].append(word)        

two_letter_words = holder[2]
three_letter_words = holder[3]
four_letter_words = holder[4]
five_letter_words = holder[5]
six_letter_words = holder[6]
seven_letter_words = holder[7]
eight_letter_words = holder[8]
nine_letter_words = holder[9]
ten_letter_words = holder[10]
eleven_letter_words = holder[11]
twelve_letter_words = holder[12]
thirdteen_letter_words = holder[13]
fourteen_letter_words = holder[14]
fithteen_letter_words = holder[15]

another_dict = {}
for word in two_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in three_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in four_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in five_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in six_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in seven_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in eight_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in nine_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in ten_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in eleven_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in twelve_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in thirdteen_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in fourteen_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)
for word in fithteen_letter_words:
    signature = get_signature(word)
    #print (word, signature)
    if signature not in another_dict:
        another_dict[signature] = [word]
    else:
        another_dict[signature].append(word)


one = {}
two = {}
three = {}
four = {}
five = {}
seven = {}
eight = {}
twelve = {}


for x in another_dict:
    if len(another_dict[x]) == 12:
        for y in range(12):
            word = tuple(another_dict[x])
            twelve[word] = []
    if len(another_dict[x]) == 8:
        for y in range(8):
            word = tuple(another_dict[x])
            eight[word] = []
    if len(another_dict[x]) == 7:
        for y in range(7):
            word = tuple(another_dict[x])
            seven[word] = []
    if len(another_dict[x]) == 5:
        for y in range(5):
            word = tuple(another_dict[x])
            five[word] = []
    if len(another_dict[x]) == 4:
        for y in range(4):
            word = tuple(another_dict[x])
            four[word] = []
    if len(another_dict[x]) == 3:
        for y in range(3):
            word = tuple(another_dict[x])
            three[word] = []
    if len(another_dict[x]) == 2:
        for y in range(2):
            word = tuple(another_dict[x])
            two[word] = []
    if len(another_dict[x]) == 1:
        for y in range(1):
            word = tuple(another_dict[x])
            one[word] = []


while True:
    choice = int(input("Please enter the anagram group size (1-12) or 0 to quit: "))  
    if choice == 0:
        break
    if choice == 12:
        for x in twelve:
            alist = list(x)
            print (alist)
    if choice == 11:
        
            print("There are no word(s) with", choice,"anagram.")
    if choice == 10:

            print("There are no word(s) with" , choice ,"anagram.")
    if choice == 9:

            print("There are no word(s) with", choice, "anagram.")
    if choice == 8:
        for x in eight:
            alist = list(x)
            print (alist)
    if choice == 7:
        for x in seven:
            alist = list(x)
            print (alist)
    if choice == 6:
            print("There are no word(s) with",choice ,"anagram.")
    if choice == 5:
        for x in five:
            alist = list(x)
            print (alist)
    if choice == 4:
        for x in four:
            alist = list(x)
            print (alist)
    if choice == 3:
        for x in three:
            alist = list(x)
            print (alist)
    if choice == 2:
        for x in two:
            alist = list(x)
            print (alist)
    if choice == 1:
        for x in one:
            alist = list(x)
            print (alist)
    elif choice > 12 or choice < 0:
        print ("Invalid Selection >", choice,"<, please try again.")
            
            
print ("Thank You!")    