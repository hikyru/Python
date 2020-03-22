"""
Created on Sat Mar 7 8:17 2020

@author: KatherineYu
"""

# printing solid triangle
for i in range(1, 6, 1):
    # for every i, j will print '*' i times
    for j in range(1, i + 1, 1):
        print("*", end='\t')
    # two lines are skipped after each i
    print()
    print()

print()

for i in range(1, 6, 1):
    # for every i, j will print '*' i times
    for j in range(1, i + 1, 1):
        # print '*' if it is the first or last one in the row
        if j == 1 or j - i == 0:  # i is the max, so if j is the last '*', j - i should equal zero
            print("*", end='\t')
        # the whole last (5th) row should print '*' like normal
        elif i == 5:
            print("*", end='\t')
        else:
            print(end='\t')  # if not the first or last, print spaces in between

    # two lines are skipped after each i
    print()
    print()
