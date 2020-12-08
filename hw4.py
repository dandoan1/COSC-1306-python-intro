# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 14:38:02 2020
hw4
cosc1306
@author: dan doan 1986920
"""
#finished
def sequence(number):
    starting = number
    alist = []
    alist.append(starting)
    while starting != 1:
        if starting % 2 == 0:

            ending = starting // 2
            starting = ending
            alist.append(ending)
        else:

            ending = 3*(starting) + 1
            starting = ending
            alist.append(ending)

    return alist
    
    
up_to = 2000000
up_to +=1
results = {}
for x in range(1, up_to):
    results[x] = sequence(x)
longest = 0
biggest_num_list = 0
number = 0
for x in results:
    if len(results[x]) > longest:
        longest = len(results[x])
        biggest_num_list = results[x]
        number = x

#print ("The longest sequence up to {} starts with {} and has a length of {}.".format(up_to, number, longest))
print ("The longest sequence starts with {} and has a length of {}.".format(number, longest))
print (biggest_num_list)
    
    
