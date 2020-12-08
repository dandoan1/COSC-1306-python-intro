# -*- coding: utf-8 -*-
"""
Created on Nov 5 14:36:30 2020
assignment9
cosc1306
@author: dan doan 1986920
"""

def binary(password, password_list):
    start = 0
    end = len(password_list) - 1
    count = 0
    while start <= end:
        middle = (start + end)//2
        count +=1
        if (password == password_list[middle]):
            return (True, count)
        if password > password_list[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return (False, count)
def linear(password, password_list):
    count = 0
    for x in range(len(password_list)):
        if password == password_list[x]:
            count += 1
            return (True, count)
        else:
            count += 1
    return (False, count)



file1 = open("passwords_long.txt")
lines = file1.readlines()
passwords = []
for x in lines:
    passwords.append(x.strip()) #take away the \n inside the lines then make password into list
passwords.sort()
file1.close()
print("Reading password data ... Complete!")


while True:
    given = input("Please enter the password to search for (input blank to exit): ")
    if given == "":
        break
    found, steps = binary(given, passwords)
    found2, steps2 = linear(given, passwords)
    if found2:
        print("Linear search: Password found after {} steps.".format(steps2))
    else:
        print("Linear search: Password not found after {} steps.".format(steps2))
    if found:
        print("Binary search: Password found after {} steps.".format(steps))
        print("Password found! You should change your password!")
    else:
        print("Binary search: Password not found after {} steps.".format(steps))
print('Thank you for using.')

