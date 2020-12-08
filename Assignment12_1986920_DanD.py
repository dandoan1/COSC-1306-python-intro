# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:38:02 2020
assignment12
cosc1306
@author: dan doan 1986920
"""
#finished
def read(name):
    wordslist = []
    letter_count = {}
    with open(name) as file:
        for line in file.readlines():
            wordslist.append(line.strip())

    for words in wordslist:
        for letter in words:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] +=1
    total = 0
    for key in letter_count:
        #print(key, letter_count[key])
        total += letter_count[key]
    #print (total)
    for key in letter_count:
        #print(key, round((((letter_count[key]/total)*100)), 3), "{}".format("%"))
        print("{} - {:6.3f}{}".format(key, (round((((letter_count[key]/total)*100)), 3)), "%"))
        print ()
    



try:
    name = "zingarelli2005.txt"
    print ("The letter frequencies are: ")
    print ()
    read(name)
except IOError:
        print ("""Error reading data ...
The file does not exist. Please check the name and try again.
""")