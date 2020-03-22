# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 7:28 2020

@author: KatherineYu
"""
import random
computer = random.randint(1, 3)

print(computer) # litte cheat sheet

while True:
    player = int(input("Enter: 1(rock), 2(paper), or 3(scissors)"))
    if (computer == 1 and player == 3) or (computer == 2 and player == 1) or (computer == 3 and player == 2):
        print("You lose!")
        break
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
        print("You win!")
        break
    else:
        if computer == 1:
            print("You both chose ROCK")
        elif computer == 2:
            print("You both chose PAPER")
        elif computer == 3:
            print("You both chose SCISSORS")
        continue

if computer == 1:
    print("Computer chose ROCK")
elif computer == 2:
    print("Computer chose PAPER")
elif computer == 3:
    print("Computer chose SCISSORS")

if player == 1:
    print("You chose ROCK")
elif player == 2:
    print("You chose PAPER")
elif player == 3:
    print("You chose SCISSORS")




