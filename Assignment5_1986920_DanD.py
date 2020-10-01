# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:05:47 2020
Assignment5
cosc1306
@author: dan doan 1986920
"""

def getgrade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 86:
        return "A-"
    elif grade >= 82:
        return "B+"
    elif grade >= 78:
        return "B"
    elif grade >= 74:
        return "B-"
    elif grade >= 70:
        return "C+"
    elif grade >= 66:
        return "C"
    elif grade >= 62:
        return "C-"
    elif grade >= 58:
        return "D+"
    elif grade >= 54:
        return "D"
    elif grade >= 50:
        return "D-"
    elif grade < 50:
        return "F"
    else:
        pass


def highergrade(grade):
    if grade >= 90:
        print ("Good job! This is the highest grade you can get.")
    elif grade >= 86:
        print ("You are", round((90 - grade), 2), "points away from A" )
    elif grade >= 82:
        print ("You are", round((86 - grade), 2), "points away from A-" )
    elif grade >= 78:
        print ("You are", round((82 - grade), 2), "points away from B+" )
    elif grade >= 74:
        print ("You are", round((78 - grade), 2), "points away from B" )
    elif grade >= 70:
        print ("You are", round((74 - grade), 2), "points away from B-" )
    elif grade >= 66:
        print ("You are", round((70 - grade), 2), "points away from C+" )
    elif grade >= 62:
        print ("You are", round((66 - grade), 2), "points away from C" )
    elif grade >= 58:
        print ("You are", round((62 - grade), 2), "points away from C-" )
    elif grade >= 54:
        print ("You are", round((58 - grade), 2), "points away from D+" )
    elif grade >= 50:
        print ("You are", round((54 - grade), 2), "points away from D" )
    elif grade < 50:
        print ("You are", round((50 - grade), 2), "points away from D-" )
    else:
        pass

final_average = float(input("Please enter the final average: "))
print ()
print ()
print ("Congratulations, you earned a/an " + (getgrade(final_average)) + ".")
print ("="*40)
(highergrade(final_average))