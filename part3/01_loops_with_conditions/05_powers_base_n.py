"""Modify the program so that the user gets to input
also the base which is multiplied (in the previous
program the base was always 2).
"""

limit = int(input("Upper limit: "))
base = int(input("Base: "))
number = 1

while limit >= number:
    print(number)
    number *= base
