# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 8:17 2020

@author: KatherineYu
"""

InfoLog = {}
while True:
    ID = input("Enter ID: ")
    if ID == '-1':
        break
    elif ID not in InfoLog:
        InfoLog['ID'] = ID
    else:
        continue
    InfoLog['Name'] = input("Enter Name: ")
    InfoLog['Mobile Number'] = input("Enter Mobile number: ")
    InfoLog['Birthday'] = input("Enter Birthday: ")
    InfoLog['Address'] = input("Enter Address: ")

print(InfoLog, '\n')

while True:
    action = int(input("Choose an option (1 = search by ID; 2 = show full data; 3 = edit data; -1 = exit program): "))
    if action == 1:
        ID = input("Enter existing ID: ")
        if ID not in InfoLog:
            print("This ID does not exist. Try again")
            continue
        elif ID in InfoLog:
            print(InfoLog['ID'])

    elif action == 2:
        print(InfoLog)

    elif action == 3:
        ID = input("Enter existing ID: ")
        if ID not in InfoLog:
            print("This ID does not exist. Try again")
            continue
        elif ID in InfoLog:
            edit = input("Choose an item to edit(1 = Name; 2 = Mobile; 3 = Address: ")
            if edit == 1:
                InfoLog['Name'] = input("Edit your Name: ")
            elif edit == 2:
                InfoLog['Mobile'] = input("Edit Mobile: ")
            elif edit == 3:
                InfoLog['Address'] = input("Edit your Address: ")

    elif action ==  -1:
        break

