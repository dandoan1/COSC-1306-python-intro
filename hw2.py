# -*- coding: utf-8 -*-
"""
Created on Nov 3 16:10:38 2020
File lecture
cosc1306
@author: dan doan 1986920
"""
"""
file = open("GOOG.csv")
data = file.readlines()
file.close()
"""

#date0,high1,low2
def profit(filename):
    result = []
    file = open(filename)
    data = file.readlines()
    
    for index in range(1, len(data)):
        entry = data[index]
        part = entry.split(',')
        result.append((part[0], float(part[2]), float(part[3])))
        
    buy_price = result[0][2]
    buy_day = result[0][0]
    start_date = 0
    for i in range(len(result)): #find lowest
        if buy_price > result[i][2]:
            buy_day = result[i][0]
            buy_price = result[i][2]
            sell_price = result[i+1][1]
            sell_day = result[i+1][0]
    for x in range(0,len(result)):
        if sell_day == result[x][0]:
            start_date = x
    for x in range(start_date,len(result)): #find highest
        if sell_price < result[x][1]:
            sell_day = result[x][0]
            sell_price = result[x][1]
    max_profit = sell_price - buy_price #max profit
    print("Reading data ...")
    print("*"*40)
    print("The maximum profit is", round((max_profit), 2), "per share.")
    print()
    print("Buy on", buy_day, "at a price of", round((buy_price), 2))
    print("Sell on", sell_day, "at a price of", round((sell_price), 2))
    print()
    print('Change in value ratio: ', round((sell_price/buy_price), 3))
    print("*"*40)
    file.close()


while True:
    try:
        name = input('Please enter the data file name (input blank to exit): ')
        if name == "":
            break
        profit(name)
    except IOError:
        print ("""Error reading data ...
The file does not exist. Please check the name and try again.
""")
    