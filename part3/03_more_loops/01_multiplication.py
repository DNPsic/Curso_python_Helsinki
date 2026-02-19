"""Please write a program which asks the user for a positive integer number.
The program then prints out a list of multiplication operations until both operands
reach the number given by the user."""

# My solution
number: int = int(input("Please type in a number: "))
i = 1
while number >= i:
    x = 1
    while number >= x:
        print(f"{i} x {x} = {i * x}")
        x += 1
    i += 1

# Model's solution
print("\n*Model's solution*")
number = int(input("Please type in a number: "))
counter1 = 1
while counter1 <= number:
    counter2 = 1
    while counter2 <= number:
        print(f"{counter1} x {counter2} = {counter1 * counter2}")
        counter2 += 1
    counter1 += 1
