"""Please write a program which asks the user to type in a number.
The program then prints out the positive integers between 1 and the
number itself, alternating between the two ends of the range as in the
examples below."""

# Please type in a number: 5
# 1
# 5
# 2
# 4
# 3

number = int(input("Please type in a number: "))
i = 1
while i <= number:
    print(i)
    if i == number:
        break
    print(number)

    number -= 1

    i += 1
