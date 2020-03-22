# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 1:47 2020

@author: KatherineYu
"""
# Print Store Discount
print('\n' "Great Deals Today!", end='\n''\n')

# user input for variables

totalPrice = float(input("Total Spent: "))

# Determine % discount and price after discount

if totalPrice >= 10000:
    print('\n' "30% OFF")
    print("Total After Discount: ", round(totalPrice * .7))
elif totalPrice >= 5000:
    print('\n' "20% OFF")
    print("Total After Discount: ", round(totalPrice * .8))
elif totalPrice >= 1000:
    print('\n' "10% OFF")
    print("Total After Discount: ", round(totalPrice * .9))
else:
    print('\n' "NO DISCOUNT")
    print("Total: ", totalPrice)