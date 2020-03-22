"""
Created on Sat Mar 7 7:50 2020

@author: KatherineYu
"""

# define variable m (m is the counter for the number of digits per line)
m = 0
# User Input
n = int(input("Enter a number n: "))

# prints all multiples of 3 in number n
for i in range(1, n, 1):
    if i % 3 == 0:
        print(i, end='\t')
        m += 1
    # after program printed i, it will check whether there has been 5 digits on the same line already
    # if true, it will skip a line
    # if false in returns to the top of for loop i
    if m % 5 == 0:
        print()
# new line for formatting purposes
print()
