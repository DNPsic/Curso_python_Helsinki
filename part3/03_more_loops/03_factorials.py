"""
Please write a program which asks the user to type in an integer number.
If the user types in a number equal to or below 0, the execution ends.
Otherwise the program prints out the factorial of the number.
"""

while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break
    factorial = 1
    i = 1
    while i <= number:
        factorial *= i
        i += 1
    print(f"The factorial number of {number} is {factorial}")
print("Thanks and bye!")
