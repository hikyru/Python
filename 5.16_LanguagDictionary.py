# -*- coding: utf-8 -*-
"""
Created on Sat Mar 7 8:17 2020

@author: KatherineYu
"""

def quiz(question, ans, score):
    print(question)
    answer = input("Enter your answer: ")
    if answer != ans:
        print("Incorrect. The correct answer is", ans, sep=' ')
    elif answer == ans:
        print("Correct!")
        score += 1

    return score

import random

dictionary = {'apple': 'fruit',
              'ball': 'toy',
              'happy': 'mood'}

while True:
    action = int(input("Choose an option (1 = add word; 2 = show dictionary; 3 = search by word; 4 = search by definition; 5 = quiz; -1 = exit program): "))

    if action == -1:
        break

    elif action == 1:
        word = input("Enter a new word: ")
        dictionary[word] = input("Enter definition: ")

    elif action == 2:
        for key, value in dictionary.items():
            print(key, value)

    elif action == 3:
        word = input("Enter an existing word: ")
        if word not in dictionary:
            print("Word not found.")
            dictionary[word] = input("Enter definition to add word to dictionary: ")
        else:
            print(word, ':', dictionary[word], sep = '')

    elif action == 4:
        word = input("Enter a definition: ")
        temp = False
        for key, value in dictionary.items():
            if value == word:
                print(key, ':', value, sep = '')
                temp = True
        if temp == False:
            print("not found")

    elif action == 5:
        wordList = []
        for key, value in dictionary.items():
            temp = [key, value]
            wordList.append(temp)

        choose = int(input("Test by word(1) or definition(2)? "))
        score = 0
        for i in range(0, 3, 1):
            key, value = random.choice(wordList)
            if choose == 1:
                score = quiz(key, value, score)
            elif choose == 2:
                score = quiz(value, key, score)
        print("Your total score is: ", score, sep = ' ')