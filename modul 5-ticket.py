# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 15:28:52 2024

@author: Dewi aulia nurjanah
"""

n = 0
money = 0
people = 0

while (n != ''):
    n = str(input("Input Age: "))
    people += 1
    if (n == str('')):
        break;
    else:
        
        if (int(n) <= 2):
            print('FREE')
            money += 0
            print("total payment = ", money)
        elif (3 <= int(n) <= 12):
            print("Price $14.00")
            money += 14.00
            print("total payment = ", money)
        elif (150 >= int(n) >= 65):
            print('Price $18.00')
            money += 18.00
            print("total payment = ", money)
        elif (13 <= int(n) <= 64):
            print('Price $23.00')
            money += 23.00
            print("total payment = ", money)
        else:
            people -= 1
            print('INVALID')
            
if(people == 1):
    print(" ")
else:
    pay = float(input("Payment = "))
    chance = pay - money
    print('Change = ', chance)