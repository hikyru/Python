# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4/18 7:33 2020

@author: KatherineYu
"""

quantity = 0
price = 0
sale = []
remaining = 0

while True:
    choice = int(input("Choose a system(1- Settings; 2- Imports; 3- Exports; 4- Gains; 5- Storage; 6- Print Start off Quantity & Price): "))
    if choice == -1:  # checks to see if user wants to end program first thing, so won't let program run for nothing
        break

    elif choice == 1:
        quantity = int(input("Please enter how many apples are in stock: "))
        while quantity < 1:
            quantity = int(input("Please enter how many apples are in stock: "))
        remaining = quantity  # remaining is how many apples left in stock after a series of imports and exports
        # quantity is how many apples you started with (value does not change throughout the program)

        price = int(input("Enter the price per apple: "))
        while price < 1:
            price = int(input("Enter the price per apple: "))

    elif choice == 2:
        enter = int(input("Enter the amount of imports: "))
        while enter < 1:
            enter = int(input("Enter the amount of imports: "))
        remaining += enter # the amount of imports is added to what you have left in stock

    elif choice == 3:
        sold = int(input("Enter the amount of apples sold: "))
        while sold < 1:
            sold = int(input("Enter the amount of apples sold: "))
            
        if remaining < 1:
            print("There are no more apples in stock.")
        elif remaining < sold:
            sale.append(remaining)
            print("Only", remaining, "apples were in stock.")
            print("You gained $", remaining * price)
            remaining = 0
        else:
            sale.append(sold)
            remaining -= sale[-1]  # sale[-1] is the most recently added item in the list, aka the most recent sale
            # remaining - sale[-1] tells you what you have left after each sale
            print("You sold", sale[-1], "apples this time")
            print("You gained", sale[-1]*price, "from this sale.")

    elif choice == 4:
        print("You made", len(sale), "sales today.") # each index in the list 'sale' represents every deal you made
        print("Amount sold per sale:")
        for i in sale:
            print(i)
        print("Total gained:", sum(sale)*price)

    elif choice == 5:
        print("Your storage has", remaining, "apples left.")

    elif choice == 6:
        print("\nThere were ", quantity, "apples in stock.")
        print("The price is $", price, "per apple.\n")

    else:
        continue

