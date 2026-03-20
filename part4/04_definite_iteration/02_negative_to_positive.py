"""Please write a program which asks the user for a positive
integer N. The program then prints out all numbers between
-N and N inclusive, but leaves out the number 0. Each number
should be printed on a separate line."""

number: int = int(input("Please type in a positive integer: "))
for x in range(-1 * number, number + 1):
    if x != 0:
        print(x)
