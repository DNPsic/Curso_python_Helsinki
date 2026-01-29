"""
Pre-task.
Please write a program which asks the user for integer numbers.
The program should keep asking for numbers until the user types in zero.

Part 1: Count:
After reading in the numbers the program should print out how many numbers
were typed in. The zero at the end should not be included in the count.

Part 2: Sum
The program should also print out the sum of all the numbers typed in.
The zero at the end should not be included in the calculation.

Part 3: Mean
The program should also print out the mean of the numbers. The zero at
the end should not be included in the calculation. You may assume the
user will always type in at least one valid non-zero number.

Part 4: Positives and negatives
The program should also print out statistics on how many of the numbers
were positive and how many were negative. The zero at the end should not
be included in the calculation.
"""

# Pre-task ✅
# Part 1 ✅
# Part 2 ✅
# Part 3 ✅
# Part 4 ✅

counter = 0
n_sum = 0
negatives = 0
positives = 0

print("Please type integer numbers. Type 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        print("Numbers typed in", counter)
        print("The sum of the numbers is", n_sum)
        print(f"The mean of the numbers is {n_sum / counter}")
        print("Positive numbers", positives)
        print("Negative numbers", negatives)
        break
    if number < 0:
        negatives += 1
    elif number > 0:
        positives += 1
    counter += 1
    n_sum += number

# Model's solution:
# print("Please type in integer numbers. Type in 0 to finish.")
# numbers = 0
# sum = 0
# positives = 0
#
# while True:
#     number = int(input("Number: "))
#     if number == 0:
#         break
#     numbers += 1
#     sum += number
#     if number>0:
#         positives += 1
#
# print("Numbers typed in", numbers)
# print("The sum of the numbers is", sum)
# print("The mean of the numbers is", sum/numbers)
# print("Positive numbers", positives)
# print("Negative numbers", numbers-positives)
