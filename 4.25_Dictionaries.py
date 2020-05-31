# -*- coding: utf-8 -*-
"""
Created on Sat Apr 4/25 8:46 2020

@author: KatherineYu
"""

# create two dictionaries

classes1 = {'chinese': 83,
            'math': 96,
            'history': 78}

classes2 = {'social': 60,
            'science': 99}

classes1.update(classes2)
print(classes1)

classes1['social'] = 80
classes1['art'] = 75

print(classes1)

for key, value in classes1.items():
    print(key, value)