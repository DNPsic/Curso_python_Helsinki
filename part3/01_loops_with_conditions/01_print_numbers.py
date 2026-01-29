"""
Please write a program which prints out all the even numbers between
two and thirty, using a loop. Print each number on a separate line.
"""

# My solution:

numbers = 2

while numbers <= 30:
    if numbers % 2 == 0:
        print(numbers)
    numbers += 1
