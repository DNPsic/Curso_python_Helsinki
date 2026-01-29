"""
Please write a program which asks the user for a number. The program then prints
out all integer numbers greater than zero but smaller than the input.
"""

number = int(input("Upper limit: "))
count = 1

while count < number:
    print(count)
    count += 1
